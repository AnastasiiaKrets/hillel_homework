from unicodedata import digit

number = int (input("Enter a 4-digit numbers:"))
digit1 = number % 10
digit2 = (number // 10 ) % 10
digit3 = (number // 100 ) % 10
digit4 = (number //1000 ) % 10
reserved_number = digit1 * 1000 + digit2 * 100 + digit3 * 10 + digit4
print("reversed number:", reserved_number)


