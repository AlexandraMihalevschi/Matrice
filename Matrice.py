A = [[1, 4, 5, 12, 14], 
    [-5, 8, 9, 0, 17],
    [-6, 7, 11, 19, 21],
    [14, 7, 0, 1, 2], 
    [-19, 4, 18, 5, 20]]

print('Suma fiecărui rând din matrice')
for i in range(0, len(A)):
    print(sum(A[i]))

print('Suma elementelor din fiecare coloană')
for j in range(0, 5):
    sum = 0
    for i in range(len(A)):
        sum = sum + A[i][j]
    print(sum)

print("Diagonala principala")
diagonala = []
for i in range(len(A)):
    diagonala.append(A[i][i])
print(diagonala)

print("Diagonala secundara")
diagonala = []
for i in range(len(A)):
    j=5-1-i
    diagonala.append(A[i][j])
print(diagonala)