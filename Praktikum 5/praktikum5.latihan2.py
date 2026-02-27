#=================================================================
# Nama  : Yasri Azmi Bishara
# NIM   : J0403251062
# Kelas : TPL A1
# Praktikum 5
#=================================================================

# ==========================================================
# Latihan 2: Tracing Rekursi
# ==========================================================
def countdown(n): # Inisialisasi fungsi countdown 
    if n == 0:  # Jika n == 0. maka print "Selesai" dan return 
        print("Selesai") 
        return
    
    print("Masuk:", n)
    countdown(n - 1) # Recursive call sampai n == 0
    print("Keluar:", n) # Karena baris ini dijalankan setelah proses rekursi selesai, 
                        # dan program sedang kembali ke atas satu per satu, 
                        # ini menjadi sebab kenapa baris 'keluar' output angkanya dari yang terkecil sampai terbesar
countdown(3)