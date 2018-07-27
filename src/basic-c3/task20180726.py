from random import randint


def shake_dice():
    '''
    Function that make random int values 1-6

    Parameters
    ----------
    None

    Return
    ------
    Int
        random int values 1-6
    '''
    return randint(1, 6)


def go_forward(num):
    '''
    Function that make piece move ahead

    Parameters
    ----------
    num: int
        Number of movements

    Return
    ------
    None
        Change global cur_pos values and it move ahead
    '''
    global cur_pos
    if cur_pos != [0, 0]:
        draw(True)
    for i in range(num):
        if cur_pos == [10, 0] or cur_pos == [10, -10]:
            turn_right()
        cur_pos[0] += direction[0]
        cur_pos[1] += direction[1]
        if cur_pos[0] > 0:
            draw(True)


def go_back(num):
    '''
    Function that make move back

    Parameters
    ----------
    num: int
        Number of movements

    Return
    ------
    None
        Change global cur_pos values and it move back
    '''
    global cur_pos
    for i in range(num):
        cur_pos[0] += 1
        if cur_pos[0] > 0:
            draw(False)


def turn_right():
    '''
    Function that make piece turn right

    Parameters
    ----------
    None

    Return
    ------
    None
        Change global directon values and it turn right
    '''
    global direction
    direction = [direction[1], -direction[0]]


def draw(is_go_forward):
    '''
    Function that draw sugoroku_map

    Prameters
    ---------
    is_go_forward: bool
        Piece'll move ahead or not

    Return
    ------
    None
        Change global sugoroku_map value and update
    '''
    global sugoroku_map
    if is_go_forward:
        sugoroku_map[abs(cur_pos[1])][cur_pos[0]] = "*"
    else:
        sugoroku_map[abs(cur_pos[1])][cur_pos[0]] = "."


def main():
    '''
    Main Function

    Parameter
    ---------
    None

    Return
    ------
    None
    '''
    global cur_pos
    print("スゴロクしよっか")
    while True:
        input("エンターでサイコロを降る")
        d = shake_dice()
        go_forward(d)
        if cur_pos[0] < 0:
            go_back(abs(cur_pos[0] * 2))
            print("{}がでました。{}オーバしたので戻ります。現在地は{}です。".format(d, abs(cur_pos[0]), cur_pos))
        else:
            print("{}がでました。現在地は{}です。".format(d, cur_pos))
        for i in sugoroku_map:
            print("".join(i))
        if cur_pos == [0, -10]:
            print("おめでとうございます、ゲームクリアです")
            break


if __name__ == "__main__":
    cur_pos = [0, 0]
    direction = [1, 0]
    sugoroku_map = [["." if j == 0 or j == 10 or i == 10 else " " for i in range(11)] for j in range(11)]
    sugoroku_map[0][0] = "S"
    sugoroku_map[10][0] = "G"

    main()
