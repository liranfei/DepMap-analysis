# DepMap Lineage-Specific Dependency Analysis
This repository contains code for the paper:
"A Selectivity-Based Computational Framework for Identifying Lineage-Specific Cancer Dependencies from DepMap Data"

## System Requirements
- Python 3.8+
- 8GB RAM (16GB recommended)

## Installation
git clone https://github.com/liranfei/DepMap-analysis.git
cd DepMap-analysis
pip install -r requirements.txt

## Data
DepMap 22Q1 data available at https://depmap.org/portal/download/
Required files:
- CRISPRGeneEffect.csv
- sample_info.csv

## Reproduce Analysis
python scripts/01_data_preprocessing.py
python scripts/02_gene_selection.py --top_n 500
python scripts/03_selectivity_analysis.py
python scripts/04_statistical_testing.py --q_threshold 0.05

## Key Parameters
- Chronos < -1.0
- Selectivity < -0.3
- Top 500 variable genes
- Wilcoxon test + Benjamini-Hochberg FDR < 0.05

## Results
- 1,991 candidate pairs
- 87 significant pairs (q < 0.05)
- Top target: ABL1 in myeloproliferative neoplasms
