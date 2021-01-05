mutants=["Gd7","Toll9","Toll10b"]
times=["3h","5h"]
gene_names=open("input/geneNames.txt","r")
gene_names=open(gene_names.readline(),"r")
known_targets=open("input/KnownTargets.txt","r")

next(known_targets)
d_genes={}
for line in gene_names.readlines():
	line=line.replace('"', '')
	line=line.strip("\n").split("\t")
	d_genes[line[0]]=line[2]

d_targets={}
for line in known_targets.readlines():
	line=line.strip("\n").split("\t")
	if line[1] not in d_targets.keys():
		d_targets[line[1]]=[line[0]]
	else:
		d_targets[line[1]].append(line[0])


for mutant in mutants:
	for time in times:
		pred=open(f'input/Predictions_{mutant}_{time}.txt',"r")
		out=open(f'output/out_{mutant}_{time}.txt',"w")
		out.write('Chr\tStart\tEnd\tTarget\tScore\tIM_PET\n')
		overlap_mutant_enhancers=open(f'output/overlap_{mutant}_{time}_enhancers.txt',"r")
		next(pred)
		next(overlap_mutant_enhancers)

		en=[]

		for line in overlap_mutant_enhancers.readlines():
			line=line.strip("\n").split(" ")
			en.append(int(line[2]))
		c=1
		for line in pred.readlines():
			line=line.strip("\n").split("\t")
			line.append('0')
			if line[3] in d_genes.keys():
				line[3]=d_genes[line[3]]
			if c in en:
				if line[3] in d_targets[mutant]:
					line[5]='1'
			# print(line)
			out.write('\t'.join(line)+'\n')
			c+=1
