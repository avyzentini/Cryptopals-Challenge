s = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
key = 'ICE'
res = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'

s_byte = bytes(s,'utf-8')
key_byte = bytes(key,'utf-8')
output = b''
pos= 0
for i in s_byte:
    output += bytes([i ^key_byte[pos]])
    if pos +1 == 3:
        pos =0
    else:
        pos+=1

print('Output: ', output.hex())
print('Expected result: ', res)
