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

"""
5)  On va accélérer la promenade, c’est-à-dire prendre T de plus en plus petit, tout en faisant des pas s de longueur également de plus en plus petite. 
    On choisit de prendre s proportionnel à T, plus précisément on va poser s² = alpha * T. On s’intéresse  à  ce  qui  se passe lorsque T tend vers 0.  
    D’après les calculs de l’espérance et de la variance, expliquer pourquoi on ne prend pas s = alpha * T. 

    Calcule de E(X(nT)) & V(X(nT)) pour s² = a*T et s = a*T => cf. Photos

    "La distance parcourue est proprotionnelle à la racine carré du temps" cf. cours "Marche Aleatoire" p.5

    Distance = sqrt( V(X(nT)) ) => pour s² = a*T :
                                    distance = sqrt(n * a * T) -> Proportionnelle au temps -> C'est validé 
                                => pour s = a*T :
                                    distance = sqrt(n * a² * T²) = sqrt(n * a²) * T -> PAS Proportionnelle au temps -> C'est pas validé 
"""

"""
6)  Représenter des trajectoires de X, pour n fixé, et pour T de plus en plus petit.
    Plus T est petit, plus le step est petit, et donc moins la courbe varie 
"""
def comparaison():
    #You need to close the first window to acced to the second 
    n = 1000
    temps = 1
    marcheAleatoire(temps,n)
    temps = 0.01
    acceleration(temps,n)

def acceleration(temps,n):
    #TODO: found alpha value 
    alpha = 1

    step = (alpha * temps)**0.5
    marcheAleatoire(step, n)

"""
7)  En utilisant le théorème central limite, démontrer que X(t) suit la loi N(0,sqrt(t)). 
    On l’appelle le mouvement brownien.  

    cf. cours "Chap 3 - Convergences stochastiques" p.5

    E(Xn) = mu ; V(Xn) = sigma²
    Sn = X1 + X2 + ... + Xn

    pour n ----> +Inf
    Zn ----> N(0,1)

    Zn = (Sn - n*mu) / ( sqrt(n) * sigma)

    Dans notre cas : 
    cf. photos

    X(nT) = B sqrt(T) ( 2 * Sn - n)         s² = a * T
    E(X(nT)) = 0 
    V(X(nT)) = n * s²       sigma² = n * s² = n * a * T
                            sigma = sqrt( n * a * T)

    Sn = SUM X(nT)


    Zn = (Sn - n*mu) / ( sqrt(n) * sigma )           n * mu = n * 0 = 0
    Zn = (Sn) / ( sqrt(n) * sqrt(n * a * T )) 
    Zn = (Sn) / ( n * sqrt( a * T )) 
    

"""

if __name__ == "__main__" :
    print("OK")
    comparaison()

