import copy


def read_inf_from_file(filename):
    input_file = open(filename, "r")

    length_of_number = int(input_file.readline())
    input_file.close()

    return length_of_number


def find_value_of_numbers(length_of_number):
    previos = [4, 2, 1, 0]
    current = [0 for _ in range(4)]

    if length_of_number > 1:
        for i in range(length_of_number - 1):
            current[0] += previos[1] * 2 + previos[2] * 2
            current[1] += previos[0] + previos[3] * 2
            current[2] += previos[0]
            current[3] += previos[1]
            previos = copy.copy(current)
            current = [0 for _ in range(4)]

        return sum(previos)
    else:
        return 8


length_of_number = read_inf_from_file("input.txt.txt")
result = find_value_of_numbers(length_of_number)

output_file = open("output.txt", "w")
output_file.write(str(result))
output_file.close()

