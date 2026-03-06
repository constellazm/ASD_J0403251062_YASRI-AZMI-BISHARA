# =================================================================
# Nama  : Yasri Azmi Bishara
# NIM   : J0403251062
# Kelas : TPL A1
# Praktikum 6
# =================================================================

"""
Latihan 5: Shell Sort
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
        
        while position >= gap and data[position - gap] < currentvalue: # Masih sama seperti latihan sebelumnya, kita cukup mengubah pembanding dari lebih besar(>), menjadi lebih kecil(<)
            data[position] = data[position - gap]
            position = position - gap

        data[position] = currentvalue

data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shellSort(data)
print("Final Sorted List:", data)