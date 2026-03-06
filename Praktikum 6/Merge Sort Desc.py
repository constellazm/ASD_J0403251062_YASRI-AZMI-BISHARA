# =================================================================
# Nama  : Yasri Azmi Bishara
# NIM   : J0403251062
# Kelas : TPL A1
# Praktikum 6
# =================================================================

"""
Latihan 5: Merge Sort Descending
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
            if lefthalf[i] >= righthalf[j]: # Jika angka di kiri lebih besar atau sama dengan angka di kanan, maka ambil angka kiri duluan 
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

# Output
"""
Splitting  [54, 26, 93, 17, 77, 31, 44, 55, 20]
Splitting  [54, 26, 93, 17]
Splitting  [54, 26]
Splitting  [54]
Splitting  [26]
Merging  [54, 26]
Splitting  [93, 17]
Splitting  [93]
Splitting  [17]
Merging  [93, 17]
Merging  [93, 54, 26, 17]
Splitting  [77, 31, 44, 55, 20]
Splitting  [77, 31]
Splitting  [77]
Splitting  [31]
Merging  [77, 31]
Splitting  [44, 55, 20]
Splitting  [44]
Splitting  [55, 20]
Splitting  [55]
Splitting  [20]
Merging  [55, 20]
Merging  [55, 44, 20]
Merging  [77, 55, 44, 31, 20]
Merging  [93, 77, 55, 54, 44, 31, 26, 20, 17]
[93, 77, 55, 54, 44, 31, 26, 20, 17]
"""