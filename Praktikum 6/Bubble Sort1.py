# =================================================================
# Nama  : Yasri Azmi Bishara
# NIM   : J0403251062
# Kelas : TPL A1
# Praktikum 6
# =================================================================

"""
Latihan 1   : Bubble Sort Ascending
Perintah    : Ketik kembali kode program di atas. Setelah itu, modifikasilah program yang awalnya
mengurutkan secara menaik (ascending) menjadi mengurutkan secara menurun (descending).
"""

def bubbleSort(data):
    for passnum in range(len(data)-1, 0, -1):
        for i in range(passnum):
             # Untuk mengubah yang tadinya menaik (ascending) menjadi menurun (descending), cukup ubah pembanding menjadi lebih kecil (<)
            if data[i] < data[i+1]:
                # Fungsi ini digunakan untuk membandingkan elemen di sebelahnya, jika memenuhi kondisi maka akan ditukar posisinya 
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp

data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort(data)
print(data)

# Output
# [17, 20, 26, 31, 44, 54, 55, 77, 93]                