#=================================================================
# Nama  : Yasri Azmi Bishara
# NIM   : J0403251062
# Kelas : TPL A1
# Praktikum 5
#=================================================================

# ==========================================================
# Latihan 1: Rekursi Pangkat
# ==========================================================
def pangkat(a, n): # Fungsi dipanggil menggunakan variabel a dan n
    # Base case : 
    # Jika n == 0, maka berhenti dan kembalikan 1
    if n == 0: 
        return 1 
    
    # Recursive case
    # Fungsi rekursi memanggil dirinya sendiri jika n lebih dari 0, kalikan a dengan hasil pangkat(a, n - 1)
    return a * pangkat(a, n - 1) 

# Memanggil fungsi untuk menghitung 2^4 
print(pangkat(2, 4)) # Output: 16 