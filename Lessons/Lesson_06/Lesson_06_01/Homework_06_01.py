incoming_data = str(input("Enter your first string: ")) # incoming data from user
convert_to_set = set(incoming_data) # convert to set
unique_symbols = len(convert_to_set) # count the number of unique characters

print(f"Кількість унікальних символів введених користувачем: {unique_symbols} ")

if unique_symbols > 10:
    print(True)
else: print(False)