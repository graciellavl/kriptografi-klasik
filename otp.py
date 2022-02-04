def generatekey(n):
    # generate kunci dari file key.txt

    with open("kriptografi-klasik/key.txt", "r") as keyin:
        tmp1 = keyin.read()
        kunci = tmp1[:n]

    with open("kriptografi-klasik/key.txt", "w") as keyout:
        tmp2 = tmp1[n:]
        keyout.write(tmp2)

    return kunci


def otp_encrypt(text):
    text_clean = ''
    key_clean = ''

    # Ambil hanya alfabet, selain itu dihilangkan
    for i in text:
        if (ord(i) >= 65 and ord(i) <= 122):
            text_clean += i

    key = generatekey(len(text_clean))

    # print(key)

    for j in key:
        if (ord(j) >= 65 and ord(j) <= 122):
            key_clean += j

    # Ubah menjadi uppercase
    text_clean = text_clean.upper()
    key_clean = key_clean.upper()

    # Enkripsi
    hasil = ''
    for i in range (0, len(text_clean)):
        hasil +=  chr(((ord(text_clean[i])-65) + (ord(key_clean[i])-65))%26 + 65)

    # Simpan ke file
    with open("kriptografi-klasik/otpcipher.txt", "a") as file:
        file.write(hasil)

    with open("kriptografi-klasik/otpkey.txt", "a") as file:
        file.write(key)

    return hasil


def otp_decrypt(text):
    try:
        with open("kriptografi-klasik/otpcipher.txt") as file:
            i = file.read().index(text)
    
    except (ValueError):
        raise ValueError("Cipher tidak ditemukan")

    with open("kriptografi-klasik/otpkey.txt") as file:
        key = file.read()[i:i+len(text)]

    hasil = ''
    for i in range (0, len(text)):
        hasil += chr(((ord(text[i])-65) - (ord(key[i])-65))%26 + 65)

    return hasil


# print (otp_decrypt("XJVH"))