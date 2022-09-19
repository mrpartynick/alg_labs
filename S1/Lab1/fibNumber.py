def fibNumber(fileName):
    f = open(fileName, "r")
    n = int(f.readline())

    if n<=2:
        b = 1
    else:
        a,b = 0,1

        for i in range(1, n):
            a,b = b, a+b

    output = open("../../../../Playgrounds/output.txt", "w")
    output.write(str(b))

    f.close()
    output.close()
