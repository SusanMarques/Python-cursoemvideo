#faça um programa que leia algo pelo teclado e mostre na tela 
# o seu tipo primitivo e todas as informações possíveis sobre ele
'''
primeira forma:

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
'''
'''
segunda forma 

a=input("Digite algo:")
print(f"O tipo primitivo de {a} é:",type(a),f"{a} é alfabético?",a.isalpha(),f"{a} é numérico?",a.isnumeric(),f"{a} é alpha numérico?",a.isalnum())
'''
    