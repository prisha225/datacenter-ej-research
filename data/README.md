## Data sources

All sources used in this project are publicly available and free to access.

| Dataset                  | Source                       | Format        | Notes                       |
| ------------------------ | ---------------------------- | ------------- | --------------------------- |
| Data center locations    | OpenStreetMap (Overpass API) | JSON          | No key required             |
| Air quality (PM2.5)      | OpenAQ v2 API                | JSON          | No key required             |
| Median household income  | US Census ACS 5-year         | JSON          | No key required             |
| Water stress             | WRI Aqueduct                 | GeoTIFF / CSV | Free download               |
| Land surface temperature | NASA Earthdata / Landsat     | GeoTIFF       | Free, registration required |

---

## On data gaps

Several key data types are not publicly available:

* Energy consumption per facility: not required to be disclosed in most US states
* Water extraction volumes: reported inconsistently across utility jurisdictions
* Land acquisition records: accessible via FOIA but not centrally aggregated

These gaps are documented in `data/gap_report.json` and treated as findings, not limitations.