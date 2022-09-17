""" Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота "интеллектом"
 """
import os
from random import randint

number_candies = 202

INSTRUCTIONS_PLYER = f"""
На столе {number_candies} конфет
Каждый игрок берет со стола конфеты от 1 до 28
Выигрывает тот кто последний заберет оставшиеся конфеты
"""

INSTRUCTIONS_COMPUTER = f"""
На столе {number_candies} конфет
Игрок берет со стола конфеты от 1 до 28
Чтобы выиграть необходимо последним забрать все конфеты
"""

GAME_SETTINGS = """
1 - Игрок против игрока
2 - Игрок против компьютера
"""


def Setting_game(number):
    os.system('cls')
    if number == 1:
        print(INSTRUCTIONS_PLYER)
        Game("Игрок 1", number_candies, number)
    elif number == 2:
        print(INSTRUCTIONS_COMPUTER)
        Game("Игрок 1", number_candies, number)
    else:
        print("Сделайте корректный выбор \n")
        print(GAME_SETTINGS)
        Setting_game(int(input("Выберите рижим игры: ")))


def Game(plyer, candies, game_mode):
    if game_mode == 1:
        if candies >= 28:
            print(f'Ходит {plyer}')
            print(f"Осталось {candies} конфет")
            num = int(input("Введите число от 1 до 28: "))
            print("")
            if 28 >= num >= 1:
                candies -= num
                if plyer == "Игрок 1":
                    plyer = "Игрок 2"
                    Game(plyer, candies, game_mode)
                elif plyer == "Игрок 2":
                    plyer = "Игрок 1"
                    Game(plyer, candies, game_mode)
            else:
                print("Введеное число не соответсвует правилам игры")
                Game(plyer, candies, game_mode)
        else:
            print(f"Выиграл {plyer}")
    else:
        Game_PC(plyer, candies, game_mode)


def Game_PC(plyer, candies, game_mode):
    if candies >= 28:
        print(f'Ходит {plyer}')
        print(f"Осталось {candies} конфет")
        if plyer == "Игрок 1":
            num = int(input("Введите число от 1 до 28: "))
            print("")
        elif plyer == "Компьютер":
            if candies <= 28:
                num = candies
            else:
                num = int(randint(1, 28))
            print(f"Введите число от 1 до 28: {num}")
            print("")
        if 28 >= num >= 1:
            candies -= num
        else:
            print("Введеное число не соответсвует правилам игры")
            Game_PC(plyer, candies, game_mode)
        if plyer == "Игрок 1":
            plyer = "Компьютер"
            Game_PC(plyer, candies, game_mode)
        elif plyer == "Компьютер":
            plyer = "Игрок 1"
            Game_PC(plyer, candies, game_mode)
    else:
        print(f"Выиграл {plyer}")


os.system('cls')

print(GAME_SETTINGS)
Setting_game(int(input("Выберите рижим игры: ")))
