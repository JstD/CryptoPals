

def get_english_score(string):
    character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }

    return sum([character_frequencies.get(c, 0) for c in string.lower()])
if __name__ == "__main__":
    h = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    temp = bytes.fromhex(h)
    lst = []
    for c in range(256):
        s = ''.join(chr(c^x) for x in temp)
        score = get_english_score(s)
        lst.append({
            'score': score,
            'string': s
        })
    lst.sort(key=lambda item: item.get('score'))
    print(lst[-1])