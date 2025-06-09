# 1 × 20 × 3 = 1 × 1 × 3 = 3
wykladnik=int(input())
wynik=1*pow(2,wykladnik)*3

reszta_z_dzielenia=wynik%2

if reszta_z_dzielenia == 0:
    print('TAK')
else:
    print('NIE')