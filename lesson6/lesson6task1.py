import string

letters = string.ascii_letters

inp = input("Enter two letters : ")
start, end = inp.split('-')
start_index = letters.index(start)
end_index = letters.index(end)

print(letters[start_index:end_index+1])
