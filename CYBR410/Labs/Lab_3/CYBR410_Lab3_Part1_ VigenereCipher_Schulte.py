# CYBR 410 Encyrption
# Created by Pratik Somwanshi
# Modified by Dr. D.Vo On 10/09/22
# Modifyied By: Dustin Schulte
# Modified On: 10/14/22
#
# Python code to implement Vigenere Cipher

# This function generates the key in a cyclic manner until
# it's length isn't equal to the length of original text
def generateKey(string, key):
	key = list(key)
	if len(string) == len(key):
		return(key)
	else:
		for i in range(len(string) -
					len(key)):
			key.append(key[i % len(key)])
	return("" . join(key))

# This function returns the encrypted text generated with the help of the key
def cipherText(string, key):
	cipher_text = []
	for i in range(len(string)):
		x = (ord(string[i]) +
			ord(key[i])) % 26
		x += ord('A')
		cipher_text.append(chr(x))
	return("" . join(cipher_text))

# This function decrypts the encrypted text and returns the original text
def originalText(cipher_text, key):
	orig_text = []
	for i in range(len(cipher_text)):
		x = (ord(cipher_text[i]) -
			ord(key[i]) + 26) % 26
		x += ord('A')
		orig_text.append(chr(x))
	return("" . join(orig_text))

# Prompt the user for the mode (encrypt or decrypt)
mode = input("Do you want to encrypt or decrypt the text? (Enter 'encrypt' or 'decrypt'): ").upper()

# Driver code
if __name__ == "__main__" and mode == "ENCRYPT":
	# Add your poem here
	# Make sure to use ALL CAPS and remove punctuation/spaces
	string = """YOURLIFEISYOURLIFEDONTLETITBECLUBBEDINTODANKSUBMISSION
			 BEONTHEWATCHTHEREAREWAYSOUTTHEREISLIGHTSOMEWHEREITMAYNOTBEMUCHLIGHTBUT
			 ITBEATSTHEDARKNESSBEONTHEWATCHTHEGODSWILLOFERYOUCHANCESKNOWTHEMTAKETHEM
			 YOUCANTBEATDEATHBUTYOUCANBEATDEATHINLIFESOMETIMESANDTHEMOREOFTENYOULEARN
			 TODOITTHEMORELIGHTTHEREWILLBEYOURLIFEISYOURLIFEKNOWITWHILEYOUHAVEITYOUARE
			 MARVELOUSTHEGODSWAITTODELIGHTINYOU"""
	# Change the key
	keyword = "LAUGHING"
	key = generateKey(string, keyword)
	cipher_text = cipherText(string,key)
	print("Ciphertext :", cipher_text)
	print("Original/Decrypted Text :", originalText(cipher_text, key))


if __name__ == "__main__" and mode == "DECRYPT":
	# Prompt the user for the text to encrypt or decrypt
	string = input("Enter the text: ").upper()
	# Prompt the user for the keyword
	keyword = input("Enter the keyword: ").upper()
	key = generateKey(string, keyword)
	print("Ciphertext :", string)
	print("Original/Decrypted Text :", originalText(string, key))
