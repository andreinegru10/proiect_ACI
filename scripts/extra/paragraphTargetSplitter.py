inputFolder = "./paragraph_refs/"
outputFolder = "./line_refs/"

fileBaseName = "target"
fileEndName = ".txt"
numInputFiles = 35

count = 1
targets = {}

for i in range(1, numInputFiles + 1):
    fileName = inputFolder + fileBaseName + str(i) + fileEndName
    #print(fileName)

    # Using readlines() 
    fileInput = open(fileName, 'r') 
    lines = fileInput.readlines()
    fileInput.close()

    for line in lines:
        targets[count] = line
        count += 1


for targetKey in targets:
    targetText = targets[targetKey]
    targetText = targetText.replace("\n", "")
    fileName = outputFolder + fileBaseName + str(targetKey) + fileEndName
    fileOutput = open(fileName, 'w')
    fileOutput.write(targetText)
    fileOutput.close()