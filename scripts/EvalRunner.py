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

def parseReport():
    report = open(DEFAULT_OUTPUT, "r")
    content = report.readlines()
    report.close()

    total = int(list(filter(lambda a: a != "", content[2].split(" ")))[0])
    errors = int(list(filter(lambda a: a != "", content[3].split(" ")))[0])
    accuracy = float(list(filter(lambda a: a != "", content[4].split(" ")))[0].split("%")[0])
    return [total, errors, accuracy]

def eval(correctFile, generatedFile, words=False):
    if words:
        evalWords(correctFile, generatedFile)
    else:
        evalCharacters(correctFile, generatedFile)
    
    report = parseReport()
    os.system("del " + DEFAULT_OUTPUT.replace("/", "\\"))
    
    return report

    # do something with output file
    # clean out file