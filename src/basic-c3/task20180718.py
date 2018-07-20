import sys


def data(num):
    main = {"DripCoffee": 280,
            "ColdBrewCoffee": 320,
            "CafeLatte": 330,
            "SoyLatte": 380,
            "Cappuccino": 330,
            "CaramelFrappuccino": 470,
            "MacchaCreamFrappuccino": 470}

    option = {"LowFatMilk": 0,
              "NonFatMilk": 0,
              "SoyMilk": 50,
              "DeepCoffee": 60,
              "WhipCream": 70,
              "CaramelShrup": 60,
              "ChocoSource": 0,
              "DeCafe": 50}

    if num == 0:
        return main
    if num == 1:
        return option


def mainMenu(selected):
    main = data(0)
    while True:
        print("***** MainMenu *****")
        for k, v in main.items():
            print("{:<25}: {}".format(k, v))
        order = input("メニューを選べ。用がないなら「q」か何も言わずEnterするんだな\n")
        if order == "q" or order == "":
            print("ちっ、冷やかしか")
            sys.exit()
        if order in main:
            selected[order] = main[order]
            print("『{}』 だな。もう後戻りはできないぞ\n".format(order))
            return selected
        print("そんな物はない\n")


def optionMenu(selected):
    option = data(1)
    is_ordering = True
    while True:
        print("***** OptionMenu *****")
        for k, v in option.items():
            print("{:<25}: {}".format(k, v))
        if is_ordering:
            order = input("オプションはいるか？必要ないなら「q」を入力するんだな\n")
        else:
            order = input("他に必要なオプションはあるか？無いなら「q」だ\n")
        if order == "q" or order == "":
            break
        if order in option:
            selected[order] = option[order]
            is_ordering = False
            print("『{}』 だな。返品はできないぞ。そういう仕様だ\n".format(order))
        else:
            print("残念ながら無いな\n")
    return selected


def main():
    selected = {}
    selected = mainMenu(selected)
    selected = optionMenu(selected)
    print("注文内容は{}だな".format(", ".join(selected)))
    print("合計金額は{}$。支払いは現金のみ、受取は来月の１日、場所はまあ、いつものコインランドリーだ。".format(sum(selected.values())))


if __name__ == "__main__":
    main()
