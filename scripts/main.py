import os
import FineReaderRunner as frr
import TesseractRunner as tr
import OcropusRunner as ocr
import EvalRunner as er
import Voter as vote

inputImage = "../inputs/line/image137.tiff"
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
    
    #er.eval("../refs/line/target217.txt", "./out3.txt")
    
    result = vote.getSolution(outputFile, outputFile2 + ".txt", outputFile3)

    print("----------------")
    print("[" + result + "]")
    print("----------------")

    # cleanUp()

if __name__ == "__main__":
    main()