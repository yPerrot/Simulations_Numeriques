import random
import math

"""
1) Ecrire un programme d’exponentiation rapide
"""
def expo_rapide(a, b) :
	p = 1

	binary = "{0:b}".format(b) # Transforme b en binaire
	reversedBinary = binary[::-1] # Récupère l'inverse de la chaine. Ex : 1011100 devient 0011101

	#Pour chaque élément bit, a = a^2 et si le bit est à 1 p = p X a
	for e in reversedBinary :
		if e == '1' :
			p = p * a
		a = a**2

	return p

def expo_rapido_modulo(a, b, modulo) :
	p = 1
	binaryNum = "{0:b}".format(b)[::-1]

	for e in binaryNum :
		if e == '1' :
			p = (p * a) % modulo
		a = (a**2) % modulo

	return p

"""
2) Ecrire un programme du calcul des coefficients de Bezout
TODO
"""
def calculCoefBezout(a,b) :
	# http://aalami.e-monsite.com/medias/files/fonction-python-fournissant-les-coefficients-de-bezout.pdf
	if b == 0 :
		return (1,0)
	(u,v) = calculCoefBezout(b, a%b)
	return (v, u -(a//b)*v)

"""
3) Ecrire un programme de chiffrement RSA
"""
def rsaEncrypting() :
	# publicKey, privateKey = getRSAKeys()
	publicKey, privateKey = TESTgetRSAKeys()

	print("Bob a comme clef privé : ",privateKey,", et comme clef publique : ", publicKey,".")
	print("Bob envoie sa clef publis à Alice.")
	print("Alice veut envoyer un message crypté à Bob.")
	print("Le message d'Alice : ")
	message = str(input())

	encryptedMsgAsArray = encryptMessage(message,publicKey)
	print("Le message chiffré d'Alice, reçu par Bob est le suivant : ")
	print("\t",' '.join(map(str, encryptedMsgAsArray)))

	decryptedMsg = decryptedMsgArray(encryptedMsgAsArray,privateKey)
	print("Le message déchiffré par Bob est le suivant : ")
	print("\t",decryptedMsg)

	if message == decryptedMsg :
		print("Bob a bien reçu le message d'Alice")
	else : 
		print("Il y a eu une erreur, Bob n'a pas réçu le message d'Alice ...")


	pass

"""
4) Imaginer un scénario et une attaque du chiffrement RSA
"""
def rsaAttack() :
	# publicKey, privateKey = getRSAKeys()
	publicKey, privateKey = TESTgetRSAKeys()

	print("Bob a comme clef privé : ",privateKey,", et comme clef publique : ", publicKey,".")
	print("Bob envoie sa clef à tout le monde.")
	print("Alice veut envoyer un message crypté à Bob.")
	print("Le message d'Alice : ")
	message = str(input())

	encryptedMsgAsArray = encryptMessage(message,publicKey)
	print("Le message chiffré d'Alice, envoyé à Bob et intercépté par Oscar, est le suivant : ")
	print("\t",' '.join(map(str, encryptedMsgAsArray)))

	print("Oscar cherche à retrouver la clef privée de Bob depuis sa clef publique")
	print("Il cherche 'p' et 'q' depuis n")

	try :
		q,p = findQPfromN(publicKey['n'])
	except TypeError :
		print("Oscar n'a pas réussir à retrouver p et q ...")
		return 

	d = findD(p,q,publicKey['e'])

	if d == privateKey['d'] :
		print("Oscar a réussi à retouver la clef publique de Bob depuis sa clef privée ")
	else : 
		print("Oscar n'a pas réussi à retouver la clef publique de Bob depuis sa clef privée ... ")

"""
Ensemble de fonctions utiles 
"""
def pgcd(a,b) :
	while (b>0):
		tmp = a % b
		a,b = b,tmp
	return a

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
	
	for x in range(3, int(r), 2):
		if number % x == 0:
			return False	
	
	return True

def TESTgetRSAKeys() :
	publicKey = {"e":565,"n":283189}
	privateKey = {"d":140313,"n":283189}

	return publicKey, privateKey

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
	

	d = findD(p,q,e)

	publicKey = {"e":e,"n":n}
	privateKey = {"d":d,"n":n}

	return publicKey, privateKey

def findD(p,q,e) :
	phi_n = (p-1)*(q-1)
	u,v = calculCoefBezout(e,phi_n)
	return u if ((u*e) % phi_n) == 1 else v

def encryptMessage(message, publicKey) :
	# messageAsAsciiTab = [ord(char) for char in message]
	# cryptedMessage = [ for char in messageAsAsciiTab]

	messageAsAsciiTab = []
	for char in message :
		messageAsAsciiTab.append(ord(char))

	encryptedMessage = []
	for elem in messageAsAsciiTab :
		encryptedMessage.append(expo_rapido_modulo(elem,publicKey['e'], publicKey['n']))

	return encryptedMessage

def decryptedMsgArray(messageArray, privateKey) :
	# decryptedMsg = [expo_modulo_rapido(char,privateKey['d'],privateKey['n']) for char in cryptedMessage]
	# print(' '.join(map(str, uncryptedMessage)))

	decryptedMsg = [] 
	for elem in messageArray :
		charId = expo_rapido_modulo(elem,privateKey['d'],privateKey['n'])
		decryptedMsg.append(chr(charId))

	return ''.join(decryptedMsg)

def findQPfromN(n) :
	# for i in range(2,int(n**0.5) + 2) :
	for i in range(2,(n//2) + 1) :
		for j in range(2,int(n**0.5) + 2) :
		# for j in range(2,(n//2) + 1) :
			if i*j == n and isPrime(i) and isPrime(j) :
				return [i,j]
	return None

def programClosure() :
	print("\n","Press Enter to exite ... ")
	input()

if __name__ == "__main__":
	# print(calculCoefBezout(7,180))
	# print(findQPfromN(283189))
	rsaAttack()
	# rsaEncrypting()
	programClosure()
	pass