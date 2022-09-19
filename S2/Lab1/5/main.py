def read_inf_from_file(filename):
    input_file = open(filename, "r")

    value_of_candies = int(input_file.readline())

    input_file.close()
    return value_of_candies


# Функция находит наибольшее число, на которое без остатка делится данное
def find_max_det(number):
    for i in range(number - 1, 0, -1):
        if number % i == 0:
            return i


def happy_kids(value_of_candies):
    value_of_pairs = find_max_det(value_of_candies)
    k = value_of_pairs
    candies = []

    while value_of_pairs != 0:
        candies.append(value_of_pairs)
        value_of_pairs -= 1

    return k, candies


value_of_candies = read_inf_from_file("input")
k, candies = happy_kids(value_of_candies)

print(k)
print(*candies)
