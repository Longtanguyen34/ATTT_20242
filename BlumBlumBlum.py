import random
import sympy
import math

def generate_large_prime(bits=512):
    """Tạo một số nguyên tố có số bit xác định."""
    while True:
        prime = sympy.randprime(2**(bits-1), 2**bits)
        if prime % 4 == 3:
            return prime

def blum_blum_shub(bit_length=10**6):
    """Tạo chuỗi bit giả ngẫu nhiên bằng thuật toán Blum Blum Shub."""
    p = generate_large_prime(512)
    q = generate_large_prime(512)
    n = p * q
    seed = random.randint(2, n-1)
    while math.gcd(seed, n) != 1:
        seed = random.randint(2, n-1)
    
    x = seed
    bitstream = ""
    for _ in range(bit_length):
        x = (x * x) % n
        bitstream += str(x % 2)  # Lấy bit cuối
    
    return bitstream

# Sinh chuỗi bit dài 10^6
bitstream = blum_blum_shub(10**6)

# Lưu vào file
with open("BBB_output.txt", "w") as file:
    file.write(bitstream)

print("Đã tạo chuỗi bit BBS và lưu vào file BBB_output.txt")
