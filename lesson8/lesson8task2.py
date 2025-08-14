def is_palindrome(text: str) -> bool:
    """
    Перевіряє, чи є рядок паліндромом.
    Ігнорує регістр букв та знаки пунктуації.

    Args:
        text (str): рядок для перевірки

    Returns:
        bool: True, якщо паліндром, інакше False
    """
    # Залишаємо лише буквено-цифрові символи та зводимо до нижнього регістру
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())

    # Перевіряємо, чи читається однаково вперед і назад
    return cleaned == cleaned[::-1]


# ТЕСТИ

def test_is_palindrome() -> None:
    assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
    assert is_palindrome('0P') == False, 'Test2'
    assert is_palindrome('a.') == True, 'Test3'
    assert is_palindrome('aurora') == False, 'Test4'
    assert is_palindrome('Madam') == True, 'Extra Test5'
    assert is_palindrome('No lemon, no melon!') == True, 'Extra Test6'
    print("ok")
