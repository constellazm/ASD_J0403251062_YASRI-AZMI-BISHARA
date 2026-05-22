# =======================================================
# Nama  : Yasri Azmi Bishara
# NIM   : J0403251062
# Kelas : A/1
# Praktikum 12 - Graph II: Shortest Path
# =======================================================

# ==========================================================
# Latihan 2: Implementasi Dijkstra
# ==========================================================
import heapq  # Mengimpor library priority queue (Min-Heap) untuk mengambil jarak terkecil secara efisien

# Representasi Graf Berbobot menggunakan struktur data Dictionary di dalam Dictionary
graph = {
    'A': {'B': 4, 'C': 2},  # Node A terhubung ke B (bobot 4) dan C (bobot 2)
    'B': {'D': 5},          # Node B terhubung ke D (bobot 5)
    'C': {'D': 1},          # Node C terhubung ke D (bobot 1)
    'D': {}                 # Node D tidak memiliki jalur keluar
}

def dijkstra(graph, start):
    # Inisialisasi: Atur semua jarak node ke 'inf' (tak terhingga) di awal
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # Jarak dari node asal ke dirinya sendiri diatur menjadi 0

    # Membuat antrean prioritas (priority queue) dan memasukkan node awal (bobot, nama_node)
    priority_queue = [(0, start)]

    # Perulangan berjalan selama masih ada node yang tersisa di dalam antrean
    while priority_queue:
        # Mengambil node dengan akumulasi jarak paling kecil/terdekat dari antrean
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak yang diambil lebih besar dari jarak yang sudah tercatat, abaikan proses ini
        if current_distance > distances[current_node]:
            continue

        # Memeriksa semua node tetangga (neighbor) beserta bobotnya (weight) dari node yang aktif
        for neighbor, weight in graph[current_node].items():
            # Hitung akumulasi total jarak baru menuju node tetangga tersebut
            distance = current_distance + weight

            # Proses Relaksasi: Periksa apakah jalur baru ini lebih pendek dari rute sebelumnya
            if distance < distances[neighbor]:
                distances[neighbor] = distance  # Perbarui catatan jarak terpendek ke node tetangga
                heapq.heappush(priority_queue, (distance, neighbor))  # Masukkan tetangga ke antrean untuk dieksplorasi lanjut

    return distances  # Mengembalikan kamus/dictionary berisi hasil akhir jarak terpendek ke semua node

# Menjalankan fungsi Dijkstra dengan menentukan node 'A' sebagai titik awal perjalanan
hasil = dijkstra(graph, 'A')

# Mencetak hasil akhir perhitungan jarak terpendek ke terminal
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)  # Menampilkan pasangan nama node beserta total nilai jaraknya

"""
Jawaban Analisis:
1. Berapa jarak terpendek dari A ke B?
   Jawaban: Jarak terpendek dari A ke B adalah 4.

2. Berapa jarak terpendek dari A ke C?
   Jawaban: Jarak terpendek dari A ke C adalah 2.

3. Berapa jarak terpendek dari A ke D?
   Jawaban: Jarak terpendek dari A ke D adalah 3.

4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B?
   Jawaban: Karena akumulasi bobot pada jalur lewat C jauh lebih ringan. 
   Jika lewat B (A -> B -> D), total bobotnya adalah 4 + 5 = 9. 
   Sedangkan jika lewat C (A -> C -> D), total bobotnya hanya 2 + 1 = 3.

5. Apa fungsi priority_queue dalam algoritma Dijkstra?
   Jawaban: Fungsi priority_queue (antrean prioritas) adalah untuk memastikan bahwa 
   node yang memiliki jarak akumulasi terkecil/terdekat selalu diproses terlebih dahulu 
   (menggunakan prinsip Min-Heap). Hal ini membuat algoritma menjadi serakah (greedy) 
   dan sangat efisien karena kita tidak perlu memeriksa seluruh node secara acak.

6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?
   Jawaban: Karena Dijkstra mengadopsi prinsip "Greedy" yang mengasumsikan bahwa 
   sekali sebuah node dikunjungi dan jalurnya diperbarui, jarak ke node tersebut 
   sudah final dan tidak akan bisa menjadi lebih kecil lagi. Jika ada bobot negatif, 
   asumsi ini rusak; jalur berputar yang awalnya terlihat lebih jauh bisa saja 
   menjadi lebih pendek di akhir karena pengurangan bobot negatif tersebut. 
   Dijkstra tidak bisa mendeteksi perubahan ini dan berpotensi terjebak dalam 
   perhitungan yang salah atau loop tak terbatas. Untuk bobot negatif, algoritma 
   yang tepat adalah Bellman-Ford.
"""