from unicodedata import digit

number = int (input("Enter a 4-digit numbers:"))
digit1 = (number // 1000 ) % 10
digit2 = (number // 100 ) % 10
digit3 = (number // 10 ) % 10
digit4 = number  % 10
print (digit1)
print (digit2)
print(digit3)
print (digit4)
