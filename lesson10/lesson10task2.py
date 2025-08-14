def first_word(text):
    """Пошук першого слова."""
    # Замінюємо крапки і коми на пробіли
    for ch in ('.', ','):
        text = text.replace(ch, ' ')
    # Розділяємо по пробілах і повертаємо перший непорожній елемент
    for word in text.split():
        return word
    return ""  # якщо текст порожній


# Тести
assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
