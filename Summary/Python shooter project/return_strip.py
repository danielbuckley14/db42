list1 = []
with open("text.txt") as f:
    list1.append("".join(line for line in f if not line.isspace()))

print(list1)

with open('new.txt', 'w') as f:
    for i in list1:
        f.write(f"{i}")