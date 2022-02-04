def generatekey(n):
    # generate kunci dari file key.txt

    with open("key.txt", "r") as keyin:
        kunci = keyin.read()[:n]

    with open("key.txt", "w") as keyout:
        keyout.write(keyin[n:])

    return kunci


def otp_encrypt(text):
    text_clean = ''
    key_clean = ''

    # Ambil hanya alfabet, selain itu dihilangkan
    for i in text:
        if (ord(i) >= 65 and ord(i) <= 122):
            text_clean += i

    key = generatekey(len(text_clean))

    for j in key:
        if (ord(j) >= 65 and ord(j) <= 122):
            key_clean += j

    # Ubah menjadi uppercase
    text_clean = text_clean.upper()
    key_clean = key_clean.upper()

    # Enkripsi
    hasil = ''
    for i in range (0, len(text_clean)):
        hasil +=  chr(((ord(text_clean[i])-65) + (ord(key[i])-65))%26 + 65)

    return (hasil, key_clean)