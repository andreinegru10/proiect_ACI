import os

LOCAL_BOOK_DIR = "book"
OCRO_HOME = os.getenv("OCROPYHOME")
BINARIZATION_EXE = "\ocropus-nlbin -n"
LAYOUT_EXE = "\ocropus-gpageseg -n"
RECOGNITION_EXE = "\ocropus-rpred"
HOCR_EXE = "\ocropus-hocr"

def run(inputImage, outputFile):
    #initial setup
    createBookDir()

    # do your job
    binarizeImage(inputImage)
    layoutAnalysis()
    textLineRecognition()
    saveOutput(outputFile)
    
    # final cleanup
    removeBookDir()

def createBookDir():
    os.system("if not exist " + LOCAL_BOOK_DIR + " mkdir " + LOCAL_BOOK_DIR)

def removeBookDir():
    os.system("rmdir /S /Q " + LOCAL_BOOK_DIR)

def binarizeImage(inputImage):
    command = OCRO_HOME + BINARIZATION_EXE + " " + inputImage
    command += " -o " + LOCAL_BOOK_DIR
    command = "bash -c \"" + command + "\""
    command = command.replace("\\", "/")
    command = command.replace("C:", "/mnt/c")
    os.system(command)

def layoutAnalysis():
    command = OCRO_HOME + LAYOUT_EXE + " "
    command += LOCAL_BOOK_DIR + "/0001.bin.png"
    command = "bash -c \"" + command + "\""
    command = command.replace("\\", "/")
    command = command.replace("C:", "/mnt/c")
    os.system(command)

def textLineRecognition():
    command = OCRO_HOME + RECOGNITION_EXE + " -Q 4 -m "
    command += OCRO_HOME + "\models\en-default.pyrnn.gz " + LOCAL_BOOK_DIR
    command += "/0001/010001.bin.png"
    command = "bash -c \"" + command + "\""
    command = command.replace("\\", "/")
    command = command.replace("C:", "/mnt/c")
    os.system(command)

def saveOutput(outputFileName):
    #get result and update
    resultFileName = LOCAL_BOOK_DIR + "/0001/010001.txt"
    resultFile = open(resultFileName, "r")
    result = resultFile.read().replace("\n", "")
    resultFile.close()
    # save result
    outputFile = open(outputFileName, "w")
    outputFile.write(result)
    outputFile.close()