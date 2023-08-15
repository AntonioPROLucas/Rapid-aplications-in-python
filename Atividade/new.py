#Atividades Python aula 01 (remover aspas triplas para executar as outras questões)
#Questão1
#Solicitar ao usuario o tamanho da lista 
a     = 1
b     = 0 
x     = 0  
lista =[ ]
while (a%2 != 0):
    a   = int(input("Quantas palavras tera esta lista? (tem que ser um valor par): "))
for i in range (a):
    p1     = input("Digite a {}° palavra: ".format(i+1))
    lista += [p1]
print ("Pares inversos:")
while(b <= (len(lista)-1)):
    for i in range (len(lista)-1):
        if(len(lista)> b):
            c = len(lista[i])
            lista[b] = lista[b].lower()
            lista[i] = lista[i].lower()
            lista[b] = lista[b].replace(' ','')
            lista[i] = lista[i].replace(' ','')
            if (lista[b]==lista[i][c-1::-1]):
                print ('{} e {}'.format(lista[b], lista[i]))
                del lista[b]
                x+=1
    b += 1
if(x<=0):
    print('nenhum')
'''#Questão2
a     = 0 
b     = 0 
c     = 0 
d     = 0 
e     = 0 
f     = 0
lista = []
for i in range (50):
    n = int(input('Digite o {}° numero(de 1 a 6): '.format(i+1)))
    if (1<=n<=6):
        lista += [n]
    else :
        print("Erro você deveria digitar um valor de 1 a 6.Tente novamente")
        break
for j in range (len(lista)):
    g = lista[j]
    if (g == 1):
        a += 1
    elif(g == 2):
        b += 1
    elif(g == 3):
        c += 1
    elif(g == 4):
        d += 1
    elif(g == 5):
        e += 1
    elif(g == 6):
        f += 1
a = a*100/50
b = b*100/50
c = c*100/50
d = d*100/50
e = e*100/50
f = f*100/50
print("Valores : um {}%, dois {}% , três {}% , quatro {}% , cinco {}% , seis {}%".format(a,b,c,d,e,f))'''

'''#Questão3
s1 = input('Digite a 1° string:   ')
s2 = input('Digite a 2° string:   ')

print(s1)
print(s2)

if (len(s1)==len(s2)):
    print('As duas strings possuem o mesmo comprimento')
elif(len(s1)<len(s2)):
    print('A primeira string é menor do que a segunda')
elif(len(s1)>len(s2)): 
    print('A segunda string é menor do que a primeira')
    
s1 = s1.replace(' ', '')
s2 = s2.replace(' ', '')
s1 = s1.lower()
s2 = s2.lower()

if (s1==s2):
    print('As strings são iguais')
else:
    print('As strings são diferentes')'''

'''#Questão4
lista_name = []
lista_num  = []
infinity = 0
while (infinity==0):
    solicitacao = input("Olá como posso ajudar?(Digite 00 ou enter para parar): ")
    def incluirNovoNome(name,lista_name):
        for i in range (len(lista_name)):
            if (lista_name[i]==name):
                print ('Esse nome já existe !!')
                break
        lista_name += [name]
        print (lista_name)
    def incluirTelefone(num,lista_num):
        for i in range (len(lista_num)):
            if (lista_num[i]==num):
                print ('Esse numero já existe !!')
                break
        lista_num += [num]
        print(lista_num)
    def excluirTelefone(num,lista_num):
        for i in range (len(lista_num)):
            if (lista_num[i]==num):
                del lista_num[i] 
                break
    def excluirNome(name,lista_name):
        for i in range (len(lista_name)):
            if (lista_name[i]==name):
                del lista_name[i]
                break
    def consultarTelefone(num,lista_num):
        for i in range (len(lista_num)):
            if (lista_num[i]==num):
                print(num)
                break
        print ('Esse numero não existe !!')
    if(solicitacao=='incluirNovoNome'):
        n = input('Digite seu nome: ')
        incluirNovoNome(n,lista_name)
    elif(solicitacao=='incluirTelefone'):
        m = input('Digite seu numero: ')
        incluirTelefone(m,lista_num)
    elif(solicitacao=='excluirTelefone'):
        m = input('Digite seu numero: ')
        excluirTelefone(m,lista_num)
    elif(solicitacao=='excluirNome'):
        n = input('Digite seu nome: ')
        excluirNome(n,lista_name) 
    elif(solicitacao=='consultarTelefone'):
        m = input('Qual telefone você deseja consultar? ')
        consultarTelefone(m,lista_num)
    else:
        infinity += 1
        print (lista_name)
        print(lista_num)'''
