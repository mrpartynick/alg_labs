def read_inf_from_file(filename):
    input_file = open(filename, "r")

    value_of_stuffs, capacity_of_bag = map(int, input_file.readline().split())
    stuffs = []

    for _ in range(value_of_stuffs):
        stuffs.append(list(map(int, input_file.readline().split())))

    stuffs.sort(key=lambda x: x[1])

    input_file.close()
    return value_of_stuffs, capacity_of_bag, stuffs


def little_thief(value_of_stuffs, capacity_of_bag, stuffs):
    A = [0] * value_of_stuffs
    V = 0

    for i in range(value_of_stuffs):
        if capacity_of_bag == 0:
            return V
        a = min(stuffs[i][1], capacity_of_bag)
        V += stuffs[i][0] / stuffs[i][1] * a
        stuffs[i][1] -= a
        A[i] += a
        capacity_of_bag -= a
    return V


value_of_stuffs, capacity_of_bag, stuffs = read_inf_from_file("input")
result = little_thief(value_of_stuffs, capacity_of_bag, stuffs)

print(result)
