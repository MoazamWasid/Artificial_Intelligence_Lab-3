
arr = [0, 1, 2, 3, 4, 5, 6]

for i in range(7):
    if arr[i] == 3 or arr[i] == 6:
        continue
    print(arr[i], end=" ")