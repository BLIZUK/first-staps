# Какой ужас, нужно переделать, или нет?!?
a, b = int(input()), int(input())
s = [i for i in range(1,a + 1)]
while len(s) > 1:
    for i in range(0 , b - 1):
        s.append(s[i])
    del s[:b]
print(*s)


