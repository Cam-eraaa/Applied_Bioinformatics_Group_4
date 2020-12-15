This folder contains all the necessary steps to creating the files of IM-PET. Just like for CSI-ANN, the content of the input files will have to be changed with the path of the concerned files in your own computer.

Step 1: 1_chr_files.py (time ≈65 sec)
Input:
- ANNoutput_Gd7
- ANNoutput_Toll9
- ANNoutput_Toll10b
Output:
- chr2L.txt
- chr2R.txt
- chr3L.txt
- chr3R.txt
- chr4.txt
- chrX.txt
- chrY.txt

Step 2: 2_enhancers_positions.py (time ≈0.2 sec)
Input:
- Predictions_Gd7.txt
- Predictions_Toll9.txt
- Predictions_Toll10b.txt
Output:
- CRM_Gd7.txt
- CRM_Toll9.txt
- CRM_Toll10b.txt

Step 3_1: 3_1_counts.py (time ≈37.4 sec)
Input:
- counts.CDS.txt
- counts.QC.tab.txt
Output:
- counts.txt

Step 3_2: 3_2_FPKM.R (time ≈1.4 sec)
Input:
- counts.txt
Output:
- gene_expr.txt

Step 3_3: 3_3_separate_FPKM.py (time ≈0.5 sec)
Input:
- gene_expr.py
Output:
- Gd7_3h_expr.txt
- Gd7_5h_expr.txt
- Toll9_3h_expr.txt
- Toll9_5h_expr.txt
- Toll10b_3h_expr.txt
- Toll10b_5h_expr.txt

Step 4: 4_other_files.py (time ≈37.8 sec)
Input:
- counts.CDS.txt
- gene_expr.txt
Output:
- transcript_Gd7_3h.gtf
- transcript_Gd7_5h.gtf
- transcript_Toll9_3h.gtf
- transcript_Toll9_5h.gtf
- transcript_Toll10b_3h.gtf
- transcript_Toll10b_5h.gtf