# DONE
from os import listdir
from os.path import isfile, join
import os
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

# wrapper for the evaluation module functionalities
def evaluate(path, refsPath, words=False):
    outputs = getFilesFromPath(path)
    accSum = 0
    count = 0

    for output in outputs:
        f = open(path+output, "r")
        line = f.readline()

        refFile = 'target' + output.split('_')[0].split('image')[1] + '.txt'
        report = er.eval(refsPath+refFile, path+output, words)
        accSum += report[2]
        count += 1
    
    accAvg = accSum / count
    print(accAvg)

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