print("  |  1  2  3  4  5  6  7  8  9")
print("--+---------------------------")

x = 1
y = 1
while True:
    if x > 9: break
    y = 1
    str_line = ""
    str_line += str(x).rjust(2) + "|"
    while True:
        if y > 9: break
        str_line += str(x * y).rjust(3)
        y += 1
    print(str_line)
    x += 1
