alph = "abcdefghijklmnopqrstuvwxyz"	# Accessbile alphabet
word = input("Give me a message. ")	# The plaintext
key = input("Give me a key. ")	# The key
ciphertext = ""	# Empty space for the encoded message
j = 0 #index variable
while len(ciphertext) < len(word):	# Loops the key until it matches the length of the plaintext
	ciphertext += alph[(alph.index(word[j]) + alph.index(key[j % len(key)])) % 26]	# Creates the final message
	j+=1 #increment var
print(ciphertext)
