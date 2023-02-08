


matriz=[[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for l in range(0, n):
    for c in range (0, 3):
     matriz[l][c] = int(input(f'Digite o valor: [{l}, {c}]: '))
print('-=' * 30)
for l in range (0, n):
    for c in range (0, 3):
        print(f'[{matriz[l][c]}]', end='')
    print()




'''
matriz_devedores=[
    ["Jenny","Nascimento","2"],
    ["Cleiton","Goulart","0"],
    ["Valentina","Romanelli","1"],

]
for nomes,sobrenomes,divida in matriz_devedores:
    print("Nomes: " + nomes + " | Sobrenomes: " + sobrenomes + " | Dívidas: " + divida + "\n")
'''