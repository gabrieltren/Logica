# -*- coding: utf-8 -*-
'''
###################################################################################################################################
# PRODUÇOES 2 HOMENS E MEIO
# EQUIPE :
# 1 - Gabriel Silveira Trentini
#       Matricula: 404497
# 2 - Cíero Romão Ribeiro]
#       Matricula: 411674
###################################################################################################################################
'''







# Siglas
sigla1 = "A1"
sigla2 = "A2"
sigla3 = "A3"
sigla4 = "A4"
sigla5 = "A5"
sigla6 = "A6"
sigla7 = "A7"
sigla8 = "A8"
sigla9 = "A9"
sigla10 = "A10"

# Axiomas
A1 = "(p>(q>p))"
A2 = "(p>(q>r))>((p>q)>(p>r))"
A3 = "p>(q>(p∧q))"
A4 = "(p∧q)>p"
A5 = "(p∧q)>q"
A6 = "p>(p∨q)"
A7 = "q>(p∨q)"
A8 = "(p>r)>((q>r)>((p∨q)>r))"
A9 = "(p>q)>((p>~q)>~p)"
A10 = "~~p>p"


#Compara se a string1 esta contida em string2, se sim informa qual
#posição esta localizada, se nao retorna -1
def compara_str(string1, string2):

    if(string2.find(string1) != -1):
        return 1
    else:
        return 0
#Subistui os atomos para verificar se á coerencia no axioma


def substitui_atomos(linha, regra, identificador):
    p = "p="
    q = "q="
    r = "r="
    aux_p = ""
    aux_q = ""
    aux_r = ""
    aux_regra = regra
    if(identificador == 0):
        if(linha.find(p) != -1):
            aux_linha = linha.split(' ')
            if(len(aux_linha) == 4):
                aux_atomo = aux_linha[3].split(';')
                aux_atomo = aux_atomo[0]
                aux_p = aux_atomo[0][2:]
                aux_regra = aux_regra.replace('p', aux_p)
                if(aux_regra == aux_linha[1]):
                    return 1
                else:
                    return 0
        else:
            return 0
        return 1
    elif(identificador == 1):
        if (linha.find(p) != -1) and (linha.find(q) != -1):
            aux_linha = linha.split(' ')
            if(len(aux_linha) == 4):
                aux_atomo = aux_linha[3].split(';')
                aux_atomo = aux_atomo[0:2]
                aux_p = aux_atomo[0]
                aux_q = aux_atomo[1]
                aux_regra = aux_regra.replace('p', aux_p[2:])
                aux_regra = aux_regra.replace('q', aux_q[2:])
                if(aux_regra == aux_linha[1]):
                    return 1
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    else:
        if (linha.find(p) != -1) and (linha.find(q) != -1) and (linha.find(r) != -1):
            aux_linha = linha.split(' ')
            if(len(aux_linha) == 4):
                aux_atomo = aux_linha[3].split(';')
                aux_atomo = aux_atomo[0:3]
                aux_p = aux_atomo[0][2:]
                aux_q = aux_atomo[1][2:]
                aux_r = aux_atomo[2][2:]
                aux_regra = aux_regra.replace('p', aux_p)
                aux_regra = aux_regra.replace('q', aux_q)
                aux_regra = aux_regra.replace('r', aux_r)
                if(aux_regra == aux_linha[1]):
                    return 1
                else:
                    return 0
            else:
                return 0
        else:
            return 0


#Procura a sigla dentro da linha e retornar 1 ou 0 ( True or False)
#e tambem verifica se os atomos estao totalmente certos
def procurar_sigla_regra(linha):
    if(linha.find(sigla1) != -1):
        return substitui_atomos(linha, A1, 1)
    elif(linha.find(sigla2) != -1):
        return substitui_atomos(linha, A2, 2)
    elif(linha.find(sigla3) != -1):
        return substitui_atomos(linha, A3, 1)
    elif(linha.find(sigla4) != -1):
        return substitui_atomos(linha, A4, 1)
    elif(linha.find(sigla5) != -1):
        return substitui_atomos(linha, A5, 1)
    elif(linha.find(sigla6) != -1):
        return substitui_atomos(linha, A6, 1)
    elif(linha.find(sigla7) != -1):
        return substitui_atomos(linha, A7, 1)
    elif(linha.find(sigla8) != -1):
        return substitui_atomos(linha, A8, 2)
    elif(linha.find(sigla9) != -1):
        return substitui_atomos(linha, A9, 1)
    elif(linha.find(sigla10) != -1):
        return substitui_atomos(linha, A10, 0)
    else:
        return 0


def procurar_mp(mp_axioma, lista):
    aux_mp = mp_axioma.split(' ')
    i1 = int(aux_mp[3][0]) - 1
    i2 = int(aux_mp[3][2]) - 1
    aux_lista1 = lista[i1].split(' ')
    aux_lista2 = lista[i2].split(' ')
    #Condicionao abaixo, verifica se uma esta contida na outra( no caso a string)
    # 1 if, aux_lista2[1] esta contida em aux_lista1[1]
    if(aux_lista1[1].find(aux_lista2[1]) != -1):
        return fazer_mp(aux_mp[1], aux_lista1[1], aux_lista2[1])
    elif(aux_lista2[1].find(aux_lista1[1]) != -1):
        return fazer_mp(aux_mp[1], aux_lista2[1], aux_lista1[1])
    else:
        return 0


def fazer_mp(mp_lista, lista1, lista2):
    aux_mp = mp_lista
    aux_lista1 = lista1
    aux_lista2 = lista2
    aux_feito = aux_lista1.split(aux_lista2)
    if(aux_feito[1][1:].find(aux_mp) != -1):
        return 1
    else:
        return 0
    return 0


def abrir_arquivo():
    arquivo = open('text.txt', 'r')
    lista = []
    a = ""
    for line in arquivo:
        a = line
        lista.append(a)
    arquivo.close()
    return lista


def numeracao_de_axioma(lista_axioma):
    i = 1
    axioma = int(0)
    for line in lista_axioma:
        axioma = int(line[0])
        if(axioma != i):
            return 0
        i += 1
    return 1


def programinha():
    axiomas_lista = abrir_arquivo()
    verdade = 1
    i = len(axiomas_lista)
    j = 0
    if(axiomas_lista == None or axiomas_lista == []):
        print("###############################################################")
        print("                      #### ERRO ####")
        print("         Arquivo nao encotrado ou Erro ao abrir o arquivo ")
        print("                 2  Programa finalizado!!!")
        print("###############################################################")
        return 0
    elif(numeracao_de_axioma(axiomas_lista) == 0):
        print("###############################################################")
        print("                      #### ERRO ####")
        print("   Ordem errada de Axioma ou Falta de um ou mais Axioma(s) ")
        print("                 2  Programa finalizado!!!")
        print("###############################################################")
        return 0
    else:
        while verdade:
            if(axiomas_lista[j].find("MP") != -1):
                if(procurar_mp(axiomas_lista[j], axiomas_lista)):
                    print("{}" .format(axiomas_lista[j]))
                    j += 1
                else:
                    print("{}     (incorreto Mp)" .format(axiomas_lista[j]))
                    verdade = 0
                    return 0
            else:
                if(procurar_sigla_regra(axiomas_lista[j])):
                    print("{}" .format(axiomas_lista[j]))
                    j += 1
                else:
                    print("{}   (incorreto A)" .format(axiomas_lista[j]))
                    verdade = 0
                    return 0
            if(j == (i)):
                verdade = 0
                return 1

        return 1


r = programinha()

if(r == 0):
    print(" ")
    print("Finalizado")
else:
    print(" ")
    print("Parece que de bom")




'''
###################################################################################################################################
# PRODUÇOES 2 HOMENS E MEIO
# EQUIPE :
# 1 - Gabriel Silveira Trentini
#       Matricula: 404497
# 2 - Cíero Romão Ribeiro]
#       Matricula: 411674
###################################################################################################################################
'''