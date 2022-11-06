import random



cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
is_game = "y"
while is_game == "y":
    computer = [random.choice(cards)]
    player = [random.choice(cards)]
    score = 0
    get_card = "у"
    while get_card == "у":
        player.append(random.choice(cards))    # апенд добавить
        if sum(player) > 21 and 11 in player:
            """     если туз в руки и сума  > 21     """
            for i in range(0, len(player)):
                if player[i] == 11 :
                    player[i]
                    break
        score = sum(player)
        print(f"твоя рука: {player}. очков: {score}")
        print("первая карта компьютора: ", computer[0])
        if score >21:
            get_card = "n"
        else:
            get_card = input("'y' - взять карту, n  - остановится")

        while sum(computer) < 17:
            computer.append(random.choice(cards))

        if sum(computer) > 21 and 11 in computer:
            """     если туз в руки и сума  > 21     """
            for i in range(0, len(computer)):
                if computer[i] == 11:
                    computer[i]
                    break
        score_computer = sum(computer)
        print("=" * 177)
        print(f"твоя итоговая рука:{player}. очков: {score}")
        print(f"компа итоговая рука:{computer}. очков: {score_computer}")


        if score >21 and score_computer >21:
            print("перелет у обоих ничья")
        elif score >21:
            print("твой перелет ты проиграл")
        elif score_computer >21:
            print("перелет компа, ты выиграл")
        elif score >21:
            print("перелет компа, ты выиграл")
        elif score == score_computer:
            print("ничья")
        elif score > score_computer:
            print("победа")

        is_game = input("играем дальше? y - да, n - нет")
