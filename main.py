from email.policy import default
import PySimpleGUI as sg                        # Part 1 - The import
from pathlib import Path
from extended_vigenere import extended_vigenere_decrypt, extended_vigenere_encrypt
from otp import otp_decrypt, otp_encrypt
from playfair import playfair_cipher_decrypt, playfair_cipher_encrypt
from vigenere import *
from enigma import *

sg.theme('DarkAmber')

# Define the window's contents
layout = [[sg.Text("Welcome, please select a cipher method!")],     # Part 2 - The Layout
          [sg.Radio('Vigenere Basic', "Cipher", default=False),
           sg.Radio('Vigenere Autokey', "Cipher", default=False),
           sg.Radio('Extended Vigenere', "Cipher", default=False),
           sg.Radio('Playfair', "Cipher", default=False),
           sg.Radio('Engima', "Cipher", default=False),
           sg.Radio('OTP', "Cipher", default=False)
           ],
          [sg.Text('_' * 80)],
          [sg.Text("Cipher output type")],
          [sg.Radio("No spasi", "Space", default=True, key="nospace"), sg.Radio(
              "5-huruf", "Space", default=False, key="5huruf")],
          [sg.Text('_' * 80)],
          [
              sg.Text("Input File Name"),
    sg.Input(key='-INPUT-'),
    sg.FileBrowse(file_types=(("TXT Files", "*.txt"), ("ALL Files", "*.*"))),
],
    [sg.Text("Output File Name"), sg.Input(key='OUTPUTFILE')],
    [sg.Text('_' * 80)],
    [sg.Text("Plain Text  "), sg.Multiline(size=(43, 3), key='PLAINTEXT')],
    [sg.Text("Key           "), sg.Input(key='KEY')],
    [sg.Text("Key File Name (for OTP)"), sg.Input(key='KEYFILE'), sg.FileBrowse(
        file_types=(("TXT Files", "*.txt"), ("ALL Files", "*.*"))), ],
    [sg.Text("Cipher Text"), sg.Multiline(size=(43, 3), key='CIPHERTEXT')],
    [sg.Button('Encrypt'), sg.Button('Decrypt'), sg.Button('Save Plain to File'), sg.Button('Save Cipher to File'), sg.Button('RESET')]]

# Create the window
# Part 3 - Window Defintion
window = sg.Window('Kriptografi Klasik', layout)

while True:
    # Display and interact with the Window
    event, values = window.read()
    outputfile = "output.txt"

    if (values["OUTPUTFILE"]):
        outputfile = values["OUTPUTFILE"]

    print(event, values)

    if (values['-INPUT-']):
        filename = values['-INPUT-']
        if Path(filename).is_file():
            try:
                with open(filename, "rb") as f:
                    text = f.read()

                window.Element(key='PLAINTEXT').Update(text)

            except Exception as e:
                print("Error: ", e)

    if event == "Save Plain to File":
        with open(outputfile, 'wb') as f:
            f.write(bytes(values["PLAINTEXT"], "utf-8"))
    if event == "Save Cipher to File":
        with open(outputfile, 'wb') as f:
            f.write(bytes(values["CIPHERTEXT"], "utf-8"))
    if event == "RESET":
        window.Element(key="PLAINTEXT").Update("")
        window.Element(key="CIPHERTEXT").Update("")
        window.Element(key="KEY").Update("")
        window.Element(key="-INPUT-").Update("")
        window.Element(key="OUTPUTFILE").Update("")

    if values[0]:
        print("Vigenere Basic")
        if event == "Encrypt":
            cipher = vigenere(values["KEY"], values["PLAINTEXT"], True, False)
            if (values["nospace"]):
                window.Element(key='CIPHERTEXT').Update(cipher)
            else:
                temp = ' '.join([cipher[i:i+5]
                                for i in range(0, len(cipher), 5)])
                window.Element(key='CIPHERTEXT').Update(temp)
        elif event == "Decrypt":
            plain = vigenere(values["KEY"], values["CIPHERTEXT"], False, False)
            window.Element(key='PLAINTEXT').Update(plain)

    elif values[1]:
        print("Vigenere Autokey")
        if event == "Encrypt":
            cipher = vigenere(values["KEY"], values["PLAINTEXT"], True, True)
            if (values["nospace"]):
                window.Element(key='CIPHERTEXT').Update(cipher)
            else:
                temp = ' '.join([cipher[i:i+5]
                                for i in range(0, len(cipher), 5)])
                window.Element(key='CIPHERTEXT').Update(temp)
        elif event == "Decrypt":
            plain = vigenere(values["KEY"], values["CIPHERTEXT"], False, True)
            window.Element(key='PLAINTEXT').Update(plain if values["nospace"] else [
                plain[i:i+5] for i in range(0, len(plain), 5)])

    elif values[2]:
        print("Extended Vigenere")
        if (len(values['KEY']) != 0):
            if event == "Encrypt":
                if (values["-INPUT-"]):
                    cipher_ext_vig = extended_vigenere_encrypt(
                        bytes(values["KEY"], "utf-8"), text)
                    with open(outputfile, 'wb') as f:
                        f.write(cipher_ext_vig)
                else:
                    cipher_ext_vig = extended_vigenere_encrypt(
                        bytes(values["KEY"], "latin-1"), bytes(values["PLAINTEXT"], "latin-1"))
                    cipher_ext_vig = str(cipher_ext_vig, 'latin-1')
                    window.Element(key='CIPHERTEXT').Update(cipher_ext_vig)

            elif event == "Decrypt":
                if (values["-INPUT-"]):
                    plain_ext_vig = extended_vigenere_decrypt(
                        bytes(values["KEY"], "utf-8"), text)
                    with open(outputfile, 'wb') as f:
                        f.write(plain_ext_vig)
                else:
                    plain_ext_vig = extended_vigenere_decrypt(
                        bytes(values["KEY"], "latin-1"), bytes(values["CIPHERTEXT"], "latin-1"))
                    plain_ext_vig = str(plain_ext_vig, 'latin-1')
                    window.Element(key='PLAINTEXT').Update(
                        plain_ext_vig if values["nospace"] else [
                            plain_ext_vig[i:i+5] for i in range(0, len(plain_ext_vig), 5)])

    elif values[3]:
        print("Playfair Cipher")
        if event == "Encrypt":
            cipher = playfair_cipher_encrypt(
                values["KEY"], values["PLAINTEXT"])
            if (values["nospace"]):
                window.Element(key='CIPHERTEXT').Update(cipher)
            else:
                temp = ' '.join([cipher[i:i+5]
                                for i in range(0, len(cipher), 5)])
                window.Element(key='CIPHERTEXT').Update(temp)

        elif event == "Decrypt":
            plain = playfair_cipher_decrypt(
                values["KEY"], values["CIPHERTEXT"])
            window.Element(key='PLAINTEXT').Update(plain)

    elif values[4]:
        print("Engima")
        if event == "Encrypt":
            cipher = enigma(values["KEY"], values["PLAINTEXT"])
            if (values["nospace"]):
                window.Element(key='CIPHERTEXT').Update(cipher)
            else:
                temp = ' '.join([cipher[i:i+5]
                                for i in range(0, len(cipher), 5)])
                window.Element(key='CIPHERTEXT').Update(temp)
        elif event == "Decrypt":
            plain = enigma(values["KEY"], values["CIPHERTEXT"])
            window.Element(key='PLAINTEXT').Update(plain if values["nospace"] else [
                plain[i:i+5] for i in range(0, len(plain), 5)])

    elif values[5]:
        if event == "Encrypt":
            cipher = otp_encrypt(values["PLAINTEXT"])
            if (values["nospace"]):
                window.Element(key='CIPHERTEXT').Update(cipher)
            else:
                temp = ' '.join([cipher[i:i+5]
                                for i in range(0, len(cipher), 5)])
                window.Element(key='CIPHERTEXT').Update(temp)
        elif event == "Decrypt":
            plain = otp_decrypt(values["CIPHERTEXT"])
            window.Element(key='PLAINTEXT').Update(plain)

    if event == sg.WIN_CLOSED:
        break

# Finish up by removing from the screen
window.close()                                  # Part 5 - Close the Window
