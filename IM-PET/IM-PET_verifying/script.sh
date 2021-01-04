#!/bin/bash
mkdir output
mkdir images
#Step 1
python3 1_filter.py

#Step 2
Rscript 2_overlapping.R

#Step 3
python3 3_find_TP.py

#Step 4
Rscript 4_ROC.R

rm output/filtered_Predictions_*
rm output/overlap_*