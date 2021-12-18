f = open("C:/Users/Alexandra/Desktop/Python/Matrix.txt", 'r')
mat = []
for i in f:
    i_split = i.strip()
    lista = i_split.split()
    mat.append(lista)
f.close()

s = 0
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j]==mat[2][2]:
            s = s + int(mat[i][j])
print(s)