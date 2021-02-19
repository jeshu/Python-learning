# Cypher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type you message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amt):
    print(f'Your input {plain_text} and shift {shift_amt}')

    enc_text = ''
    for char in plain_text:
        alp = alphabet.index(char)
        num = alp+3
        enc_text += alphabet[num]

    print(f'{enc_text}')


encrypt(text, shift)
