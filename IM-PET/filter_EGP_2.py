mutants=["Gd7","Toll9","Toll10b"]
times=["3h","5h"]
# predictions=open("Predictions.txt","w")
# predictions.write("Mutant\tTime\tChr\tStart\tEnd\tTarget\tScore\n")
gene_names=open("geneNames.txt","r")
known_targets=open("KnownTargets.txt","r")

next(known_targets)
d_genes={}
for line in gene_names.readlines():
	line=line.replace('"', '')
	line=line.strip("\n").split("\t")
	d_genes[line[0]]=line[2]
# print(d_genes)

list_targets=[]
for line in known_targets.readlines():
	line=line.strip("\n").split("\t")
	list_targets.append([line[0],line[1]])

for mutant in mutants:
	for time in times:
		pred=open(f'Predictions_IM-PET/Predictions_{mutant}_{time}.txt',"r")
		out=open(f'out_{mutant}_{time}.txt',"w")
		out.write('Chr\tStart\tEnd\tTarget\tScore\tIM_PET\n')
		if mutant=="Gd7":
			enhancers=open("h3k27ac_gd7_csaw_intersect.bed","r")
		elif mutant=="Toll9":
			enhancers=open("h3k27ac_Tollrm910_csaw_intersect.bed","r")
		elif mutant=="Toll10b":
			enhancers=open("h3k27ac_Toll10B_csaw_intersect.bed","r")
		overlap_mutant_enhancers=open(f'overlap_{mutant}_{time}_enhancers.txt',"r")

		next(pred)
		next(overlap_mutant_enhancers)

		pr=[]
		for line in pred.readlines():
			line=line.strip("\n").split("\t")
			if line[3] in d_genes.keys():
				line[3]=d_genes[line[3]]
				pr.append(line)
			else:
				pr.append(line)

		en=[]

		for line in enhancers.readlines():
			line=line.strip("\n").split("\t")
			en.append(line)

		for line in overlap_mutant_enhancers.readlines():
			line=line.strip("\n").split(" ")
			line=[int(line[1]),int(line[2])]
			chrom=pr[line[1]-1][0]
			start=en[line[0]-1][1]
			end=en[line[0]-1][2]
			target=pr[line[1]-1][3]
			score=pr[line[1]-1][4]
			list_line=[]
			list_line=[mutant,time,chrom,start,end,target,score,0]
			for i in list_targets:
				if mutant==i[1] and target in i:
					list_line[7]=1
			out.write(f'{list_line[2]}\t{list_line[3]}\t{list_line[4]}\t{list_line[5]}\t{list_line[6]}\t{list_line[7]}\n')
	
