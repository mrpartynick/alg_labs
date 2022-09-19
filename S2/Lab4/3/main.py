import random


def read_inf_from_file(filename):
    input_file = open(filename, "r")

    substring = input_file.readline().strip()
    text = input_file.readline()

    return text, substring


def hash(string, module_number, x):
    hashed_string = 0

    for i in range(len(string) - 1, 0, -1):
        char = string[i]
        hashed_string += ord(char) * x ** i

    return hashed_string % module_number


def rabin_karp(text, substring):
    length_of_text = len(text)
    length_of_substring = len(substring)

    module_number = 1000000009
    x = random.randint(1, module_number - 1)

    hashed_substring = hash(substring, module_number, x)

    counter = 0
    result = []

    for i in range(0, (length_of_text - length_of_substring) + 1):

        hashed_part_of_text = hash(text[i:length_of_substring + i], module_number, x)

        if hashed_substring == hashed_part_of_text:
            if substring == text[i:length_of_substring + i]:
                counter += 1
                result.append(i + 1)
        else:
            continue

    return counter, result


text, substring = read_inf_from_file("input.txt")
counter, result = rabin_karp(text, substring)

out_file = open("output.txt", "w")
out_file.write(str(counter))
out_file.write("\n")

for elem in result:
    out_file.write(str(elem))
    out_file.write(" ")
