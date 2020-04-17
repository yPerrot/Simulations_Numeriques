import random
import numpy as np
import matplotlib.pyplot as plt 


"""
1) Quelle est l’espérance de X_n barre ? son écart-type ? 
"""
def q1() :
    """
    Soit X_i une v.a. représentant le nombre de Face obtenues en 10 lancé d'une pièce non truquée 

    n le nombre d'expériences réalisées = 10
    p la probabilité de succès = 1/2
    q la probabilité d'échec = 1 - p = 1/2

    X_i ~> Binomiale(10,1/2)

    E(X_i) = n * p = 10 * 1/2 = 5
    V(X_i) = n * p * q = 10 * 1/2 * 1/2 = 2,5
    """
    pass

"""
2)Représenter graphiquement une réalisation x_N barre en fonction de N. 
    Que constatez-vous ? 
        On constate que, plus N est grand, plus la moyenne de x_N se rapproche de l'espérance.
    Comment l’expliquez-vous ?
        Cela s'explique par la loi des grands nombres.
"""
def q2(N) :
    n = 10
    # result = tableau des résultats des lancés
    result = []

    # Pour N essayes de lancé de 10 pièces 
    for _ in range(N) :
        # p = nombre de lancé ayant obtenue Face
        p = sum([random.randint(0,1) for _ in range(n)])
        result.append(p)
    
    # Ajoute l'espérance à la représentation graphique
    E = n * 0.5
    plt.plot([0,N],[E,E],"y",  linewidth=1)

    # Ajoute la variance à la représentation graphique
    varMin = E - E/2
    varMax = E + E/2 
    plt.plot([0,N],[varMin, varMin],"grey",  linewidth=1)
    plt.plot([0,N],[varMax, varMax],"grey",  linewidth=1)

    # Ajoute un point par résultats de 10 lancés à la représentation graphique
    plt.plot( range(1,N+1), result, "ro",linewidth=1)

    # Ajoute la moyenne des lancés à la représentation graphique
    plt.plot([0,N],[sum(result)/N,sum(result)/N],"r--",linewidth=1)

    # Ajoute les axes X et Y à la représentation graphiques
    plt.xlabel('i')
    plt.ylabel('Xi')
    plt.axis([1, N, 0, n])

    plt.grid()
    plt.show() 

if __name__ == "__main__" :
    print(q2(100))
    pass