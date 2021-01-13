# NB: change all the paths to the corresponding ones on your computer. IM-PET runs only on Linux.

input_folder=/home/camil/private/Applied_Bioinformatics/IM-PET_Package/INPUT_Drosophila
IM-PET_folder=/home/camil/private/Applied_Bioinformatics/IM-PET_Package
result_folder=/home/camil/private/Applied_Bioinformatics/Results_Drosophila
cd IM-PET_folder

export CLASSPATH=/home/camil/private/Applied_Bioinformatics/IM-PET_Package/weka-3-6-9/weka.jar:$CLASSPATH
./LiftOver_3/liftOver
./ALF_EVO_4/alf –h
java weka.classifiers.trees.RandomForest

for mutant in Gd7 Toll9 Toll10b
do
	for time in 3h 5h
	do
		cp ${input_folder}/transcript_${mutant}_${time}.gtf ${IM-PET_folder}/SelectPromoter_1/transcript.gtf
		perl ${IM-PET_folder}/IM-PET.pl -p ${IM-PET_folder}/ -e ${input_folder}/CRM_${mutant}.txt -s ${input_folder}/ANNoutput_${mutant} -x ${input_folder}/${mutant}_${time}_expr.txt
		mv ${IM-PET_folder}/Predictions.txt ${result_folder}/Predictions_${mutant}_${time}.txt
		rm ${IM-PET_folder}/SelectPromoter_1/transcript.gtf
	done
done
