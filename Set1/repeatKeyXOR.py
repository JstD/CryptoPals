plaintext = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
ciphertext = '''0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'''


key = 'ICE'
repKey = key*(len(plaintext)//len(key))
for i in range(len(plaintext)%len(repKey)):
    repKey += key[i]
plaintext = plaintext.encode()
repKey = repKey.encode()
out = ''.join(hex(a^b)[2:].zfill(2) for a,b in zip(plaintext,repKey))

assert out == ciphertext, 'failed'