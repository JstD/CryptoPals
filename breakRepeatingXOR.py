
def harmming_distance(s1,s2):
    result =0
    for a,b in zip(s1,s2):
        temp1 = bin(ord(a))[2:].zfill(8)
        temp2 = bin(ord(b))[2:].zfill(8)
        for x,y in zip(temp1,temp2):
            if x !=y:
                result +=1
    return result
assert harmming_distance('this is a test','wokka wokka!!!') == 37, 'failed'

