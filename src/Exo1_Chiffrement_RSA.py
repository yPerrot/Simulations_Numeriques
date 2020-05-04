import random
import math

"""
1) Ecrire un programme d’exponentiation rapide
"""
def expo_rapide(a, b) :
	p = 1

	# Transforme b en binaire	
	# Exemple : 13 => 0b1101
	binary = bin(b) 

	# Retire '0b' en début de ligné 
	binary = binary[2:]

	#Pour chaque bit, en partant de la fin 
	# a = a^2 et si le bit est à 1, p = p * a
	for e in reversed(binary) :
		if e == '1' :
			p = p * a
		a = a**2

	return p

# Fonction proche de la précédente
# On y a ajouté l'application d'un mudolo à chaque calcul
def expo_rapido_modulo(a, b, modulo) :
	p = 1
	binary = bin(b)[2:]

	for e in reversed(binary) :
		if e == '1' :
			p = (p * a) % modulo
		a = (a**2) % modulo

	return p

"""
2) Ecrire un programme du calcul des coefficients de Bezout
"""
def calculCoefBezout(a,b) :
	if b == 0 :
		return (1,0)
	(u,v) = calculCoefBezout(b, a%b)
	return (v, u -(a//b)*v)

"""
3) Ecrire un programme de chiffrement RSA
"""
# Progamme simulant la communication sécurisé, via RSA, entre deux personnes Bob et Alice.
def rsaEncrypting() :
	# publicKey, privateKey = getRSAKeys()
	publicKey, privateKey = TESTgetRSAKeys()

	print("Bob a comme clef privée : ",privateKey,", et comme clef publique : ", publicKey,".")
	print("Bob envoie sa clef publique a Alice.")
	print("Alice veut envoyer un message crypté a Bob.")
	
	print("Le message d'Alice : ")
	message = str(input())

	encryptedMsgAsArray = encryptMessage(message, publicKey)
	print("Le message chiffré d'Alice, reçu par Bob est le suivant : ")
	print("\t",' '.join(map(str, encryptedMsgAsArray)))

	decryptedMsg = decryptedMsgArray(encryptedMsgAsArray,privateKey)
	print("Le message déchiffré par Bob est le suivant : ")
	print("\t", decryptedMsg)

	if message == decryptedMsg :
		print("Bob a bien recu le message d'Alice")
	else : 
		print("Il y a eu une erreur, Bob n'a pas reçu le message d'Alice ...")

"""
4) Imaginer un scénario et une attaque du chiffrement RSA
"""
# Progamme simulant l'attaque d'une communication sécurisé via RSA, par un utilisateur Oscare
def rsaAttack() :
	# publicKey, privateKey = getRSAKeys()
	publicKey, privateKey = TESTgetRSAKeys()

	print("Bob a comme clef privée : ",privateKey,", et comme clef publique : ", publicKey,".")
	print("Bob envoie sa clef à tout le monde.")
	print("Alice veut envoyer un message crypté à Bob.")
	print("Le message d'Alice : ")
	message = str(input())


	encryptedMsgAsArray = encryptMessage(message,publicKey)
	print("Le message chiffré d'Alice, envoyé à Bob et intercépté par Oscar, est le suivant : ")
	print("\t",' '.join(map(str, encryptedMsgAsArray)))


	print("Oscar cherche à retrouver la clef privée de Bob depuis sa clef publique")
	print("Il cherche 'p' et 'q' depuis n")


    # La fonction findQPfromN() retourne 'None' si elle n'arrive pas à trouver Q et P
    # Cela va générer une erreur 'TypeError' car 'None' ne peut pas être affecté à nos deux variables 'q' et 'p'
	try :
		q,p = findQPfromN(publicKey['n'])
	except TypeError :
		print("Oscar n'a pas réussir à retrouver p et q ...")
		return 
	phi_n = (p - 1)*(q - 1)
	d = findD(publicKey['e'], phi_n)


	if d == privateKey['d'] :
		print("Oscar a réussi à retrouver la clef publique de Bob depuis sa clef privée ")
	else : 
		print("Oscar n'a pas réussi à retouver la clef publique de Bob depuis sa clef privée ... ")
		return


	decryptedMsg = decryptedMsgArray(encryptedMsgAsArray,{'d':d,'n':q*p})
	print("Le message déchiffré par Oscar est le suivant : ")
	print("\t",decryptedMsg)


	if message == decryptedMsg :
		print("Oscar à bien décrypté le message d'Alice")
	else : 
		print("Il y a eu une erreur, Oscar à mal décrypté le message d'Alice ...")


"""
Ensemble de fonctions utiles 
"""
# Trouve le PGCD entre deux nombres 'a' et 'b'
def pgcd(a,b) :
	while (b>0):
		tmp = a % b
		a,b = b,tmp
	return a

# Trouve si 'number' est un nombre premier
def isPrime(number) :
	if number <= 1 :
		return False
	if number == 2:
		return True
		
	if number%2 == 0:
		return False
		
	r = number**0.5
	
	if r == int(r):
		return False
	
    # parcours tous les nombres impairs entre 3 et 'r'
    # Exemple des nombres parcourus si r = 15 : [3,5,7,9,11,13]
	for x in range(3, int(r), 2):
		if number % x == 0:
			return False	
	
	return True

# Retourne une clef privée et une clef publique prédéfinies
def TESTgetRSAKeys() :
	publicKey = {"e":565,"n":283189}
	privateKey = {"d":140313,"n":283189}

	return publicKey, privateKey

# Permet à l'utilisateur de choisir la valeur de 'q', 'p' et 'e'
def getRSAKeys() :
	# Récupère et vérifie le valeur P
	print("Entrer la valeur de p :")
	p = int(input())
	if not isPrime(p) :
		print("P n'est pas un nombre premier")
		raise ValueError("Invalid P")

	# Récupère et vérifie le valeur Q
	print("Entrer la valeur de q :")
	q = int(input())
	if not isPrime(q) :
		print("Q n'est pas un nombre premier")
		raise ValueError("Invalid Q")

	# Vérifie que n et Phi_n sont valides
	n = p * q
	phi_n = (p - 1)*(q - 1)

	# Récupère et vérifie le valeur P
	print("Entrer la valeur de e :")
	e = int(input())

	if e <= p or e <= q or e >= phi_n or pgcd(e,phi_n) != 1 :
		print("e n'est pas valide")
		raise ValueError("Invalid e")
	

	d = findD(e, phi_n)

	publicKey = {"e":e,"n":n}
	privateKey = {"d":d,"n":n}

	return publicKey, privateKey

# Trouve l'inverse de e modulo phi_n
def findD(e, phi_n) :
	u,v = calculCoefBezout(e,phi_n)
	return u if ((u*e) % phi_n) == 1 else v

# Chiffre la chaine de caractère passé en paramètre et la retourne sous la forme d'un tableau d'entier
def encryptMessage(message, publicKey) :
	# Shortest version
	# messageAsAsciiTab = [ord(char) for char in message]
	# encryptedMessage = [ for char in messageAsAsciiTab]

	messageAsAsciiTab = []
	for char in message :
		messageAsAsciiTab.append(ord(char))

	encryptedMessage = []
	for elem in messageAsAsciiTab :
		encryptedMessage.append(expo_rapido_modulo(elem,publicKey['e'], publicKey['n']))

	return encryptedMessage

# Déchiffre un tableau d'entier passé en paramètre, afin de retrouver le message d'origine
def decryptedMsgArray(messageArray, privateKey) :
	# Shortest version
	# decryptedMsg = [expo_modulo_rapido(char,privateKey['d'],privateKey['n']) for char in cryptedMessage]
	# return ' '.join(map(str, uncryptedMessage))

	decryptedMsg = [] 
	for elem in messageArray :
		charId = expo_rapido_modulo(elem,privateKey['d'],privateKey['n'])
		decryptedMsg.append(chr(charId))

	return ''.join(decryptedMsg)

# Retrouve les deux nombre premier Q et N qui ont permit de trouver 'n'
# Si aucun nombre n'est trouvé, retourne 'None'
def findQPfromN(n) :
	for i in range(2,(n//2) + 1) :
		for j in range(2,int(n**0.5) + 2) :
			if i*j == n and isPrime(i) and isPrime(j) :
				return [i,j]
	return None

def programClosure() :
	print("\n","Press Enter to exite ... ")
	input()

if __name__ == "__main__":
	print(" ------- RSA classique -------")
	rsaEncrypting() 

	print(" ------- Attaque RSA -------")
	rsaAttack()

	programClosure()
	pass