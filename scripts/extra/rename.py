baseName = "image"
endName = ".tiff"
startNum = 134
endNum = 226
delta = +3

for i in range(endNum, startNum-1, -1):
    fileName = baseName + str(i) + endName
    newFileName = baseName + str(i + delta) + endName

    fOut = open(newFileName, "wb")

    with open(fileName, "rb") as f:
        while (byte := f.read(1)):
            fOut.write(byte)

    fOut.close()
    f.close()