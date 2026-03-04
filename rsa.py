# ===============================================================
# IMPLEMENTASI RSA
# Nama: Yusma Rohmatus Sholikha
# NIM: 25051204445
# ===============================================================

# ===============================================================
# FUNGSI 1: MENCARI GCD (FPB - Faktor Persekutuan Terbesar)
# ===============================================================

def gcd(a, b):
    """
    Menghitung Greatest Common Divisor (GCD)
    menggunakan Algoritma Euclinean.

    Digunakan untuk memastikan bahwa:
    gcd(e. phi) = 1
    Artinya e dan phi relatif prima.
    """
    while b !=0:
        a, b = b, a % b
    return a

# ================================================================
# FUNGSI 2: MENCARI MODULAR INVERSE
# Menggunakan Extended Euclinean Algorithm
# ================================================================

def mod_inverse(e, phi):
    """
    Mencari nilai d sehingga:
    (d * e) mod phi = 1

    Nilai d inilah yang menjadi private key
    """
    t, new_t = 0, 1
    r, new_r = phi, e

    while new_r !=0:
        quotient = r // new_r

        # Update nilai t
        t, new_t = new_t, t - quotient * new_t

        # Update nilai r
        r, new_r = new_r, r - quotient * new_r

    # Jika gcd(e, phi) bukan 1 maka tidak ada inverse
    if r > 1:
        return None
        
    # Jika hasil negatif, ubah ke positif
    if t < 0:
        t = t + phi
            
    return t
    
# ================================================================
# KEY GENERATION (GENERATE KUNCI)
# ================================================================

# 1. Pilih dua bilangan prima
p = 17
q = 11

# 2. Hitung Modulus
n = p * q

# 3. Hitung Fungsi Totient Euler
phi = (p - 1) * (q - 1)

# 4. Pilih public exponent (e)
e = 7

# Pastikan e relatif dengan phi
if gcd(e, phi) !=1:
    print("Nilai e tidak valid karena tidak relatif prima dengan phi")
    exit()

# Hitung private exponent (d)
d = mod_inverse(e, phi)

print("=== HASIL KEY GENERATION ===")
print("Public Key  :", (e, n))
print("Private Key :", (d, n))

# ====================================================================
# PROSES ENKRIPSI
# ====================================================================

"""
Rumus enkripsi
C = M^e mod n

Setiap karakter diubah ke ASCII,
lalu dipangkatkan dengan e dan dimodulo n.
"""

plaintext = input("\nMasukkan Pesan: ")

ciphertext = []

for char in plaintext:
    m = ord(char)         # Ubah huruf menjadi angka ASCII
    c = pow(m, e, n)      # Hitung M^e mod n (lebih efisien)
    ciphertext.append(c)

    print("Ciphertext :", ciphertext)

# ====================================================================
# PROSES DEKRIPSI
# ====================================================================

"""
Rumus dekripsi:
M = C^d mod n

Ciphertext dipangkatkan dengan d, 
kemudian dikembalikan menjadi karakter.
"""

decrypted = ""

for c in ciphertext:
    m = pow(c, d, n)        # Hitung C^d mod n
    decrypted += chr(m)     # Ubah kembali ke huruf

print("Hasil Dekripsi :", decrypted)