#Questão 01
for i in range (0,51):
    print(i)

'''#Questão 02
for i in range (0 , 51 , 2):
    print(i)'''
      
'''#Questão 03
a = int(input("digite um valor: "))
b = int(input("digite outro valor maior: "))
 
if (a%2==0):
    for i in range (a , b , 2):
        print (i)
else :
    a= a+1
    for i in range (a , b , 2):
        print (i)'''

'''#Questão 04
a = int(input("Digite um valor:  "))
b = a
while (a>1):
    a = a-1
    b = b*a
    c = (b*a)
    
print("O fatorial deste numero é {}".format(c))'''

'''#Questão 5
a = int(input("Digite um valor:  "))
b = int(input("Digite um segundo valor:  "))

for i in range (b-1):
    a = a*a
    
print (a)'''

'''#Questão 06
a = int(input("Digite um valor:  "))
b = 1  

for i in range (10):
    print ('{}X{}={}'.format(a,b,a*b))
    b=b+1'''
    
'''#Questão 08
a = int(input("Digite um valor:  "))
b = a
if(a>0):
    while (a>0):
        a = a-1
        b = b+a
        c = (b+a)
    print(c)
else:
    print ("Você não pode por um numero nulo nem negativo!!")'''

'''#Questão 09
n = int(input("Digite um valor:  "))
ant=1
ant2=1
post=1

print(ant)
print(ant2)
for i in range (n-2):
    post = ant+ant2
    print (post)
    ant=ant2
    ant2=post'''
    
'''#Questão 10
ant=1
ant2=1
post=1

print(ant)
print(ant2)
for i in range (13):
    post = ant+ant2
    print (post)
    ant=ant2
    ant2=post'''
    
'''#Questão 11
a = int(input("Digite um valor:  "))
b = a
while (a>1):
    a = a-1
    b = b*a
    c = (b*a)
    
print("O fatorial deste numero é {}".format(c))'''

'''#Questão 12
nomedacidade = (input("Qual o nome da cidade? "))
pop = int(input("Qual o tamanho da população? "))
limite = 0  
media_salario   = 0 
media_filhos    = 0  
maior_salario   = 0
salario_pequeno = 0
while (limite<=pop-1):
    salario = int(input("Digite o seu salario(digite 000 para parar):  "))
    if (salario == 000):
        break
    else:
        filhos  = int(input("Digite quantos filhos você tem :  "))
        limite = limite + 1
        media_salario = media_salario + salario 
        media_filhos  = media_filhos  + filhos 
    if (salario > maior_salario):
        maior_salario = salario
    if (salario < 150):
        salario_pequeno = salario_pequeno + 1
            
print ("A media salarial de {} é de {}".format(nomedacidade,media_salario/limite))
print ("A media filhos de {} é de {}".format(nomedacidade,media_filhos/limite))
print ("O maior salario de {} é de {}R$".format(nomedacidade,maior_salario))
print ("Em media {}% da populção de {} recebe menos de R$150.00".format(salario_pequeno*100/limite,nomedacidade))'''