#DONE
import os

EXE = "tesseract"
LANG = ""
PSM = "--psm 3"
DPI = "--dpi 300"

def run(inputImage, outputFile):
    command = EXE + " " + inputImage + " " + outputFile + " "
    command += LANG + " " + PSM + " " + DPI + " >nul 2>&1"
    os.system(command)
    cleanOutput(outputFile + ".txt")
    return outputFile

def cleanOutput(outputFile):
    #read content
    fileIn = open(outputFile, "r")
    linesIn = fileIn.read()
    fileIn.close()
    # update content
    fileOut = open(outputFile, "w")
    fileOut.write(linesIn.split("\n")[0])
    fileOut.close()