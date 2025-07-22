lst = [0, 1, 0, 12, 3]

no_zeros = [x for x in lst if x != 0]

result = no_zeros + [0] * (len(lst) - len(no_zeros))

print(result)