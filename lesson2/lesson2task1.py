from unicodedata import digit

number = int (input("Enter a 5-digit numbers:"))
digit1 = number % 10
digit2 = (number // 10 ) % 10
digit3 = (number // 100 ) % 10
digit4 = (number // 1000 ) % 10
digit5 = (number // 10000) % 10
reserved_number = digit1 * 10000 + digit2 * 1000 + digit3 * 100 + digit4 * 10 + digit5
print("reversed number:", reserved_number)


