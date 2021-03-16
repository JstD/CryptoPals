import base64
from singleXOR import get_english_score

def harmming_distance(s1,s2):
    result =0
    for a,b in zip(s1,s2):
        temp1 = bin(int(a))[2:].zfill(8)
        temp2 = bin(int(b))[2:].zfill(8)
        for x,y in zip(temp1,temp2):
            if x !=y:
                result +=1
    return result
assert harmming_distance('this is a test'.encode(),'wokka wokka!!!'.encode()) == 37, 'failed'

def brute_force_single_xor(bytes_input):
    lst = []
    for c in range(256):
        s = ''.join(chr(c^x) for x in bytes_input)
        score = get_english_score(s)
        lst.append({
            'score': score,
            'string': s,
            'key': c
        })
    lst.sort(key=lambda item: item.get('score'))
    return lst[-1]

def repeating_key_xor(message_bytes, key):
    """Returns message XOR'd with a key. If the message, is longer
    than the key, the key will repeat.
    """
    output_bytes = b''
    index = 0
    for byte in message_bytes:
        output_bytes += bytes([byte ^ key[index]])
        if (index + 1) == len(key):
            index = 0
        else:
            index += 1
    return output_bytes

with open('c6.txt','r') as f:
    ctxt = base64.b64decode(f.read())
    # Take the keysize from suggested range
    result = []
    for keysize in range(2,41):
        '''“For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes, 
        and find the edit distance between them. Normalize this result by dividing by KEYSIZE”'''
        distances = []
        chunks = [ctxt[i:i+keysize] for i in range(0,len(ctxt),keysize)]
        for i in range(0,len(chunks)-1,2):
            try:
                distance = harmming_distance(chunks[i],chunks[i+1])
                distances.append(distance/keysize)
            except:
                break
        result.append({
            'distance': sum(distances) / len(distances),
            'keysize' : keysize
        })
    result.sort(key= lambda item: item.get('distance'))
    
    possible_key_length = result[0]['keysize']
    possible_plaintext = []
    key = b''
    for i in range(possible_key_length):
        
        # Creates an block made up of each nth byte, where n
        # is the keysize
        block = b''
        for j in range(i, len(ctxt), possible_key_length):
            block += bytes([ctxt[j]])
        key += bytes([brute_force_single_xor(block)['key']]) 
    possible_plaintext.append((repeating_key_xor(ctxt, key), key)) 
    print(max(possible_plaintext, key=lambda x: get_english_score(x[0])))