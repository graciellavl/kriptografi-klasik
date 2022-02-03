def vigenere (key, text, isencrypt, isautokey):
    # Vigenere dengan 26 huruf alfabet
    # key       : kunci
    # text      : plaintext apabila enkripsi, ciphertext apabila dekripsi
    # isencrypt : true apabila enkripsi, false apabila dekripsi
    # isautokey : true apabila auto-key vigenere cipher, false jika tidak

    text_clean = ''
    key_clean = ''

    # Ambil hanya alfabet, selain itu dihilangkan
    for i in text:
        if (ord(i) >= 65 and ord(i) <= 122):
            text_clean += i

    for j in key:
        if (ord(j) >= 65 and ord(j) <= 122):
            key_clean += j

    # Ubah menjadi uppercase
    text_clean = text_clean.upper()
    key_clean = key_clean.upper()
    
    # Apabila panjang kunci 0 tidak menghasilkan apa-apa
    if (len(key_clean) == 0):
        return ''
    
    # Membuat kunci untuk berulang
    if (len(key_clean) < len(text_clean)):
        selisih = len(text_clean) - len(key_clean)

        if not(isautokey):
            for i in range (0, selisih):
                key_clean += key_clean[i]
            
    # print(key_clean)

    # Enkripsi
    hasil = ''
    if (isencrypt):
        if (isautokey):
            for i in range (0, selisih):
                key_clean += text_clean[i]

        for i in range (0, len(text_clean)):
            hasil +=  chr(((ord(text_clean[i])-65) + (ord(key_clean[i])-65))%26 + 65)
    else:

        # Dekripsi
        for i in range (0, len(text_clean)):
            hasil += chr(((ord(text_clean[i])-65) - (ord(key_clean[i])-65))%26 + 65)
            if (isautokey):
                key_clean += chr(((ord(text_clean[i])-65) - (ord(key_clean[i])-65))%26 + 65)
    

    return hasil


# print(vigenere ('halo', 'vayvay', True, True))






