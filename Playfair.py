def generate_key_square(key):
    key = key.upper().replace("J", "I")  # Thay 'J' bang 'I'
    used = set()
    processed_key = ""

    # Bo ky tu trung lap
    for c in key:
        if c.isalpha() and c not in used:
            processed_key += c
            used.add(c)

    # Them chu cai con thieu vao ma tran 5x5
    for c in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if c not in used:
            processed_key += c

    # tra lai ma tran 5x5
    return [list(processed_key[i:i+5]) for i in range(0, 25, 5)]

def find_position(matrix, char):
    if char == "J":
        char = "I"
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return -1, -1

def preprocess_plaintext(text):
    text = text.upper().replace("J", "I")  # Thay 'J' bang 'I'
    processed_text = "".join(c for c in text if c.isalpha())  # giu lai chu cai

    result = ""
    i = 0
    while i < len(processed_text):
        result += processed_text[i]
        if i + 1 < len(processed_text) and processed_text[i] == processed_text[i + 1]:
            result += "X"  # Chen 'X' neu co 2 ky tu giong nhau lien tiep
        i += 1

    if len(result) % 2 != 0:
        result += "X" 

    return result

def encrypt(plaintext, key_square):
    plaintext = preprocess_plaintext(plaintext)
    ciphertext = ""

    for i in range(0, len(plaintext), 2):
        a, b = plaintext[i], plaintext[i+1]
        rowA, colA = find_position(key_square, a)
        rowB, colB = find_position(key_square, b)

        if rowA == rowB:  # TH1 cung hang
            ciphertext += key_square[rowA][(colA + 1) % 5]
            ciphertext += key_square[rowB][(colB + 1) % 5]
        elif colA == colB:  # TH2cung cot
            ciphertext += key_square[(rowA + 1) % 5][colA]
            ciphertext += key_square[(rowB + 1) % 5][colB]
        else:  # TH HCN
            ciphertext += key_square[rowA][colB]
            ciphertext += key_square[rowB][colA]

    return ciphertext

if __name__ == "__main__":
    key = input("Nhap khoa: ")
    plaintext = input("Nhap ban ro: ")

    key_square = generate_key_square(key)
    ciphertext = encrypt(plaintext, key_square)

    print("Ban ma:", ciphertext)
