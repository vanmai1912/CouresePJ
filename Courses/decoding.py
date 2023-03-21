from  Courses.securable_data import *


# Thuat giai Caeser
def decoding_no1 (ciphertext):
    n = 280
    cipherindex_range = []
    plaintext = ""

    decode = create_decode()
    encode = create_encode()

    for i in ciphertext:
        cipherindex_range.append(decode[i])

    for c in cipherindex_range:
        index = (c-caesar_key)
        while index < 0:
            index += n
        plaintext += encode[index]

    return plaintext

# Thuat ma Vigener
def decoding_no2 (ciphertext):
    n = 280
    cipherindex_range = []
    keyindex_rang = []
    plaintext = ""
    index=0

    decode = create_decode()
    encode = create_encode()

    for c in ciphertext:
        cipherindex_range.append(decode[c])

    for k in vigenere_key:
        keyindex_rang.append(decode[k])

    while len(cipherindex_range) != len(keyindex_rang):
        if len(cipherindex_range) > len(keyindex_rang):
            keyindex_rang.append(keyindex_rang[index])
            index += 1
        else:
            temp = len(keyindex_rang) - 1
            keyindex_rang.remove(keyindex_rang[temp])

    for i in range(len(cipherindex_range)):
        index = (cipherindex_range[i]-keyindex_rang[i])
        while index < 0:
            index += n
        plaintext += encode[index]

    return plaintext