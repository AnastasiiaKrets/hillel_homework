import string, keyword

name = input()


if name in keyword.kwlist:
    print(False)
elif name == "":
    print(False)
elif name[0].isdigit():
    print(False)
elif any(ch.isupper() for ch in name):
    print(False)
elif "__" in name and name != "_":
    print(False)
elif any((ch in string.punctuation and ch != "_") or ch.isspace() for ch in name):
    print(False)
else:
    print(True)
