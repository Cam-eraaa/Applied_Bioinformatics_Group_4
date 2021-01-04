library("heatmaps")
library(patchwork)
library(ROCit)
library(tidyverse)
library(GenomicRanges)

enhancers_Gd7 = read.table(
  file = "/Users/Camille/Desktop/IM-PET_TEST/Applied_Bioinformatics_Group_4/data_johan/results/cleaned/enhancers/h3k27ac_gd7_csaw_intersect.bed",
  quote = "",
  sep = "\t",
  header = F,
  stringsAsFactors = F
)

enhancers_Gd7_Info = enhancers_Gd7 %>% dplyr::rename(
  'Chr' = V1,
  'Start' = V2,
  'End' = V3,
  'Name' = V4,
  'Score' = V5,
  'Strand' = V6
)

enhancers_Gd7_Data = makeGRangesFromDataFrame(enhancers_Gd7_Info,
                                              seqnames.field = "Chr", 
                                              start.field = "Start", 
                                              end.field = "End")
enhancers_Toll9 = read.table(
  file = "/Users/Camille/Desktop/IM-PET_TEST/Applied_Bioinformatics_Group_4/data_johan/results/cleaned/enhancers/h3k27ac_Tollrm910_csaw_intersect.bed",
  quote = "",
  sep = "\t",
  header = F,
  stringsAsFactors = F
)

enhancers_Toll9_Info = enhancers_Toll9 %>% dplyr::rename(
  'Chr' = V1,
  'Start' = V2,
  'End' = V3,
  'Name' = V4,
  'Score' = V5,
  'Strand' = V6
)

enhancers_Toll9_Data = makeGRangesFromDataFrame(enhancers_Toll9_Info,
                                              seqnames.field = "Chr", 
                                              start.field = "Start", 
                                              end.field = "End")

enhancers_Toll10b = read.table(
  file = "/Users/Camille/Desktop/IM-PET_TEST/Applied_Bioinformatics_Group_4/data_johan/results/cleaned/enhancers/h3k27ac_Toll10B_csaw_intersect.bed",
  quote = "",
  sep = "\t",
  header = F,
  stringsAsFactors = F
)

enhancers_Toll10b_Info = enhancers_Toll10b %>% dplyr::rename(
  'Chr' = V1,
  'Start' = V2,
  'End' = V3,
  'Name' = V4,
  'Score' = V5,
  'Strand' = V6
)

enhancers_Toll10b_Data = makeGRangesFromDataFrame(enhancers_Toll10b_Info,
                                                seqnames.field = "Chr", 
                                                start.field = "Start", 
                                                end.field = "End")

Gd7_3h = read.table(
  file = "output/filtered_Predictions_Gd7_3h.txt",
  quote = "",
  sep = "\t",
  header = F,
  stringsAsFactors = F
)

Gd7_3h_Info = Gd7_3h %>% dplyr::rename(
  'Chr' = V1,
  'Start' = V2,
  'End' = V3,
  'Name' = V4,
  'Score' = V5
)

Gd7_3h_Data = makeGRangesFromDataFrame(Gd7_3h_Info,
                                       seqnames.field = "Chr", 
                                       start.field = "Start", 
                                       end.field = "End")

Gd7_5h = read.table(
  file = "output/filtered_Predictions_Gd7_5h.txt",
  quote = "",
  sep = "\t",
  header = F,
  stringsAsFactors = F
)

Gd7_5h_Info = Gd7_5h %>% dplyr::rename(
  'Chr' = V1,
  'Start' = V2,
  'End' = V3,
  'Name' = V4,
  'Score' = V5
)

Gd7_5h_Data = makeGRangesFromDataFrame(Gd7_5h_Info,
                                       seqnames.field = "Chr", 
                                       start.field = "Start", 
                                       end.field = "End")

Toll9_3h = read.table(
  file = "output/filtered_Predictions_Toll9_3h.txt",
  quote = "",
  sep = "\t",
  header = F,
  stringsAsFactors = F
)

Toll9_3h_Info = Toll9_3h %>% dplyr::rename(
  'Chr' = V1,
  'Start' = V2,
  'End' = V3,
  'Name' = V4,
  'Score' = V5
)

Toll9_3h_Data = makeGRangesFromDataFrame(Toll9_3h_Info,
                                       seqnames.field = "Chr", 
                                       start.field = "Start", 
                                       end.field = "End")

Toll9_5h = read.table(
  file = "output/filtered_Predictions_Toll9_5h.txt",
  quote = "",
  sep = "\t",
  header = F,
  stringsAsFactors = F
)

Toll9_5h_Info = Toll9_5h %>% dplyr::rename(
  'Chr' = V1,
  'Start' = V2,
  'End' = V3,
  'Name' = V4,
  'Score' = V5
)

Toll9_5h_Data = makeGRangesFromDataFrame(Toll9_5h_Info,
                                       seqnames.field = "Chr", 
                                       start.field = "Start", 
                                       end.field = "End")

Toll10b_3h = read.table(
  file = "output/filtered_Predictions_Toll10b_3h.txt",
  quote = "",
  sep = "\t",
  header = F,
  stringsAsFactors = F
)

Toll10b_3h_Info = Toll10b_3h %>% dplyr::rename(
  'Chr' = V1,
  'Start' = V2,
  'End' = V3,
  'Name' = V4,
  'Score' = V5
)

Toll10b_3h_Data = makeGRangesFromDataFrame(Toll10b_3h_Info,
                                         seqnames.field = "Chr", 
                                         start.field = "Start", 
                                         end.field = "End")

Toll10b_5h = read.table(
  file = "output/filtered_Predictions_Toll10b_5h.txt",
  quote = "",
  sep = "\t",
  header = F,
  stringsAsFactors = F
)

Toll10b_5h_Info = Toll10b_5h %>% dplyr::rename(
  'Chr' = V1,
  'Start' = V2,
  'End' = V3,
  'Name' = V4,
  'Score' = V5
)

Toll10b_5h_Data = makeGRangesFromDataFrame(Toll10b_5h_Info,
                                         seqnames.field = "Chr", 
                                         start.field = "Start", 
                                         end.field = "End")

overlap_Gd7_3h_enhancers = data.frame(findOverlaps(enhancers_Gd7_Data,Gd7_3h_Data, maxgap = 0))
overlap_Gd7_5h_enhancers = data.frame(findOverlaps(enhancers_Gd7_Data,Gd7_5h_Data, maxgap = 0))
overlap_Toll9_3h_enhancers = data.frame(findOverlaps(enhancers_Toll9_Data,Toll9_3h_Data, maxgap = 0))
overlap_Toll9_5h_enhancers = data.frame(findOverlaps(enhancers_Toll9_Data,Toll9_5h_Data, maxgap = 0))
overlap_Toll10b_3h_enhancers = data.frame(findOverlaps(enhancers_Toll10b_Data,Toll10b_3h_Data, maxgap = 0))
overlap_Toll10b_5h_enhancers = data.frame(findOverlaps(enhancers_Toll10b_Data,Toll10b_5h_Data, maxgap = 0))

write.table(overlap_Gd7_3h_enhancers, "output/overlap_Gd7_3h_enhancers.txt", append = FALSE, sep = " ", dec = ".",
            row.names = TRUE, col.names = TRUE)
write.table(overlap_Gd7_5h_enhancers, "output/overlap_Gd7_5h_enhancers.txt", append = FALSE, sep = " ", dec = ".",
            row.names = TRUE, col.names = TRUE)
write.table(overlap_Toll9_3h_enhancers, "output/overlap_Toll9_3h_enhancers.txt", append = FALSE, sep = " ", dec = ".",
            row.names = TRUE, col.names = TRUE)
write.table(overlap_Toll9_5h_enhancers, "output/overlap_Toll9_5h_enhancers.txt", append = FALSE, sep = " ", dec = ".",
            row.names = TRUE, col.names = TRUE)
write.table(overlap_Toll10b_3h_enhancers, "output/overlap_Toll10b_3h_enhancers.txt", append = FALSE, sep = " ", dec = ".",
            row.names = TRUE, col.names = TRUE)
write.table(overlap_Toll10b_5h_enhancers, "output/overlap_Toll10b_5h_enhancers.txt", append = FALSE, sep = " ", dec = ".",
            row.names = TRUE, col.names = TRUE)
