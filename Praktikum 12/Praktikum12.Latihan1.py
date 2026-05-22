# =======================================================
# Nama  : Yasri Azmi Bishara
# NIM   : J0403251062
# Kelas : A/1
# Praktikum 12 - Graph II: Shortest Path
# =======================================================

# ==========================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur
# ==========================================================
# Representasi Graf Berbobot menggunakan struktur data Dictionary
graph = {
    'A': {'B': 4, 'C': 2},  # Node A terhubung ke B (bobot 4) dan C (bobot 2)
    'B': {'D': 5},          # Node B terhubung ke D (bobot 5)
    'C': {'D': 1},          # Node C terhubung ke D (bobot 1)
    'D': {}                 # Node D tidak memiliki jalur keluar
}

# Menghitung total bobot Jalur 1 (A -> B -> D) secara manual dengan menjumlahkan bobot edge-nya
jalur_1 = graph['A']['B'] + graph['B']['D']

# Menghitung total bobot Jalur 2 (A -> C -> D) secara manual dengan menjumlahkan bobot edge-nya
jalur_2 = graph['A']['C'] + graph['C']['D']

# Mencetak total bobot hasil perhitungan Jalur 1 ke terminal
print("Jalur 1: A -> B -> D =", jalur_1)

# Mencetak total bobot hasil perhitungan Jalur 2 ke terminal
print("Jalur 2: A -> C -> D =", jalur_2)

# Melakukan perbandingan logis untuk menentukan jalur mana yang memiliki bobot lebih kecil (terpendek)
if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")  # Dicetak jika Jalur 1 lebih kecil
else:
    print("Jalur terpendek adalah A -> C -> D")  # Dicetak jika Jalur 2 lebih kecil (atau sama dengan Jalur 1)

"""
Jawaban Analisis:
1. Berapa total bobot jalur A -> B -> D?
    Jawaban: Total bobotnya adalah 9 (didapat dari 4 + 5).

2. Berapa total bobot jalur A -> C -> D?
    Jawaban: Total bobotnya adalah 3 (didapat dari 2 + 1).

3. Jalur mana yang dipilih sebagai jalur terpendek?
    Jawaban: Jalur yang dipilih adalah A -> C -> D.

4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?
    Jawaban: Karena pada graf berbobot (weighted graph), setiap edge memiliki nilai/beban 
    yang berbeda (seperti jarak, waktu, atau biaya). Jalur dengan jumlah edge sedikit bisa 
    saja memiliki bobot edge yang sangat besar (seperti A -> B -> D yang totalnya 9), 
    sedangkan jalur memutar dengan jumlah edge lebih banyak bisa jadi memiliki akumulasi 
    bobot yang jauh lebih kecil (seperti A -> C -> D yang totalnya hanya 3). Algoritma 
    shortest path seperti Dijkstra atau Bellman-Ford selalu fokus meminimalkan total bobot, 
    bukan meminimalkan jumlah langkah/edge.
"""