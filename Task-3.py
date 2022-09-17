""" Создайте программу для игры в "Крестики-нолики". """


import os


def Creating_field(lst):
    os.system('cls')
    for item in lst:
        print(' '.join(map(str, item)))


def Game(lst, plyer):
    if plyer == "X":
        plyer = "O"
    else:
        plyer = "X"
    print(f"Ходит игрок {plyer}")
    move_with = int(input("Позиция по горизонтали: "))  # Строка
    move_height = int(input("Позиция по вертикали: "))  # Столбец
    if lst[move_height-1][move_with-1] == "---":
        lst[move_height-1][move_with-1] = f"-{plyer}-"
    else:
        print("Сделайте другой ход")
        Game(lst, plyer)
    Creating_field(lst)
    Checking_winner(lst, plyer)


def Checking_winner(lst, plyer):
    if (lst[0][0] == "-X-" and lst[0][1] == "-X-" and lst[0][2] == "-X-") or (lst[0][0] == "-O-" and lst[0][1] == "-O-" and lst[0][2] == "-O-"):
        print(f"\nПобедитель {plyer}\n")
    elif (lst[1][0] == "-X-" and lst[1][1] == "-X-" and lst[1][2] == "-X-") or (lst[1][0] == "-O-" and lst[1][1] == "-O-" and lst[1][2] == "-O-"):
        print(f"\nПобедитель {plyer}\n")
    elif (lst[2][0] == "-X-" and lst[2][1] == "-X-" and lst[2][2] == "-X-") or (lst[2][0] == "-O-" and lst[2][1] == "-O-" and lst[2][2] == "-O-"):
        print(f"\nПобедитель {plyer}\n")

    elif (lst[0][0] == "-X-" and lst[1][0] == "-X-" and lst[2][0] == "-X-") or (lst[0][0] == "-O-" and lst[1][0] == "-O-" and lst[2][0] == "-O-"):
        print(f"\nПобедитель {plyer}\n")
    elif (lst[0][1] == "-X-" and lst[1][1] == "-X-" and lst[2][1] == "-X-") or (lst[0][1] == "-O-" and lst[1][1] == "-O-" and lst[2][1] == "-O-"):
        print(f"\nПобедитель {plyer}\n")
    elif (lst[0][2] == "-X-" and lst[1][2] == "-X-" and lst[2][2] == "-X-") or (lst[0][2] == "-O-" and lst[1][2] == "-O-" and lst[2][2] == "-O-"):
        print(f"\nПобедитель {plyer}\n")

    elif (lst[0][0] == "-X-" and lst[1][1] == "-X-" and lst[2][2] == "-X-") or (lst[0][0] == "-O-" and lst[1][1] == "-O-" and lst[2][2] == "-O-"):
        print(f"\nПобедитель {plyer}\n")
    elif (lst[0][2] == "-X-" and lst[1][1] == "-X-" and lst[2][0] == "-X-") or (lst[0][2] == "-O-" and lst[1][1] == "-O-" and lst[2][0] == "-O-"):
        print(f"\nПобедитель {plyer}\n")
    else:
        Game(lst, plyer)


field = [
        ["---", "---", "---"],
        ["---", "---", "---"],
        ["---", "---", "---"],
]

plyer = "O"

Creating_field(field)

Game(field, plyer)
