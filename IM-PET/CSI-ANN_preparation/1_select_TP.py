mutants=["h3k27ac_Toll10B_csaw_intersect.bed","h3k27ac_Tollrm910_csaw_intersect.bed","h3k27ac_gd7_csaw_intersect.bed"]
for mutant in mutants:
	f=open(f'input/{mutant}',"r")
	f=open(f.readline(),"r")
	if mutant=="h3k27ac_Toll10B_csaw_intersect.bed":
		name_mutant="Toll10b"
	elif mutant=="h3k27ac_Tollrm910_csaw_intersect.bed":
		name_mutant="Toll9"
	elif mutant=="h3k27ac_gd7_csaw_intersect.bed":
		name_mutant="Gd7"
	nf=open(f'output/enhancers_{name_mutant}.txt',"w")
	for line in f.readlines():
		line=line.strip("\n").split('\t')
		position=(int(line[1])+int(line[2]))/2
		nf.write(f'{line[0]}\t{int(position)}\n')
