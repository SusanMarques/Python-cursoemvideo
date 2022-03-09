#aula 06 tipos primitivos e saída de dados
#resolução do desafio 03 da aula 04 (cire um script
# python que leia dois números e tente mostrar a soma entre eles)
n1=int(input("Digite um número "))
n2=int(input("Digite outro número "))
s=n1+n2
#print("A soma entre ",n1," e ",n2," vale: ",s)
print("A soma entre {} e {} vale: {}".format(n1,n2,s))