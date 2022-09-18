""" Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Пример:
Введите текст для кодировки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
Текст после кодировки: 12W1B12W3B24W1B14W
Текст после дешифровки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW

Входные и выходные данные хранятся в отдельных текстовых файлах.
 """


def read_file(path):
    with open(path) as data:
        text_coding = data.readline()
    return text_coding


def write_file(path, text, coding):
    with open(path, "w") as data:
        if coding == "encode":
            code_text = ""
            char = ""
            count = 1
            for i in text:
                if i != char:
                    if char != "":
                        code_text += str(count) + char
                        count = 1
                    char = i
                else:
                    count += 1
            else:
                code_text += str(count) + char
        elif coding == "decode":
            code_text = ""
            count = ""
            for i in text:
                if i.isdigit():
                    count += i
                else:
                    code_text += i * int(count)
                    count = ""
        data.writelines(code_text)


# Для записи начального файла
text = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
with open("text.txt", "w") as data:
    data.writelines(text)


write_file("encode.txt", read_file("text.txt"), "encode")
write_file("decode.txt", read_file("encode.txt"), "decode")

print(read_file("text.txt"))
print(read_file("encode.txt"))
print(read_file("decode.txt"))
