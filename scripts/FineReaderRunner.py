import os

EXE = "FineCmd.exe"
LANG = "/lang Mixed"
QUIT = "/quit"
OUT = "/out"

def run(inputImage, outputFile):
    command = EXE + " " + inputImage + " " + LANG + " "
    command += OUT + " " + outputFile + " " + QUIT
    os.system(command)
    return outputFile