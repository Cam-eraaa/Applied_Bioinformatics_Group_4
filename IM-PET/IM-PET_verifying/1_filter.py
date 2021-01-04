mutants=["Gd7","Toll9","Toll10b"]
times=["3h","5h"]
for mutant in mutants:
	for time in times:
		f=open(f'input/Predictions_{mutant}_{time}.txt','r')
		next(f)
		nf=open(f'output/filtered_Predictions_{mutant}_{time}.txt','w')
		for line in f.readlines():
			line=line.strip("\n").split("\t")
			line[0]=line[0][3:]
			nf.write(f'{line[0]}\t{line[1]}\t{line[2]}\t{line[3]}\t{line[4]}\n')
