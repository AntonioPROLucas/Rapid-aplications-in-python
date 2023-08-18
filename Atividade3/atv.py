#Questão 01
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
n3 = int(input("Digite outro valor: "))

maior = n1
menor = n1

if(n2>maior):
    maior = n2
elif(n2<menor):
    menor = n2
    
if(n3>maior):
    maior = n3
elif(n3<menor):
    menor = n3
    
print(maior,menor)

'''#Questão 02
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
n3 = int(input("Digite outro valor: "))

if (n1>n2):
    aux = n2
    n2  = n1
    n1  = aux
if (n2>n3):
    aux = n3
    n3  = n2
    n2  = aux
if (n1>n2):
    aux = n2
    n2  = n1
    n1  = aux
print(n1,n2,n3)'''

'''#Questão 3
age = int(input("Digite sua idade: "))

if (5<=age<=7):
    print("Infantil A")

elif(8<=age<=10):
    print("Infantil B")
    
elif(11<=age<=13):
    print("Juvenil A")
    
elif(14<=age<=17):
    print("Juvenil B")

elif(age>=18):
    print("Adulto")
    
else:
    print("Alien")'''

'''#Questão 04
n = int(input("Digite um numero: "))

if (n%2 == 0):
    print("Par")
elif(n==0):
    print("Nulo")
else:
    print("Inpar")
    
if (n<0):
    print("negativo")
elif(n>0):
    print("positivo")'''

'''#Questão 05
code = int(input("Insira seu codigo(310,456,885): "))
salr = float(input("Digite seu salario: "))
x    = salr
if (code==310):
    salr = (salr + ((salr*5)/100))
elif(code==456):
    salr = (salr + ((salr*7.5)/100))
elif(code==885):
    salr = (salr + ((salr*10)/100))
else:
    salr = (salr + ((salr*15)/100))
print("Seu salario aumentou de R${} para R${}".format(x,salr))'''

'''#Questão 06
p = bool(input("Qual o valor de p(0 ou 1): "))
q = bool(input("Qual o valor de q(0 ou 1): "))

print((p and q) and not(p or q))
print((p and not q) or q)'''
