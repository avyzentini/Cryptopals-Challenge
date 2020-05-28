import codecs
x='1c0111001f010100061a024b53535009181c'
y='686974207468652062756c6c277320657965'
res='746865206b696420646f6e277420706c6179'
def xor(x,y,z):
    #x=bytearray.fromhex(x)
    x=codecs.decode(x,'hex')

    #y=bytearray.fromhex(y)
    y=codecs.decode(y,'hex')

    xor1=bytes(a^b for (a,b) in zip(x,y))
    
    if(codecs.encode(xor1,'hex').decode()==z):
        print(xor1.hex())
    else: print("not the same")

if(len(x)==len(y)):
    xor(x,y,res)
else: print("not the same length")
