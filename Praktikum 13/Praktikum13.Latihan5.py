# =======================================================
# Nama  : Yasri Azmi Bishara
# NIM   : J0403251062
# Kelas : A/1
# Praktikum 13 - Graph III: Spanning Trees 
# =======================================================

# 1. Representasi Weighted Graph Kasus 1: Jaringan Jalan Antar Kota berbentuk List of Edge
# Format: (bobot, kota1, kota2)
jalan_edges = [
    (5, 'Bogor', 'Jakarta'),
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok', 'Bandung')
]

# 2. Implementasi Algoritma Kruskal untuk penentuan rute jalan minimum
# Langkah pertama: Urutkan jalan berdasarkan jarak/bobot terkecil
jalan_edges.sort()

mst_jalan = []
total_jarak = 0
connected_cities = set()

# Iterasi penggabungan kota
for weight, u, v in jalan_edges:
    # Memilih rute jalan jika kota tujuan belum terhubung sepenuhnya (mencegah loop)
    if u not in connected_cities or v not in connected_cities:
        mst_jalan.append((u, v, weight))
        total_jarak += weight
        connected_cities.add(u)
        connected_cities.add(v)

# 3 & 4. Output MST dan Total Bobot Minimum
print("Minimum Spanning Tree (Rute Jalan Antar Kota):")
for kota1, kota2, jarak in mst_jalan:
    print(f"{kota1} - {kota2} (Bobot/Jarak: {jarak})")
print("Total bobot minimum =", total_jarak)

# ==============================================================================
# JAWABAN ANALISIS:
# 1. Kasus apa yang dipilih?
#    Jawab: Kasus 1 — Jaringan Jalan Antar Kota (Bogor, Depok, Jakarta, Bandung).
#
# 2. Algoritma apa yang digunakan?
#    Jawab: Algoritma Kruskal (dengan pengurutan edge global).
#
# 3. Edge mana saja yang dipilih dalam MST?
#    Jawab:
#    - Bogor - Depok (Bobot: 2)
#    - Depok - Jakarta (Bobot: 3)
#    - Depok - Bandung (Bobot: 4)
#
# 4. Berapa total bobot MST?
#    Jawab: Total bobot minimum = 9.
#
# 5. Mengapa edge tertentu tidak dipilih?
#    Jawab: Edge 'Bogor - Jakarta' (bobot 5) dan 'Jakarta - Bandung' (bobot 6) 
#    tidak dipilih karena seluruh kota telah terhubung sempurna melalui jalur alternatif 
#    Depok yang biayanya jauh lebih murah. Memasukkan rute tersebut hanya akan membuat 
#    jalur memutar melingkar (cycle) yang tidak efektif.
# ==============================================================================