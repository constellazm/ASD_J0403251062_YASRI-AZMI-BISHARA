# =======================================================
# Nama  : Yasri Azmi Bishara
# NIM   : J0403251062
# Kelas : A/1
# Praktikum 12 - Graph II: Shortest Path
# =======================================================

# ==========================================================
# Materi 2: Implementasi Bellman-Ford
# ==========================================================

# Representasi Graf dengan Bobot (termasuk bobot negatif) menggunakan Dictionary
graph = {
    'A': {'B': 5, 'C': 4},  # Node A terhubung ke B (bobot 5) dan C (bobot 4)
    'B': {},                # Node B tidak memiliki jalur keluar
    'C': {'B': -2}          # Node C terhubung ke B dengan bobot negatif (-2)
}

def bellman_ford(graph, start):
    # Inisialisasi: Atur semua jarak node ke 'inf' (tak terhingga)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0    # Jarak dari node awal ke dirinya sendiri adalah 0

    # Perulangan utama dilakukan sebanyak (Jumlah Node - 1) kali untuk menjamin keakuratan rute
    for _ in range(len(graph) - 1):

        # Melakukan iterasi ke setiap node dan memeriksa seluruh edge (jalur) yang ada di dalam graf
        for node in graph:
            for neighbor, weight in graph[node].items():

                # Proses Relaksasi: Periksa apakah jalur baru melalui 'node' saat ini 
                # menghasilkan jarak yang lebih pendek ke 'neighbor' (tetangga)
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight # Perbarui dengan jarak yang lebih pendek

    return distances  # Mengembalikan dictionary berisi jarak terpendek ke semua node

# Menjalankan fungsi Bellman-Ford dengan node awal 'A'
hasil = bellman_ford(graph, 'A')
print(hasil)  # Mencetak hasil akhir jarak terpendek dari A