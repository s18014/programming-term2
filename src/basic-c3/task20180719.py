from decimal import Decimal, ROUND_HALF_UP

round = lambda v, d="1": float(Decimal(str(v)).quantize(Decimal(d), rounding=ROUND_HALF_UP))


def add(x, y):
    '''
    sum x and y

    Parameters
    ----------
    x : int, float
        addend value
    y : int, float
        addend value

    Returns
    -------
    float
        Return sum x and y
    '''
    return x + y


def sub(x, y):
    '''
    subtract x from y

    Parameters
    ----------
    x : int, float
        minuend value
    y : int, float
        subtrahend value

    Returns
    -------
    float
        return subract x from y
    '''
    return x - y


def mul(x, y):
    '''
    multiply x and y

    Parameters
    ----------
    x : int, float
        multiplier value
    y : int, float
        multiplicand value

    Returns
    -------
    float
        return multiply x and y
    '''
    return x * y


def div(x, y):
    '''
    x divid by y

    Parameters
    ----------
    x : int, float
        dividend value
    y : int, float
        divisor value

    Returns
    -------
    float
        return x divid by y
    '''
    return x / y


def isNumber(num):
    try:
        float(num)
    except ValueError:
        return False
    return True


def main():
    operator = {"+": add,
                "-": sub,
                "*": mul,
                "/": div}

    print("四則演算プログラムです")
    while True:
        x = input("第1パラメータを入力してください>>> ")
        if isNumber(x):
            x = float(x)
            break
        print("Error: 数字以外は入力できません")

    while True:
        y = input("第2パラメータを入力してください>>> ")
        if isNumber(y):
            y = float(y)
            break
        print("Error: 数字以外は入力できません")

    while True:
        op = input("演算方法を入力してください>>> ")
        if op in operator:
            break
        print("Error: (+, -, *, /) の四種類のみ使用できます")

    result = operator[op](x, y)
    print("計算結果は {} です".format(round(result, "0.001")))


if __name__ == "__main__":
    main()
