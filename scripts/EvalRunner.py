#DONE
import os
import Levenshtein as L

WORDS_ACC_EXE = "wordacc"
CHARS_ACC_EXE = "accuracy"
DEFAULT_OUTPUT = "./report.txt"

# the function computes word level recognition accuracy
def evalWords(correct, generated):
    command = WORDS_ACC_EXE + " " + correct + " " + generated + " " + DEFAULT_OUTPUT
    command = "bash -c \"" + command + " > /dev/null 2>&1\""
    os.system(command)

# the function computes character level recignition accuracy
def evalCharacters(correct, generated):
    command = CHARS_ACC_EXE + " " + correct + " " + generated + " " + DEFAULT_OUTPUT
    command = "bash -c \"" + command + " > /dev/null 2>&1\""
    os.system(command)

# the function parses the output report to extract the desired values
def parseReport():
    report = open(DEFAULT_OUTPUT, "r")
    content = report.readlines()
    report.close()

    total = int(list(filter(lambda a: a != "", content[2].split(" ")))[0])
    errors = int(list(filter(lambda a: a != "", content[3].split(" ")))[0])
    accuracy = float(list(filter(lambda a: a != "", content[4].split(" ")))[0].split("%")[0])
    return [total, errors, accuracy]

# the function selects the type of evaluation
def eval(correctFile, generatedFile, words=False):
    if words:
        evalWords(correctFile, generatedFile)
    else:
        evalCharacters(correctFile, generatedFile)
    
    report = parseReport()
    os.system("del " + DEFAULT_OUTPUT.replace("/", "\\"))
    
    return report

# character level evalution based on Levensthein distance
def evalLevensthein(refFilePath, outputFilePath):
    fRef = open(refFilePath, "r")
    refContent = fRef.readline()

    fOut = open(outputFilePath, "r")
    outContent = fOut.readline()
    
    return L.ratio(refContent, outContent)