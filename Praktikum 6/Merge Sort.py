# =================================================================
# Nama  : Yasri Azmi Bishara
# NIM   : J0403251062
# Kelas : TPL A1
# Praktikum 6
# =================================================================

"""
Latihan 6: Merge Sort
Perintah : Ketik kembali kode program di atas. Setelah itu, modifikasilah program yang
awalnya mengurutkan secara menaik (ascending) menjadi mengurutkan secara menurun (descending).
"""

def mergeSort(data):
    print("Splitting ", data)
    if len(data) > 1:
        mid = len(data) // 2
        lefthalf = data[:mid]
        righthalf = data[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
        # Beda dari latihan sebelumnya, kita perlu mengubah pembanding dari lebih besar sama dengan(>=), menjadi lebih kecil sama dengan(<=)
            if lefthalf[i] >= righthalf[j]: 
                data[k] = lefthalf[i]
                i = i + 1
            else:
                data[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            data[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            data[k] = righthalf[j]
            j = j + 1
            k = k + 1
        
        print("Merging ", data)

data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(data)
print(data)