##this script bruteforces the key of the Caesar Cipher! you then have to interpret the results! 
#possible further implementation could be the guesing of the key (frequency analysis)


print("insert the string you want to decrypt that has been encrypted with the Caesar Cipher")
ciphertext = raw_input()

for index in range(26):
	supposed_plaintext = ""
	print (index)
	for letter in ciphertext:
		x = ord(letter) + index
		if x > ord('z'):                                #we need to make this check since lowercase letters are mapped between 97 and 122 in ASCI code

			supposed_plaintext = supposed_plaintext + chr(ord('a')-1 + (x - ord('z')))

		else: 

			supposed_plaintext = supposed_plaintext + chr(x)
	print supposed_plaintext                         #this is the case the addition does not go over borders

