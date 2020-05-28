import base64
import codecs
#hex to base 64
#convert to raw byte always

string="49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
b=codecs.decode(string,'hex')
b1=codecs.encode(b,'base64').decode()
print(b1)
