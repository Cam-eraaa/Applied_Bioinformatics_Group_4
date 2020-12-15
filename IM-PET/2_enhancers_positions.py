from operator import itemgetter
pred_gd7=open("input/Predictions_Gd7.txt","r")
pred_gd7=open(pred_gd7.readline(),"r")
pred_toll9=open("input/Predictions_Toll9.txt","r")
pred_toll9=open(pred_toll9.readline(),"r")
pred_toll10b=open("input/Predictions_Toll10b.txt","r")
pred_toll10b=open(pred_toll10b.readline(),"r")

liste_chr=["chr2L","chr2R","chr3L","chr3R","chr4","chrX","chrY"]
l_gd7=[]
l_toll9=[]
l_toll10b=[]

CRM_gd7=open("output/CRM_Gd7.txt","w")
CRM_toll9=open("output/CRM_Toll9.txt","w")
CRM_toll10b=open("output/CRM_Toll10b.txt","w")

for line in pred_gd7.readlines():
	line=line.strip("\n").split("\t")
	l_gd7.append([line[0],int(line[1])-1000,int(line[1])+1000])

for line in pred_toll9.readlines():
	line=line.strip("\n").split("\t")
	l_toll9.append([line[0],int(line[1])-1000,int(line[1])+1000])

for line in pred_toll10b.readlines():
	line=line.strip("\n").split("\t")
	l_toll10b.append([line[0],int(line[1])-1000,int(line[1])+1000])

l2_gd7=sorted(l_gd7, key=itemgetter(1))
l2_gd7=sorted(l2_gd7, key=itemgetter(0))
l2_toll9=sorted(l_toll9, key=itemgetter(1))
l2_toll9=sorted(l2_toll9, key=itemgetter(0))
l2_toll10b=sorted(l_toll10b, key=itemgetter(1))
l2_toll10b=sorted(l2_toll10b, key=itemgetter(0))
for i in l2_gd7:
	CRM_gd7.write(f'{i[0]}\t{i[1]}\t{i[2]}\n')
for i in l2_toll9:
	CRM_toll9.write(f'{i[0]}\t{i[1]}\t{i[2]}\n')
for i in l2_toll10b:
	CRM_toll10b.write(f'{i[0]}\t{i[1]}\t{i[2]}\n')
