from typing import List, Union

def find_unique_value(some_list: List[Union[int, float]]) -> Union[int, float]:
    """
    Знаходить унікальне число у списку.

    Args:
        some_list (List[Union[int, float]]): список чисел

    Returns:
        Union[int, float]: унікальне число
    """
    for num in some_list:
        if some_list.count(num) == 1:
            return num
    # Якщо не знайдено
    raise ValueError("Унікальне число не знайдено")


# ТЕСТИ
def test_find_unique_value() -> None:
    assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
    assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
    assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
    print("ok")

# Запуск тестів
test_find_unique_value()
