# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------------
#Author_ Rafael Leon
# tis but a data analysis program using nltk for the ehealth project StressTest
# we say Ni!
#--------------------------------------------------------------------------------
#Function Module

#Function block para fetchear de la base de datos todos los cosos y guardarlos en listas

import nltk

def getAllText(conn):
    cur = conn.cursor()
    try:
        sql= "SELECT * FROM `comments` "
        cur.execute(sql)
        results = cur.fetchall()
        resultList = []
        for row in results:
            identifier = row[0]
            comment = row[1]

            tempResult = [identifier, comment]

            resultList.append(tempResult)
        return resultList
    except:
        err = "Error: unable to fetch data"
        return err

def getControlText(conn):
    cur = conn.cursor()
    try:
        sql = "SELECT * FROM `comments` WHERE `tipo` LIKE 'control' "
        cur.execute(sql)
        results = cur.fetchall()
        resultList = []
        for row in results:
            identifier = row[0]
            comment = row[1]

            tempResult = [identifier, comment]
            resultList.append(tempResult)
        return resultList
    except:
        err = "Error: unable to fetch data"
        return err

def getStressText(conn):
    cur = conn.cursor()
    try:
        sql = "SELECT * FROM `comments` WHERE `tipo` LIKE 'stress' "
        cur.execute(sql)
        results = cur.fetchall()
        resultList = []
        for row in results:
            identifier = row[0]
            comment = row[1]
            tempResult = [identifier, comment]
            resultList.append(tempResult)
        return resultList
    except:
        err = "Error: unable to fetch data"
        return err


def tokenizeShit(list):
    fullString = ""
    for i in list:
        tempString = i[1] + " . "
        fullString = fullString + tempString
        fullToken = nltk.word_tokenize(fullString)
    return fullToken
def tokenizeSentences(list):
    fullString = ""
    for i in list:
        tempString = i[1] + " . "
        fullString = fullString + tempString
        fullToken = nltk.sent_tokenize(fullString)
    return fullToken

def getWords(tokens):
    vocab = set([word.lower() for word in tokens if word.isalpha()])
    return vocab

def wordRepeat(tokens):
    fDist = nltk.FreqDist(word.lower() for word in tokens if (word.isalpha() and (len(word) >= 5)))
    fDist.plot(50)
    return fDist

def vocabRepeatPercent(basicDBinput):
    indivTokenList = []
    vocabRepeatPercentage = []
    for i in basicDBinput:
        tempString= i[1]
        tempTokenList= nltk.word_tokenize(tempString)
        indivTokenList.append(tempTokenList)
    for i in indivTokenList:
        tempVocab = getWords(i)
        if (len(i) != 0):
            #print(len(tempVocab))
            #print(len(i))
            repeatPercent =100-((len(tempVocab)/float(len(i))*100))
            vocabRepeatPercentage.append(repeatPercent)
    return vocabRepeatPercentage

def dispersionPlot(basicDBinput, dispersionWords):
    indivTokenList =[]
    for i in basicDBinput:
        tempString = i[1]
        tempTokenList = nltk.word_tokenize(tempString)
        indivTokenList.append(tempTokenList)
    for i in indivTokenList:
        if (len(i) != 0):
            tempText = nltk.Text(i)
            tempText.dispersion_plot(dispersionWords)

def sentenceLengthList(basicDBinput):
    todoSentences = tokenizeSentences(basicDBinput)
    sentenceLengthLong = []
    for i in todoSentences:
        if (len(i)>60 and len(i)<100):
            sentenceLengthLong.append(len(i))

    return sentenceLengthLong

def commentLength(basicDBinput):
    indivTokenList =[]
    tokenLengthList= []
    for i in basicDBinput:
        tempString = i[1]
        tempTokenList = nltk.word_tokenize(tempString)
        indivTokenList.append(tempTokenList)
    for i in indivTokenList:
        if (len(i) != 0):
            tokenLengthList.append(len(i))
    return tokenLengthList
