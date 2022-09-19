def sumOfNumbersFromFile(file):
    sourceFile = open(file, "r")
    outputFile = open("../../../../Playgrounds/output.txt", "w")
    line = sourceFile.readline()

    a,b = map(int, line.split())
    sum = a+b

    outputFile.write(str(sum))

    sourceFile.close()
    outputFile.close()