
print("Enter lines of text:")
lines = []

while True:
    line = input()
    if not line:
        break
    lines.append(line.lower())

for line in lines:
    print("Your entered string in lower case is: ", line)