# =======================================================
# Nama  : Yasri Azmi Bishara
# NIM   : J0403251062
# Kelas : A/1
# Praktikum 12 - Graph II: Shortest Path
# =======================================================

# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================
import heapq  # Mengimpor library priority queue (Min-Heap) untuk mengambil waktu tempuh terkecil secara efisien

# Representasi Peta Kampus Berbobot menggunakan struktur data Dictionary di dalam Dictionary
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},  # Dari Gerbang ke Perpustakaan (6 mnt) dan Kantin (2 mnt)
    'Perpustakaan': {'Lab': 3},                    # Dari Perpustakaan ke Lab (3 mnt)
    'Kantin': {'Lab': 4, 'Aula': 7},               # Dari Kantin ke Lab (4 mnt) dan Aula (7 mnt)
    'Lab': {'Aula': 1},                            # Dari Lab ke Aula (1 mnt)
    'Aula': {}                                     # Aula tidak memiliki jalur keluar selanjutnya
}

def dijkstra(graph, start):
    # Inisialisasi: Atur semua waktu tempuh lokasi ke 'inf' (tak terhingga) di awal
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # Waktu tempuh dari titik start (Gerbang) ke dirinya sendiri diatur menjadi 0

    # Membuat antrean prioritas (priority queue) dan memasukkan lokasi awal (waktu, nama_lokasi)
    priority_queue = [(0, start)]

    # Perulangan berjalan selama masih ada lokasi yang tersisa di dalam antrean
    while priority_queue:
        # Mengambil lokasi dengan akumulasi waktu paling cepat/kecil dari antrean
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika waktu yang diambil lebih besar dari waktu yang sudah tercatat, abaikan proses ini
        if current_distance > distances[current_node]:
            continue

        # Memeriksa semua lokasi tetangga (neighbor) beserta bobot waktunya (weight) dari lokasi aktif
        for neighbor, weight in graph[current_node].items():
            # Hitung akumulasi total waktu baru menuju lokasi tetangga tersebut
            distance = current_distance + weight

            # Proses Relaksasi: Periksa apakah rute baru ini lebih cepat dari rute sebelumnya
            if distance < distances[neighbor]:
                distances[neighbor] = distance  # Perbarui catatan waktu tercepat ke lokasi tetangga
                heapq.heappush(priority_queue, (distance, neighbor))  # Masukkan lokasi tetangga ke antrean untuk dieksplorasi lanjut

    return distances  # Mengembalikan kamus/dictionary berisi hasil akhir waktu tercepat ke semua lokasi

# Menjalankan fungsi Dijkstra dengan menentukan 'Gerbang' sebagai titik awal perjalanan kampus
hasil = dijkstra(graph, 'Gerbang')

# Mencetak hasil akhir perhitungan waktu tempuh terpendek ke terminal
print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")  # Menampilkan nama lokasi beserta total menitnya

"""
Jawaban Analisis:
1. Lokasi mana yang paling dekat dari Gerbang?
   Jawaban: Kantin, dengan waktu tempuh hanya 2 menit.

2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
   Jawaban: Waktu tempuh terpendeknya adalah 7 menit. 
   Rutenya adalah: Gerbang -> Kantin -> Lab -> Aula (2 + 4 + 1 = 7 menit).

3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
   Jawaban: Tidak selalu. Contoh nyatanya di kasus ini adalah perjalanan ke Aula. 
   Jika lewat jalur langsung Gerbang -> Kantin -> Aula, waktu tempuhnya adalah 9 menit (2 + 7). 
   Namun, jika kita mengambil jalur memutar Gerbang -> Kantin -> Lab -> Aula, waktunya 
   justru lebih singkat, yaitu 7 menit. Ini membuktikan bahwa jalur dengan pos pemberhentian 
   lebih banyak bisa memiliki bobot total yang lebih kecil.

4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini? 
   Jawaban: Karena representasi jarak atau waktu tempuh antar-fasilitas di dunia nyata 
   (seperti wilayah kampus) nilainya selalu positif (tidak ada jarak atau waktu yang bernilai minus). 
   Dijkstra sangat efisien dan akurat dalam mencari rute tercepat pada graf berbobot positif, 
   sehingga sangat ideal untuk melacak rute jalan kaki atau navigasi seperti ini.
"""