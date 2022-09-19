def binnary(i, N):
    string = format(i, 'b')
    string = string[::-1]
    while len(string) < N: string += "0"
    return list(map(int, list(string)))


def check(array_1, array_2):
    for i in range(len(array_1)): array_1[i] += array_2[i]
    for i in range(1, len(array_1)):
        if array_1[i] == 0 and array_1[i - 1] == 0: return False
        if array_1[i] == 2 and array_1[i - 1] == 2: return False
    return True


def opportunities(N):
    results = []
    var_1 = generator_options(N)
    for i in var_1:
        results.append([])
        var_2 = generator_options(N)
        for j in var_2:
            if check(i[:], j[:]):
                results[-1].append(1)
            else:
                results[-1].append(0)
    return results


def generator_options(N):
    for i in range(pow(2, N)): yield binnary(i, N)


def main(array, W):
    result = [1] * len(array)
    new = [0] * len(array)

    for i in range(W - 1):
        for j in range(len(new)):
            for k in range(len(array[j])):
                if array[j][k] == 1: new[j] += result[k]
        result = new.copy()
        new = [0] * len(array)

    return sum(result)


input_file = open("input.txt", "r")
H, W = map(int, input_file.readline().split())
result = main(opportunities(min(H, W)), max(H, W))

out_file = open("output.txt", "w")
out_file.write(str(result))
