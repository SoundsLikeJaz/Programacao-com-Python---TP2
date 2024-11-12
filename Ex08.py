LISTA1 = [1, 2, 3, 4, 5, 6, 7, 8];
LISTA2 = [10, 20, 30, 40, 50, 60, 70, 80];

LISTA3 = [];

for i in range(0, len(LISTA1)):
    LISTA3.append(LISTA1[i] + LISTA2[i]);
    
print(f"LISTA1: {LISTA1}");
print(f"LISTA2: {LISTA2}");
print(f"LISTA3: {LISTA3}");