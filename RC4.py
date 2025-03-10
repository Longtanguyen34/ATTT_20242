def KSA(key):
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def PRGA(S, text_length):
    i = j = 0
    key_stream = []
    for _ in range(text_length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        key_stream.append(S[(S[i] + S[j]) % 256])
    return key_stream

def RC4_encrypt(text, key):
    key = [ord(c) for c in key]
    S = KSA(key)
    key_stream = PRGA(S, len(text))
    cipher = [ord(text[i]) ^ key_stream[i] for i in range(len(text))]
    return key_stream, cipher

key = "IOTK67"
text = "Hanoi University of Science and Technology"

key_stream, cipher_text = RC4_encrypt(text, key)

print("Key Stream:", key_stream)
print("Cipher Text:", cipher_text)
