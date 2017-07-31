# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------------
#_Author_ Rafael Leon
# tis but a data analysis program using nltk for the ehealth project StressTest
# we say Ni!
#--------------------------------------------------------------------------------
import pymysql
import StressModule as sm
import nltk
import numpy as np
import matplotlib
hostname = "localhost"
database = "stressdb"
username = "root"
password = ""

myConnection = pymysql.connect(host=hostname, user=username, passwd=password, db=database)

todaLaDB = sm.getAllText(myConnection)
controltext = sm.getControlText(myConnection)
stresstext = sm.getStressText(myConnection)

fullString = ""
FullToken = sm.tokenizeShit(todaLaDB)
controlToken = sm.tokenizeShit(controltext)
stressToken = sm.tokenizeShit(stresstext)

#print (FullToken)
#print (controlToken)
#print (stressToken)

#------------------------------------------------------------------------
#VocabularyBasics
fullvocab=sm.getWords(FullToken)
controlvocab=sm.getWords(controlToken)
stressvocab = sm.getWords(stressToken)
print(len(fullvocab))
print(len(controlvocab))
print(len(stressvocab))
#print (sorted(vocab))

#------------------------------------------------------------------------
#Frequency Distributions
#fullDist= sm.wordRepeat(FullToken)
#controlDist = sm.wordRepeat(controlToken)
#stressDist = sm.wordRepeat(stressToken)

#------------------------------------------------------------------------
#Collocations
fullText = nltk.Text(FullToken)
stressText = nltk.Text(stressToken)
controlText = nltk.Text(controlToken)

fullCollocations = fullText.collocations()
stressCollocations = stressText.collocations()
controlCollocations = controlText.collocations()
#------------------------------------------------------------------------
#stress Repeat Percentages
stressRepeatPerc = sm.vocabRepeatPercent(stresstext)

repeatMean = np.mean(stressRepeatPerc)
repeatSDV = np.std(stressRepeatPerc)
repeatMedian = np.median(stressRepeatPerc)
print("Stress repetition percentages")
print("Mean: "+str(repeatMean)+"%")
print("STDV: "+str(repeatSDV)+"%")
print("Median: "+str(repeatMedian)+"%"+"\n")
#------------------------------------------------------------------------
#Control Repeat Percentages
controlRepeatPerc = sm.vocabRepeatPercent(controltext)


repeatMean = np.mean(controlRepeatPerc)
repeatSDV = np.std(controlRepeatPerc)
repeatMedian = np.median(controlRepeatPerc)

print("Control repetition percentages")
print("Mean: "+str(repeatMean)+"%")
print("STDV: "+str(repeatSDV)+"%")
print("Median: "+str(repeatMedian)+"%"+"\n")
#------------------------------------------------------------------------
#Total Repeat Percentages
totalRepeatPerc = sm.vocabRepeatPercent(todaLaDB)

repeatMean = np.mean(totalRepeatPerc)
repeatSDV = np.std(totalRepeatPerc)
repeatMedian = np.median(totalRepeatPerc)

print("Total data repetition percentages")
print("Mean: "+str(repeatMean)+"%")
print("STDV: "+str(repeatSDV)+"%")
print("Median: "+str(repeatMedian)+"%"+"\n")

#------------------------------------------------------------------------
#10 most common words dispersion plots

fullTextDispersion = ["sonidos", "cambio", "letra", "color", "prueba", "problema", "colores", "ruido","dificil"]
controlTextDispersion = ["prueba", "estaba", "tiempo", "sentí","sonidos", "interesante", "requiere", "analisis", "poder", "presion"]
stressTextDispersion = ["cambio", "sonidos", "letra", "color", "colores", "sonido", "fondo", "ruido", "molesto", "lectura"]

#sm.dispersionPlot(todaLaDB,fullTextDispersion)
#sm.dispersionPlot(controtext, controlTextDispersion)
#sm.dispersionPlot(stresstext, stressTextDispersion)
#------------------------------------------------------------------------
#Sentence length averages
todoLength=sm.sentenceLengthList(todaLaDB)
stressLength=sm.sentenceLengthList(stresstext)
controlLength=sm.sentenceLengthList(controltext)

#------------------------------------------------------------------------
#Todo data
print("Sentence Length data for total entries")
sentLenMean = np.mean(todoLength)
sentLenSDV = np.std(todoLength)
sentLenMedian = np.median(todoLength)


print("Mean: "+str(sentLenMean))
print("STDV: "+str(sentLenSDV))
print("Median: "+str(sentLenMedian)+"\n")

#------------------------------------------------------------------------
#Stress data
print("Sentence Length data for  Stress entries")
sentLenMean = np.mean(stressLength)
sentLenSDV = np.std(stressLength)
sentLenMedian = np.median(stressLength)

print("Mean: "+str(sentLenMean))
print("STDV: "+str(sentLenSDV))
print("Median: "+str(sentLenMedian)+"\n")

#------------------------------------------------------------------------
#Comment Length

#------------------------------------------------------------------------
#Todo data
print("Sentence Length data for total entries")
sentLenMean = np.mean(controlLength)
sentLenSDV = np.std(controlLength)
sentLenMedian = np.median(controlLength)

print("Mean: "+str(sentLenMean))
print("STDV: "+str(sentLenSDV))
print("Median: "+str(sentLenMedian)+"\n")

#------------------------------------------------------------------------
#Control data
print("Sentence Length data for Control entries")
sentLenMean = np.mean(controlLength)
sentLenSDV = np.std(controlLength)
sentLenMedian = np.median(controlLength)

print("Mean: "+str(sentLenMean))
print("STDV: "+str(sentLenSDV))
print("Median: "+str(sentLenMedian)+"\n")
