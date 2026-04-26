"""
fetch_datacenter_locations.py
─────────────────────────────
Pulls data center locations from OpenStreetMap via the Overpass API,
then enriches each location with nearest air quality readings from OpenAQ.

Outputs: data/datacenter_locations.csv
         data/datacenter_aq_enriched.csv

Usage:
    python scrapers/fetch_datacenter_locations.py
"""

import requests
import pandas as pd
import json
import time
import os

# ── CONFIG ────────────────────────────────────────────────────────────────────

OUTPUT_DIR = "data"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Bounding boxes: Virginia and Texas
REGIONS = {
    "virginia": (36.54, -83.68, 39.47, -75.24),
    "texas":    (25.84, -106.65, 36.50, -93.51),
}

OVERPASS_URL = "https://overpass-api.de/api/interpreter"
OPENAQ_URL   = "https://api.openaq.io/v2/locations"


# ── STEP 1: Fetch data center locations from OpenStreetMap ────────────────────

def fetch_datacenters(region_name, bbox):
    south, west, north, east = bbox
    print(f"\n[+] Fetching data centers in {region_name}...")

    query = f"""
    [out:json][timeout:60];
    (
      node["building"="data_center"]({south},{west},{north},{east});
      way["building"="data_center"]({south},{west},{north},{east});
      node["telecom"="data_center"]({south},{west},{north},{east});
    );
    out center;
    """

    response = requests.post(OVERPASS_URL, data={"data": query})
    response.raise_for_status()
    elements = response.json().get("elements", [])

    records = []
    for el in elements:
        lat = el.get("lat") or el.get("center", {}).get("lat")
        lon = el.get("lon") or el.get("center", {}).get("lon")
        tags = el.get("tags", {})
        records.append({
            "region":   region_name,
            "osm_id":   el.get("id"),
            "osm_type": el.get("type"),
            "lat":      lat,
            "lon":      lon,
            "name":     tags.get("name", "Unknown"),
            "operator": tags.get("operator", ""),
            "address":  tags.get("addr:full", tags.get("addr:city", "")),
        })

    print(f"    Found {len(records)} data centers.")
    return records


# ── STEP 2: Enrich with OpenAQ air quality data ───────────────────────────────

def fetch_air_quality(lat, lon, radius_km=25):
    """Get nearest AQ monitoring station within radius."""
    try:
        params = {
            "coordinates": f"{lat},{lon}",
            "radius":      radius_km * 1000,
            "limit":       1,
            "order_by":    "distance",
        }
        resp = requests.get(OPENAQ_URL, params=params, timeout=10)
        resp.raise_for_status()
        results = resp.json().get("results", [])
        if not results:
            return None, None, None
        station = results[0]
        parameters = station.get("parameters", [])
        pm25 = next((p["lastValue"] for p in parameters if p["parameter"] == "pm25"), None)
        return station.get("name", ""), station.get("distance", None), pm25
    except Exception:
        return None, None, None


# ── MAIN ──────────────────────────────────────────────────────────────────────

def main():
    all_records = []

    # Fetch locations
    for region, bbox in REGIONS.items():
        records = fetch_datacenters(region, bbox)
        all_records.extend(records)
        time.sleep(2)  # be polite to the API

    df = pd.DataFrame(all_records)
    df.to_csv(f"{OUTPUT_DIR}/datacenter_locations.csv", index=False)
    print(f"\n[✓] Saved {len(df)} locations → {OUTPUT_DIR}/datacenter_locations.csv")

    # Enrich with air quality
    print("\n[+] Enriching with OpenAQ air quality data (this may take a minute)...")
    aq_station, aq_distance, aq_pm25 = [], [], []

    for _, row in df.iterrows():
        if pd.notna(row["lat"]) and pd.notna(row["lon"]):
            station, dist, pm25 = fetch_air_quality(row["lat"], row["lon"])
            aq_station.append(station)
            aq_distance.append(dist)
            aq_pm25.append(pm25)
        else:
            aq_station.append(None)
            aq_distance.append(None)
            aq_pm25.append(None)
        time.sleep(0.5)

    df["aq_station"]      = aq_station
    df["aq_distance_m"]   = aq_distance
    df["aq_pm25_last"]    = aq_pm25

    df.to_csv(f"{OUTPUT_DIR}/datacenter_aq_enriched.csv", index=False)
    print(f"[✓] Saved enriched data → {OUTPUT_DIR}/datacenter_aq_enriched.csv")
    print(f"\nSample output:\n{df[['name','region','lat','lon','aq_pm25_last']].head(10).to_string()}")


if __name__ == "__main__":
    main()
