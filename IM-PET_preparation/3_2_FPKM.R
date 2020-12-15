library(limma)
library(edgeR)
expressioncount <- read.delim("/Users/Camille/Desktop/IM-PET_TEST/Applied_Bioinformatics_Group_4/IM-PET/output/counts.txt", row.names=1)
colnames(expressioncount) <- substring(colnames(expressioncount),1)
dim(expressioncount)
head(expressioncount)
y <- DGEList(expressioncount[,2:7])
keep <- rowSums(cpm(y) > 1) >= 1
y <- calcNormFactors(y)
y$samples
RPKM<-rpkm(y, gene.length=expressioncount$length)
write.table(RPKM, "/Users/Camille/Desktop/IM-PET_TEST/Applied_Bioinformatics_Group_4/IM-PET/output/gene_expr.txt", append = FALSE, sep = " ", dec = ".",
            row.names = TRUE, col.names = TRUE)