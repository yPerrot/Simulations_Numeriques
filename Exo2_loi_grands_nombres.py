# python -m pip install -U pip
import random

import numpy as np # python -m pip install -U numpy
import matplotlib.pyplot as plt # python -m pip install -U matplotlib

"""
TODO : https://www.youtube.com/watch?v=zOhc6I29lqI

Soit X_i une v.a. représentant le nombre de Face obtenues en 100 lancés d'une pièce non truquée 

n le nombre d'expériences réalisée = 100
p la probabilité de succès = 1/2
q la probabilité d'échec = 1 - p = 1/2

X_i ~> Binomiale(100,1/2)

E(X_i) = n * p = 100 * 1/2 = 50
V(X_i) = n * p * q = 100 * 1/2 * 1/2 = 25
"""

"""
1) Quelle est l’espérance de X_n barre ? son écart-type ? 
"""
def q1() :
    pass

"""
2)Représenter graphiquement 1 réalisation Nx en fonction de N. Que constatez-vous ? comment l’expliquez-vous ?
"""
def q2(N) :
    n = 100
    result = []
    for _ in range(N) :
        # sum = 0
        # for j in range(n) :
        #     sum += 
        # print([random.randint(0,1) for _ in range(n)])
        # s = sum()
        p = sum([random.randint(0,1) for _ in range(n)])
        result.append(p)
        # total += p
    
    # Moyenne
    E = n * 0.5
    plt.plot([0,N],[E,E],"y",  linewidth=1)
    varMin = E - E/2
    varMax = E + E/2 
    plt.plot([0,N],[varMin, varMin],"grey",  linewidth=1)
    plt.plot([0,N],[varMax, varMax],"grey",  linewidth=1)

    plt.plot( range(1,N+1), result, "ro",linewidth=1) # point rond rouge

    print(sum(result)/N)
    plt.plot([0,N],[sum(result)/N,sum(result)/N],"r--",linewidth=1)
    plt.xlabel('i')
    plt.ylabel('Xi')
    plt.axis([1, N, 0, n])
    plt.show() 
    # return total/N

def ProbaLoiBinomaile() :
    pass

"""

"""

"""

"""

if __name__ == "__main__" :
    print(q2(100))
    
    # x = np.array([1, 3, 4, 6])
    # y = np.array([2, 3, 5, 1])
    # plt.plot(x, y)

    # plt.show() # affiche la figure a l'ecran

    # plt.plot([50,100,150,200], [1,2,3,4], "r--", [50,100,150,200], [2,3,7,10], "bs", [50,100,150,200], [2,7,9,10], "g^")

    # plt.plot([50,100,150,200], [1,2,3,4], "r--") # ligne pointillets rouge
    # plt.plot([50,100,150,200], [2,7,9,10], "g^") # points triangles rouge
    # plt.plot([50,100,150,200], [2,3,7,10], "bs") # point carret bleu
    # plt.plot([50,100,150,200], [2,3,7,10], "ro") # point rond rouge
    # plt.show() 