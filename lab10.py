#Rian Costa Ferreira
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def suites():
    """ A função conta a frequência da coluna "suites" e retornar um Series com o resultado"""
    fig, ax = plt.subplots()
    df = pd.read_csv("dados.csv")
    df["suites"].value_counts().plot.pie(ax=ax,autopct='%1.1f%%')
    plt.show()
    return df["suites"].value_counts()


def area():
    """Função mostra um histograma de áreas dos apartamentos,e retorna com a maior área"""
    fig, ax = plt.subplots()
    dx = pd.read_csv("dados.csv")
    dx["area"].plot.hist(ax=ax, bins=20, edgecolor='green',color='green')
    plt.show()
    return dx.loc[[452,1770]]


