# MetroPT-3 Statistical Analysis

**Peyman Mohammad Hassan**

This independent statistical analysis examines authentic sensor measurements from the MetroPT-3 railway compressor, including observed operating-state differences in pressure. The executable notebook contains dataset inspection, documented cleaning, descriptive statistics, labeled visualizations, an explicit statistical hypothesis test, and a sensitivity analysis. The observations are research sensor records, not confirmed work orders or automatically inferred fault events.

**Dataset:** UCI Machine Learning Repository, MetroPT-3, https://archive.ics.uci.edu/dataset/791/metropt%2B3%2B (DOI: https://doi.org/10.24432/C5VW3R). The reproducibly sampled CSV contains 30,339 recorded observations and 17 fields. Compressed archival parts are also included for lossless restoration.

## Run

1. Use Python 3.12 and create a virtual environment: `python -m venv .venv`; activate with `source .venv/bin/activate` (Windows: `.venv\Scripts\activate`).
2. Restore the included CSV if it is not present: `python prepare_dataset.py` (uses standard Python libraries, reads committed archival parts, verifies SHA-256).
3. Install packages: `pip install -r requirements.txt`
4. Launch Jupyter: `jupyter lab analysis.ipynb`
5. Run all cells in order. The restored CSV is in the same directory as the notebook.

Methods, statistical interpretations, figures, and scholarly citations are in `module_summary.pdf`.
