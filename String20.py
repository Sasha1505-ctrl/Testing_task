print("Дано целое положительное число. Вывести символы, изображающие цифры этого числа (в порядке слева направо).")


def int_to_string(integer=input("Введите целое положительное число\n")):
    assert integer != '', "Введите не пустое число"
    try:
        integer = int(integer)
    except:
        return "Введено не число"
    return str(integer)


print(int_to_string())
