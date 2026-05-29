# =======================================================
# Nama  : Yasri Azmi Bishara
# NIM   : J0403251062
# Kelas : A/1
# Praktikum 13 - Graph III: Spanning Trees 
# =======================================================

# ==========================================================
# Implementasi Kruskal
# ==========================================================
# Daftar edge: (bobot, node1, node2)
# Mendefinisikan daftar edge (sisi) dalam bentuk tuple: (bobot, node_asal, node_tujuan)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan elemen pertama (bobot) dari terkecil ke terbesar
edges.sort()

# Inisialisasi list untuk menyimpan edge yang terpilih menjadi MST
mst = []

# Inisialisasi variabel untuk menghitung total bobot dari MST
total_weight = 0

# Menggunakan set untuk mencatat node mana saja yang sudah terhubung
connected = set()

# Melakukan perulangan untuk mengecek setiap edge yang sudah diurutkan
for weight, u, v in edges:
    # Menggunakan logika sederhana: jika salah satu atau kedua node belum ada di set 'connected'
    if u not in connected or v not in connected:
        mst.append((u, v, weight))  # Masukkan edge ke dalam list MST
        total_weight += weight      # Tambahkan bobotnya ke total_weight
        connected.add(u)            # Masukkan node u ke dalam set connected
        connected.add(v)            # Masukkan node v ke dalam set connected

# Menampilkan hasil akhir dari Minimum Spanning Tree
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

# Menampilkan total bobot keseluruhan dari MST
print("Total bobot =", total_weight)