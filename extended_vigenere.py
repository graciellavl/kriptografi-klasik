def extended_vigenere_encrypt (key, plain: bytes):
    temp = b''
    for i in range (len(plain)):
        temp += ((plain[i] + key[i % len(key)]) % 256).to_bytes(1, 'big')
    return temp

def extended_vigenere_decrypt (key, cipher: bytes):
    tempnew = b''
    for i in range (len(cipher)):
        tempnew += ((cipher[i] - key[i % len(key)]) % 256).to_bytes(1, 'big')
    return tempnew

