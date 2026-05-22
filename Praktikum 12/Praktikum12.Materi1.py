# =======================================================
# Nama  : Yasri Azmi Bishara
# NIM   : J0403251062
# Kelas : A/1
# Praktikum 12 - Graph II: Shortest Path
# =======================================================

# ==========================================================
# Materi 1: Implementasi Dijkstra
# ==========================================================

import heapq  # Mengimpor library priority queue (Min-Heap) untuk mengambil jarak terkecil dengan cepat

# Representasi Graf Berbobot menggunakan Dictionary di dalam Dictionary
graph = {
    'A': {'B': 4, 'C': 2},  # Node A terhubung ke B (bobot 4) dan C (bobot 2)
    'B': {'D': 5},          # Node B terhubung ke D (bobot 5)
    'C': {'D': 1},          # Node C terhubung ke D (bobot 1)
    'D': {}                 # Node D tidak memiliki jalur keluar
}

def dijkstra(graph, start):
    # Inisialisasi: Atur semua jarak node ke 'inf' (tak terhingga)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # Jarak dari node awal ke dirinya sendiri adalah 0

    # Membuat antrean prioritas (priority queue) dan memasukkan node awal (jarak, nama_node)
    pq = [(0, start)]

    # Loop berjalan selama masih ada node yang harus diproses di dalam antrean
    while pq:
        # Mengambil node dengan jarak akumulasi terkecil dari antrean
        current_distance, current_node = heapq.heappop(pq)

        # Memeriksa semua tetangga dari node yang saat ini sedang diproses
        for neighbor, weight in graph[current_node].items():
            # Hitung total jarak baru menuju node tetangga
            distance = current_distance + weight

            # Relaksasi: Jika ditemukan jalur yang lebih pendek dari yang dicatat sebelumnya
            if distance < distances[neighbor]:
                distances[neighbor] = distance  # Perbarui jarak terpendek ke node tetangga tersebut
                heapq.heappush(pq, (distance, neighbor))  # Masukkan tetangga ke antrean untuk diproses nanti

    return distances  # Mengembalikan dictionary berisi jarak terpendek ke semua node

# Menjalankan fungsi Dijkstra dengan node awal 'A'
hasil = dijkstra(graph, 'A')
print(hasil)  # Mencetak hasil akhir berupa jarak terpendek dari A ke semua node