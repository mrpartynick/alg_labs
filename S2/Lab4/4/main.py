import random


def read_inf_from_file(filename):
    input_file = open(filename, "r")

    string = input_file.readline().strip()
    value_of_queries = int(input_file.readline().strip())
    queries = []

    for line in input_file.readlines():
        line = line.strip()

        query = list(map(int, line.split()))
        queries.append(query)

    return string, queries


def polyhash(string, module, x):
    length_of_string = len(string)
    hash = 0

    for i in range(length_of_string):
        hash += (ord(string[i]) * x ** length_of_string - i - 1) % module

    return hash


def make_queries_to_string(string, queries):
    first_module = 10 ** 9 + 7
    second_module = 10 ** 9 + 9
    x = random.randint(1, first_module)

    # Создаем хеш-таблицы преыиксов.
    first_array = [None for _ in range(len(string))]
    second_array = [None for _ in range(len(string))]

    # Заполняем хеш-таблицы префиксов.
    for i in range(len(string)):
        prefix = string[0:i]
        first_hash_prefix = polyhash(prefix, first_module, x)
        second_hash_prefix = polyhash(prefix, second_module, x)

        first_array[i] = first_hash_prefix
        second_array[i] = second_hash_prefix

    for query in queries:
        a_index, b_index, l = query[0], query[1], query[2]

        a_prefix = string[a_index:l+a_index]
        b_prefix = string[b_index:l+b_index]

        first_a_hash = first_array[a_index + l-1] - x ** l * \
                       first_array[a_index]
        second_a_hash = second_array[a_index + l-1] - x ** l * \
                        second_array[a_index]

        first_b_hash = first_array[b_index + l-1] - x ** l * \
                       first_array[b_index]
        second_b_hash = second_array[b_index + l-1] - x ** l * \
                        second_array[b_index]

        if first_a_hash == first_b_hash and second_a_hash == second_b_hash:
            print("Yes")
        else:
            print("No")


string, queries = read_inf_from_file("input")
make_queries_to_string(string, queries)
