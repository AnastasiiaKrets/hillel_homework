def popular_words(text, words):
    text_lower = text.lower().split()
    return {word: text_lower.count(word) for word in words}
