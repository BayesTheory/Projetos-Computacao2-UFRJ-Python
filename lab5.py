#RIAN COSTA FERREIRA
def positivo(x):
    """Retorna o valor absoluto do número passado"""
    try:
        return abs(float(x))
    except:
        print("\'{}\' não pode ser convertido em um número".format(x))  
        return None


def encontraIndices(lista, x):
    """Retorna lista de índices se tiver o elemento dentro da lista ou lista vazia"""
    resultado = []
    y = -1
    while True:
        try:
            y = lista.index(x, y+1)
        except ValueError:
            return resultado
        resultado.append(y)


def inversos(i):
    """Retorna uma lista cujos elementos são inversos dos elementos originais"""
    inverso = []
    for x in i:
        try:
            inverso.append(1/float(x))
        except ZeroDivisionError:
            print("Divisão por zero")
            inverso.append('Nan')
        except TypeError:
            print("Entrada de tipo '{}' não válida".format(type(x)))
            inverso.append('Nan')
        except ValueError:
            print("Inverso de '{}' não definido".format(x))
            inverso.append('Nan')
    return inverso



