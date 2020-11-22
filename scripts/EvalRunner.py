import os

WORDS_ACC_EXE = "wordacc"
CHARS_ACC_EXE = "accuracy"
DEFAULT_OUTPUT = "./report.txt"

def evalWords(correct, generated):
    command = WORDS_ACC_EXE + " " + correct + " " + generated + " " + DEFAULT_OUTPUT
    command = "bash -c \"" + command + "\""
    os.system(command)

def evalCharacters(correct, generated):
    command = CHARS_ACC_EXE + " " + correct + " " + generated + " " + DEFAULT_OUTPUT
    command = "bash -c \"" + command + "\""
    os.system(command)

def eval(correctFile, generatedFile, words=False):
    
    if words:
        evalWords(correctFile, generatedFile)
    else:
        evalCharacters(correctFile, generatedFile)
    
    # do something with output file
    # clean out file