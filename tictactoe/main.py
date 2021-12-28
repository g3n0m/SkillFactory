name_1 = input('Введите Ваше имя: ')
name_2 = input('Введите Ваше имя: ')
print(f'Добрый день,{name_1} и {name_2} добро пожаловать в игру "Крестики-нолики" ')
print('Первыми играют крестики')
field = [['-']*3 for _ in range(3)]

def show_field(f):
    print('  0 1 2')
    for i in range(len(field)):
        print(str(i) + " " + " ".join(field[i]))

def user_input(f):
    while True:
        place = input(
            "Ваш ход, введите, пожалуйста, желаемые координаты: ").split()
        if len(place) != 2:
            print("Введите, пожалуйста, только две координаты через пробел")
            continue
        if not(place[0].isdigit() and place[1].isdigit()):
            print("Введите, пожалуйста, только числа")
            continue
        x, y = map(int, place)
        if not(x >= 0 and x < 3 and y >= 0 and y < 3):
            print('Введенные координаты выходят за пределы поля, '
                  'введите, пожалуйста, координаты, соотвествующие полю игры "Крестики-нолики" ')
            continue
        if f[x][y] != "-":
            print(
                "Клетка уже занята, введите, пожалуйста другие координаты, чтобы продолжить игру")
            continue
        break
    return x, y


def win_1(f, user):
    f_list = []
    for l in f:
        f_list += l
    positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                 [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    indeces = set([i for i, x in enumerate(f_list) if x == user])
    for p in positions:
        if len(indeces.intersection(set(p))) == 3:
            return True
    # Было:
    #     return False
    # Стало:
    return False


count = 0
while True:
    if count == 9:
        print("Ничья")
        break
    if count % 2 == 0:
        user = 'x'
    else:
        user = 'o'
    show_field(field)
    x, y = user_input(field)
    field[x][y] = user
    if win_1(field, user):
        print(f"Поздравляю, выйграл {user}")
        show_field(field)
        break
    count += 1