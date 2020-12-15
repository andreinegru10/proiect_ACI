from os import listdir
from os.path import isfile, join
import FineReaderRunner as frr
import TesseractRunner as tr
import OcropusRunner as ocr
import EvalRunner as er
import Voter as vo

def getFilesFromPath(path):
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

    return onlyfiles

SYMBOLS = '!$%-,.;\'?/'
path = "../refs/line/"
pathNew = "../refs/line_no_special/"

files = getFilesFromPath(path)

for fila in files:
    f = open(path+fila, "r")
    content = f.read()
    f.close()
    content = content.replace(SYMBOLS, "")

    f = open(pathNew+fila, "w")
    f.write(content)
    f.close()