# =================================================================
# Nama  : Yasri Azmi Bishara
# NIM   : J0403251062
# Kelas : TPL A1
# Praktikum 6
# =================================================================

"""
Latihan 2   : Bubble Sort Descending.
Perintah    : Ketik kembali kode program di atas. Setelah itu, modifikasilah program yang
awalnya mengurutkan secara menaik (ascending) menjadi mengurutkan secara menurun (descending).
"""

def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges: 
        exchanges = False
        for i in range(passnum):
            if alist[i] < alist[i+1]: # Sama seperti latihan 1, kita cukup mengubah pembanding dari lebih besar(>), menjadi lebih kecil(<)
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum-1
        
alist=[20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(alist)
print(alist)