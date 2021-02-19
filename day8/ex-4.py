# Cypher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type you message:\n").lower()
shift = int(input("Type the shift number:\n"))


def ceaser_chiper(plain_text, shift_amt, direction):
    output = ''
    for char in plain_text:
        alp = alphabet.index(char)
        if(direction == 'encode'):
            num = alp+shift_amt
        else:
            num = alp-shift_amt
        output += alphabet[num]
    return output


ceaser_chiper(text, shift, direction)
