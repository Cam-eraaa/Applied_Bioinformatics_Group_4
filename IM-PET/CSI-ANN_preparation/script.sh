#!/bin/bash
#Step 0
mkdir output
cp input/hgTables.txt output/genes.txt
#Step 1
python3 1_select_TP.py
#Step 2_1
python3 2_1_H3K27ac.py
#Step 2_2
python3 2_2_CBP.py
#Step 3
Rscript 3_bed_to_wig.R
rm output/*.bedGraph
#Step 4
python3 4_histones.py
