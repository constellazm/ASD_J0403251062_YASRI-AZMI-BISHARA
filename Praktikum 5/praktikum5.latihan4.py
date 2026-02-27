#=================================================================
# Nama  : Yasri Azmi Bishara
# NIM   : J0403251062
# Kelas : TPL A1
# Praktikum 5
#=================================================================

# ==========================================================
# Latihan 4: Kombinasi Huruf
# ==========================================================
def kombinasi(n, hasil=""): 
    # Jika panjang hasil sudah sama dengan n,
    # maka cetak kombinasi tersebut
    if len(hasil) == n: 
        print(hasil)
        return 
    
    # Setiap langkah selalu bercabang 2, tambah "A" atau tambah "B"
    kombinasi(n, hasil + "A")
    kombinasi(n, hasil + "B")

# Memanggil fungsi dengan panjang 2
kombinasi(2)

# Jumlah kombinasi yang dihasilkan = 2**n
# Karena setiap posisi punya 2 pilihan (A atau B), jadi jika n = 2, maka jumlah kombinasi adalah 2**2 = 4