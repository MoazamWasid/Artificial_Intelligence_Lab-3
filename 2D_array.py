
m = int(input("Input rows: "))
n = int(input("Input columns: "))

matrix = [[i * j for j in range(n)] for i in range(m)]
print(matrix)