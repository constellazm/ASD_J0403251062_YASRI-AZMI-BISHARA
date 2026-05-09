# =====================================================================
# Nama  : Yasri Azmi Bishara
# NIM   : J0403251062
# Kelas : A1
# =====================================================================

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