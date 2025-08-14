def add_one(some_list):
    number = int("".join(map(str, some_list)))
    number += 1
    return [int(d) for d in str(number)]
