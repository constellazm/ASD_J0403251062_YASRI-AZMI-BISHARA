# =================================================================
# Nama  : Yasri Azmi Bishara
# NIM   : J0403251062
# Kelas : TPL A1
# Praktikum 6
# =================================================================

"""
Latihan 6: Quick Short Ascending
Perintah : Ketik kembali kode program di atas. Setelah itu, modifikasilah program yang
awalnya mengurutkan secara menaik (ascending) menjadi mengurutkan secara menurun (descending).
"""

def quickSort(data):
    quickSortHelper(data, 0, len(data) - 1)

def quickSortHelper(data, first, last):
    if first < last:
        splitpoint = partition(data, first, last)
        quickSortHelper(data, first, splitpoint - 1)
        quickSortHelper(data, splitpoint + 1, last)

def partition(data, first, last):
    pivotvalue = data[first]
    leftmark = first + 1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and data[leftmark] <= pivotvalue: # Selama angka di kiri lebih besar atau sama, biarkan. Berhenti jika bertemu yang lebih kecil
            leftmark = leftmark + 1

        while data[rightmark] >= pivotvalue and rightmark >= leftmark: # Selama angka di kanan lebih besar atau sama, biarkan. Berhenti jika bertemu yang lebih kecil
            rightmark = rightmark - 1
        
        if rightmark < leftmark:
            done = True
        else:
            temp = data[leftmark]
            data[leftmark] = data[rightmark]
            data[rightmark] = temp

    temp = data[first]
    data[first] = data[rightmark]
    data[rightmark] = temp

    return rightmark

data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(data)
print(data)

# Output
# [17, 20, 26, 31, 44, 54, 55, 77, 93]