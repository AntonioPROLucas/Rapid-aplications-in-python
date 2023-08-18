#Atividades Python aula 06 (remover aspas triplas para executar as outras questões)
# Criação de pasta
ref_arquivo = open('notas_estudantes.txt',"w")

with open('notas_estudantes.txt',"w") as file :
    file.write("Jose 10 15 20 30 40")
    file.write("\nPedro 23 16 19 22")
    file.write("\nSuzana 8 22 17 14 32 17 24 21 2 9 11 21")
    file.write("\nGisela 12 28 21 45 26 10")
    file.write("\nJoão 14 32 25 16 29")
#QUESTÃO 01

ref_arquivo.close

ref_arc = open('notas_estudantes.txt',"r")
for linha in ref_arc:
    valores = linha.split()
    if(len(valores[1:len(valores)])>=6):
        print(valores)
        
'''#QUESTÃO 02
    
ref_arquivo.close

ref_arc = open('notas_estudantes.txt',"r")
line    = ref_arc.readline()
x       = 0
type(line)
line = line.split(' ')
for i in range (len(line)-1):
    a = int(line[i+1])
    x += a
media = x/(len(line) - 1)
print(line[0],round(media,2))
line2    = ref_arc.readline()
x       = 0
type(line2)
line2    = line2.split()
for i in range (len(line2)-1):
    a = int(line2[i+1])
    x += a
media = x/(len(line2)-1)
print(line2[0],round(media,2))
line3    = ref_arc.readline()
x       = 0
type(line3)
line3    = line3.split()
for i in range (len(line3)-1):
    a = int(line3[i+1])
    x += a
media = x/(len(line3)-1)
print(line3[0],round(media,2))
line4    = ref_arc.readline()
x       = 0
type(line4)
line4    = line4.split()
for i in range (len(line4)-1):
    a = int(line4[i+1])
    x += a
media = x/(len(line4)-1)
print(line4[0],round(media,2))
line5    = ref_arc.readline()
x       = 0
type(line5)
line5    = line5.split()
for i in range (len(line5)-1):
    a = int(line5[i+1])
    x += a
media = x/(len(line5)-1)
print(line5[0],round(media,2))'''

'''#QUESTÃO 03

ref_arquivo.close

ref_arc = open('notas_estudantes.txt',"r")
line    = ref_arc.readline()
maior   = 0
menor   = 0
type(line)
line = line.split(' ')
menor = int(line[1])
for i in range (len(line)-1):
    a = int(line[i+1])
    if(a > maior):
        maior = a
    elif(a < menor):
        menor = a
print(line[0], maior, menor)
line2    = ref_arc.readline()
maior    = 0
type(line2)
line2    = line2.split()
menor = int(line2[1])
for i in range (len(line2)-1):
    a = int(line2[i+1])
    if(a > maior):
        maior = a
    elif(a < menor):
        menor = a
print(line2[0],maior,menor)
line3    = ref_arc.readline()
maior    = 0
type(line3)
line3    = line3.split()
menor = int(line3[1])
for i in range (len(line3)-1):
    a = int(line3[i+1])
    if(a > maior):
        maior = a
    elif(a < menor):
        menor = a
print(line3[0],maior,menor)
line4    = ref_arc.readline()
maior       = 0
type(line4)
line4    = line4.split()
menor = int(line4[1])
for i in range (len(line4)-1):
    a = int(line4[i+1])
    if(a > maior):
        maior = a
    elif(a < menor):
        menor = a
print(line4[0],maior,menor)
line5    = ref_arc.readline()
maior    = 0
type(line5)
line5    = line5.split()
menor = int(line5[1])
for i in range (len(line5)-1):
    a = int(line5[i+1])
    if(a > maior):
        maior = a
    elif(a < menor):
        menor = a
print(line5[0],maior, menor)
ref_arc.close'''