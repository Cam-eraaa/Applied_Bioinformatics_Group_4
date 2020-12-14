mutants=["Gd7","Toll9","Toll10b"]
for mutant in mutants:
	f=open(f"output/histones_{mutant}.txt","w")
	f.write(f"output/CBP_{mutant}.wig\n")
	f.write(f"output/H3K27ac_{mutant}.wig\n")
