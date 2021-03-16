from Crypto.Cipher import AES
import base64
def xor_bytes(inp_bytes1,inp_bytes2):
    result = b''
    for a,b in zip(inp_bytes1,inp_bytes2):
        result += bytes([a^b])
    return result

def cbc_decrypt(key,iv,ciphertext):
    assert len(ciphertext)%16==0
    assert len(key) == 16
    assert len(iv) == 16
    plaintext = b''
    cipher = AES.new(key,AES.MODE_ECB)

    for i in range(0,len(ciphertext),16):
        temp = cipher.decrypt(ciphertext[i:i+16])
        plaintext += xor_bytes(temp,iv)
        iv = ciphertext[i:i+16]
    return plaintext

def cbc_encrypt(key,iv,plaintext):
    assert len(plaintext)%16 ==0
    assert len(key) == 16
    assert len(iv) == 16
    ciphertext = b''
    cipher = AES.new(key,AES.MODE_ECB)

    for i in range(0,len(plaintext),16):
        temp = xor_bytes(plaintext[i:i+16],iv)
        temp = cipher.encrypt(temp)
        ciphertext += temp
        iv = temp
    return ciphertext
    
if __name__ == '__main__':
    key = b"YELLOW SUBMARINE"
    iv = bytes([0])*16
    with open('c10.txt','r') as f:
        ciphertext = base64.b64decode(f.read())
        plaintext = cbc_decrypt(key,iv,ciphertext)
        assert ciphertext== cbc_encrypt(key,iv,plaintext), 'failed'