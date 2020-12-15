#!/bin/bash
#Step 0
mkdir output

#Step 1
python3 1_chr_files.py

#Step 2
python3 2_enhancers_positions.py

#Step 3
python3 3_1_counts.py
Rscript 3_2_FPKM.R
python3 3_3_separate_FPKM.py

#Step 4
python3 4_other_files.py

rm output/counts.txt
rm output/gene_expr.txt
