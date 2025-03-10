def rc4(key, text):

    S = list(range(256))
    key_length = len(key)

    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]

    result = []
    i = j = 0
    for char in text:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        result.append(chr(ord(char) ^ k))

    return ''.join(result), ''.join([f"{ord(c):02x}" for c in result])


key = "E9thieugai"
text = "Hanoi University of Science and Technology"

cipher_text, keystream = rc4([ord(c) for c in key], text)

print(f"Keystream: {keystream}")
print(f"Ciphertext: {''.join([f'{ord(c):02x}' for c in cipher_text])}")