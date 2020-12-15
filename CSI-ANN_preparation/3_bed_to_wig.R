library(GenomicRanges)
library(rtracklayer)

bg <- import("output/CBP_Gd7.bedGraph")
gp <- GPos(bg) # unfortunately need to carry over metadata manually
score(gp) <- rep(score(bg), width(bg))
export(gp, "output/CBP_Gd7.wig")

bg <- import("output/CBP_Toll9.bedGraph")
gp <- GPos(bg) # unfortunately need to carry over metadata manually
score(gp) <- rep(score(bg), width(bg))
export(gp, "output/CBP_Toll9.wig")

bg <- import("output/CBP_Toll10b.bedGraph")
gp <- GPos(bg) # unfortunately need to carry over metadata manually
score(gp) <- rep(score(bg), width(bg))
export(gp, "output/CBP_Toll10b.wig")

bg <- import("output/H3K27ac_Gd7.bedGraph")
gp <- GPos(bg) # unfortunately need to carry over metadata manually
score(gp) <- rep(score(bg), width(bg))
export(gp, "output/H3K27ac_Gd7.wig")

bg <- import("output/H3K27ac_Toll9.bedGraph")
gp <- GPos(bg) # unfortunately need to carry over metadata manually
score(gp) <- rep(score(bg), width(bg))
export(gp, "output/H3K27ac_Toll9.wig")

bg <- import("output/H3K27ac_Toll10b.bedGraph")
gp <- GPos(bg) # unfortunately need to carry over metadata manually
score(gp) <- rep(score(bg), width(bg))
export(gp, "output/H3K27ac_Toll10b.wig")