from Crypto.Cipher import AES
import base64
key = "YELLOW SUBMARINE"
cipher = AES.new(key,AES.MODE_ECB)

with open('c7.txt','r') as f:
    ctxt = base64.b64decode(f.read())
    print(cipher.decrypt(ctxt))