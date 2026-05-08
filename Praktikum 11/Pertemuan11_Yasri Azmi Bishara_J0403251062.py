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



# Praktikum 2 -  Membuat Adjacency List
# Representasi menggunakan dictionary
adj_list = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

# Tampilkan Adjacency List
print("Adjacency List Representation:")
for node, neighbors in adj_list.items():
    print(f"{node}: {neighbors}")



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



# Praktikum 4 - Studi Kasus Dunia Nyata: Sosial Media
# 1. Adjacency List
list_media_sosial = {
    "Bayu": ["Udin", "Nisa"],
    "Udin": ["Bayu", "Ucup"],
    "Nisa": ["Nadia"],
    "Ucup": ["Bayu", "Nadia"],
    "Nadia": ["Bayu", "Nisa"]
}

# 2. Adjacency Matrix
users = ["Bayu", "Ucup", "Udin", "Nadia", "Nisa"]
V = 5

sosial_matrix = [[0 for _ in range(V)] for _ in range(V)]

edges = [
    (0,1), (0,2),
    (1,0), (1,3),
    (2,4),
    (3,0), (3,4),
    (4,0), (4,2)
]

for u, v in edges:
    sosial_matrix[u][v] = 1

# Menampilkan Adjacency List
print("Adjacency List:")
for user, hubungan in list_media_sosial.items():
    print(f"{user} -> {hubungan}")

# Menampilkan Adjacency Matrix
print("\nAdjacency Matrix:")

# Header kolom
print("      ", end="")
for user in users:
    print(f"{user:>6}", end="")
print()

# Isi matrix
for i in range(V):
    print(f"{users[i]:<6}", end="")
    for j in range(V):
        print(f"{sosial_matrix[i][j]:>6}", end="")
    print()
  
# Menampilkan Nama Node  
print("\nNama Node:")
for user in users:
    print(user)

# Menampilkan Hubungan Antar node
print("\nHubungan Antar Node:")
print("Bayu - Friend: Udin | Follow: Nisa")
print("Udin - Friend: Bayu | Follow: Ucup")
print("Nisa - Friend: Nadia")
print("Ucup - Follow: Bayu, Nadia")
print("Nadia - Friend: Nisa | Follow: Bayu")