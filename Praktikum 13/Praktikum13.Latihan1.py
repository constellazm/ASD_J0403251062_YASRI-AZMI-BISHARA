# =======================================================
# Nama  : Yasri Azmi Bishara
# NIM   : J0403251062
# Kelas : A/1
# Praktikum 13 - Graph III: Spanning Trees 
# =======================================================

# 1. Representasi daftar edge pada graph awal menggunakan list of tuple
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# 2. Menentukan contoh salah satu Spanning Tree yang valid (menghubungkan semua node tanpa cycle)
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

# 3. Menampilkan daftar edge pada graph awal
print("Edge pada graph:")
for edge in edges:
    print(edge)

# 4. Menampilkan edge pada Spanning Tree
print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

# 5. Menampilkan jumlah edge pada masing-masing struktur
print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# ==============================================================================
# JAWABAN ANALISIS:
# 1. Apa perbedaan graph awal dan spanning tree?
#    Jawab: Graph awal masih memiliki semua jalur koneksi yang mungkin dan mengandung 
#    cycle (siklus). Sedangkan Spanning Tree adalah subgraph (bagian dari graph awal) 
#    yang menghubungkan seluruh node tanpa membentuk cycle sama sekali.
#
# 2. Mengapa spanning tree tidak boleh memiliki cycle?
#    Jawab: Karena cycle menyebabkan penggunaan edge berlebih yang membuat koneksi 
#    menjadi tidak efisien dan meningkatkan total biaya (bobot) tanpa memberikan 
#    manfaat konektivitas baru (semua node sudah terhubung).
#
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
#    Jawab: Karena jumlah edge pada Spanning Tree dikunci oleh rumus baku, yaitu 
#    (jumlah node - 1). Rumus ini adalah jumlah minimal edge yang paling efisien 
#    untuk menghubungkan seluruh node tanpa membuat jalur melingkar (cycle).
# ==============================================================================