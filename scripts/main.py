import os
import FineReaderRunner as frr
import TesseractRunner as tr
import OcropusRunner as ocr

inputImage = "../inputs/line/image1.tiff"
outputFile = "./out1.txt"
outputFile2 = "./out2"
outputFile3 = "./out3.txt"

def cleanUp():
    command = "del out*.txt"
    os.system(command)

def main():
    frr.run(inputImage, outputFile)
    tr.run(inputImage, outputFile2)
    ocr.run(inputImage, outputFile3)
    cleanUp()

if __name__ == "__main__":
    main()