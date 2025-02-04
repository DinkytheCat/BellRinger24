alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","!"," "]
newalphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","!"," "]
for i in range (13):
    rainda= alphabet[-1]
    alphabet.insert(0,rainda)
    alphabet.pop(-1)



password = "baez knows!"
encoded = []
for item in password:
    meow = newalphabet.index(item)
    encoded.insert(-1,item)

print (encoded)



