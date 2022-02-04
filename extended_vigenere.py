def extended_vigenere_encrypt (key, plain: bytes):
    if (len(key) == 0):
        return ''
    else:
        temp = b''
        for i in range (len(plain)):
            temp += ((plain[i] + key[i % len(key)]) % 256).to_bytes(1, 'big')
        return temp

def extended_vigenere_decrypt (key, cipher: bytes):
    if (len(key) == 0):
        return ''
    else:
        tempnew = b''
        for i in range (len(cipher)):
            tempnew += ((cipher[i] - key[i % len(key)]) % 256).to_bytes(1, 'big')
        return tempnew

