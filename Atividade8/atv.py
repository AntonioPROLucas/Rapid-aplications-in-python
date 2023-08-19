import re
from collections import Counter
import random

#Questão 01

with open('frase.txt', 'w') as file:
    file.write('A imaginação é mais importante que o conhecimento, ')
    file.write('porque o conhecimento é limitado, ao passo que a imaginação abrange o mundo inteiro.')
file.close

with open('frase.txt', 'r') as file:
    line = file.readline()
    type(line)
    a     = 0
    linha = line
    line  = line.split(' ')
    linha = linha.split(' ')
    for i in range (len(linha)):
        linha[i] = linha[i].lower()
        linha[i] = linha[i].replace(',', '')
        linha[i] = linha[i].replace('.', '')
    print(len(line))
    for i in range(len(line)):
        b = 0
        line[i] = line[i].lower()
        line[i] = line[i].replace(',', '')
        line[i] = line[i].replace('.', '')
        linha[i] = ['']
        for j in range(len(line)):
            if(line[i]==linha[j]):
                b = 0
                break
            elif(line[i]!=linha[j]):
                b = 1
        a += b
    print(a)

#Questão 02

'''with open('aleatoriedade.txt', 'w') as file:
    for i in range(10):    
        file.write(str(random.randint(1,10)))
        file.write('\n')'''

#Questão 03

'''with open('cont_lines.txt',"w") as file :
    file.write("A vida de um homem é mais ")
    file.write("\npassageiracdo que calendario, ")
    file.write("\nporém um calendario depois de um ano ")
    file.write("\né jogado fora ,já a sua vida é ")
    file.write("\nlembrada pelos outros pela eternidade!")
    
file.close
ref_arquivo = open('cont_lines.txt',"r")
line = ref_arquivo.readlines()
type(line)
print("O arquivo possui {} linhas".format(len(line)))'''
#Questão 04

'''with open('frase.txt', 'w') as file:
    file.write('A imaginação é mais importante que o conhecimento, ')
    file.write('porque o conhecimento é limitado, ao passo que a imaginação abrange o mundo inteiro.')
file.close
with open('frase.txt', 'r') as file:
    line = file.readline()
    type(line)
    a     = 0
    line  = line.split(' ')
    palavra = input("Digite uma palavra: ")
    for i in range (len(line)):
        line[i] = line[i].lower()
        line[i] = line[i].replace(',', '')
        line[i] = line[i].replace('.', '')
        if(line[i]==palavra.lower()):
            a+=1 
    print("Essa palavra aparece {} vezes.".format(a))'''

#Questão 05

'''with open('frase.txt', 'w') as file:
    file.write('A imaginação é mais importante que o conhecimento, ')
    file.write('porque o conhecimento é limitado, ao passo que a imaginação abrange o mundo inteiro.')
file.close
with open('frase.txt', 'r') as file:
    line = file.readline()
    type(line)
    a     = 0
    line  = line.split(' ')
    #Dar um input para o usuario substituir uma palavra por outra
    palavra      = input("Digite uma palavra pertencente ao texto: ")
    p_substituta = input("Digite a palavra pela qual você deseja substituir: ")
    for i in range (len(line)):
        line[i] = line[i].lower()
        line[i] = line[i].replace(',', '')
        line[i] = line[i].replace('.', '')
        if(line[i]==palavra.lower()):
            line[i] = [p_substituta]
    print(line)'''

#Questão 06

'''with open('notas_estudantes.txt',"w") as file :
    file.write("Jose  ,18 anos,10,15,20,30")
    file.write("\nPedro ,20 anos,23,16,19,22")
    file.write("\nSuzana ,19 anos,8,22,17,14")
    file.write("\nGisela,22 anos,12,28,21,45")
    file.write("\nJoão  ,20 anos,14,32,25,16")

file.close

ref_arc = open('notas_estudantes.txt',"r")
line    = ref_arc.readline()
x       = 0
type(line)
line = line.split(',')
for i in range (len(line)-2):
    a = int(line[i+2])
    x += a
media = x/(len(line) - 2)
print(line[0],round(media,2))
line2    = ref_arc.readline()
x       = 0
type(line2)
line2    = line2.split(',')
for i in range (len(line2)-2):
    a = int(line2[i+2])
    x += a
media = x/(len(line2)-2)
print(line2[0],round(media,2))
line3    = ref_arc.readline()
x       = 0
type(line3)
line3    = line3.split(',')
for i in range (len(line3)-2):
    a = int(line3[i+2])
    x += a
media = x/(len(line3)-2)
print(line3[0],round(media,2))
line4    = ref_arc.readline()
x       = 0
type(line4)
line4    = line4.split(',')
for i in range (len(line4)-2):
    a = int(line4[i+2])
    x += a
media = x/(len(line4)-2)
print(line4[0],round(media,2))
line5    = ref_arc.readline()
x       = 0
type(line5)
line5    = line5.split(',')
for i in range (len(line5)-2):
    a = int(line5[i+2])
    x += a
media = x/(len(line5)-2)
print(line5[0],round(media,2))'''
    
#Questão 07

'''with open('frase.txt', 'w') as file:
    file.write('A imaginação é mais importante que o conhecimento, ')
    file.write('porque o conhecimento é limitado, ao passo que a imaginação abrange o mundo inteiro.')
file.close
with open('frase.txt', 'r') as file:
    line = file.readline()
    type(line)
    maior = 0
    line  = line.split(' ')
    def get_most_common_words(filename, num_words):
        with open(filename, 'r') as file:
            text = file.read().lower()
        words = re.findall(r'\b\w+\b', text)
        word_counts = Counter(words)
        return word_counts.most_common(num_words)
    most_common_words = get_most_common_words('frase.txt',len(line) )
    print(most_common_words)'''
    
#Questão 08

'''with open('notas_estudantes.txt',"w") as file :
    file.write("Action Figure , 180.00 reais , {}".format(int(15)))
    file.write("\nPapel higiênico , 8.00 reais , {}".format(int(583)))
    file.write("\nSmartphone , 1.080.00 reais , {}".format(int(35)))
    file.write("\nTinta Suvinil grande(vermelha) , 30.00 reais , {}".format(int(17)))
    file.write("\nPacote de fraudas, 20.00 reais , {}".format(int(50)))

file.close

ref_arc = open('notas_estudantes.txt',"r")

#Solicitar ao usuario um valor meta de estoque

a = int(input('Digite um valor: '))
for i in range(5):
    line    = ref_arc.readline()
    x       = 0
    type(line)
    line = line.split(',')
    if(a>int(line[2])):
        print(line[0],':',line[2])'''