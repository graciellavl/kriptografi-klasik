def enigma(key, text):
    # key       : kunci, berupa 3 huruf alfabet
    # text      : plaintext apabila enkripsi, ciphertext apabila dekripsi

    # Tentukan alfabet rotor
    alfabet = ['A','B','C','D','E','F','G','H','I','J','K','L',
              'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    rotor1 = ['E','K','M','F','L','G','D','Q','V','Z','N','T','O','W','Y',
            'H','X','U','S','P','A','I','B','R','C','J']

    rotor2 = ['A','J','D','K','S','I','R','U','X','B','L','H','W','T','M',
            'C','Q','G','Z','N','P','Y','F','V','O','E']

    rotor3 = ['B','D','F','H','J','L','C','P','R','T','X','V','Z','N','Y',
            'E','I','W','G','A','K','M','U','S','Q','O']

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

    
        rotor3_1 = rotor3[(pos3 + ord(i) - 65)%26]
        rotor2_1 = rotor2[(pos2 + ord(rotor3_1) - 65)%26]
        rotor1_1 = rotor1[(pos1 + ord(rotor2_1) - 65)%26]
        reflektor_1 = reflektor[(ord(rotor1_1) - 65)%26]
        reflektor_2 = reflektor[(ord(reflektor_1) - 65)%26]
        rotor1_2 = rotor1[(pos1 + ord(reflektor_2) - 65)%26]
        rotor2_2 = rotor2[(pos2 + ord(rotor1_2) - 65)%26]
        rotor3_2 = rotor3[(pos3 + ord(rotor2_2) - 65)%26]
        

        print(rotor3_1)
        print(rotor2_1)
        print(rotor1_1)
        print(reflektor_1)
        print(reflektor_2)
        print(rotor1_2)
        print(rotor2_2)
        print(rotor3_2)


        for j in range (0, len(rotor3)):
            if (rotor3[j] == rotor3_2):
                hasil += alfabet[j]

        # hasil += rotor3_2

    return hasil

print (enigma('CAT', 'BTXQOS'))

                

        

        

    
