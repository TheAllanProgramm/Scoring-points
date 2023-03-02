while True:
    print("Очистить кеш? y/n")
    z = input()
    if z == "y":
        file = open("data/text.txt", "w")
        file.write(str(0))
        file.close()
        print("Кеш очищен!")
    elif z == "n":
        file = open("data/text.txt", "r")
        n = 0
        s = int(file.read())
        r = 1
        file.close()
        print("Programm by The Allan ^_^")
        print("Остановить программу: 0")
        while r >= 1:
            try:
                while r >= 1:
                    n = int(input())
                    s = s + n
                    r = n
            except ValueError:
                print("Введите числовое значение!")
        file = open("data/text.txt", "w")
        file.write(str(s))
        file.close()
        print("Количество баллов:", s)
        print("Bay Bay ^_^")
        z = "zzz"
    else:
        print("Не корректное значение")
    if z == "zzz":
        break
input()
#