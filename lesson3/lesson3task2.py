#lst = [12, 3, 4, 10]
#lst = []
#lst = [1]
lst = [12, 3, 4, 10, 8]
if len(lst) > 1:
    lst = [lst[-1]] + lst[:-1]

print(lst)