def find_unique_value(some_list):
    for num in some_list:
        if some_list.count(num) == 1:
            return num
