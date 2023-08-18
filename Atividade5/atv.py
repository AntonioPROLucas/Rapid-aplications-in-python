#Atividades Python aula 05 (remover aspas triplas para executar as outras questões)

#Questão 01

# Identicar se dois textos possuem conteudo e comprimento iguais ou diferentes
str1 = input("Digite um texto: ")
str2 = input("Digite outro texto: ")

a = len(str1)
b = len(str2)

print("{}, {}".format(str1,a))
print("{}, {}".format(str2,b))

if(a==b):
    print("Os textos tem o mesmo comprimento")
else:
    print("Os textos possuem comprimentos diferentes")
str1 = str1.replace(' ','')
str2 = str2.replace(' ','')

if(str1!=str2):
    print("Os textos são diferentes")
else:
    print("Ambos possuem o mesmo conteudo")
  
'''#Questão 02

# Deixar nome solicitado em letras maiusculas
name = input("Digite seu nome : ")
a=len(name)
b=name.upper()
print(b[a-1::-1])'''
    

'''#Questão 03

name = input("Digite seu nome : ")
b=1
for i in range (len(name)):
    a = 0
    b = b
    print(name[a:b])
    b = b + 1'''
    
'''#Questão 04

name = input("Digite seu nome : ")
for i in range (len(name)):
    print(name[i:len(name)])'''

'''#Questão 05

# Identificar um palindromo
name  = input("Digite uma palavra: ")
a     = len(name)
polin = name[a-1::-1]

name  = name.replace(" ","")
polin = polin.replace(" ","")

if(name.lower()==polin.lower()):
    print("Esta palavra/frase é um palindromo")
else:
    print("Esta palavra/frase NÃO é um palindromo")'''
    
'''#Questão 06

dna = str("AATCTGCAC")

res = dna.replace("A","t")
res = res.replace("T","a")
res = res.replace("C","g")
res = res.replace("G","c")

print("A cadeia de dna é: {} e a sua cadeia complementar é: {}".format(dna, res.upper()))'''

'''#Questão 07

data = input("Digite uma data dd/mm/aa: ")

data = data.replace("/01/"," de Janeiro de ")
data = data.replace("/02/"," de Fevereiro de ")
data = data.replace("/03/"," de Março de ")
data = data.replace("/04/"," de Abril de ")
data = data.replace("/05/"," de Maio de ")
data = data.replace("/06/"," de Junho de ")
data = data.replace("/07/"," de Julho de ")
data = data.replace("/08/"," de Agosto de ")
data = data.replace("/09/"," de Setembro de ")
data = data.replace("/10/"," de Outubro de ")
data = data.replace("/11/"," de Novembro de ")
data = data.replace("/12/"," de Dezembro de ")

print(data)'''

'''#Questão 08

str1 = input("Digite a primeira string: ")
str2 = input("Digite a segunda string: ")

p    = str1.find(str2)

if p == -1:
    print(f"'{str2}' não encontrada em '{str1}'")
else:
    print(f"{str2} encontrada na posição {p} de {str1}")'''

'''#Questão 09

str1 = input("Digite a primeira string: ")
str2 = input("Digite a segunda string: ")

p    = str1.find(str2)

if p == -1:
    print(str2)
else:
    print(str2)'''

'''#Questão 10
str_ = input("Digite a primeira string: ")

str_ = str_.lower()
vogais  = str_.count('a') + str_.count('e') + str_.count('i') + str_.count('o') + str_.count('u')
espaços = str_.count(' ')

print ("A frase possui {} vogais e {} espaços em branco".format(vogais,espaços))'''

'''#Questão 11

string = input("Digite uma string : ")
a=0
b=1
for i in range (len(string)):
    
    print("{}: {}X ".format(string[a:b], string.count(string[a:b])))
    a = a+1 
    b = b+1'''
    

'''#Questão 12


n = input("Digite um valor de 0 a 99 : ")
if(len(n)==2):
        if(n[0]=="0"):
            n = n.replace("00","Zero")
        if(n[0]=="1"):
            n = n.replace("10","Dez")
            n = n.replace("11","Onze")
            n = n.replace("12","Doze")
            n = n.replace("13","Treze")
            n = n.replace("14","Quatorze")
            n = n.replace("15","Quinze")
            n = n.replace("1","Deze")
        elif(n[0]=="2"):
            n = n.replace("20","Vinte")
            n = n.replace("22","Vinte e dois")
            n = n.replace("2", "Vinte e ")
        elif(n[0]=="3"):
            n = n.replace("30","Trinta")
            n = n.replace("33","Trinta e tres")
            n = n.replace("3","Trinta e ")
        elif(n[0]=="4"):
            n = n.replace("40","Quarenta")
            n = n.replace("44","Quarenta e quatro")
            n = n.replace("4","Quarenta e ")
        elif(n[0]=="5"):
            n = n.replace("50","Cinquenta")
            n = n.replace("55","Cinquenta e cinco")
            n = n.replace("5","Cinquenta e ")
        elif(n[0]=="6"):
            n = n.replace("60","Sessenta")
            n = n.replace("66","Sessenta e seis")
            n = n.replace("6","Sessenta e ")
        elif(n[0]=="7"):
            n = n.replace("70","Setenta")
            n = n.replace("77","Setenta e sete")
            n = n.replace("7","Setenta e ")
        elif(n[0]=="8"):
            n = n.replace("80","Oitenta")
            n = n.replace("88","Oitenta e oito")
            n = n.replace("8","Oitenta e ")
        elif(n[0]=="9"):
            n = n.replace("90","Noventa")
            n = n.replace("99","Noventa e nove")
            n = n.replace("9","Noventa e ")
if(len(n)>1):    
    n = n.replace("1","um")
    n = n.replace("2","dois")
    n = n.replace("3","tres")
    n = n.replace("4","quatro") 
    n = n.replace("5","cinco")
    n = n.replace("6","seis")
    n = n.replace("7","sete")
    n = n.replace("8","oito")
    n = n.replace("9","nove")
else:
    n = n.replace("0","Zero")
    n = n.replace("1","Um")
    n = n.replace("2","Dois")
    n = n.replace("3","Tres")
    n = n.replace("4","Quatro") 
    n = n.replace("5","Cinco")
    n = n.replace("6","Seis")
    n = n.replace("7","Sete")
    n = n.replace("8","Oito")
    n = n.replace("9","Nove")
print(n.strip("0"))'''

'''Questão 13

#ASCII

ASCII = input("Digite uma palavra: ")
a     = 1
d     = ""
for i in range (len(ASCII)):
    b = ord(ASCII[i:a])
    a = a + 1
    c = (chr(b+1))
    d = d + c
    
print (d)'''

'''#Questão 14

ASCII = input("Digite uma palavra: ")
a     = 1
d     = ""
for i in range (len(ASCII)):
    b = ord(ASCII[i:a])
    a = a + 1
    c = (chr(b-32))
    d = d + c
    
print (d)'''

'''#Questão 15

L1    = input("Digite uma letra: ")
L2    = input("Digite outra letra: ")
ASCII = input("Digite uma string com essas duas letras: ")
a     = 1
d     = ""
e     = ord(L1)
f     = ord(L2)
for i in range (len(ASCII)):
    b = ord(ASCII[i:a])
    if(b==e):
        b = f
        a = a + 1
        c = chr(b)
        d = d + c
    elif(b==f): 
        b = e
        a = a + 1
        c = chr(b)
        d = d + c
    else:
        a = a + 1
        c = chr(b)
        d = d + c
print (d)'''

'''#Questão 16

a = int(input("Digite um valor: "))
b = int(input("Digite outro valor: "))
c = int(input("Digite outro valor: "))
d = int(input("Digite outro valor: "))
e = int(input("Digite outro valor: "))

lista = [a,b,c,d,e]

print(lista)'''

'''#Questão 17

L1   = ["Lista de impares"]
L2   = ["Lista de pares"]
for i in range (10):
    n   = int(input("Digite um valor:    "))

    if(n % 2 != 0):
        L1 += [n]
    elif(n % 2 == 0):
        L2 += [n]

print(L1)
print(L2)'''

'''#Questão 18

i1    = int(input('Digite sua idade:  '))
alt1  = float(input('Digite sua altura: '))
i2    = int(input('Digite sua idade:  '))
alt2  = float(input('Digite sua altura: '))
i3    = int(input('Digite sua idade:  '))
alt3  = float(input('Digite sua altura: '))
i4    = int(input('Digite sua idade:  '))
alt4  = float(input('Digite sua altura: '))
conta = 0
media = (alt1+alt2+alt3+alt4)/4
a1    = [i1,alt1 ]
a2    = [i2,alt2 ]
a3    = [i3,alt3 ]
a4    = [i4,alt4 ]
if(a1[0]==13)and(a1[1]<media):
    conta += 1
if(a2[0]==13)and(a2[1]<media):
    conta += 1
if(a3[0]==13)and(a3[1]<media):
    conta += 1  
if(a4[0]==13)and(a4[1]<media):
    conta += 1  
print("{} alunos possuem 13 anos e uma idade abaixo da media de alunos".format(conta))'''

'''#Questão 19
alunos = int(input('Solicite o numero de alunos: '))
a = 0
aluno = []
conta = 0
for i in range(alunos):
    alt   = float(input('Digite a altura do aluno {}: '.format(i+1)))
    a     = a + alt
    media = a/alunos
    aluno += [alt]
for i in range(alunos):  
    i2    = int(input('Digite a idade do aluno {}:  '.format(i+1)))
    aluno += [i2]
    if(aluno[i+alunos]==13)and(aluno[i]<media):
        conta += 1
   
print("{} alunos possuem 13 anos e uma idade abaixo da media de alunos".format(conta))'''

'''#Questão 20

infinito = 0
a        = 0
aluno    = []
conta    = 0
b        = 0
while(infinito == 0):
    altura = float(input('Digite a altura do aluno (digite -1 para parar): '))
    if (altura == -1.0):
        break
    else:
         a     =  a + alt
         media =  a/alunos
         aluno += [alt]
         b     +=  1
for i in range(b):  
    i2    = int(input('Digite a idade do aluno {}:  '))
    aluno += [i2]
    if(aluno[i+alunos]==13)and(aluno[i]<media):
        conta += 1
   
print("{} alunos possuem 13 anos e uma idade abaixo da media de alunos".format(conta))'''

'''#Questão 21

m1  = int(input("Digite a temperatura de Janeiro em °C:   "))
m2  = int(input("Digite a temperatura de Fevereiro em °C: "))
m3  = int(input("Digite a temperatura de Março em °C:     "))
m4  = int(input("Digite a temperatura de Abril em °C:     "))
m5  = int(input("Digite a temperatura de Maio em °C:      "))
m6  = int(input("Digite a temperatura de Junho em °C:     "))
m7  = int(input("Digite a temperatura de Julho em °C:     "))
m8  = int(input("Digite a temperatura de Agosto em °C:    "))
m9  = int(input("Digite a temperatura de Setembro em °C:  "))
m10 = int(input("Digite a temperatura de Outubro em °C:   "))
m11 = int(input("Digite a temperatura de Novembro em °C:  "))
m12 = int(input("Digite a temperatura de Dezembro em °C:  "))

a = 1
media       = (m1+m2+m3+m4+m5+m6+m7+m8+m9+m10+m11+m12)/12
temperatura = [m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,"Janeiro","Fevereiro","Março",'Abril',"Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]

print("A media anual é {}".format(media))
for i in range(12):
    if (temperatura[i] > media):
       print("{}- {};".format(a,temperatura[i+12]))
       a += 1'''

'''#Questão 22
infinity = 0
a        = 0
saltos   = []
while(infinity == 0):
    nome = input("Digite seu nome: ")
    if (nome == "") or (nome==" "):
        break
    for i in range(5):
        alt_salto = float(input('Qual a altura do {}° salto: '.format(i+1)))
        a         = a + alt_salto
        saltos   += [alt_salto]
    media = a/5
    print ("Atleta: {}".format(nome))
    print ("Saltos :",saltos)
    print ("Media dos saltos: {}".format(media))'''