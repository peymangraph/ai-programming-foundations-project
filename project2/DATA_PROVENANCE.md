# MetroPT-3 source data provenance

Dataset: MetroPT-3 (UCI Machine Learning Repository), https://doi.org/10.24432/C5VW3R.
The official full archive contains 1,516,948 time-series observations. These files
contain a deterministic subset of 30,339 real source rows, selected by original
row position modulo 50 == 0; no data are simulated or generated.

To respect file transport constraints, the CSV has been losslessly compressed
with xz and split into three binary Git blobs under data_parts/. Execute
`python prepare_dataset.py` to recreate exactly
`metropt3_compressor_sample.csv`, then run the Jupyter notebook.

CSV SHA256: 2281e4ad5b677a233c1246ad418e63795ee33d0d2772543ec46455e043de7167
Compressed data SHA256: 6542028b7ce3880b3bcfc5985448de360689de47a6d58afc1f6117aeb12b4a0d

The dataset is distributed by UCI under CC BY 4.0. Refer to the original
repository for source metadata and attribution.
