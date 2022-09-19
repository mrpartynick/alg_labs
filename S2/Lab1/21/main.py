def read_inf_from_file(filename):
    input_file = open(filename, "r")

    my_card_value, opponent_card_value, trump_lear = input_file.readline().split()
    my_card_value, opponent_card_value = int(my_card_value), int(opponent_card_value)

    my_cards = list(map(str, input_file.readline().split()))
    opponent_cards = list(map(str, input_file.readline().split()))

    return my_card_value, opponent_card_value, trump_lear, my_cards, opponent_cards


def cardsharper(my_card_value, opponent_card_value, trump_lear, my_cards, opponent_cards):
    cards_dict = {'6': ['7', '8', '9', 'T', 'J', 'Q', 'K', 'A'],
                  '7': ['8', '9', 'T', 'J', 'Q', 'K', 'A'],
                  '8': ['9', 'T', 'J', 'Q', 'K', 'A'],
                  '9': ['T', 'J', 'Q', 'K', 'A'],
                  'T': ['J', 'Q', 'K', 'A'],
                  'J': ['Q', 'K', 'A'],
                  'Q': ['K', 'A'],
                  'K': ['A'],
                  'A': [None],
                  'koz': ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']}
    lears_of_mine_cards = {"S": [],
                           "C": [],
                           "D": [],
                           "H": []}

    # Распределяем имеющиеся у нас карты по мастям.
    for i in range(my_card_value):
        card = my_cards[i]
        lear_of_card = card[1]
        rang_of_card = card[0]

        lears_of_mine_cards[lear_of_card].append(rang_of_card)

    # Проходимся по картам противника.
    for opponent_card in opponent_cards:
        beated_flag = False
        rang_of_opponent_card = opponent_card[0]
        lear_of_opponent_card = opponent_card[1]

        # Берем все карты, которыми мы можем побить карту оппонента.
        needed_cards = cards_dict[rang_of_opponent_card]

        # Перебираем карты, которыми мы можем побить.
        for needed_card in needed_cards:
            # Если среди наших карт находится та, которой мы можем побить - бьем
            if needed_card in lears_of_mine_cards[lear_of_opponent_card]:
                lears_of_mine_cards[lear_of_opponent_card].remove(needed_card)
                beated_flag = True
                break

        # Если мы не смогли побить карту картой той же масти, то нужно достать наши козыри.
        if beated_flag is False:
            # Если карта противника и так козырная, то ничего нас уже не спасет.
            if lear_of_opponent_card == trump_lear:
                return "NO"
            else:
                my_trump_cards = lears_of_mine_cards[trump_lear]

                needed_trump_cards = cards_dict[rang_of_opponent_card]

                for needed_trump_card in needed_trump_cards:
                    if needed_trump_card in my_trump_cards:
                        lears_of_mine_cards[trump_lear].remove(needed_trump_card)
                        beated_flag = True
                        break

        if beated_flag is False:
            return "NO"

    # Ура! Мы отбились!
    return "YES"


my_card_value, opponent_card_value, trump_lear, my_cards, opponent_cards = read_inf_from_file("input.txt")
result = cardsharper(my_card_value, opponent_card_value, trump_lear, my_cards, opponent_cards)

output_file = open("output.txt", "w")
output_file.write(result)
output_file.close()
