n = int(input("Enter a number: "))

while n > 9:
    result = 1
    for digit in str(n):
        result *= int(digit)
    n = result

print(n)
