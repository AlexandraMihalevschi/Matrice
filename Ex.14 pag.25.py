r=int(input("Dati numarul de randuri si coloane(2 <= n <= 10): "))
#c=int(input("Dati un numar de coloane: "))
matrice=[]
for m in range(r):
    a=[]
    for n in range(r):
        a.append(0)
    matrice.append(a)

for i in range(len(matrice)):
    for j in range(len(matrice[0])):
        matrice[i][j]=int(input("Dati un element: "))
print("Aceasta este matricea introdusa:",matrice)

d_principala = []
for i in range(len(matrice)):
    d_principala.append(matrice[i][i])

d_secundara = []
for i in range(len(matrice)):
    j=r-1-i
    d_secundara.append(matrice[i][j])

d_principala_sus = []
for i in range(r):
    for j in range(r):
        if (i < j):
            d_principala_sus.append(matrice[i][j])

d_principala_jos = []
for i in range(r):
    for j in range(r):
        if (i > j):
            d_principala_jos.append(matrice[i][j])

d_secundara_sus = []
for i in range(r):
    for j in range(r):
        if (i+j < r-1):
            d_secundara_sus.append(matrice[i][j])

d_secundara_jos = []
for i in range(r):
    for j in range(r):
        if (i+j > r-1):
            d_secundara_jos.append(matrice[i][j])

if (r >= 2) and (r <= 10):
    print("Suma elementelor diagonalei principale: ", sum(d_principala))
    print("Suma elementelor diagonalei secundare: ", sum(d_secundara))
    print("Suma elementelor deasupra diagonalei principale: ", sum(d_principala_sus))
    print("Suma elementelor sub diagonala principala: ", sum(d_principala_jos))
    print("Suma elementelor deasupra diagonalei secundare: ", sum(d_secundara_sus))
    print("Suma elementelor sub diagonala secundare: ", sum(d_secundara_jos))
else: print('Ati incalcat conditia. Numarul de randuri si coloane trebuia sa se contina in intervalul [2;10].')