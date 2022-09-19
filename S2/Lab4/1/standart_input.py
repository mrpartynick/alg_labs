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
            # Если буква в s, идущая на entry_counter после первое совпадает с такой же буквой в sub_s
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
            number_of_entry += 1

        position_counter += 1

    string_indices_of_entry = ""

    for index in indices_of_entry:
        string_indices_of_entry += str(index)
        string_indices_of_entry += " "

    return str(number_of_entry), string_indices_of_entry


sub_s = input()
s = input()

number_of_entry, indices_of_entry = find_substring_indices(s, sub_s)

print(number_of_entry)
print(indices_of_entry)
