from lingpy import *

def readContent(filename):
    f = open(filename, "r", encoding='utf-8-sig')
    content = f.read()
    f.close()

    return content

def allign(word1, word2, word3):
    return tuple(mult_align([word1, word2, word3]))

def buildDict(c1, c2, c3):
    d = {}
    d[c1] = 1
    
    if c2 in d:
        d[c2] += 1
    else:
        d[c2] = 1

    if c3 in d:
        d[c3] += 1
    else:
        d[c3] = 1

    return d

def dictMax(d):
    maxx = 0
    c = '-'

    for k in d:
        if k != '-' and d[k] > maxx:
            maxx = d[k]
            c = k
    
    return maxx, c

def majority(c1, c2, c3):
    d = buildDict(c1, c2, c3)

    if '-' not in d or d['-'] == 1:
        maxx, c = dictMax(d)
        return c
    else:
        if c1 != '-':
            return c1
        elif c2 != '-':
            return c2
        else:
            return c3
    
def vote(word1, word2, word3):
    (w1, w2, w3) = allign(word1, word2, word3)
    result = ""

    for i in range(len(w1)):
        result += majority(w1[i], w2[i], w3[i])
    
    return result

def getResult(str1, str2, str3):
    tokens1 = str1.split(" ")
    tokens2 = str2.split(" ")
    tokens3 = str3.split(" ")

    if len(tokens1) == len(tokens2) and len(tokens1) == len(tokens3):
        result = ""
        
        for i in range(len(tokens1)):
            result += vote(tokens1[i], tokens2[i], tokens3[i]) + " "
        
        result = result[:-1]

        return result
    else:
        return "NOT IMPLEMENTED YEET"

def getSolution(fileName1, fileName2, fileName3):
    return getResult(readContent(fileName1), readContent(fileName2), readContent(fileName3))