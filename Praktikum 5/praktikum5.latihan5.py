#=================================================================
# Nama  : Yasri Azmi Bishara
# NIM   : J0403251062
# Kelas : TPL A1
# Praktikum 5
#=================================================================

# ==========================================================
# Studi Kasus: Generator PIN
# ==========================================================
def buat_pin(panjang, hasil=""):
    if len(hasil) == panjang: # Jika panjang PIN sudah sesuai, cetak dan berhenti
        print("PIN:", hasil)
        return
    
    for angka in ["0", "1", "2"]:
        if angka not in hasil: # Untuk mencegah angka yang sama muncul berulang, dengan mekanisme melewatkan angka yang sudah ada di 'hasil'
            buat_pin(panjang, hasil + angka)
            
buat_pin(3)