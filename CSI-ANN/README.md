This file contains all the information on how to obtain the required files for CSI-ANN in the context of our project on three mutants of Drosophila.
Note about the input files: they contain paths to the required files that are in the GitHub, they will have to be modified to have the correct path on your computer. The same goes to the paths put in the histones files.
The new files will be contained in a new folder called "output"

Step 1: 1_select_TP.py (time ~0.2 sec)\
From a list of enhancers that we consider true, we extract the chromosome and the position and put it in a file for each mutant.\
Input:
- h3k27ac_Toll10B_csaw_intersect.bed
- h3k27ac_Tollrm910_csaw_intersect.bed
- h3k27ac_gd7_csaw_intersect.bed\

Output:
- enhancers_Gd7.txt
- enhancers_Toll9.txt
- enhancers_Toll10b.txt

Step 2_1: 2_1_H3K27ac.py (time ~18.1 sec)\
From the data that is available to us, we create a bedGraph file.\
Input:
- H3K27ac.counts.QC.tab.txt
- H3K27ac.peak.QC.tab.txt\

Output:
- H3K27ac_Gd7.bedGraph
- H3K27ac_Toll9.bedGraph
- H3K27ac_Toll10b.bedGraph

Step 2_2: 2_2_CBP.py (time ~42.6 sec)\
From the data that is available to us, we create a bedGraph file.\
Input:
- CBP-CBP_dm6.featureCount.tab.txt
- CBP.CBP.counts.QC.tab.txt\

Output:
- CBP_Gd7.bedGraph
- CBP_Toll9.bedGraph
- CBP_Toll10b.bedGraph

Step 3: 3_bed_to_wig.R (time ~1.30 min)\
From the output of the previous steps, we convert the bedGraph files into wig files.\
Input:
- H3K27ac_Gd7.wig
- H3K27ac_Toll9.wig
- H3K27ac_Toll10b.wig
- CBP_Gd7.wig
- CBP_Toll9.wig
- CBP_Toll10b.wig\

Output:
- H3K27ac_Gd7.wig
- H3K27ac_Toll9.wig
- H3K27ac_Toll10b.wig
- CBP_Gd7.wig
- CBP_Toll9.wig
- CBP_Toll10b.wig

Step 4: 4_histones.py (time ~0.4 sec)\
Creates a file for each mutant with the paths for each wig file of the said mutant.\
Output:
- histones_Gd7.txt
- histones_Toll9.txt
- histones_Toll10b.txt
