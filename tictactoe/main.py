NameFirst = input('Игрок за крестики: ')
NameSecond = input('Игрок за нолики: ')
print(f'Приветствуем вас,{NameFirst} и {NameSecond}. Сыграем в "Крестики-нолики" ')
print('Первыми играют крестики')
field = [['-']*3 for _ in range(3)]

def FieldShow(f):
    print('  0 1 2')
    for i in range(len(field)):
        print(str(i) + " " + " ".join(field[i]))

def UserInput(f):
    while True:
        place = input(
            "Ваш ход, введите координаты: ").split()
        if len(place) != 2:
            print("Введите, пожалуйста, только две координаты через пробел")
            continue
        if not(place[0].isdigit() and place[1].isdigit()):
            print("Введите, пожалуйста, только числа")
            continue
        x, y = map(int, place)
        if not(x >= 0 and x < 3 and y >= 0 and y < 3):
            print('Введенные координаты выходят за пределы поля, '
                  'введите, пожалуйста, координаты в границах поля "Крестики-нолики" ')
            continue
        if f[x][y] != "-":
            print(
                "Клетка уже занята. Для продолжения введите, пожалуйста, другие координаты")
            continue
        break
    return x, y

def Winner(f, user):
    f_list = []
    for l in f:
        f_list += l
    positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                 [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    indexes = set([i for i, x in enumerate(f_list) if x == user])
    for p in positions:
        if len(indexes.intersection(set(p))) == 3:
            return True
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
    FieldShow(field)
    x, y = UserInput(field)
    field[x][y] = user
    if Winner(field, user):
        print(f"Поздравляем, выйграл {user}")
        FieldShow(field)
        break
    count += 1