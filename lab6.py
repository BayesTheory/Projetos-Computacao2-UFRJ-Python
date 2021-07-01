#Rian Costa Ferreira

def compararStrings(x,y): 
    """retorna função para deletar todos os espaços das strings e comparar""" 
    x=x.replace(" ", "")
    y=y.replace(" ", "")
    if len(y) < len(x):
        tamanho_menor = len(y)
    else:
        tamanho_menor = len(x) 
    n=0
    for i in range(tamanho_menor):
        if x[i] == y[i]:
            n = n+1
    return n/tamanho_menor


def lerArquivo(arq):
    """Retorna é uma lista contendo as linhas do arquivo não nula"""
    lista = []
    arq  =  open(arq, 'r')
    for  linha  in  arq:
         if linha != '\n' and not linha.startswith('#'):
           lista.append(linha)
    arq.close()
    return lista


def compararArquivos(arq1, arq2):
    """Retorno é a soma similar das linhas dividida do comprimento da lista menor"""
    arq1 = lerArquivo(arq1)
    arq2 = lerArquivo(arq2)
    n = 0
    if len(arq1) < len(arq2):
        tamanho_menor = len(arq1)
    else:
        tamanho_menor = len(arq2)   
    for i in range(tamanho_menor):
        n = n + compararStrings(arq1[i], arq2[i])
    return n/tamanho_menor


def descobrirCola(lista):
    """Retorna é o número de comparações que foram feitas"""
    resultado = []
    n = 0
    for i in range (0, len(lista)-1):
        for j in range(i+1, len(lista)):
            n = n+1
            resultado.append('{} com {} deu {}\n'.format(lista[i], lista[j], 
            compararArquivos(lista[i], lista[j])))
    arquivo  =  open("resultado.txt", 'w')
    arquivo.writelines(resultado)
    arquivo.close()
    return n


