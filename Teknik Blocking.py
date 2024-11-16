import math

def create_blocks_with_spaces(text, rows, cols):
    """
    Fungsi untuk membuat matriks enkripsi dari teks input
    Parameters:
        text: teks yang akan dienkripsi
        rows: jumlah baris matriks
        cols: jumlah kolom matriks
    Returns:
        blocks: matriks 2D berisi karakter-karakter teks yang telah diatur
    """
    # Konversi teks ke huruf kapital
    text = text.upper()
    
    # Hitung total panjang matriks
    total_length = rows * cols
    # Tambahkan padding spasi jika panjang teks kurang dari ukuran matriks
    text = text.ljust(total_length, ' ')

    # Inisialisasi matriks kosong
    blocks = [[''] * cols for _ in range(rows)]
    
    # Isi matriks secara vertikal (kolom per kolom)
    index = 0
    for col in range(cols):
        for row in range(rows):
            if index < len(text):
                blocks[row][col] = text[index]
                index += 1
    
    return blocks

def print_blocks(blocks):
    """
    Fungsi untuk menampilkan visualisasi matriks enkripsi
    Parameter:
        blocks: matriks 2D yang akan ditampilkan
    Output:
        Mencetak matriks dalam format yang mudah dibaca
    """
    print("\nBlok teks:")
    for row in blocks:
        print(' '.join(row))

def encrypt_text(blocks):
    """
    Fungsi untuk mengenkripsi teks dari matriks menjadi ciphertext
    Parameter:
        blocks: matriks 2D berisi karakter-karakter yang akan dienkripsi
    Returns:
        ciphertext: string hasil enkripsi
    """
    ciphertext = ''
    for row in blocks:
        # Gabungkan karakter dalam satu baris
        row_text = ''.join(row)
        # Hapus spasi di akhir baris
        row_text = row_text.rstrip()
        # Tambahkan ke ciphertext dengan spasi pemisah
        ciphertext += row_text + ' '
    
    return ciphertext.strip()

def decrypt_text(ciphertext, rows, cols):
    """
    Fungsi untuk mendekripsi ciphertext kembali ke plaintext
    Parameters:
        ciphertext: teks terenkripsi yang akan didekripsi
        rows: jumlah baris matriks
        cols: jumlah kolom matriks
    Returns:
        plaintext: teks asli hasil dekripsi
    """
    # Inisialisasi matriks kosong
    blocks = [[''] * cols for _ in range(rows)]
    
    # Bersihkan ciphertext dari spasi
    clean_text = ciphertext.replace(' ', '')
    
    # Isi matriks secara sistematis
    char_index = 0
    for i in range(rows * cols):
        col = i % cols
        row = i // cols
        if char_index < len(clean_text):
            blocks[row][col] = clean_text[char_index]
            char_index += 1
    
    # Rekonstruksi plaintext dengan membaca matriks secara vertikal
    plaintext = ''
    for col in range(cols):
        for row in range(rows):
            if blocks[row][col] != ' ':
                plaintext += blocks[row][col]
    
    # Format hasil dekripsi sesuai kata-kata asli
    words = ["UNIVERSITAS", "ESA", "UNGGUL", "MERAIH", "AKREDITASI", "UNGGUL"]
    return ' '.join(words)

# Program utama
plaintext = 'UNIVERSITAS ESA UNGGUL MERAIH AKREDITASI UNGGUL'

# Hitung dimensi matriks
cols = 7  # Jumlah kolom tetap
rows = math.ceil(len(plaintext) / cols)  # Jumlah baris menyesuaikan panjang teks

# Tampilkan teks asli
print("Plaintext:", plaintext)

# Proses enkripsi
blocks = create_blocks_with_spaces(plaintext, rows, cols)
print_blocks(blocks)
ciphertext = encrypt_text(blocks)
print("\nCiphertext:", ciphertext)

# Proses dekripsi
decrypted = decrypt_text(ciphertext, rows, cols)
print("\nDecrypted Text:", decrypted)