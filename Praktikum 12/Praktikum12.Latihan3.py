# =======================================================
# Nama  : Yasri Azmi Bishara
# NIM   : J0403251062
# Kelas : A/1
# Praktikum 12 - Graph II: Shortest Path
# =======================================================

# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================
# Representasi Graf dengan Bobot (termasuk bobot negatif) menggunakan Dictionary
graph = {
    'A': {'B': 5, 'C': 4},  # Node A terhubung ke B (bobot 5) dan C (bobot 4)
    'B': {},                # Node B tidak memiliki jalur keluar
    'C': {'B': -2}          # Node C terhubung ke B dengan bobot negatif (-2)
}

def bellman_ford(graph, start):
    # Inisialisasi: Atur semua jarak node ke 'inf' (tak terhingga) di awal
    distances = {node: float('inf') for node in graph}
    distances[start] = 0    # Jarak dari node asal ke dirinya sendiri diatur menjadi 0

    # Perulangan utama dilakukan sebanyak (Jumlah Node - 1) kali untuk menjamin keakuratan rute
    for _ in range(len(graph) - 1):

        # Melakukan iterasi ke setiap node untuk memeriksa seluruh edge (jalur) yang ada di dalam graf
        for node in graph:
            # Memeriksa semua node tetangga (neighbor) beserta bobotnya (weight) dari node yang aktif
            for neighbor, weight in graph[node].items():

                # Proses Relaksasi: Periksa apakah jalur baru melalui 'node' saat ini
                # menghasilkan jarak yang lebih pendek ke 'neighbor' (tetangga)
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight  # Perbarui catatan jarak terpendek ke node tetangga

    return distances  # Mengembalikan kamus/dictionary berisi hasil akhir jarak terpendek ke semua node

# Menjalankan fungsi Bellman-Ford dengan menentukan node 'A' sebagai titik awal perjalanan
hasil = bellman_ford(graph, 'A')

# Mencetak hasil akhir perhitungan jarak terpendek ke terminal
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)  # Menampilkan pasangan nama node beserta total nilai jaraknya

"""
Jawaban Analisis:
1. Berapa bobot langsung dari A ke B?
   Jawaban: Bobot langsung dari A ke B adalah 5.

2. Berapa total bobot jalur A -> C -> B?
   Jawaban: Total bobotnya adalah 2 (didapat dari 4 + (-2)).

3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
   Jawaban: Jalur A -> C -> B menghasilkan jarak yang lebih kecil (nilai 2) 
   dibandingkan jalur langsung A -> B (nilai 5).

4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
   Jawaban: Karena Bellman-Ford tidak bersifat greedy (serakah) seperti Dijkstra. 
   Algoritma ini melakukan iterasi secara menyeluruh sebanyak (V - 1) kali pada semua 
   edge yang ada. Hal ini memastikan bahwa perubahan jarak akibat bobot negatif akan 
   selalu terdeteksi dan diperbarui pada iterasi berikutnya, terlepas dari urutan 
   mana edge tersebut diproses.

5. Apa yang dimaksud dengan proses relaksasi edge?
   Jawaban: Relaksasi edge adalah proses memeriksa apakah kita bisa menemukan jalur 
   yang lebih pendek ke suatu node tujuan (`neighbor`) melalui node perantara (`node`). 
   Jika jarak saat ini menuju node tujuan lebih besar daripada (jarak ke node perantara 
   + bobot edge menuju tujuan), maka jarak ke node tujuan tersebut akan diperbarui 
   (diperkecil).

6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
   Jawaban: 
   - Penanganan Bobot Negatif: Bellman-Ford dapat menangani bobot negatif dan mampu 
     mendeteksi negative cycle (siklus negatif), sedangkan Dijkstra akan gagal/salah hitung.
   - Cara Kerja: Dijkstra menggunakan pendekatan greedy dengan bantuan priority queue (Min-Heap) 
     untuk memproses node terdekat, sedangkan Bellman-Ford melakukan perulangan kaku (brute-force) 
     pada seluruh edge sebanyak (V - 1) kali.
   - Performa (Kompleksitas): Dijkstra jauh lebih cepat, sedangkan Bellman-Ford lebih 
     lambat karena memeriksa semua kombinasi berulang kali.
"""