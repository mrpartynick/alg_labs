"""
Мы сортируем список сувениров по убыванию и добавляем по очереди каждому сувениры, пока их стоимость не будет
равна общей стоимости сувениров / 3. Если списки пустые - то все распределилось попровну.
"""


def read_inf_from_file(filename):
    input_file = open(filename, "r")

    value_of_souvenirs = int(input_file.readline())
    prices = list(map(int, input_file.readline().split()))
    input_file.close()

    return prices


def we_are_still_friends(prices):
    total_cost = sum(prices)

    # При таком условии разделить уж точно не получится
    if len(prices) < 3 or total_cost % 3 != 0:
        return 0
    else:
        prices.sort()
        prices = prices[-1:0:-1]

        part_of_each = total_cost // 3

        for i in range(3):
            souvenirs_of_person = []
            index_of_souvenir = 0

            while sum(souvenirs_of_person) < part_of_each:
                if len(prices) - 1 < index_of_souvenir:
                    return 0
                else:
                    adding_souvenir = prices[index_of_souvenir]

                    if sum(souvenirs_of_person) + adding_souvenir <= part_of_each:
                        souvenirs_of_person.append(adding_souvenir)
                        prices.pop(index_of_souvenir)

                    else:
                        index_of_souvenir += 1

        if prices is []:
            return 1


prices = read_inf_from_file("input")
result = we_are_still_friends(prices)

print(result)
