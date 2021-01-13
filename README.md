# Applied_Bioinformatics_Group_4

## Vaid et al. approach
The implementing of the Vaid et al. approach can be found in the folder script. 
The identified genes can be found in the file results/original_method/PROseq/PROseq.data.tsv.
The identified enhancers can be found in the file results/altered_method/from_joint_peak.
The pairs found by combinding all enhancers with all genes in results/altered_method/pairs. The result file containing the pairs found with UMAP was too large to upload to GitHub.
The pairs found with the nearest distance method is found in results/altered_method/pairs/nearest_distance.

## IM-PET
The IM-PET and CSI-ANN files are too large to be uploaded on GitHub, therefore it is necessary to download it from the Tan Laboratory website at http://tanlab4generegulation.org/IM-PET.html and http://tanlab4generegulation.org/CSIANNWebpage.html.
The preparation of the files for those two algorithms are located in the folder IM-PET. It is important to note that the scripts and the files that are present there contain paths that have to be adapted your own computer.
The result files from CSI-ANN containing the predictions are located in IM-PET/IM-PET_preparation/input, however the files containing genome wide enhancer signals were too big to be uploaded to GitHub.
The result files from IM-PET can be found in IM-PET/IM-PET_verifying/input, along with the other files that are necessary to the verifying step.
