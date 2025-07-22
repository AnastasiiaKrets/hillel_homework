lst = [0, 1, 7, 2, 4, 8]

if len(lst) == 0:
    result = 0
else:
    suma = 0
    i = 0
    while i < len(lst):
        if i % 2 == 0:
            suma = suma + lst[i]
        i = i + 1
    result = suma * lst[-1]

print(result)