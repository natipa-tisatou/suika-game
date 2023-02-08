import random
import math
''''
                y
                ^
                |
                |
  -x<-------- |---------> x
                |
                |
                y-
'''
def calc_distance(x1, y1, x2, y2):
        diff_x = x1 - x2
        diff_y = y1 - y2
        return math.sqrt(diff_x**2 + diff_y**2)

#スイカとプレイヤーの位置を奇数と偶数で指定
suika_coll=[1,3,5,7,9]
player_coll=[2,4,6,8,10]

#スイカの位置
suika_x = suika_coll[random. randrange(0, 5)]
suika_y = suika_coll[random. randrange(0, 5)]

#プレイヤー
player_x = player_coll[random. randrange(0, 5)]
player_y = player_coll[random. randrange(0, 5)]

suika_x != player_x
suika_y != player_y

while (suika_x != player_x) or (suika_y != player_y):
    #スイカとの距離を表示
    distance = calc_distance(player_x, player_y, suika_x, suika_y)
    print("スイカへの距離:", distance)

    #プレイヤー移動
    c = input("w:上に移動　s:下に移動　a:左に移動　d:右に移動")
    if c == "w":
        player_y = player_y + 1
    elif c == "s":
        player_y = player_y - 1
    elif c == "a":
        player_x = player_x - 1
    elif c == "d":
        player_x = player_x + 1

print("スイカを割りました！")