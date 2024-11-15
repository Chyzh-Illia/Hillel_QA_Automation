from os.path import split

incoming_data = str(input("Enter any numbers: "))
convert_to_list = incoming_data.split(" ")
total_numbers = 0
for i in convert_to_list:
    total_numbers += int(i)
print(f"Sum all entered values: {total_numbers}")