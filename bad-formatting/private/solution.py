lst = [112, 4, 10, 18, 4, 17, 68, 94, 49, 44, 26, 54, 41, 69, 65, 1, 4, 12, 29, 18, 23, 23, 13]
for i in range(len(lst)):
    lst[i] ^= lst[(len(lst) + i - 1) % len(lst)]

for i in lst[::-1]:
    print(chr(i), end='')
