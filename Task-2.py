""" Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота "интеллектом"
 """
import os
from random import randint

number_candies = 2021

INSTRUCTIONS_PLYER = f"""
Игрок против игрока\n
На столе {number_candies} конфета
Каждый игрок по очереди берет со стола конфеты от 1 до 28
Выигрывает тот кто последний заберет оставшиеся конфеты
"""

INSTRUCTIONS_COMPUTER = f"""
Игрок против компьютера\n
На столе {number_candies} конфета
Игрок берет со стола конфеты от 1 до 28
Чтобы выиграть необходимо последним забрать все конфеты
"""

GAME_SETTINGS = """
1 - Игрок против игрока
2 - Игрок против компьютера
"""


def Clear():
    os.system('cls')


def Setting_game(game_run):
    while game_run:
        try:
            number = int(input("Выберите рижим игры: "))
            if number == 1:
                return 1
            elif number == 2:
                return 2
            else:
                print("Вы ввели некоректное число")
        except:
            print("Вы ввели не число")


def Game(candies, game_run):
    game_mode = Setting_game(game_run)
    Clear()
    if game_mode == 1:
        plyer = "Игрок 1"
        Game_Plyer(plyer, candies, game_run)
    elif game_mode == 2:
        plyer = "Игрок"
        Game_PC(plyer, candies, game_run)


def Game_Plyer(plyer, candies, game_run):  # Игра между игроками
    while game_run:
        if candies > 28:
            if plyer == "Игрок 1":
                print(INSTRUCTIONS_PLYER)
                print(f'Ходит {plyer}')
                print(f"Осталось {candies} конфет")
            elif plyer == "Игрок 2":
                print(f'Ходит {plyer}')
                print(f"Осталось {candies} конфет")
            try:
                num = int(input("Введите число от 1 до 28: "))
                if 28 >= num >= 1:
                    candies -= num
                    if plyer == "Игрок 1":
                        plyer = "Игрок 2"
                    else:
                        Clear()
                        plyer = "Игрок 1"
                else:
                    print("Вы ввели число не удовлетворяющее условию")
            except:
                print("Вы ввели не число")
        else:
            print(f"Победитель {plyer}")
            game_run = False
    else:
        print("Игра окончена")


def Game_PC(plyer, candies, game_run):  # Игра с компьютером
    while game_run:
        if candies > 28:
            if plyer == "Игрок":
                print(INSTRUCTIONS_COMPUTER)
                print(f'Ходит {plyer}')
                print(f"Осталось {candies} конфет")
            elif plyer == "Компьютер":
                print(f'Ходит {plyer}')
                print(f"Осталось {candies} конфет")
            if plyer == "Игрок":
                try:
                    num = int(input("Введите число от 1 до 28: "))
                    if 28 >= num >= 1:
                        candies -= num
                        plyer = "Компьютер"
                    else:
                        print("Вы ввели число неудовлетворяющее условию")
                except:
                    print("Вы ввели не число")
            else:
                Clear()
                if candies >= 28:
                    num = randint(1, 28)
                else:
                    num = candies
                candies -= num
                print(f"Компьютер ввел: {num}")
                plyer = "Игрок"
        else:
            print(f"Победитель {plyer}")
            game_run = False
    else:
        print("Игра окончена")


run = True
Clear()
print(GAME_SETTINGS)
Game(number_candies, run)
