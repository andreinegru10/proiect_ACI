#DONE
import os

EXE = "FineCmd.exe"
LANG = "/lang Mixed"
QUIT = "/quit"
OUT = "/out"

def run(inputImage, outputFile):
    command = EXE + " " + inputImage + " " + LANG + " "
    command += OUT + " " + outputFile + " " + QUIT + " >nul 2>&1"
    os.system(command)
    return outputFile