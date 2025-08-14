def first_word(text):
    import re
    return re.search(r"[a-zA-Z']+", text).group()

