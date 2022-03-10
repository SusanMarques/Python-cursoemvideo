#faça um programa que leia algo pelo teclado e mostre na tela 
# o seu tipo primitivo e todas as informações possíveis sobre ele
print("")
leitor=input("Digite alguma coisa: ")
print("")
#tipos
tipo=type(leitor)
#oque
numero=bool(leitor.isnumeric())
letra=bool(leitor.isalpha())
letra_numero=bool(leitor.isalpha())
minusculo=bool(leitor.islower())
maiusculo=bool(leitor.isupper())
todas_as_iniciais_maiusculo=bool(leitor.istitle())
print(f"topo de variavel {tipo}")
print(f"contem números{numero}\n contem letras{letra}\n contem letras com numeros{letra_numero}\n E maiuscula{maiusculo}\n É minusculo {todas_as_iniciais_maiusculo}")

