from singleXOR import get_english_score

lst = []
with open('c4.txt','r') as f:
    counter = 0
    for line in f:
        try:
            counter = 1
            h = line[:-1]
            string = bytes.fromhex(h)
            for c in range(256):
                s = ''.join(chr(c^x) for x in string)
                score = get_english_score(s)
                lst.append({
                    'counter': counter,
                    'score': score,
                    'string': s
                })
        except:
            pass
lst.sort(key=lambda item: item.get('score'))
print(lst[-1])
