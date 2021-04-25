import random
import math

def Again(frase, call):
    opcao1 = input(frase)
    if opcao1 == "s" or opcao1 == "S":
        call()
    elif opcao1 == "n" or opcao1 == "N":
        Escolha()
    else:
        Again(frase, call)

def Escolha():
    print(""" \033[30mOlá! Esse programa é baseado no método de criptografia e descriptografia RSA!
    Você pode realizar uma das seguintes operações nele, escolha uma inserindo seu número correspondente:\033[1;m

    \033[1;31mCriptografar gerando nova chave pública e privada no processo\033[1;m \033[1;32m -------(1)\033[1;m
    \033[1;31mGerar nova chave pública e privada para operações futuras\033[1;m \033[1;32m -----------(2)\033[1;m
    \033[1;31mCriptografar usando uma chave pública desejada\033[1;m \033[1;32m ----------------------(3)\033[1;m
    \033[1;31mDescriptografar uma mensagem\033[1;m \033[1;32m ----------------------------------------(4)\033[1;m
    \033[1;34mCriptografar um arquivo de texto\033[1;m \033[1;32m ------------------------------------(5)\033[1;m
    \033[1;34mDescriptografar um arquivo de texto\033[1;m \033[1;32m ---------------------------------(6)\033[1;m
    \033[1;31mSair do programa\033[1;m \033[1;32m ----(7)\033[1;m""")
    opcao1 = input("\n\033[1;36m->\033[1;m ")

    if opcao1 == "1":
        e1()
    elif opcao1 == "2":
        e4()
    elif opcao1 == "3":
        e3()
    elif opcao1 == "4":
        e2()
    elif opcao1 == "5":
        e5()
    elif opcao1 == "6":
        e6()
    elif opcao1 == "7":

        exit()
    else:
        Escolha()



def totiente(numero):
    if (primo(numero)):
        return numero - 1
    else:
        return False



def primo(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i += 6
    return True



def CalcE(num):
    def mdc(n1, n2):
        rest = 1
        while (n2 != 0):
            rest = n1 % n2
            n1 = n2
            n2 = rest
        return n1

    while True:
        p2 = random.randrange(2, num)
        if (mdc(num, p2) == 1):
            return p2



def CalcPri():
    while True:
        x = random.randrange(1, 100)
        if (primo(x) == True):
            return x


def mod(a, b):
    if (a < b):
        return a
    else:
        c = a % b
        return c


def Concatenar(list):
    result= ''
    for element in list:
        result += str(element)
    return result

def Criptografar(words, p2, p1):
    tam = len(words)
    c = 0
    lista = []
    while (c < tam):
        letter = words[c]
        s = ord(letter)
        s = s ** p2
        d = mod(s, p1)
        lista.append(d)
        c += 1
    return lista


def Dividir(lista):
    half = len(lista)//2
    return lista[:half], lista[half:]

def Descriptografar():
    cifra = [int(x) for x in input(" \033[32mInsira a mensagem criptografada: \033[1;m").split()]
    cp = int(input("\033[32mInsira a chave privada:\033[1;m "))
    p1=int(input(" \033[32mInsira a 1º parte da chave pública(XXXX): \033[1;m"))

    c = 0
    tamanho = len(cifra)
    while c < tamanho:
        resultado = cifra[c] ** cp
        texto = mod(resultado, p1)

        letra = chr(texto)
        cifra.append(letra)
        c = c + 1
    return cifra


def CalcCP(toti, p2):
    cp = 0
    while (mod(cp * p2, toti) != 1):
        cp += 1
    return cp

def crypt(conteudo):
    k1 = CalcPri()
    k2 = CalcPri()
    p1 = k1 * k2
    t1 = totiente(k1)
    t2 = totiente(k2)
    totiN = t2 * t1
    p2 = CalcE(totiN)
    ChavePub = (p1, p2)

    print(' \033[32mSua chave pública gerada: \033[1;m', ChavePub)

    cp = CalcCP(totiN, p2)
    print(' \033[32mSua chave privada gerada: \033[1;m', cp)

    Mensacrip = Criptografar(conteudo, p2, p1)

    nome = input("\n\033[1;36mDefina um nome para o arquivo criptografado(nomedoarquivo.txt): \033[1;m ")
    file = open(nome,'w')
    file.write((' ').join(str(x) for x in Mensacrip))
    file.close()

    print(' \033[32mArquivo gerado com sucesso!\033[1;m')
    print("")
    Again("\n\033[36mQuer criptografar outro  arquivo? (s / n): \033[1;m ", e5)

def decrypt(conteudo):
    cifra = [int(x) for x in conteudo.split()]
    cp = int(input("\033[32mInsira a chave privada: \033[1;m "))
    p1=int(input(" \033[32mInsira a 1º parte da chave pública(XXXX): \033[1;m"))
    c = 0
    tamanho = len(cifra)
    while c < tamanho:
        resultado = cifra[c] ** cp
        texto = mod(resultado, p1)

        letra = chr(texto)
        cifra.append(letra)
        c = c + 1


    B, C = Dividir(cifra)
    C = (Concatenar(C))

    file = open("descriptografado.txt", 'w')
    file.write(C)

    file.close()
    print(' \033[32mArquivo gerado com sucesso! Nome: descriptografado.txt \033[1;m')
    print("")

    Again("\n\033[36mQuer decriptografar outro arquivo(s/n)? : \033[1;m ", e6)

def encspec(conteudo):
    print("\033[32mInsira a chave pública(XXXX XXXX):\033[1;m ")
    p1, p2 = [int(p1) for p1 in input().split()]
    Mensacrip = Criptografar(conteudo, p2, p1)
    nome = input("\n\033[1;36mDefina um nome para o arquivo criptografado(nomedoarquivo.txt):\033[1;m ")
    file = open(nome, 'w')
    file.write((' ').join(str(x) for x in Mensacrip))
    file.close()

    print(' \033[32mArquivo gerado com sucesso!\033[1;m')
    print("")
    Again("\n\033[36mQuer criptografar outro arquivo com uma chave especifica? (s / n) \033[1;m ", e5)


def e1():
    mensagem = input(" \033[32mInsira a mensagem para criptografar:\033[1;m ")
    k1 = CalcPri()
    k2 = CalcPri()
    p1 = k1 * k2
    t1 = totiente(k1)
    t2 = totiente(k2)
    totiN = t2 * t1
    p2 = CalcE(totiN)
    ChavePub = (p1, p2)

    print(' \033[32mSua chave pública gerada:\033[1;m', ChavePub)
    Mensacrip = Criptografar(mensagem, p2, p1)

    print(' \033[32mSua mensagem criptografada:\033[1;m', (' ').join(str(x) for x in Mensacrip))

    cp = CalcCP(totiN, p2)
    print(' \033[32mSua chave privada gerada:\033[1;m', cp)
    print("")
    Again("\n\033[36mQuer criptografar outro texto criando novas chaves (s/n)? : \033[1;m ", e1)


def e2():
    Mensagem = Descriptografar()
    B, C = Dividir(Mensagem)
    C = (Concatenar(C))
    print(' \033[32mSua mensagem descriptografada:\033[1;m', C)
    print("")
    Again("\n\033[36mQuer decriptografar outro texto criptografado (s/n)? : \033[1;m ", e2)

def e3():
    texto= input(" \033[32mInsira o texto que quer criptografar: \033[1;m ")
    print("\033[32mInsira a chave pública (XXXX XXXX): \033[1;m ")
    p1, p2 = [int(p1) for p1 in input().split()]
    Mensacrip = Criptografar(texto, p2, p1)
    print('\033[32mSua mensagem criptografada:\033[1;m', (' ').join(str(x) for x in Mensacrip))
    print("")
    Again("\n\033[36mQuer criptografar outro texto inserindo uma chave pública (s/n)? : \033[1;m ", e3)

def e4():
    k1 = CalcPri()
    k2 = CalcPri()
    p1 = k1 * k2
    t1 = totiente(k1)
    t2 = totiente(k2)
    totiN = t2 * t1
    p2 = CalcE(totiN)
    ChavePub = (p1, p2)
    print('\033[32mSua chave pública gerada:\033[1;m', ChavePub)
    cp = CalcCP(totiN, p2)
    print('\033[32mSua chave privada gerada:\033[1;m', cp)
    print("")
    Again("\n\033[36mQuer gerar novas chaves para futuras criptografias e descriptografias (s/n)? :\033[1;m  ", e4)

def e5():
    print (" \033[31mPor favor antes de prosseguir certifique-se que seu arquivo se encontra na mesma pasta que este script!\033[1;m ")
    print(""" \033[32mGostaria de:\033[1;m
         \033[1;35mCriptografar arquivo existente gerando nova chave pública e privada no processo\033[1;m \033[1;32m -------(1)\033[1;m
         \033[1;35mCriptografar arquivo existente usando uma chave pública desejada\033[1;m \033[1;32m ----------------------(2)\033[1;m
         \033[1;35mVoltar ao menu principal\033[1;m \033[1;32m --------------------------------------------------------------(3)\033[1;m""")



    opcao1 = input("\n\033[1;36m-> \033[1;m ")

    if opcao1 == '1':
       nome=input('\033[32mInsira o nome de seu arquivo(nomedoarquivo.txt): \033[1;m')
       arquivo = open(nome, 'r')
       conteudo =arquivo.read()
       crypt(conteudo)

    elif opcao1 == '2':
        nome = input('\033[32mInsira o nome de seu arquivo(nomedoarquivo.txt): \033[1;m')
        arquivo = open(nome, 'r')
        conteudo = arquivo.read()
        encspec(conteudo)
    elif opcao1=='3':
        Escolha()
    else:
        e5()

def e6():
    print(" \033[31mPor favor, antes de prosseguir certifique-se que seu arquivo se encontra na mesma pasta que este script!\033[1;m ")
    nome=input('\033[32mInsira o nome do arquivo que será descriptografado(nomedoarquivo.txt): \033[1;m')
    arquivo = open(nome, 'r')
    conteudo =arquivo.read()
    decrypt(conteudo)



Escolha()