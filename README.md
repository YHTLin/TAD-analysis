# TAD-analysis
Effect of the size of copy number variations on topologically associated domain formation.

## Motivation
Topologically associated domains (TADs) are contiguous segments of DNA that interact and cluster closely inside the nuclear space. It is thought that the TAD architecture is responsible for gene regulation and are often rewired in the event of large genomic perturbations, e.g. copy number variations (CNVs). Given this information, we hypothesize that CNVs that cross TAD boundaries are more likely to contribute to diesase because such changes may disrupt normal TAD formation leading to dysregulated gene expression. If our hypothesis holds, then it would follow that patients carrying larger CNVs have a greater likelihood of contracting disease. To evaluate this prediction statistically, we first assume that a CNV of any given size can occur anywhere on a chromosome of interest with equal probability. The script below then calculates the percentage of times a copy number alteration would overlap at least one TAD boundary.

## File Description
+ *chromosomeLengths.txt*: Text file containing the length of each chromosome.
+ *Domain Boundaries.xls*: Excel file (xls) containing TAD boundaries.
+ *CNV_Analysis2.py*: Python script for performing analysis.
+ *CNV_Analysis.py*: Script written by Jacob and used as the basis for version 2.

## Usage
Download and save files in the same directory. Load *CNV_Analysis2.py* into Python 2.7 for analysis.
+ May need to install *xlrd* package for working with Excel files. Go to command prompt and type *[python2.7 directory]\python.exe -m pip install xlrd*.
