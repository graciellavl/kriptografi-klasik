from email.policy import default
import PySimpleGUI as sg                        # Part 1 - The import
from pathlib import Path
from playfair import playfair_cipher_decrypt, playfair_cipher_encrypt

sg.theme('DarkAmber')

# Define the window's contents
layout = [[sg.Text("Welcome")],     # Part 2 - The Layout
          [sg.Radio('Vigenere', "Cipher", default=False),
           sg.Radio('Extended Vigenere', "Cipher", default=False),
           sg.Radio('Playfair', "Cipher", default=False),
           sg.Radio('Engima', "Cipher", default=False)],
          [
    sg.Input(key='-INPUT-'),
    sg.FileBrowse(file_types=(("TXT Files", "*.txt"), ("ALL Files", "*.*"))),
    sg.Button("Open"),
],
    [sg.Text("Plain Text"), sg.Input(key='PLAINTEXT')],
    [sg.Text("Key"), sg.Input(key='KEY')],
    [sg.Text("Cipher Text"), sg.Input(key='CIPHERTEXT')],
    [sg.Button('Encrypt'), sg.Button('Decrypt')]]

# Create the window
# Part 3 - Window Defintion
window = sg.Window('Kripyografi Klasik', layout)

while True:
    # Display and interact with the Window
    event, values = window.read()

    print(event, values)

    if (values['-INPUT-']):
        filename = values['-INPUT-']
        if Path(filename).is_file():
            try:
                with open(filename, "rt", encoding='utf-8') as f:
                    text = f.read()
                print(text)
                window.Element(key='PLAINTEXT').Update(text)

            except Exception as e:
                print("Error: ", e)

    if values[0]:
        print("Vigenere")
        if event == "Encrypt":
            print("Encrypt")
        elif event == "Decrypt":
            print("Decrypt")

    elif values[1]:
        print("Extended Vigenere")
        if event == "Encrypt":
            print("Encrypt")
        elif event == "Decrypt":
            print("Decrypt")

    elif values[2]:
        print("Playfair Cipher")
        if event == "Encrypt":
            cipher = playfair_cipher_encrypt(values["KEY"], values["PLAINTEXT"])
            window.Element(key='CIPHERTEXT').Update(cipher)

        elif event == "Decrypt":
            plain = playfair_cipher_decrypt(values["KEY"], values["CIPHERTEXT"])
            window.Element(key='PLAINTEXT').Update(plain)

    elif values[3]:
        print("Engima")
        if event == "Encrypt":
            print("Encrypt")
        elif event == "Decrypt":
            print("Decrypt")

    elif event == sg.WIN_CLOSED:
        break

# Finish up by removing from the screen
window.close()                                  # Part 5 - Close the Window
