# =======================================================
# Nama  : Yasri Azmi Bishara
# NIM   : J0403251062
# Kelas : A/1
# Praktikum 12 - Graph II: Shortest Path
# =======================================================

# ==========================================================
# Latihan 5: Studi Kasus Shortest Path Antar Kota
# Algoritma: Dijkstra
# ==========================================================
import heapq  # Mengimpor library priority queue (Min-Heap) untuk mengambil jarak kota terkecil secara efisien

# Representasi Peta Antar Kota menggunakan struktur data Dictionary di dalam Dictionary
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},    # Dari Bogor ke Jakarta (bobot 5) dan Depok (bobot 2)
    'Jakarta': {'Bandung': 7},              # Dari Jakarta ke Bandung (bobot 7)
    'Depok': {'Jakarta': 2, 'Bandung': 6},  # Dari Depok ke Jakarta (bobot 2) dan Bandung (bobot 6)
    'Bandung': {}                           # Bandung tidak memiliki jalur keluar selanjutnya
}

def dijkstra(graph, start):
    # Inisialisasi: Atur semua jarak kota ke 'inf' (tak terhingga) di awal
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # Jarak dari kota asal (Bogor) ke dirinya sendiri diatur menjadi 0

    # Membuat antrean prioritas (priority queue) dan memasukkan kota awal (jarak, nama_kota)
    priority_queue = [(0, start)]

    # Perulangan berjalan selama masih ada kota yang tersisa di dalam antrean
    while priority_queue:
        # Mengambil kota dengan akumulasi jarak paling kecil/terdekat dari antrean
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak yang diambil lebih besar dari jarak yang sudah tercatat, abaikan proses ini
        if current_distance > distances[current_node]:
            continue

        # Memeriksa semua kota tetangga (neighbor) beserta bobot jaraknya (weight) dari kota aktif
        for neighbor, weight in graph[current_node].items():

            # Hitung akumulasi total jarak baru menuju kota tetangga tersebut
            distance = current_distance + weight

            # Proses Relaksasi: Periksa apakah rute baru ini lebih pendek/dekat dari rute sebelumnya
            if distance < distances[neighbor]:
                distances[neighbor] = distance  # Perbarui catatan jarak terpendek ke kota tetangga
                heapq.heappush(priority_queue, (distance, neighbor))  # Masukkan kota tetangga ke antrean untuk dieksplorasi lanjut

    return distances  # Mengembalikan kamus/dictionary berisi hasil akhir jarak terpendek ke semua kota

# Menentukan kota 'Bogor' sebagai titik awal perjalanan
start_node = 'Bogor'

# Menjalankan fungsi Dijkstra
hasil = dijkstra(graph, start_node)

# Mencetak hasil akhir perhitungan rute terpendek dari Bogor ke terminal
print("Jarak terpendek dari Bogor:")
for kota, jarak in hasil.items():
    print("Bogor ->", kota, "=", jarak)  # Menampilkan rute perjalanan beserta total akumulasi nilai jaraknya

"""
Jawaban Analisis:
1. Node awal yang digunakan apa?
   Jawaban: Node awal yang digunakan adalah 'Bogor'.

2. Node mana yang memiliki jarak paling kecil dari node awal?
   Jawaban: Node 'Depok', dengan jarak/bobot terkecil yaitu 2.

3. Node mana yang memiliki jarak paling besar dari node awal?
   Jawaban: Node 'Bandung', dengan jarak/bobot akumulasi terbesar yaitu 11.

4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
   Jawaban: Algoritma bekerja secara bertahap (greedy) sebagai berikut:
   - Inisialisasi: Jarak ke Bogor diatur 0, sedangkan kota lainnya (Depok, Jakarta, Bandung) diatur tak terhingga (inf). Bogor dimasukkan ke priority_queue.
   - Langkah 1: Bogor dikeluarkan dari antrean. Algoritma memeriksa tetangga Bogor, yaitu Jakarta (jarak 5) dan Depok (jarak 2). Karena keduanya lebih kecil dari inf, nilai jarak Jakarta dan Depok diperbarui dan dimasukkan ke antrean.
   - Langkah 2: Depok dikeluarkan karena memiliki jarak terkecil (2). Dari Depok, algoritma memeriksa tetangganya:
     * Ke Jakarta: akumulasi jarak menjadi 2 + 2 = 4. Nilai ini lebih kecil dari jarak Jakarta sebelumnya (5), maka jarak Jakarta diperbarui menjadi 4.
     * Ke Bandung: akumulasi jarak menjadi 2 + 6 = 8. Nilai ini diperbarui dari inf menjadi 8.
   - Langkah 3: Jakarta dikeluarkan dari antrean dengan jarak barunya (4). Tetangga Jakarta adalah Bandung. Akumulasi jarak ke Bandung lewat Jakarta menjadi 4 + 7 = 11. Karena 11 lebih besar dari jarak Bandung saat ini (8), nilai Bandung TIDAK diperbarui (tetap 8).
   - Langkah 4: Bandung dikeluarkan dari antrean, dan karena Bandung tidak memiliki tetangga keluar, proses selesai. Hasil akhir rute terpendek: Bogor=0, Depok=2, Jakarta=4, Bandung=8.
"""