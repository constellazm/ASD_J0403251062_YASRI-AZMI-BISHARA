# =====================================================================
# Nama  : Yasri Azmi Bishara
# NIM   : J0403251062
# Kelas : A1
# =====================================================================

# Praktikum 3 - Konversi Matrix ke List
# Inisialisasi matrix
matrix = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0]
]

# Buat list kosong untuk hasil konversi matrix  
adj_list_converted = {}

# Proses konversi Adjacency Matrix ke Adjacency List
for i in range(len(matrix)):
    neighbors = []
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            neighbors.append(j)
    adj_list_converted[i] = neighbors

# Menampilkan hasil konversi Adjacency Matrix ke Adjacency List
print("Hasil Konversi Matrix ke List:")
for node, connections in adj_list_converted.items():
    print(f"{node}: {connections}")