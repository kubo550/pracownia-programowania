string = ""
for i in range(7):
    for j in range(7):
        string += f"{j * 7 + i + 1} "
    string += "\n"
print(string)
