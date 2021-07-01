#Rian Costa Ferreira#Rian Costa Ferreira
import numpy as np
import matplotlib.pyplot as plt 

def logaritmos(n):
    """Plota as funções ln e log10 como linhas contínuas de largura 2."""
    fig, ax = plt.subplots(figsize = (6,6))
    k = np.linspace(0.01,2,n)
    y = np.log(k)
    x = np.log10(k)
    ax.plot(k,x,'cs-',linewidth = 2 , label=r'$y=ln(x)$')
    ax.plot(k,y,'mo-',linewidth = 2 ,label=r'$\log_{10}(x)$')
    ax.set_title("Logaritmos")
    ax.legend(loc='lower right')
    ax.set_xticks([0,1,2])
    plt.savefig('logaritmos.png')
    plt.show()
    return None

def polinomios(n):
    """´Plota todas as funções y=x**i para i de 1 até o grau máximo passado."""
    fig, ax = plt.subplots()
    k = np.linspace(-1,1,100)
    ax.set_xticks([-1,0,1])
    ax.set_yticks([-1,0,1])
    for i in range(1, n+1):
        y=k**i
        ax.plot(k,y,linewidth = 2,label = r'$x**{}$'.format(i))
        ax.legend(loc='lower right')
    plt.show()
    plt.savefig('polinomios.png')
    return None

