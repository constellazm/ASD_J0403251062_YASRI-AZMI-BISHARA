# =================================================================
# Nama  : Yasri Azmi Bishara
# NIM   : J0403251062
# Kelas : TPL A1
# Praktikum 6
# =================================================================

"""
Latihan 3: Insertion Sort Ascending
Perintah : Ketik kembali kode program di atas. Setelah itu, modifikasilah program yang
awalnya mengurutkan secara menaik (ascending) menjadi mengurutkan secara menurun (descending).
"""

def insertionSort(data):
    for index in range(1,len(data)):

        currentvalue = data[index]
        position = index

        while position > 0 and data[position-1] > currentvalue: # Menggeser elemen ke kanan selama elemen tersebut lebih besar dari currentvalue
            data[position]=data[position-1]
            position = position-1

        data[position] = currentvalue
        
data = [54,26,93,17,77,31,44,55,20]
insertionSort(data)
print(data)

# Output
# [17, 20, 26, 31, 44, 54, 55, 77, 93]