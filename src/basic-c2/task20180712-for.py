print("  |  1  2  3  4  5  6  7  8  9")
print("--+---------------------------")

for x in range(1, 10):
    str_line = ""
    str_line += str(x).rjust(2) + "|"
    for y in range(1, 10):
        str_line += str(x * y).rjust(3)
    print(str_line)
