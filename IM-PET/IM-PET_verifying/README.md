This folder contains all the scripts and inputs necessary to do the verification of the results from IM-PET with the ROC curve. Just like the previous steps with the preparations of the files, some of the input files only contain the path to the real file, this is to avoid duplicating big files and still have them close. Also some scripts might have some links to inputs that do not work if on another computer.

Step 1: 1_filter.py
We start to put our prediction files to the right format for the next step, which isn't much change in reality but it has to be done.

Input:
- Predictions_Gd7_3h.txt
- Predictions_Gd7_5h.txt
- Predictions_Toll9_3h.txt
- Predictions_Toll9_5h.txt
- Predictions_Toll10b_3h.txt
- Predictions_Toll10b_5h.txt

Output:
- filtered_Predictions_Gd7_3h.txt
- filtered_Predictions_Gd7_5h.txt
- filtered_Predictions_Toll9_3h.txt
- filtered_Predictions_Toll9_5h.txt
- filtered_Predictions_Toll10b_3h.txt
- filtered_Predictions_Toll10b_5h.txt

Step 2: 2_overlapping.R
We now want to know which enhancers are overlapping between the prediction and the real enhancers.

Input:
- filtered_Predictions_Gd7_3h.txt
- filtered_Predictions_Gd7_5h.txt
- filtered_Predictions_Toll9_3h.txt
- filtered_Predictions_Toll9_5h.txt
- filtered_Predictions_Toll10b_3h.txt
- filtered_Predictions_Toll10b_5h.txt
- h3k27ac_gd7_csaw_intersect.bed
- h3k27ac_Tollrm910_csaw_intersect.bed
- h3k27ac_Toll10B_csaw_intersect.bed

Output:
- overlap_Gd7_3h_enhancers.txt
- overlap_Gd7_5h_enhancers.txt
- overlap_Toll9_3h_enhancers.txt
- overlap_Toll9_5h_enhancers.txt
- overlap_Toll10b_3h_enhancers.txt
- overlap_Toll10b_5h_enhancers.txt

Step 3: 3_find_TP.py
We want to gather the enhancer gene pairs that overlap with the real enhancers, put the names of the genes when they are in the list and create a new column which contains a 1 if the EGP was found to be a TP, 0 otherwise.

Input:
- Predictions_Gd7_3h.txt
- Predictions_Gd7_5h.txt
- Predictions_Toll9_3h.txt
- Predictions_Toll9_5h.txt
- Predictions_Toll10b_3h.txt
- Predictions_Toll10b_5h.txt
- h3k27ac_gd7_csaw_intersect.bed
- h3k27ac_Tollrm910_csaw_intersect.bed
- h3k27ac_Toll10B_csaw_intersect.bed
- overlap_Gd7_3h_enhancers.txt
- overlap_Gd7_5h_enhancers.txt
- overlap_Toll9_3h_enhancers.txt
- overlap_Toll9_5h_enhancers.txt
- overlap_Toll10b_3h_enhancers.txt
- overlap_Toll10b_5h_enhancers.txt

Output:
- out_Gd7_3h.txt
- out_Gd7_5h.txt
- out_Toll9_3h.txt
- out_Toll9_5h.txt
- out_Toll10b_3h.txt
- out_Toll10b_5h.txt

Step 4: 4_ROC.R
Here we want to make an ROC curve for each mutant for each time and save them in the folder "images". Note: this step still has issues if one of the mutant doesn't have any true positive, the solution to that is to do it manually for now.

Input:
- out_Gd7_3h.txt
- out_Gd7_5h.txt
- out_Toll9_3h.txt
- out_Toll9_5h.txt
- out_Toll10b_3h.txt
- out_Toll10b_5h.txt

Output:
- ROCGd7_3h.jpg
- ROCGd7_5h.jpg
- ROCToll9_3h.jpg
- ROCToll9_5h.jpg
- ROCToll10b_3h.jpg
- ROCToll10b_5h.jpg
