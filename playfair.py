
# Function to create key matrix
from pydoc import plain


def get_key_matrix(key):
    temp = []
    for char in key:
        if char.isalpha() not in temp and char != 'J':
            temp.append(char)
    for i in range(26):
        if chr(i + ord('A')) != 'J' and chr(i + ord('A')) not in temp:
            temp.append(chr(i+ord('A')))
    key_matrix = [[temp[i*5+j] for j in range(5)] for i in range(5)]
    return key_matrix


def get_char(char, key_matrix):
    for i in range(len(key_matrix)):
        for j in range(len(key_matrix[i])):
            if char == key_matrix[i][j]:
                return i, j

# Function to generate bigram


def to_bigram(text):
    text = ''.join([char for char in text if char.isalpha()])
    text = text.replace('J', 'I')
    bigram = []
    temp = ''
    for i in range(len(text)):
        # if there is two duplicate char
        if text[i] == temp:
            temp += 'X'
            bigram.append(temp)
            temp = text[i]
        else:
            temp += text[i]

        if len(temp) == 2:
            bigram.append(temp)
            temp = ''
        # if the word is odd
        elif len(temp) == 1 and i == len(text)-1:
            temp += 'X'
            bigram.append(temp)
    return bigram

# Function to shift the bigram


def shift(bigram, encrypt, key_matrix):
    row1, col1 = get_char(bigram[0], key_matrix)
    row2, col2 = get_char(bigram[1], key_matrix)

    shifted = ""

    if row1 == row2:
        # same row
        if encrypt:
            shifted += (key_matrix[row1]
                        [(col1 + 1) % len(key_matrix[row1])])
            shifted += (key_matrix[row2]
                        [(col2 + 1) % len(key_matrix[row2])])
        else:
            shifted += (key_matrix[row1]
                        [(col1 - 1) % len(key_matrix[row1])])
            shifted += (key_matrix[row2]
                        [(col2 - 1) % len(key_matrix[row2])])
    elif col1 == col2:
        # same col
        if encrypt:
            shifted += (key_matrix[(row1 + 1) %
                                   len(key_matrix)][col1])
            shifted += (key_matrix[(row2 + 1) %
                                   len(key_matrix)][col2])
        else:
            shifted += (key_matrix[(row1 - 1) %
                                   len(key_matrix)][col1])
            shifted += (key_matrix[(row2 - 1) %
                                   len(key_matrix)][col2])
    else:
        # diff row and col
        shifted += (key_matrix[row1][col2] + key_matrix[row2][col1])
    return shifted

# Encrypt


def playfair_cipher_encrypt(key, text):
    plaintext = to_bigram(text.upper())
    key_matrix = get_key_matrix(key.upper())
    ciphertext = ""

    for bigram in plaintext:
        ciphertext += shift(bigram, True, key_matrix)
    return ciphertext

# Decrypt


def playfair_cipher_decrypt(key, text):
    ciphertext = to_bigram(text.upper())
    key_matrix = get_key_matrix(key.upper())
    plaintext = ""
    for bigram in ciphertext:
        plaintext += shift(bigram, False, key_matrix)
    return plaintext
