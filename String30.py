print("Дан символ C и строки S, S0. После каждого вхождения символа C в строку S вставить строку S0.")

c = input("Введите символ C\n")


def string30(C, S=input("Введите строку S\n"), S0=input("Введите строку S0\n")):
    assert len(C) == 1, "Введите не строку, символ"
    assert len(S) > 1, "Введите не пустую строку и не символ"
    assert len(S0) > 1, "Введите не пустую строку и не символ"
    for i in range(len(S)):
        if C in S[i]:
            print(S0)


print(string30(c))
