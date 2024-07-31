import random

start_game = True

while start_game:
    # 0 代表 石头
    # 1 代表 剪刀
    # 2 代表 布
    random_integer = random.randint(0, 3)
    user_number = int(input('请出拳:\n'))
    if random_integer == user_number:
        print("平局")
    elif random_integer == 0:
        if user_number == 1:
            print("恭喜你，你赢了")
        else:
            print("输了")
    elif random_integer == 1:
        if user_number == 0:
            print("输了")
        else:
            print("恭喜你，你赢了")
    elif random_integer == 2:
        if user_number == 0:
            print("输了")
        else:
            print("恭喜你，你赢了")
    y = input('请问是否再来一局？')
    if y.upper() != 'Y':
        start_game = False