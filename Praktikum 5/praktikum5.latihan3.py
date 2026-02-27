#=================================================================
# Nama  : Yasri Azmi Bishara
# NIM   : J0403251062
# Kelas : TPL A1
# Praktikum 5
#=================================================================

# ==========================================================
# Latihan 3: Mencari Nilai Maksimum
# ==========================================================
def cari_maks(data, index=0):
    # Base case:
    # Jika sudah di elemen terakhir dalam index, 
    # maka nilainya langsung dikembalikan
    if index == len(data) - 1: 
        return data[index] 
    
    # Recursive call:
    # Memanggil fungsi untuk cek elemen setelahnya
    maks_sisa = cari_maks(data, index + 1) 
    
    # Membandingkan angka sekarang dengan maksimum dari sisa
    if data[index] > maks_sisa: 
        return data[index] # Jika lebih besar ini, maka ini yang dipakai
    else: 
        return maks_sisa # Jika ini yang lebih besar, maka pakai yang ini
angka = [3, 7, 2, 9, 5] 
print("Nilai maksimum:", cari_maks(angka)) 