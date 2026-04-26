# Methodology

## Research Question

Where are data centers being built, who lives nearby, and what does the data not tell us?

## Approach

### Phase 1 (Current)
- Scrape data center locations from OpenStreetMap via Overpass API
- Enrich with nearest air quality readings (OpenAQ PM2.5)
- Pull county-level median income from US Census ACS
- Generate interactive map with gap flagging
- Produce structured gap report

### Phase 2 (Planned)
- Spatial join with Census TIGER county geometries
- Add WRI Aqueduct water stress overlay
- Add NASA Landsat land surface temperature layer
- Community annotation mechanism
- Integration with Data Center Impact Dashboard

## Confidence Tagging

Each data point is categorized by how it was obtained:

| Tag | Meaning |
|---|---|
| `public_api` | Directly from a public government or NGO API |
| `osm_community` | Contributed to OpenStreetMap — may be incomplete |
| `estimated` | Derived or inferred, not directly measured |
| `gap` | Data not available - absence is itself a finding |

## Geographic Scope

Phase 1 is constrained to **Virginia and Texas** - two of the highest-growth US data center markets with accessible public records and documented community impact.

## Limitations

- OSM data center coverage is incomplete - many facilities are untagged
- AQ monitoring stations are not uniformly distributed; gaps likely reflect undermonitoring in lower-income areas
- County-level income is a coarse proxy for community-level impact
- No real-time data in Phase 1
