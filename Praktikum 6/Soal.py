# =================================================================
# Nama  : Yasri Azmi Bishara
# NIM   : J0403251062
# Kelas : TPL A1
# Praktikum 6
# =================================================================

"""
Latihan Soal Pengurutan

Pak Budi adalah seorang manager sumber daya manusia di suatu perusahaan. Ia
saat ini harus menseleksi pelamar kerja berdasarkan skor tes potensi akademik
mereka. Skor tersebut disajikan dalam bentuk list dengan rentang nilai 0 - 100.
Berikut adalah data hasil tes potensi akademik yang tersedia:

[43, 76, 12, 89, 33, 57, 98, 22, 68, 9]

Soal:
1. Jika Pak Budi akan meloloskan lima kandidat dengan nilai tertinggi, tuliskanlah
skor lima kandidat tersebut dari yang paling tinggi hingga terendah.
2. Kandidat berapa saja yang lolos?
"""

# Saya Memakai Metode Pengurutan Selection Sort (Descending)

def seleksi_pelamar(data):
    for i in range(len(data)):
        max_idx = i
        for j in range(i + 1, len(data)):
            if data[j] > data[max_idx]:
                max_idx = j
        data[i], data[max_idx] = data[max_idx], data[i]

skor = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]

seleksi_pelamar(skor)

lima_tertinggi = skor[:5]

print("Hasil urutan skor (Tinggi ke Rendah):", skor)
print("Skor 5 kandidat yang lolos:", lima_tertinggi)

# Output
# Hasil urutan skor (Tinggi ke Rendah): [98, 89, 76, 68, 57, 43, 33, 22, 12, 9]
# Skor 5 kandidat yang lolos: [98, 89, 76, 68, 57]