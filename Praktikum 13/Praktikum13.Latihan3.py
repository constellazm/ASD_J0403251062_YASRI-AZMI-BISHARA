# =======================================================
# Nama  : Yasri Azmi Bishara
# NIM   : J0403251062
# Kelas : A/1
# Praktikum 13 - Graph III: Spanning Trees 
# =======================================================

import heapq

# Representasi Graph menggunakan Adjacency List (Dictionary)
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):
    visited = set([start])  # Mencatat node yang sudah masuk ke dalam Tree
    edges = []              # Min-Heap menampung kandidat edge terdekat
    
    # Masukkan semua edge tetangga dari node awal ke dalam Min-Heap
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))
        
    mst = []
    total_weight = 0
    
    # Looping selama priority queue (heap) masih menyimpan data edge
    while edges:
        # Ambil edge dengan bobot terkecil dari node aktif saat ini
        weight, u, v = heapq.heappop(edges)
        
        # Jika node tujuan (v) belum dikunjungi, maka edge ini aman (tidak cycle)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
            
            # Tambahkan semua edge tetangga baru dari node v ke dalam heap
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
                    
    return mst, total_weight

# Menjalankan fungsi Prim dimulai dari node 'A'
mst, total = prim(graph, 'A')

# Menampilkan output program
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
print("Total bobot =", total)

# ==============================================================================
# JAWABAN ANALISIS:
# 1. Node awal apa yang digunakan?
#    Jawab: Node awal yang digunakan adalah 'A'.
#
# 2. Edge mana yang dipilih pertama kali?
#    Jawab: Edge ('A', 'C') dengan bobot 2.
#
# 3. Bagaimana Prim menentukan edge berikutnya?
#    Jawab: Prim melihat semua edge terdekat yang terhubung dengan node-node aktif 
#    (sudah dikunjungi), lalu menggunakan struktur data Min-Heap (`heapq`) untuk 
#    menarik otomatis edge dengan bobot paling kecil menuju ke node yang belum dikunjungi.
#
# 4. Berapa total bobot MST yang dihasilkan?
#    Jawab: Total bobot = 6.
#
# 5. Apa perbedaan pendekatan Prim dan Kruskal?
#    Jawab: Kruskal berfokus langsung pada edge (memilih edge terkecil secara global 
#    dari seluruh graph tanpa memedulikan node asal). Sedangkan Prim berfokus pada 
#    node (membangun struktur pohon yang tumbuh membesar secara bertahap dari satu titik asal).
# ==============================================================================