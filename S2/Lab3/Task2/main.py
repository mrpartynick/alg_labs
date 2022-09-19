# Решить через множества. Проходиться по каждой вершине и смотреть, с какими она связана.
# Добавлять это во множество или в массив с массивами и посчитать количество уникальных таких штук??


# Написать функцию, которая проверяет, есть ли у множеств хоть один общий элемент.

def is_sets_crossed(s1, s2):
    if s1 & s2 != {}:
        return True
    else:
        return False


def line_handle(line):
    line = line.split(" ")

    if "\n" in line[-1]:
        line[-1] = line[-1][0:line[-1].index("\n")]

    line = list(map(int, line))

    return line


input_file = open("input", "r")

first_line_flag = True
value_of_peaks = 0
value_of_islands = 1
counter = 0
island_set = set()

for line in input_file:
    counter += 1
    data_line = line_handle(line)

    if first_line_flag:
        value_of_peaks = data_line[0]
        first_line_flag = False
        continue

    if len(island_set) == 0:
        island_set = set(data_line)
    else:
        new_island_set = set(data_line)

        if is_sets_crossed(island_set, new_island_set):
            island_set.update(new_island_set)
        else:
            value_of_islands += 1
            island_set = new_island_set

value_of_islands += value_of_peaks - counter

print(value_of_islands)
