"""Не смртрите сюда..."""
def find_substring_indices(s, sub_s):
    """Some var's"""

    # Флаг, показывающий, найдено ли первое совпадение s и sub_s.
    find_first_entry = False
    # Длина sub_s
    len_of_sub_s = len(sub_s)
    # Счетчик, который используется как указатель индекса сраниваемого символа.
    entry_counter = 0
    # Переменная, которая показывает номер сравниваемого символа в s
    position_counter = 1
    # Количество вхождений sub_s в s
    number_of_entry = 0
    # Номера, с которых начинаются вхождения sub_s в s
    indices_of_entry = []

    # Перебираем символы в нашей строке.
    for letter in s:
        # Если было найдено первое совпадение
        if find_first_entry:
            # Если буква в s, идущая на entry_counter после первой совпадает с такой же буквой в sub_s
            if letter == sub_s[entry_counter]:
                # Увеличиваем entry_counter
                entry_counter += 1
            # Иначе - совпало лишь entry_counter-Lab1 буква и мы обнуляем счетчики
            else:
                find_first_entry = False
                # indices_of_entry.pop(-Lab1)
                entry_counter = 0
        # Иначе
        else:
            # Если данная буква в s совпадает с первой в sub_s
            if letter == sub_s[entry_counter]:
                find_first_entry = True
                indices_of_entry.append(position_counter)
                entry_counter += 1

        if entry_counter == len_of_sub_s - 1:
            find_first_entry = False
            number_of_entry += 1
            entry_counter = 0

        position_counter += 1

    indices_of_entry = indices_of_entry[:number_of_entry]

    string_indices_of_entry = ""

    for index in indices_of_entry:
        string_indices_of_entry += str(index)
        string_indices_of_entry += " "

    return str(number_of_entry), string_indices_of_entry


"""
Функция поиска подстроки. Принимает строку и подстроку.
Возвращает количество вхождений подстроки в строку и индексы строки, где эти вхождения начинаются.
"""
def find_substring(s, sub_s):
    # Флаг, показывающий, найдено ли первое совпадение s и sub_s.
    find_first_entry = False
    sub_s = sub_s[:-1]
    # Длина sub_s
    len_of_sub_s = len(sub_s)
    # Счетчик, который используется как указатель индекса сраниваемого символа.
    entry_counter = 0
    # Переменная, которая показывает номер сравниваемого символа в s
    position_counter = 0
    # Номера, с которых начинаются вхождения sub_s в s
    indices_of_entry = []

    """
    Мы перебираем все буквы в s. От каждой рассматриваемой буквы мы берем срез, равный длине sub_s.
    Полученную строку мы сравниваем с sub_s и если они равны, то долбим по счетчикам.
    """
    for letter in s:
        if s[position_counter:len_of_sub_s] == sub_s:
            indices_of_entry.append(position_counter + 1)
            entry_counter += 1
        len_of_sub_s += 1
        position_counter += 1

    string_indices_of_entry = ""

    for index in indices_of_entry:
        string_indices_of_entry += str(index)
        string_indices_of_entry += " "

    return str(entry_counter), string_indices_of_entry


input_file = open("input.txt.txt", "r")
output_file = open("output.txt", "w")

"""Переменные, хранящие строку и искому подстроку. Нужно, чтобы они стремно не подсвечивались."""
s = ""
sub_s = ""

"""Считываем входной файл."""
first_line_flag = True
for line in input_file:

    if first_line_flag:
        sub_s = line
        first_line_flag = False
    else:
        s = line

input_file.close()

"""Запускаем функцию."""
number_of_entry, indices_of_entry = find_substring(s, sub_s)

"""Записываем результаты в файл"""
output_file.write(number_of_entry)
if number_of_entry != "0":
    output_file.write("\n")
    output_file.write(indices_of_entry)
