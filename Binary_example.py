
data = input("Enter 4-digit binary numbers separated by commas: ").split(',')
valid_numbers = []

for i in data:
    i_clean = i.strip()
    if int(i_clean, 2) % 5 == 0:
        valid_numbers.append(i_clean)

print(",".join(valid_numbers))