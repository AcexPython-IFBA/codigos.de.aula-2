#Escreva um programa que leia uma lista de números e calcule a média

numeros = [10, 20, 30, 40, 50] 

soma = 0
for numero in numeros:
    soma += numero  

media = soma / len(numeros)
print("A média é:", media)