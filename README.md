# Data Center Pattern Detection & Environmental Justice

A computational research project investigating where data centers are built, who lives nearby, and what the data does not tell us.

Proposed contribution to the Data Center Impact Dashboard by Rooted Futures Lab.

---

## The problem

Data centers are often framed as neutral digital infrastructure. In reality, they consume large volumes of water and energy, generate heat and noise, and are frequently located near lower-income or marginalized communities.

These siting patterns rarely receive public scrutiny.

This project builds a data pipeline to make those patterns visible and understandable.

---

## What this repository does

* Scrapes publicly available data center location data
* Cross-references locations with demographic and environmental datasets
* Detects spatial patterns between infrastructure and community indicators
* Produces interactive maps that are readable to affected communities, not only researchers
* Documents where data is missing and treats those gaps as findings

---

## Quickstart

Clone the repository and install dependencies:

```bash
git clone https://github.com/prisha225/datacenter-ej-research.git
cd datacenter-ej-research
pip install -r requirements.txt
```

Run the scraper:

```bash
python scrapers/fetch_datacenter_locations.py
```

Run the analysis notebook:

```bash
jupyter notebook notebooks/01_pattern_analysis.ipynb
```

---

## Repository structure

```
datacenter-ej-research/
├── scrapers/
│   └── fetch_datacenter_locations.py
├── notebooks/
│   └── 01_pattern_analysis.ipynb
├── visualizations/
│   └── map.html
├── data/
│   └── README.md
├── docs/
│   └── methodology.md
├── requirements.txt
└── README.md
```

---

## Data sources

| Source                       | What it provides            | Access         |
| ---------------------------- | --------------------------- | -------------- |
| OpenStreetMap (Overpass API) | Data center locations       | Free, no key   |
| OpenAQ                       | Air quality by location     | Free API       |
| US Census Bureau             | Demographics (income, race) | Free API       |
| WRI Aqueduct                 | Water stress levels         | Public dataset |
| NASA Earthdata               | Land surface temperature    | Public API     |

---

## Geographic scope

Phase 1 focuses on Virginia and Texas. These states have some of the fastest data center growth in the US, documented community concerns, and accessible public datasets.

National coverage is outside the scope of this phase.

---

## On data gaps

A core principle of this project is that absence of data is itself a finding.

When water usage, energy draw, or environmental reporting is missing from official records, this reflects accountability structures rather than limitations of this analysis.

All data points are tagged by source type so users can understand how each claim is supported.

---

## Project status

Active development, Summer 2026.

This repository is being developed as a proposed contribution to the Rooted Futures Lab EJIT Fellowship.

---

## Author

Prisha Balyan
B.Tech Information Technology, IGDTUW, New Delhi