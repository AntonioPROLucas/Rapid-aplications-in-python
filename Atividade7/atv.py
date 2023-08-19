#Atividades Python aula 07 (remover aspas triplas para executar as outras questões)
import random

with open("forca.txt",'w') as file :
    file.write('codorna\n')
    file.write('jacare\n')
    file.write('molusco\n')
    file.write('leao\n')
    file.write('tigre\n')
    file.write('urso\n')
    file.write('ouriço\n')
    file.write('cobra\n')
    file.write('babuino\n')
    file.write('cavalo\n')
    
ref_arquivo = open("turma.txt", "w")
with open('turma.txt', 'w') as file:
    file.write("Antonio\n")
    file.write("José\n")
    file.write("Marcus\n")
    file.write("Miguel\n")
    file.write("André\n")
    file.write("João\n")
    file.write("James\n")
    file.write("Heptor\n")
    file.write("Octavio\n")
    file.write("Nonol\n")
    file.write("Deca\n")
    file.write("Demi I.\n")
    file.write("Dodoria II.\n")
    file.write("Tereza\n")
    file.write("Qualigola Torze\n")
    file.write("Kim'Ze\n")
    file.write("Ed'Zá VI\n")
    file.write("Decimund VII\n")
    file.write("Desmond VIII\n")
    file.write("Dio IX\n")
    file.write("Leonardo Da'Vinte\n")
    file.write("Davi'n T. II\n")
    file.write("Teteu III\n")
    file.write("V. Teodore IV\n")
    file.write("Vinci'Penta\n")
    file.write("David VI\n")
    file.write("Vince Heptor\n")
    file.write("Davi´d Octavius\n")
    file.write("Vitu Norna\n")
    file.write("Zé Trinca\n")
    file.write("Zé Trinta I\n")
    file.write("Satoru Gojo")
ref_arquivo.close

#Questão 01
# Forca (arquivo:'forca.txt')

print ("Este é o jogo da forca advinhe qual é o animal digitando a letra certa! Se o você errar 6 vezes você perde.")
print ("ps:(Você NÃO pode repetir a masma letra!!)\n")

c     = []
vidas = 6
letra = ''
f = []
g = []
ref_arc = open("forca.txt",'r')
line    = ref_arc.readlines()
type(line)
random.shuffle(line)
a = len(line)
b = random.randint(1,a)
c = len(line[b])
d = len(line[b])
c -= 1
for i in range(c):
    g+=['_']
print(g)
print('\n')
while (vidas>0):
    e = 0
    letra = input("Digite uma letra (menuscula): ")
    for j in range (len(line[b])):
        for k in range(len(f)):
            if (letra==f[k]):
                letra = ''
        if (j > d-1):
            break
        for j in range (len(line[b])):
            if (letra == line[b][j]):
                g[j] = [letra]
                c -= 1
                e += 1
                f += letra
    print(g)
    if(e==0):
        vidas -= 1
        print ("Você errou! Tente novamente.\n")
    if(c==0):
        print("Você venceu! A resposta é {}".format(line[b]))
        break
    
#Questão 02
#Sorteio de turma (arquivo:'turma.txt')

'''with open("turma.txt",'r') as file:
    line    = file.readlines()
    for i in range (len(line)):
        line[i]=line[i].replace('\n', '')
        
    random.shuffle(line)
    team           = 0
    inteiro, resto = divmod(len(line), 5)
    for j in range (inteiro):
        print('Equipe {}: '.format(j+1))
        if(j<resto): print(line[5*j:5*j+5]+line[inteiro*5+j:inteiro*5+j+1])
        else: print(line[5*j:5*j+5])'''



    