alph = "abcdefghijklmnopqrstuvwxyz"
word = input("Give me a message. ")
key = input("Give me a key. ")
ciphertext = ""
j = 0
while len(ciphertext) < len(word):
	i = j % len(key)
	letter = alph.index(key[i])
	ciphertext += alph[(alph.index(word[j]) + letter) % 26]
	j+=1
print(ciphertext)
