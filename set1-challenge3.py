import codecs
encoded = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
x= codecs.decode(encoded,'hex')
# 65-122 for the english alphabet
for i in range(65,122):     #for every english character
    res =b''                # store the result in bytes form
    for byte in x:          # for each byte in the encoded string
        res = res + bytes([byte^i]) #XOR each byte with every character and store it in a line
    print(type(res))
