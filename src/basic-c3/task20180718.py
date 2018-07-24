import sys


def mainMenu(selected, menu):
    while True:
        print("***** MainMenu *****")
        for k, v in menu.items():
            print("{:<25}: {}".format(k, v))
        order = input("メニューを選べ。用がないなら「q」か何も言わずEnterするんだな\n")
        if order == "q" or order == "":
            print("ちっ、冷やかしか")
            sys.exit()
        if order in menu:
            selected[order] = menu[order]
            print("『{}』 だな。もう後戻りはできないぞ\n".format(order))
            return selected
        print("そんな物はない\n")


def optionMenu(selected, menu):
    is_ordering = True
    while True:
        print("***** OptionMenu *****")
        for k, v in menu.items():
            print("{:<25}: {}".format(k, v))
        if is_ordering:
            order = input("オプションはいるか？必要ないなら「q」を入力するんだな\n")
        else:
            order = input("他に必要なオプションはあるか？無いなら「q」だ\n")
        if order == "q" or order == "":
            break
        if order in menu:
            selected[order] = menu[order]
            is_ordering = False
            print("『{}』 だな。返品はできないぞ。そういう仕様だ\n".format(order))
        else:
            print("残念ながら無いな\n")
    return selected


def main(main_menu, option_menu):
    selected = {}
    selected = mainMenu(selected, main_menu)
    selected = optionMenu(selected, option_menu)
    print("注文内容は{}だな".format(", ".join(selected)))
    print("合計金額は{}$。支払いは現金のみ、受取は来月の１日、場所はまあ、いつものコインランドリーだ。".format(sum(selected.values())))


if __name__ == "__main__":
    main_menu = {"DripCoffee": 280,
                 "ColdBrewCoffee": 320,
                 "CafeLatte": 330,
                 "SoyLatte": 380,
                 "Cappuccino": 330,
                 "CaramelFrappuccino": 470,
                 "MacchaCreamFrappuccino": 470}

    option_menu = {"LowFatMilk": 0,
                   "NonFatMilk": 0,
                   "SoyMilk": 50,
                   "DeepCoffee": 60,
                   "WhipCream": 70,
                   "CaramelShrup": 60,
                   "ChocoSource": 0,
                   "DeCafe": 50}
    main(main_menu, option_menu)
