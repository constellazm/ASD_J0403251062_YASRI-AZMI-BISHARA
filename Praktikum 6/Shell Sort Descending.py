# =================================================================
# Nama  : Yasri Azmi Bishara
# NIM   : J0403251062
# Kelas : TPL A1
# Praktikum 6
# =================================================================

"""
Latihan 4: Shell Sort Descending
Perintah : Ketik kembali kode program di atas. Setelah itu, modifikasilah program yang
awalnya mengurutkan secara menaik (ascending) menjadi mengurutkan secara menurun (descending).
"""

def shellSort(data):
    sublistcount = len(data) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(data, startposition, sublistcount)

        print("After increments of size", sublistcount, "The list is", data)
        sublistcount = sublistcount // 2

def gapInsertionSort(data, start, gap):
    for i in range(start + gap, len(data), gap):
        currentvalue = data[i]
        position = i
        
        while position >= gap and data[position - gap] < currentvalue: # Proses menggeser angka yang lebih kecil ke arah kanan sejauh jarak gap agar angka yang lebih besar bisa pindah ke posisi kiri
            data[position] = data[position - gap]
            position = position - gap

        data[position] = currentvalue

data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shellSort(data)
print("Final Sorted List:", data)

# Output
"""
After increments of size 4 The list is [77, 31, 93, 55, 54, 26, 44, 17, 20]
After increments of size 2 The list is [93, 55, 77, 31, 54, 26, 44, 17, 20]
After increments of size 1 The list is [93, 77, 55, 54, 44, 31, 26, 20, 17]
Final Sorted List: [93, 77, 55, 54, 44, 31, 26, 20, 17]
"""