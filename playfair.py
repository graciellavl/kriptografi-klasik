def playfair_cipher(key, text, isEncrypt):
    basetext = text.upper()
    i = 0
    bigram = toBigram(text)
    print(bigram)

    if isEncrypt:
        newtext = playfair_cipher_encrypt(key, basetext)
    else:
        newtext = playfair_cipher_decrypt(key, basetext)
    return newtext


def toBigram(text):
    newtext = ''
    # append X if Two letters are being repeated
    for s in range(0, len(text)+1, 2):
        if s < len(text)-1:
            print(s)
            if text[s] == text[s+1]:
                newtext = text[:s+1]+'X'+text[s+1:]
                print(newtext)

    # append X if the total letters are odd, to make text even
    if len(newtext) % 2 != 0:
        newtext = text[:]+'X'
    return newtext


def playfair_cipher_encrypt(key, text):
    return key


def playfair_cipher_decrypt(key, text):
    return key


print(playfair_cipher("abc", "TteExt", False))

# TX TE EX TX
