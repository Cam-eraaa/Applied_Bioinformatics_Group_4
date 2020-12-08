Gd7_3h=open("Predictions_IM-PET/Predictions_Gd7_3h.txt","r")
Gd7_5h=open("Predictions_IM-PET/Predictions_Gd7_3h.txt","r")
Toll9_3h=open("Predictions_IM-PET/Predictions_Toll9_3h.txt","r")
Toll9_5h=open("Predictions_IM-PET/Predictions_Toll9_5h.txt","r")
Toll10b_3h=open("Predictions_IM-PET/Predictions_Toll10b_3h.txt","r")
Toll10b_5h=open("Predictions_IM-PET/Predictions_Toll10b_5h.txt","r")

next(Gd7_3h)
next(Gd7_5h)
next(Toll9_3h)
next(Toll9_5h)
next(Toll10b_3h)
next(Toll10b_5h)

new_Gd7_3h=open("new_Predictions_Gd7_3h.txt","w")
new_Gd7_5h=open("new_Predictions_Gd7_5h.txt","w")
new_Toll9_3h=open("new_Predictions_Toll9_3h.txt","w")
new_Toll9_5h=open("new_Predictions_Toll9_5h.txt","w")
new_Toll10b_3h=open("new_Predictions_Toll10b_3h.txt","w")
new_Toll10b_5h=open("new_Predictions_Toll10b_5h.txt","w")

for line in Gd7_3h.readlines():
	line=line.strip("\n").split("\t")
	line[0]=line[0][3:]
	new_Gd7_3h.write(f'{line[0]}\t{line[1]}\t{line[2]}\t{line[3]}\t{line[4]}\n')

for line in Gd7_5h.readlines():
	line=line.strip("\n").split("\t")
	line[0]=line[0][3:]
	new_Gd7_5h.write(f'{line[0]}\t{line[1]}\t{line[2]}\t{line[3]}\t{line[4]}\n')

for line in Toll9_3h.readlines():
	line=line.strip("\n").split("\t")
	line[0]=line[0][3:]
	new_Toll9_3h.write(f'{line[0]}\t{line[1]}\t{line[2]}\t{line[3]}\t{line[4]}\n')

for line in Toll9_5h.readlines():
	line=line.strip("\n").split("\t")
	line[0]=line[0][3:]
	new_Toll9_5h.write(f'{line[0]}\t{line[1]}\t{line[2]}\t{line[3]}\t{line[4]}\n')

for line in Toll10b_3h.readlines():
	line=line.strip("\n").split("\t")
	line[0]=line[0][3:]
	new_Toll10b_3h.write(f'{line[0]}\t{line[1]}\t{line[2]}\t{line[3]}\t{line[4]}\n')

for line in Toll10b_5h.readlines():
	line=line.strip("\n").split("\t")
	line[0]=line[0][3:]
	new_Toll10b_5h.write(f'{line[0]}\t{line[1]}\t{line[2]}\t{line[3]}\t{line[4]}\n')