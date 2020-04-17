import random
import matplotlib.pyplot as plt # python -m pip install -U matplotlib

"""
Partie 1
"""

"""
1) Soit X_i la v.a. « déplacement n°i » . Quelle est sa loi ?
X_i suit une loi de Bournoulli, soit un succès, soit un échec, avec comme probabilité de succes 1/2
"""

"""
2) Quelle est la loi de X qui représente la position du marcheur à l’instant nT ? 
X suit une loi Binomiale de paramètre (n,p) avec pour n le nombre de lancé de pièce et p le probabilité d'obtenir Face, soit 1/2
"""

"""
3) Prendre s=T=1 et représenter des trajectoires de X pour n=20,100,1000.
"""
def marcheAleatoire(step, n) :
    p = 0
    x = []
    y = []
    
    # Pour n marche, ajoute deux valeurs dans les tableaus, une pour monter ou descendre d'un niveau, une pour avancer 
    for i in range(n) :
        y.append(p)
        if random.randint(0,1) == 1 :
            # On monte de 'step'
            p += step

        else : 
            # On descend de 'step'
            p -= step
        x.extend([i,i])
        y.append(p)

    # Affiche les marches
    plt.plot(x,y, linewidth=1)
    
    # Espérance + Variance 

    # p = 1/2
    # E = n * (2*p - 1)
    # V = n*4*p * (1 - p) * step**2  
    # plt.axhline(E + V, linewidth=1)
    # plt.axhline(E, linewidth=1)
    # plt.axhline(E - V, linewidth=1)

    plt.grid()
    plt.show() 

"""
4) Calculer l’espérance de X. Est-ce bien ce que l’on observe sur les trajectoires ?  Faire de même avec la variance.
TODO 
    p = 1/2
    E = n * (2*p - 1)
    V = n*4*p * (1 - p) * step**2  
"""

"""
Partie 2
"""


if __name__ == "__main__" :
    print("OK")
    marcheAleatoire(1, 1000)
