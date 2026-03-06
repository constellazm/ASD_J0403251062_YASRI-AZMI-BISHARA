# =================================================================
# Nama  : Yasri Azmi Bishara
# NIM   : J0403251062
# Kelas : TPL A1
# Praktikum 6
# =================================================================

"""
Latihan 2: Selection Sort Descending
Perintah : Ketik kembali kode program di atas. Setelah itu, modifikasilah program yang awalnya 
mengurutkan secara menaik (ascending) menjadi mengurutkan secara menurun (descending).
"""

def selectionSort(data):
    for fillslot in range(len(data)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if data[location] < data[positionOfMax]:  # Mencari angka yang paling kecil di antara kumpulan angka yang belum terurut untuk nantinya dipindahkan ke posisi paling belakang
                positionOfMax = location
    
        # Swap
        temp = data[fillslot]
        data[fillslot] = data[positionOfMax]
        data[positionOfMax] = temp

data = [54,26,93,17,77,31,44,55,20]
selectionSort(data)
print(data)

# Output
# [93, 77, 55, 54, 44, 31, 26, 20, 17]