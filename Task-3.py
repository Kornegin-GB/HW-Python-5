""" Создайте программу для игры в "Крестики-нолики". """

import os


def Game(lst, plyer, game_run):
    Creating_field(lst)
    while game_run:
        print(f"Ходит игрок {plyer}")
        try:
            move_with = int(input("Позиция по горизонтали: "))  # Строка
            move_height = int(input("Позиция по вертикали: "))  # Столбец
            if move_with > len(lst) or move_height > len(lst):
                print("Вы ввели большое число")
            elif lst[move_height-1][move_with-1] == "---":
                lst[move_height-1][move_with-1] = f"-{plyer}-"
                Creating_field(lst)
                game_run = Checking_winner(lst, plyer)
                if plyer == "X":
                    plyer = "O"
                else:
                    plyer = "X"
            else:
                print("Сделайте другой ход")
        except:
            print("Вы ввели не число")
    else:
        print("\nИгра окончена\n")


def Creating_field(lst):
    os.system('cls')
    for item in lst:
        print(' '.join(map(str, item)))


def Checking_winner(lst, plyer):
    if (lst[0][0] == "-X-" and lst[0][1] == "-X-" and lst[0][2] == "-X-") or (lst[0][0] == "-O-" and lst[0][1] == "-O-" and lst[0][2] == "-O-"):
        print(f"\nПобедитель {plyer}\n")
        return False
    elif (lst[1][0] == "-X-" and lst[1][1] == "-X-" and lst[1][2] == "-X-") or (lst[1][0] == "-O-" and lst[1][1] == "-O-" and lst[1][2] == "-O-"):
        print(f"\nПобедитель {plyer}\n")
        return False
    elif (lst[2][0] == "-X-" and lst[2][1] == "-X-" and lst[2][2] == "-X-") or (lst[2][0] == "-O-" and lst[2][1] == "-O-" and lst[2][2] == "-O-"):
        print(f"\nПобедитель {plyer}\n")
        return False

    elif (lst[0][0] == "-X-" and lst[1][0] == "-X-" and lst[2][0] == "-X-") or (lst[0][0] == "-O-" and lst[1][0] == "-O-" and lst[2][0] == "-O-"):
        print(f"\nПобедитель {plyer}\n")
        return False
    elif (lst[0][1] == "-X-" and lst[1][1] == "-X-" and lst[2][1] == "-X-") or (lst[0][1] == "-O-" and lst[1][1] == "-O-" and lst[2][1] == "-O-"):
        print(f"\nПобедитель {plyer}\n")
        return False
    elif (lst[0][2] == "-X-" and lst[1][2] == "-X-" and lst[2][2] == "-X-") or (lst[0][2] == "-O-" and lst[1][2] == "-O-" and lst[2][2] == "-O-"):
        print(f"\nПобедитель {plyer}\n")
        return False

    elif (lst[0][0] == "-X-" and lst[1][1] == "-X-" and lst[2][2] == "-X-") or (lst[0][0] == "-O-" and lst[1][1] == "-O-" and lst[2][2] == "-O-"):
        print(f"\nПобедитель {plyer}\n")
        return False
    elif (lst[0][2] == "-X-" and lst[1][1] == "-X-" and lst[2][0] == "-X-") or (lst[0][2] == "-O-" and lst[1][1] == "-O-" and lst[2][0] == "-O-"):
        print(f"\nПобедитель {plyer}\n")
        return False
    else:
        for i in range(len(lst)):
            for j in range(len(lst)):
                if lst[j][i] == "---":
                    return True
        else:
            return False


field = [
    ["---", "---", "---"],
    ["---", "---", "---"],
    ["---", "---", "---"],
]

plyer = "X"
run = True

Game(field, plyer, run)
