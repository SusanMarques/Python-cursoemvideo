'''
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''

metros=int(input("Digite o valor em metros "))
centímetros= metros*100
milímetros= metros*1000
print("{} metros em centímetros é igual a {}cm, e em milímetros é {}mm ".format(metros,centímetros,milímetros))