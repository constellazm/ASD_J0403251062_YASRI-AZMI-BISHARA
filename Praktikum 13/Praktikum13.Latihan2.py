# =======================================================
# Nama  : Yasri Azmi Bishara
# NIM   : J0403251062
# Kelas : A/1
# Praktikum 13 - Graph III: Spanning Trees 
# =======================================================

# Daftar edge graph dengan format tuple: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan seluruh edge secara global berdasarkan bobot terkecil (Langkah 1 Kruskal)
edges.sort()

mst = []
total_weight = 0
connected = set() # Set pelacak node yang sudah terhubung

# Proses iterasi pengecekan setiap edge hasil sorting
for weight, u, v in edges:
    # Memilih edge jika salah satu atau kedua nodenya belum terhubung (mencegah cycle sederhana)
    if u not in connected or v not in connected:
        mst.append((u, v, weight))   # Masukkan ke list MST
        total_weight += weight       # Akumulasi bobot
        connected.add(u)             # Daftarkan node u ke set
        connected.add(v)             # Daftarkan node v ke set

# Menampilkan hasil MST Kruskal
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
print("Total bobot =", total_weight)

# ==============================================================================
# JAWABAN ANALISIS:
# 1. Edge mana yang dipilih pertama kali?
#    Jawab: Edge ('C', 'D') dengan bobot 1, karena memiliki bobot terkecil di graph.
#
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
#    Jawab: Karena prinsip utama algoritma Kruskal adalah "Greedy secara global", 
#    di mana ia mengurutkan semua edge lalu mengambil biaya termurah terlebih dahulu 
#    demi mencapai total bobot minimum di akhir proses.
#
# 3. Berapa total bobot MST yang dihasilkan?
#    Jawab: Total bobot = 6.
#
# 4. Mengapa edge tertentu tidak dipilih?
#    Jawab: Edge seperti ('A', 'B') berbobot 4 dan ('A', 'D') berbobot 5 tidak dipilih 
#    karena seluruh node (A, B, C, D) sudah berhasil terhubung oleh edge-edge berbobot 
#    lebih rendah sebelumnya. Jika edge tersebut dipaksakan masuk, maka akan membentuk cycle.
# ==============================================================================