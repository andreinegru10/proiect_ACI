#DONE
from lingpy import *
import os

LITTLE = 'abcdefghijklmnopqrstuvwxyz'
BIG = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
DIGITS = '0123456789'
SYMBOLS = '!$%-,.;\'?/'
SPACES = ' \t'
ALPHABET = LITTLE + BIG + DIGITS + SPACES

# the function is used to preprocess the inputs
def preprocess(content):
    result = ''

    for c in content:
        if c in ALPHABET:
            result += c
    
    result = result.replace('\t', ' ')
    result = ' '.join(result.split())
    result = result.strip()

    return result

# the function reads and returns the content of a given text file
def readContent(filename):
    f = open(filename, "r", encoding='utf-8-sig')
    content = preprocess(f.read())
    f.close()

    return content

# function is used to allign 3 words
def allign(word1, word2, word3):
    return tuple(mult_align([word1, word2, word3]))

# the function is used to allign 3 lines of text
def allign2(inputLine1, inputLine2, inputLine3):
    f1 = open("temp1.txt", "w")
    f2 = open("temp2.txt", "w")
    f3 = open("temp3.txt", "w")
    f1.write(inputLine1)
    f2.write(inputLine2)
    f3.write(inputLine3)
    f1.close()
    f2.close()
    f3.close()
    command = 'bash -c "synctext temp1.txt temp2.txt temp3.txt > allign.txt"'
    os.system(command)
    
    f = open("allign.txt", "r")
    lines = f.readlines()
    f.close()

    baseText = lines[2]
    line1 = baseText
    line2 = baseText
    line3 = baseText

    l1 = []
    l2 = []
    l3 = []

    for i in range(3, len(lines)):
        line = lines[i]
        r = ""

        if "temp1.txt" in line:
            r = line.split(" ")[1].replace("\n", "")
            l1.append(r)
        
        if "temp2.txt" in line:
            r = line.split(" ")[1].replace("\n", "")
            l2.append(r)

        if "temp3.txt" in line:
            r = line.split(" ")[1].replace("\n", "")
            l3.append(r)

    for i in range(len(l1)):
        e1 = l1[i].replace("{", "").replace("}", "")
        e2 = l2[i].replace("{", "").replace("}", "")
        e3 = l3[i].replace("{", "").replace("}", "")

        len1 = len(e1)
        len2 = len(e2)
        len3 = len(e3)
        maxim = max(len1, len2, len3)

        if len1 != len2 or len2 != len3 or len1 != len3:
            if len1 == 0:
                e1 = "#" * maxim
            
            if len2 == 0:
                e2 = "#" * maxim
            
            if len3 == 0:
                e3 = "#" * maxim

            if len(e1) == len(e2) and len(e2) == len(e3):
                e1 = e1.replace("#", "-")
                e2 = e2.replace("#", "-")
                e3 = e3.replace("#", "-")
            else:
                if len(e1) > 1 or len(e2) > 1 or len(e3) > 1:
                    (e1, e2, e3) = tuple(mult_align([e1, e2, e3]))
                    e1 = "".join(e1)
                    e2 = "".join(e2)
                    e3 = "".join(e3)

        line1 = line1.replace("{"+str(i+1)+"}", e1)
        line2 = line2.replace("{"+str(i+1)+"}", e2)
        line3 = line3.replace("{"+str(i+1)+"}", e3)

    m = max(len(line1), len(line2), len(line3))
    line1 = line1.ljust(m, '-')
    line2 = line2.ljust(m, '-')
    line3 = line3.ljust(m, '-')

    os.system("del temp1.txt")
    os.system("del temp2.txt")
    os.system("del temp3.txt")
    os.system("del allign.txt")

    return (line1, line2, line3)

# character frequency dictionary
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

# the function retrieves the predominant character in a character frequency dictionary
def dictMax(d):
    maxx = 0
    c = '-'

    for k in d:
        if k != '-' and d[k] > maxx:
            maxx = d[k]
            c = k
    
    return maxx, c

# the function returns the predominat character of the 3 inputs
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

# function used for voring at word level    
def vote(word1, word2, word3):
    (w1, w2, w3) = allign(word1, word2, word3)
    result = ""

    for i in range(len(w1)):
        result += majority(w1[i], w2[i], w3[i])
    
    return result

# function used for voting at line level 
def vote2(line1, line2, line3):
    (w1, w2, w3) = allign2(line1, line2, line3)
    result = ""

    for i in range(len(w1)):
        result += majority(w1[i], w2[i], w3[i])
    
    return result

# the main function of the module
def getResult(str1, str2, str3):
    # split textlines into words
    tokens1 = str1.split(" ")
    tokens2 = str2.split(" ")
    tokens3 = str3.split(" ")

    # check if the number of words is equal
    if len(tokens1) == len(tokens2) and len(tokens1) == len(tokens3):
        result = ""
        
        for i in range(len(tokens1)):
            result += vote(tokens1[i], tokens2[i], tokens3[i]) + " "
        
        result = result[:-1]

        return result
    # special case
    else:
        return vote2(str1, str2, str3)

# auxiliary method; reads file contents and writes final result
def getSolution(fileName1, fileName2, fileName3, outputPath):
    baseFileName = fileName1.split('/')[-1].split('_')[0]
    result = getResult(readContent(fileName1), readContent(fileName2), readContent(fileName3))
    # write the final result to a text file
    f = open(outputPath + baseFileName + '_ACI.txt', "w")
    f.write(result)
    f.close()