# =================================================================
# Nama  : Yasri Azmi Bishara
# NIM   : J0403251062
# Kelas : TPL A1
# Praktikum 6
# =================================================================

"""
Latihan 1   : Bubble Sort Ascending.
Perintah    : Ketik kembali kode program di atas. Setelah itu, modifikasilah program yang
awalnya mengurutkan secara menaik (ascending) menjadi mengurutkan secara menurun (descending).
"""

def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges: 
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]: # Menukar posisi angka jika angka di sebelah kanan lebih kecil daripada angka di sebelah kiri
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum-1
        
alist=[20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(alist)
print(alist)

# Output
# [20, 30, 40, 50, 60, 70, 80, 90, 100, 110]