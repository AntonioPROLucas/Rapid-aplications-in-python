#Questão 01 (Remova aspas triplas para executar as outras questões)
a = 0
for i in range (4):
    notas = float(input("Digite sua {}° nota :".format(i+1)))
    a += notas
    
media = a/4
print('Sua bimestral foi bimestral {}'.format(media))

'''#Questão 02
raio = 5.0
pi   = 3.14

area = pi*(raio**2)
print ('A area do circulo é de {}cm2'.format(area))'''


'''#Questão 03
lado = float(input('Digite o valor de lado: '))
area = lado**2

print("O dobro desta area é {}".format(area*2))'''


'''#Questão 04
media_de_idade = (10 + 12 + 15 + 17)/4

print ("A media de idade é igual a {}".format(media_de_idade))

media_maior = (10 + 12 + 15 + 16 + 17)/5
diferença   = media_maior - media_de_idade

diferença_percentual = ((diferença*100)/media_de_idade)

print("A diferença percentual é de {}%".format(round(diferença_percentual,2)))'''


'''#Questão 05
horas_trabalhadas = int(input("Digite quantas horas foram trabalhadas em um mês: "))
ganho_porhrs     = float(input("Quanto você ganha por hora ? "))

ganho_mensal = horas_trabalhadas*ganho_porhrs

print("Você ganhou {}".format(ganho_mensal))'''


'''#Questão 06
farenheit = float(input('Qual o atual valor em °F: '))
celsius   = (farenheit-32)/1.8 

print("Este valor em celsius é igual a {}C°".format(celsius))'''


'''#Questão 07
sec  = 1
minu = 60*sec
hra  = 60*minu

tempo_min = (1*60) + 34
tempo_sec = (1*hra)+(34*minu)


print ("O tempo decorrido em minutos foi {} min ".format(tempo_min))
print ("O tempo decorrido em segundos foi {} min ".format(tempo_sec))'''


'''#Questão 08
altura_m  = float(input('Digite quantos metros você percorreu : '))
altura_cm = altura_m *100

print('Você percorreu {}cm'.format(altura_cm))'''


'''#Questão 09
#pedir valor de lado para pegar a area de um quadrado
lado = int(input("Digite o valor de lado: "))
area = lado*lado
print("A area deste quadrado é de {}".format(area))'''


'''#Questão 10
#obtenha o valor de base e de altura para calcular a area
base   = int(input("Digite o valor do lado base: "))
altura = int(input("Digite o valor da altura: "))

area = base*altura/2
print("A area deste triangulo é de {}".format(area))'''


'''#Questão 11
pi = 3.14
# obtenha o raio do usuario
raio =int(input("Digite o valor do raio : "))
area      = pi * (raio**2)
perimetro = 2*pi*raio
diametro  = 2*raio

print("A area do circulo é de {}, seu perimetro é {}, e seu diametro é {}".format(area,perimetro,diametro))'''


'''#Questão 12
# solicite a area a ser pintada 
area = int(input("Qual devera ser a area em m2 a ser pintada ? "))
lata = 18*3

qtd_latas_nescr = area/lata

if(qtd_latas_nescr %  1 != 0):
   qtd_latas_nescr += 1 

valor = int(qtd_latas_nescr)*80

print("Você precisa de pelo menos {} latas, custando o valor de {} R$".format(int(qtd_latas_nescr),round(valor,2)))'''


'''#Questão 13
# Solicite 2 numeros inteiros e 1 numero real
n1 = int(input("Digite um valor inteiro: "))
n2 = int(input("Digite outro valor inteiro: "))
n3 = float(input("Digite um valor real: "))

print((2*n1)*(n2/2))

print((3*n1)+n3)

print(n3**3)'''