def read_inf_from_file(filename):
    array_from_file = []
    file = open(filename, "r")

    inf_from_file = list(file.read().splitlines())

    return inf_from_file


def find_beginnings_and_endings(file_inf):
    beginnings = []
    endings = []

    for i in range(1, int(file_inf[0]) + 1):
        begin, end = file_inf[i].split()

        beginnings.append(int(begin))
        endings.append(int(end))

    return beginnings, endings


def find_max_values_of_lectures(beginnings, endings, total_value_of_lectures):
    t, minutes_left, counter = 0, 0, 0

    while minutes_left < 1440:
        minutes_left = 1440

        for i in range(total_value_of_lectures):
            if beginnings[i] >= t and endings[i] < minutes_left:
                minutes_left = endings[i]

        if minutes_left < 1440:
            t = minutes_left
            counter += 1

    return counter


file_inf = read_inf_from_file("input")
beginnings, endings = find_beginnings_and_endings(file_inf)
result = find_max_values_of_lectures(beginnings, endings, int(file_inf[0]))

print(result)
