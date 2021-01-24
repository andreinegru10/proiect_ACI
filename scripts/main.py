#DONE
import Runner as run
import argparse

Tesseract_Tag = "TS"
FineReader_Tag = "FR"
Ocropus_Tag = "OP"


# create the parser
parser = argparse.ArgumentParser(description='Proiect ACI')

# add arguments to the parser
parser.add_argument('-i','--input', type=str, metavar='', required=True, help='path to the input folder')
parser.add_argument('-o','--output', type=str, metavar='', required=True, help='path to the output folder')
parser.add_argument('-r', '--reference', type=str, metavar='', help='path to the references folder')

# parse arguments
args = parser.parse_args()

# input path
inputPath = args.input
#output path
outputPath = args.output
# references path
referencePath = args.reference

def main():
    # run the 3 OCR tools for the given input files
    run.run(inputPath, outputPath)
    
    # run out solution
    run.vote("TS", "FR", "OP", outputPath, (0, 1, 2))

    # evaluate result only if asked for it
    if referencePath != None:
        # character level
        print("Tesseract Character Level Recognition Accuracy")
        run.evaluate(outputPath + "TS/", referencePath)
        print("FineReader Character Level Recognition Accuracy")
        run.evaluate(outputPath + "FR/", referencePath)
        print("Ocropus Character Level Recognition Accuracy")
        run.evaluate(outputPath + "OP/", referencePath)
        print("ACI Character Level Recognition Accuracy")
        run.evaluate(outputPath + "ACI/", referencePath)

        # word level
        print("Tesseract Word Level Recognition Accuracy")
        run.evaluate(outputPath + "TS/", referencePath, True)
        print("FineReader Word Level Recognition Accuracy")
        run.evaluate(outputPath + "FR/", referencePath, True)
        print("Ocropus Word Level Recognition Accuracy")
        run.evaluate(outputPath + "OP/", referencePath, True)
        print("ACI Word Level Recognition Accuracy")
        run.evaluate(outputPath + "ACI/", referencePath, True)

if __name__ == "__main__":
    main()