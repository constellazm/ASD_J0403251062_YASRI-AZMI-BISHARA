# =======================================================
# Nama  : Yasri Azmi Bishara
# NIM   : J0403251062
# Kelas : A/1
# Praktikum 13 - Graph III: Spanning Trees 
# =======================================================

# =======================================================
# Implementasi Prims
# =======================================================
import heapq

# Mendefinisikan graf dalam bentuk Adjacency List menggunakan dictionary
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):
    # Set untuk mencatat node yang sudah dikunjungi (dimulai dari node 'start')
    visited = set([start])
    
    # List untuk menampung edge yang akan diproses oleh Min-Heap (priority queue)
    edges = []
    
    # Memasukkan semua edge yang terhubung dengan node tetangga dari 'start' ke dalam heap
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))
        
    # List untuk menyimpan hasil akhir edge yang terpilih masuk MST
    mst = []
    
    # Variabel untuk menghitung akumulasi total bobot MST
    total_weight = 0
    
    # Melakukan perulangan selama masih ada edge di dalam heap
    while edges:
        # Mengambil edge dengan bobot terkecil dari heap (sifat Min-Heap)
        weight, u, v = heapq.heappop(edges)
        
        # Jika node tujuan (v) belum pernah dikunjungi/belum masuk MST
        if v not in visited:
            visited.add(v)                  # Tandai node v sebagai sudah dikunjungi
            mst.append((u, v, weight))       # Masukkan edge ini ke dalam list MST
            total_weight += weight           # Tambahkan bobotnya ke total_weight
            
            # Periksa semua tetangga dari node yang baru saja dikunjungi (v)
            for neighbor, w in graph[v].items():
                # Jika tetangganya belum dikunjungi, masukkan edge baru tersebut ke dalam heap
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
                    
    # Mengembalikan hasil MST dan total bobotnya setelah perulangan selesai
    return mst, total_weight

# Memanggil fungsi Prim dengan titik awal (start) dari node 'A'
mst, total = prim(graph, 'A')

# Menampilkan hasil akhir Minimum Spanning Tree
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

# Menampilkan total bobot keseluruhan dari MST
print("Total bobot =", total)