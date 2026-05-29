# =======================================================
# Nama  : Yasri Azmi Bishara
# NIM   : J0403251062
# Kelas : A/1
# Praktikum 13 - Graph III: Spanning Trees 
# =======================================================

import heapq

# 1. Representasi Weighted Graph untuk studi kasus Jaringan Jembatan/Kabel Jaringan Antar Gedung
gedung_graph = {
    'GedungA': {'GedungB': 4, 'GedungC': 2, 'GedungD': 5},
    'GedungB': {'GedungA': 4, 'GedungD': 3},
    'GedungC': {'GedungA': 2, 'GedungD': 1},
    'GedungD': {'GedungA': 5, 'GedungB': 3, 'GedungC': 1}
}

# 2. Implementasi Algoritma Prim untuk mencari biaya pemasangan kabel termurah
def prim_gedung(graph, start):
    visited = set([start])
    edges = []
    
    # Push edge awal dari start node
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))
        
    mst = []
    total_cost = 0
    
    while edges:
        weight, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_cost += weight
            
            # Scan tetangga dari gedung baru yang terhubung
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
                    
    return mst, total_cost

# Eksekusi pencarian MST jaringan kabel
mst_kabel, biaya_minimum = prim_gedung(gedung_graph, 'GedungA')

# 3. Menampilkan Output Edge yang Dipilih dan Total Biaya Minimum
print("Minimum Spanning Tree (Jaringan Kabel Kampus):")
for u, v, weight in mst_kabel:
    print(f"{u} --- {v} | Biaya: {weight}")
print("Total biaya minimum =", biaya_minimum)

# ==============================================================================
# JAWABAN ANALISIS:
# 1. Algoritma apa yang digunakan?
#    Jawab: Algoritma Prim (menggunakan priority queue/heap).
#
# 2. Edge mana saja yang dipilih?
#    Jawab: 
#    - GedungA ke GedungC (Biaya: 2)
#    - GedungC ke GedungD (Biaya: 1)
#    - GedungD ke GedungB (Biaya: 3)
#
# 3. Berapa total biaya minimum?
#    Jawab: Total biaya minimum = 6.
#
# 4. Mengapa MST cocok digunakan pada kasus ini?
#    Jawab: Karena tujuan dari kampus adalah menghubungkan seluruh gedung agar 
#    saling terintegrasi internet tanpa perkabelan ganda yang boros (mencegah cycle) 
#    dan menekan pengeluaran dana serendah mungkin (mengoptimasi total bobot minimum).
# ==============================================================================