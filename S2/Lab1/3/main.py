""""Мы сортируем массивы стоимостей и количества кликов по рекламе. Самым дорогостоящим рекламам мы даем
самое большое кол-во кликов. И так по убыванию.
"""


def read_inf_from_file(filename):
    input_file = open(filename, "r")

    value_of_ads = int(input_file.readline())
    cost_of_ad = list(map(int, input_file.readline().split()))
    value_of_clicks = list(map(int, input_file.readline().split()))

    cost_of_ad.sort()
    value_of_clicks.sort()

    return value_of_ads, cost_of_ad, value_of_clicks


def find_max_profit(value_of_ads, cost_of_ad, value_of_clicks):
    profit = 0

    for i in range(value_of_ads):
        profit += cost_of_ad[i] * value_of_clicks[i]

    return profit


value_of_ads, cost_of_ad, value_of_clicks = read_inf_from_file("input")
profit = find_max_profit(value_of_ads, cost_of_ad, value_of_clicks)

print(profit)
