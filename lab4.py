#Rian Costa Ferreira

#1
def frequenciaDomicilio(dicionario):
    '''Retornar um dicionário que domicílio é uma chave e o valor é a frequência dessa resposta.'''
    freq = {}
    for x in dicionario.values():
        if(not(x in freq)):
            freq[x] = 0
        freq[x] += 1
    return freq

# 2

def processaDados(dici):
    """Retornar um dicionário com quatro itens como o total e tambem dos elementos"""
    pros = {"total": len(dici), "tv": set(), "maquina": set(), "geladeira": set()}
    for x1 in dici:
        for x2 in dici[x1]:
           pros[x2].add(x1)
    return pros


def eletrodomesticos(dici2):
    '''Retorna uma tupla com três elementos sendo a porcentagem dos elementos'''
    m_g = len(dici2['maquina'].intersection(dici2['geladeira'])) / dici2['total'] * 100
    t_m = (dici2['total'] - len(dici2['tv']))/dici2['total'] * 100
    t_nd = (dici2['total'] - (len(dici2['maquina'].union(dici2['geladeira'].union(dici2['tv'])))))/dici2['total'] * 100
    return (m_g, t_m , t_nd) 
