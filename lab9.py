#Rian Costa Ferreira
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

def alturas(n):
    """Retorne uma np.ndarray com as alturas da população."""
    fig, ax = plt.subplots()
    z = st.norm.rvs(loc = 1.7, scale = 0.08, size = n)
    ax.hist(z, bins = 20, facecolor = 'c')
    ax.set_title("Alturas")
    plt.savefig('alturas.png')
    return z

def pesos(m):
    """Retorne uma np.ndarray com os pesos utilizando alturas"""
    fig, ax = plt.subplots() 
    s = st.norm.rvs(loc = 24.5, scale = 4.3, size = len(m))
    p = np.multiply(s, m**2)
    ax.hist(p, bins = 20, facecolor = 'm')
    ax.set_title("Pesos")
    plt.savefig('pesos.png')
    plt.show()
    return p

pesos(alturas(100)) 


