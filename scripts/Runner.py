# DONE
from os import listdir
from os.path import isfile, join
import os
import numpy as np
import FineReaderRunner as frr
import TesseractRunner as tr
import OcropusRunner as ocr
import EvalRunner as er
import Voter as vo

Tesseract_Tag = "TS"
FineReader_Tag = "FR"
Ocropus_Tag = "OP"
Our_Tag = "ACI"

# utlitary function
# retrieves all the filenames from a given path
def getFilesFromPath(path):
    return [f for f in listdir(path) if isfile(join(path, f))]

# utlitary function
# print the prgress while running the OCR tools
def printProgress(current, count):
    os.system("cls")
    print("Image " + str(current) + " / " + str(count))

# the function run all the OCR tools
def run(inputPath, outputPath):
    inputFiles = getFilesFromPath(inputPath)
    count = len(inputFiles)
    current = 1

    for inputImage in inputFiles:
        printProgress(current, count)
        baseName = inputImage.split('.')[0]
        tr.run(inputPath + inputImage, outputPath + baseName + "_" + Tesseract_Tag + ".txt")
        frr.run(inputPath + inputImage, outputPath + baseName + "_" + FineReader_Tag + ".txt")
        ocr.run(inputPath + inputImage, outputPath + baseName + "_" + Ocropus_Tag + ".txt")
        current += 1


def reportResult(data):
    mean = np.mean(data)
    std = np.std(data)

    return mean, std

# wrapper for the evaluation module functionalities
def evaluate(path, refsPath, words=False):
    outputs = getFilesFromPath(path)
    data = []

    for output in outputs:
        # f = open(path+output, "r")
        # line = f.readline()

        refFile = 'target' + output.split('_')[0].split('image')[1] + '.txt'
        report = er.eval(refsPath+refFile, path+output, words)
        data.append(report[2])

    mean, std = reportResult(data)
    print(str(mean) + " " + str(std))

# wrapper for the evaluation module functionalities
def evaluateLevensthein(path, refsPath):
    outputs = getFilesFromPath(path)
    data = []

    for output in outputs:
        refFile = 'target' + output.split('_')[0].split('image')[1] + '.txt'
        result = er.evalLevensthein(refsPath+refFile, path+output)
        data.append(result)

    mean, std = reportResult(data)
    print(str(mean) + " " + str(std))

# wrapper for the voting module functionalities
def vote(ocrTool1, ocrTool2, ocrTool3, outputPath, priorities):
    path1 = outputPath + ocrTool1 + '/'
    path2 = outputPath + ocrTool2 + '/'
    path3 = outputPath + ocrTool3 + '/'
    outputs = getFilesFromPath(path1)

    for output in outputs:
        out1 = output
        out2 = output.split('_')[0] + '_' + ocrTool2 + '.txt'
        out3 = output.split('_')[0] + '_' + ocrTool3 + '.txt'
        vo.getSolution(path1 + out1, path2 + out2, path3 + out3, outputPath + Our_Tag + "/", priorities)

# save outputs to compare visually
def saveOutputs(outputPath1, outputPath2, outputPath3, outputPath4):
    outputs1 = getFilesFromPath(outputPath1)
    outputs2 = getFilesFromPath(outputPath2)
    outputs3 = getFilesFromPath(outputPath3)
    outputs4 = getFilesFromPath(outputPath4)

    data = []

    for i in range(len(outputs1)):
        f1 = open(outputPath1+outputs1[i], "r")
        f2 = open(outputPath2+outputs2[i], "r")
        f3 = open(outputPath3+outputs3[i], "r")
        f4 = open(outputPath4+outputs4[i], "r")

        c1 = f1.readline()
        c2 = f2.readline()
        c3 = f3.readline()
        c4 = f4.readline()
        
        print(outputs1[i] + " " + outputs2[i] + " " + outputs3[i] + " " + outputs4[i] + "\n")
        print("TS: " + c1)
        print("FR: " + c2)
        print("OC: " + c3)
        print("AC: " + c4)
        print("=============================================================")

        f1.close()
        f2.close()
        f3.close()
        f4.close()