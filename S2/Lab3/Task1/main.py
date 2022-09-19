graf = {}

input_data = open("input", "r")

first_line_flag = True
counter = 0


def check_path(graf, first_peak, second_peak):
    first_bounds = graf.get(first_peak, False)
    second_bounds = graf.get(second_peak, False)

    if first_bounds is False:
        if first_peak in second_bounds:
            return True

    else:
        if second_peak in first_bounds:
            return True

    return False


for line in input_data:
    data_line = line.split(" ")

    # Убираем символы переноса строки из данных.
    if "\n" in data_line[1]:
        data_line[1] = data_line[1][0:1]

    if first_line_flag:
        value_of_connections = int(data_line[1])

        first_line_flag = False
        continue

    counter += 1
    data_line = list(map(int, data_line))

    # Если мы дошли до предпоследней строки.
    if counter == value_of_connections + 1:
        if check_path(graf, data_line[0], data_line[1]):
            print("Lab1")
        else:
            print("0")
    # Иначе.
    else:
        current_peak = data_line[0]
        bound_peak = data_line[1]

        arr_bounds_peaks = graf.get(current_peak, [])
        arr_bounds_peaks.append(bound_peak)

        graf[current_peak] = arr_bounds_peaks


