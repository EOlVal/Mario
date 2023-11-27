spisok = []
result = 0
for x in range(1, 1000):
    if len(str(x)) == 3 and x % 2 == 0 and str(x)[-1] != '8' and x % 3 != 0:
        spisok.append(x)
result += (spisok[0] + spisok[-1])
print(result)