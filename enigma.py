def enigma(key, text):
    # key       : kunci, berupa 3 huruf alfabet
    # text      : plaintext apabila enkripsi, ciphertext apabila dekripsi

    # Tentukan alfabet rotor
    alfabet = ['A','B','C','D','E','F','G','H','I','J','K','L',
              'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    rotor1 = ['U','K','P','Y','J','M','R','V','L','E','B','I','F','S','Z','C',
            'W','G','N','X','A','H','Q','T','D','O']

    rotor2 = ['X','T','H','M','C','Y','Z','U','N','W','O','B','F','E','V','L',
            'D','K','J','I','G','P','S','A','Q','R']

    rotor3 = ['X','F','S','Z','Q','B','L','T','W','R','P','G','V','U','Y','K',
            'E','J','C','H','N','M','I','A','O','D']

    reflektor = ['U','K','P','Y','J','M','R','V','L','E','B','I','F','S','Z',
            'C','W','G','N','X','A','H','Q','T','D','O']

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
    
    # Apabila panjang kunci bukan 3 tidak menghasilkan apa-apa
    if (len(key_clean) != 3):
        return ''


    # Posisi rotor teratas
    for i in range (0, len(rotor1)):
        if (rotor1[i] == key_clean[0]):
            pos1 = i
    
    for i in range (0, len(rotor2)):
        if (rotor2[i] == key_clean[1]):
            pos2 = i

    for i in range (0, len(rotor3)):
        if (rotor3[i] == key_clean[2]):
            pos3 = i

    # print("pos1", pos1)
    # print("pos2", pos2)
    # print("pos3", pos3)

    # Enkripsi
    hasil = ''
    for i in text_clean:

        # Geser
        if (pos3 == 25):
            if (pos2 == 25):
                pos1 = (pos1 + 1)%26
            pos2 = (pos2 + 1)%26

        pos3 = (pos3 + 1)%26

    
        rotor31 = rotor3[(pos3 + ord(i) - 65)%26]
        rotor21 = rotor2[(pos2 + ord(rotor31) - 65)%26]
        rotor11 = rotor1[(pos1 + ord(rotor21) - 65)%26]
        reflektor1 = reflektor[(ord(rotor11) - 65)%26]
        reflektor2 = reflektor[(ord(reflektor1) - 65)%26]
        rotor12 = rotor1[(pos1 + ord(reflektor2) - 65)%26]
        rotor22 = rotor2[(pos2 + ord(rotor12) - 65)%26]
        rotor32 = rotor3[(pos3 + ord(rotor22) - 65)%26]

        # print(rotor31)
        # print(rotor21)
        # print(rotor11)
        # print(reflektor1)
        # print(reflektor2)
        # print(rotor12)
        # print(rotor22)
        # print(rotor32)

        # for j in range (0, len(rotor3)):
        #     if (rotor3[j] == rotor32):
        #         hasil += alfabet[(j-pos3)%26]

        hasil += rotor32

    return hasil

# print (enigma('XGD', 'z'))

                

        

        

    
