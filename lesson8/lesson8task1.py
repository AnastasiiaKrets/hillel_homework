from typing import List

def add_one(some_list: List[int]) -> List[int]:
    """
    Приймає список цифр, що створюють ціле число.
    Додає до нього 1 і повертає результат як список цифр.

    Args:
        some_list (List[int]): список цифр числа

    Returns:
        List[int]: список цифр результату
    """
    number = int("".join(map(str, some_list)))
    number += 1
    return [int(d) for d in str(number)]


# ТЕСТ
def test_add_one():
    assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
    assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
    assert add_one([0]) == [1], 'Test3'
    assert add_one([9]) == [1, 0], 'Test4'
    assert add_one([4, 2, 9]) == [4, 3, 0], 'Extra Test5'
    assert add_one([1, 0, 0, 0]) == [1, 0, 0, 1], 'Extra Test6'
    print("✅ Усі тести пройдено")


# Запуск тестів
test_add_one()
