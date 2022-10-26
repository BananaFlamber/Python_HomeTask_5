import random

candies = 2021

player_candies = 0

print("\033c")
print("Здравствуйте, давайте сыграем в игру?")
print(
    f"Условия таковы: В наличии {candies} конфета. Каждый игрок, по-очереди берет себе от 1 до 28 конфет, за один раз.")
print("При попытке взять больше 28 конфет - ход перейдет сопернику!!!")
print("Игрок, чей ход оказался последним, до того как конфеты закончатся - присваивает себе конфеты оппонента.")
print("Очерёдность хода определяется жребием.\n")


def who_goes_first():
    print("Как мы уже упоминали выше, право первого хода определяется жребием!")
    print("Правила просты: обоим игрокам выпает случайное число от 1 до 10.")
    print("Кому выпало большее число - тот и ходит первый!!!")
    num = random.randint(1, 10)
    print(f"Вам выпало число:{num}")
    num_bot = random.randint(1, 10)
    print(f"Вашему сопернику выпало число:{num_bot}")
    if num == num_bot:
        print("Вот это да, выпал одинаковы жребий, необходимо заново его бросить!!!")
        who_goes_first()
    elif num > num_bot:
        print("Удача на вашей стороне, Вы ходите первый!!!!")
        player_move(candies, player_candies)
    else:
        print("Увы, неповезло... Но ничего страшного, я уверен что это не затруднит Ваш выигрыш!!!!")
        bot_move(candies, player_candies)


def player_move(candies, player_candies):
    if candies > 0:
        print(f"Остаток конфет на столе: {candies}")
        move = int(input("Ваш ход! Итак, сколько конфет возьмёте? -> "))
        player_candies = move
        if move <= 0 or move > 28:
            print(
                "Вы попытались нас надурить, жать что вылетели из игры так и не доиграв до конца =(")
        else:
            candies = candies - move
            return bot_move(candies, player_candies)
    else:
        print("Какая досада... Бот победил...")


def bot_move(candies, player_candies):
    if candies <= 28:
        print(f"Остаток конфет на столе: {candies}")
        print(f"Соперник забирает оставшиеся конфеты.")
        candies = 0
        return player_move(candies, player_candies)
    elif candies == 2021:
        print(f"Остаток конфет на столе: {candies}")
        candies = candies - 20
        print("Соперник забирает 20 конфет")
        return player_move(candies, player_candies)
    elif candies <= 2001 and candies > 0:
        print(f"Остаток конфет на столе: {candies}")
        move_bot = 29 - player_candies
        print(f"Соперник забирает {move_bot} конфет")
        candies = candies - move_bot
        return player_move(candies, player_candies)
    elif candies > 2001 and candies < 2021:
        print(f"Остаток конфет на столе: {candies}")
        print(f"Соперник забирает {candies % 29} конфет")
        candies = candies - (candies % 29)
        return player_move(candies, player_candies)
    else:
        print("Поздравляю, Вы победили!!!!! Ура!!!!!")


try:
    print("Обращаем Ваше внимание на то - что если вздумаете обмануть нас путём ввода некорректных данных - ")
    print("то Вы сразу автоматически выходите из игры !!!")
    print("Поэтому будьте внимательны при вводе данных, а то будет грустно если вы проиграете =(")
    start = int(
        input("Ну что, Вы готовы? Если Да - то введите: 1 для начала игры!!!  ->  "))
    if start != 1:
        print("Вот так сразу, да? Ладно....на первый раз прощаем, но дальше снисхождений не жди!")
        print("ВСЁ СТРОГО ПО ПРАВИЛАМ!!!!")
        who_goes_first()
    else:
        print("Отлично, удачи Вам, и результативной игры!!!")
        who_goes_first()
except:
    print("Ай, ай, ай, а мухлевать-то не надо!!! Очень жать что вы вышли из игры не начав играть.... ")
