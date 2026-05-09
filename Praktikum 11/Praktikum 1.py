# =====================================================================
# Nama  : Yasri Azmi Bishara
# NIM   : J0403251062
# Kelas : A1
# =====================================================================

# Praktikum 1 - Membuat Adjacency Matrix
# Tentukan jumlah vertex (V)
V = 4

# List of edges
edges = [[0, 1], [0, 2], [1, 3], [2, 3]]

# Inisialisasi matrix dengan nol
matrix = [[0 for i in range(V)] for j in range(V)]

# Isi matrix berdasarkan edge (Undirected Graph)
for u, v in edges:
    matrix[u][v] = 1
    matrix[v][u] = 1 # Karena graph tidak berarah
    
# Tampilkan matrix
print("Adjacency Matrix:")
for row in matrix:
    print(row)