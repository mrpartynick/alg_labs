def insertionSort(arr):
    # Traverse through Lab1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-Lab1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def bucket_sort(input_list):
    # Находим максимальное значение в списке. Затем используем длину списка, чтобы определить, какое значение в списке попадет в какой блок
    max_value = max(input_list)
    size = max_value / len(input_list)

    # Создаем n пустых блоков, где n равно длине входного списка
    buckets_list = []
    for x in range(len(input_list)):
        buckets_list.append([])
    buckets_list.append([])

    # Помещаем элементы списка в разные блоки на основе size
    for i in range(len(input_list)):
        j = int(input_list[i] / size)
        if j < 0:
            buckets_list[-1].append(input_list[i])
        else:
            if j != len(input_list):
                buckets_list[j].append(input_list[i])
            else:
                buckets_list[len(input_list) - 1].append(input_list[i])

    # Сортируем элементы внутри блоков с помощью сортировки вставкой
    for z in range(len(input_list)):
        insertionSort(buckets_list[z])

    # Объединяем блоки с отсортированными элементами в один список
    final_output = []
    final_output += buckets_list[-1]
    for x in range(len(input_list)):
        final_output = final_output + buckets_list[x]
    return final_output


l = [7, -9, -10, 29, 0, 1, 5, 4]

print(bucket_sort(l))
