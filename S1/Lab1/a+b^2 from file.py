def sumOfNumbersFromFile(file):
    sourceFile = open(file, "r")
    destinationFile = open("../../../../Playgrounds/output.txt", "w")
    line = sourceFile.readline()

    a,b = map(int, line.split())
    sum = a+b**2

    destinationFile.write(str(sum))

    sourceFile.close()
    destinationFile.close()


def fibNumber(fileName):
    f = open(fileName, "r")
    n = int(f.readline())

    if n<=2:
        c = 1
    else:
        a = 1
        b = 1
        c = 0

        for i in range(1, n - 1):
            c = a + b
            a = b
            b = c

    output = open("../../../../Playgrounds/output.txt", "w")
    output.write(str(c))

    f.close()
    output.close()

fibNumber("../../../../Playgrounds/Input.txt")
