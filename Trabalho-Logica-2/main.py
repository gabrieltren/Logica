# -*- coding: utf-8 -*-
'''
###################################################################################################################################
# PRODUÇOES 2 HOMENS E MEIO
# EQUIPE :
# 1 - Gabriel Silveira Trentini
#       Matricula: 404497
# 2 - Cícero Romão Ribeiro
#       Matricula: 411674
###################################################################################################################################
'''








from pysat.solvers import Glucose4
from pysat.formula import CNF


def arquivo():
    ar = open('text2.txt', 'r')
    a = ar.read().split('\n')
    return a
    ar.close()

def caminho_covertido(lista,aresta,c):
    caminho =[]
    l_li = len(lista)
    for i in range(l_li):
        indice = int((lista[i]-1)/c)
        caminho.append(aresta[indice])
    
    return caminho

def reverse_list(re_lista):
    n = len(re_lista)
    a = []
    for i in re_lista:
        a =  [i] + a
    return a


def return_caminho(lista,arestas,c):
    t_lista = len(lista)
    a = 0
    lista_return = []
    t= len(lista[0])
    for i in range(t):
        ln = []
        
        for j in range(t_lista):
            if j == 0:
                if(len(lista[j]) > 1):
                    a = int(lista[j][0])
                    
                    ind_ares = int((a-1)/c)
                    
                    ar = arestas[ind_ares]
                    ln.append(a)
                    lista[j].pop(0)
                else:
                    a = int(lista[j][0])
                    ind_ares = int((a-1)/c)
                    ar = arestas[ind_ares]
                    ln.append(a)

            elif j >0:
                if(len(lista[j]) > 1):
                    a = int(ln[j-1])
                    ind_ares = int((a-1)/c)
                    ar_ant = arestas[ind_ares]
                    ar_ant_split = ar_ant.split('_')
                    for k in range(len(lista[j])):
                        b = int(lista[j][k])
                        ind_j = int((b-1)/c)
                        ar_j = arestas[ind_j]
                        ar_j_split = ar_j.split('_')
                        if ar_ant_split[1] == ar_j_split[0] and ar_ant_split[0] != ar_j_split[1]:
                            ln.append(b)
                            lista[j].pop(k)
                            break
                elif(len(lista[j]) == 1):
                    a = int(ln[j-1])
                    ind_ares = int((a-1)/c)
                    ar_ant = arestas[ind_ares]
                    ar_ant_split = ar_ant.split('_')
                    b = int(lista[j][0])
                    ind_j = int((b-1)/c)
                    ar_j = arestas[ind_j]
                    
                    ar_j_split = ar_j.split('_')
                    
                    if ar_ant_split[1] == ar_j_split[0] and ar_ant_split[0] != ar_j_split[1]:
                        ln.append(b)
        
        lista_return.append(ln)
    
    return lista_return

                

def criar_lista_resutado(soluc,r_arestas,lista,linha,coluna):
    arestas = r_arestas
    c = coluna
    l = linha
    arestas_uso = []
    iar = int((soluc-1)/c)
    arestas_uso.append(arestas[iar])
    lista_res = []
    lista_res.append([soluc])
    indice = 0

    for j in range(c-2,-1,-1):

        a = []
        for i in range(l):
            indf = ((i*c)+j)
            ar = arestas[i]
            ar_split = ar.split('_')
            if (len(lista_res) == 1) and len(a) >= 0:
                iq = lista_res[0][0]
                iqi = int((iq-1)/c)
                p_ar = arestas[iqi]
                p_ar_split = p_ar.split('_')
                if ar_split[1] == p_ar_split[0] and ar_split[0] != p_ar_split[1]:
                    if arestas[i] not in arestas_uso:
                        arestas_uso.append(arestas[i])
                        
                        a.append(lista[indf])
            elif (len(lista_res) >= 1) and len(a) >= 0:

                for n in lista_res[indice]:
                    iqi = int((n-1)/c)
                    p_ar = arestas[iqi]
                    p_ar_split = p_ar.split('_')
                    if ar_split[1] == p_ar_split[0] and ar_split[0] != p_ar_split[1]:
                        if arestas[i] not in arestas_uso:
                            arestas_uso.append(arestas[i])
                            a.append(lista[indf])
            
        lista_res.append(a)
        indice+=1


    return lista_res








def fazer_Vec_Mat(tamanho):
    lista = [] # Lista a ser criada para referencia
    for i in range(tamanho):
        lista.append(i+1)
    return lista

#arestas == areastas , lista == kista , l == linham, c == coluna, r_l == l passada, r_c == c passada, ar == aresta passada
def formula(arestas,lista,l,c,r_l,r_c,ar):
    ar_split = ar.split('_')
    formulas = []
    a = []
    ind = (r_l*c)+r_c
    for i in range(l):
        if i != r_l:
            ind2 = (i*c)+r_c
            a.append([-lista[ind], -lista[ind2]])
    
    if r_c < c-1:
        j = r_c+1
        for i in range(l):
            ar2 = arestas[i]
            ar2_split = ar2.split('_')
            if i == r_l:
                for k in range(c):
                    ind2 = (i*c)+k
                    if k != r_c:
                        a.append([-lista[ind], -lista[ind2]])
            
            if i != r_l:
                if ar2_split[0] == ar_split[1] and ar2_split[1] == ar_split[0]:
                    for k in range(c):
                        ind2 = (i*c)+k
                        a.append([-lista[ind], -lista[ind2]])
            
            if ar2_split[0] == ar_split[1] and ar2_split[1] != ar_split[0]:
                ind2 = (i*c)+j
                a.append([-lista[ind], lista[ind2]])
            
        if r_c > 0:
            j = r_c - 1
            for i in range(l):
                ind2 = (i*c)+j
                if ar2_split[1] == ar_split[0]:
                    if ar2_split[0] != ar_split[1]:
                        a.append([lista[ind], -lista[ind2]])
                    else:
                        a.append([-lista[ind], -lista[ind2]])
                
    
    return a




def clausula(arestas,l,c,lista,):
    formulas = []

    for i in range(l):
        for j in range(c):
            formulas+= formula(arestas,lista,l,c,i,j,arestas[i])
            #print(formula(arestas,lista,l,c,i,j,arestas[i]))
    
    #fazer as formulas de chegada

    return formulas


def programinha():
    arestas = arquivo()
    arestas_total = int(len(arestas)) #Guardando total de arestas
    passos_total = int(len(arestas)//2) #Maximo de passo entre aresta

    linha = arestas_total
    coluna = passos_total
    tamanho_lista = linha*coluna
    
   
    r_lista = fazer_Vec_Mat(tamanho_lista) #criando uma referencia para os literais
    
    cl= clausula(arestas,linha,coluna,r_lista)
    
    
    clas = [r_lista] + cl
    f = CNF()

    for i in clas:
        f.append(i)
    
    g = Glucose4()
    
    g.append_formula(f)
    
    #Bool de retorno do solve
    solve = g.solve()
    print('---------------------------------------------------------------------------')
    print('Solução : ',solve)
    print('---------------------------------------------------------------------------')
    
    if solve:
        #Lista da Solução
        model_g = g.get_model()
        #Retorna da lista model_g so numeros positivos
        lista = list(filter(lambda x: x > 0, model_g))
        #indice da aresta em arestas
        u_v = int((lista[0]-1)/5)
        #Cria e retorna em ordem inversa o(s) caminho(s) que são verdadeiros
        re_lista = criar_lista_resutado(lista[0],arestas,r_lista,linha,coluna)
        re_lista_rec = re_lista
        #Retorna a lista Inversa, isso é a deixa na hordem certa
        lista_resv = reverse_list(re_lista)
        #retornar os caminhos para a solução
        final = return_caminho(lista_resv,arestas,coluna)

        print()
        print('Lista solve:\n',model_g)
        print('---------------------------------------------------------------------------')
        print('Positivos da Lista solve:', lista)
        print('Utimo vertice a ser pecorrido: ',arestas[u_v])
        print('---------------------------------------------------------------------------')
        print("Caminhos encontrados:")
        print('--------------------------------')
        for i in final:
            print('Idex em matriz: ',i)
            print('ou')
            lista_caminho = caminho_covertido(i,arestas,coluna)
            print('Caminho em aresta',lista_caminho)
            print('--------------------------------')
            
        print()
        print('---------------------------------------------------------------------------')
            
    a = ''
    for i in clas:
        a = a + str(i) + '\n'
    
    arquivo2  = open('cl-1.txt', 'w')
    arquivo2.write(a)
    arquivo2.close()

programinha()