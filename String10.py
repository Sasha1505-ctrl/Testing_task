print("Дана строка. Вывести строку, содержащую те же символы, но расположенные в обратном порядке.")


def reverse_string(string):
    assert len(string) >= 1, "Нужно ввести не пустую строку или символ"
    res = ""
    for i in reversed(string):
        res += i
    return res


print(reverse_string(input("Введите строку\n")))
