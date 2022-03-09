#faça um programa que leia algo pelo teclado e mostre na tela 
# o seu tipo primitivo e todas as informações possíveis sobre ele
leitor=input("Digite alguma coisa: ")
numero=bool(leitor.isnumeric())
letra=bool(leitor.isalpha())
letra_num=(leitor.isalphanum)