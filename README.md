# Implementasi Algoritma RSA dengan Python

Nama: Yusma Rohmatus Sholikha | NIM: 25051204445

Repository ini berisi implementasi sederhana dari algoritma **RSA
(Rivest--Shamir--Adleman)** menggunakan bahasa **Python**.

Program dapat melakukan: - Pembuatan kunci publik dan privat - Enkripsi
pesan - Dekripsi pesan

Kode ditulis dengan gaya **clean code** sehingga mudah dibaca dan
dipahami.

------------------------------------------------------------------------

# Struktur Repository

    rsa-project/
    │
    ├── rsa.py          # Program utama algoritma RSA
    ├── README.md       # Dokumentasi project

------------------------------------------------------------------------

# Persyaratan Sistem

Pastikan sudah menginstall:

-   Python 3.x

Cek versi Python:

    python --version

atau

    python3 --version

------------------------------------------------------------------------

# Cara Menjalankan Program

## 1. Download atau Clone Repository

Jika menggunakan Git:

    git clone https://github.com/yusmarohms/rsa-project.git

Masuk ke folder project:

    cd rsa-project

------------------------------------------------------------------------

## 2. Jalankan Program

Pastikan file **rsa.py** berada di folder yang sama dengan terminal.

Jalankan:

    python rsa.py

atau

    python3 rsa.py

------------------------------------------------------------------------

## Jika muncul error "No such file or directory"

Artinya terminal belum berada di folder yang berisi **rsa.py**.

Solusi:

1.  Buka folder tempat `rsa.py`
2.  Klik **address bar** di File Explorer
3.  Ketik:

    cmd

4.  Tekan **Enter**
5.  Jalankan kembali:

    python rsa.py

------------------------------------------------------------------------

# Contoh Output

Contoh hasil ketika program dijalankan:

    === HASIL KEY GENERATION ===
    Public Key  : (7, 187)
    Private Key : (23, 187)

    Masukkan Pesan: HELLO 
    Ciphertext : [30]
    Ciphertext : [30, 86]
    Ciphertext : [30, 86, 32]
    Ciphertext : [30, 86, 32, 32]
    Ciphertext : [30, 86, 32, 32, 139]
    Hasil Dekripsi : HELLO

------------------------------------------------------------------------

# Penjelasan Singkat RSA

Langkah utama algoritma RSA:

1.  Pilih dua bilangan prima `p` dan `q`
   
   Hitung
    
    n = p × q

   Hitung

    φ(n) = (p-1)(q-1)

2. Pilih `e` sehingga

       1 < e < φ(n)
       gcd(e, φ(n)) = 1

3.  Hitung `d` sebagai modular inverse dari `e`.

Kunci yang dihasilkan:

-   **Public Key** = `(e, n)`
-   **Private Key** = `(d, n)`

------------------------------------------------------------------------

# Tujuan Project

Project ini dibuat untuk:

-   Memahami konsep kriptografi RSA
-   Mengimplementasikan algoritma kriptografi menggunakan Python
-   Menerapkan prinsip clean code dalam penulisan program
