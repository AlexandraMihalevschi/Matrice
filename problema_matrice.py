f = open("C:/Users/Alexandra/Desktop/Python/Matrix.txt", 'r')
mat = []
for i in f:
    i_split = i.strip()
    lista = i_split.split()
    mat.append(lista)
f.close()

s1 = 0
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j]==mat[9][9]:
            s1 = s1 + int(mat[i][j])
s2 = 0
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j]==mat[9][0]:
            s2 = s2 + int(mat[i][j])
s3 = 0
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j]==mat[0][9]:
            s3 = s3 + int(mat[i][j])
s4 = 0
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j]==mat[0][0]:
            s4 = s4 + int(mat[i][j])
print(s1)
print(s2)
print(s3)
print(s4)