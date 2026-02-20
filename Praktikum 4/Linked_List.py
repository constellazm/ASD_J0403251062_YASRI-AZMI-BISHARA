#=================================================================
# Nama  : Yasri Azmi Bishara
# NIM   : J0403251062
# Kelas : TPL A1
# Praktikum 4
#=================================================================

#=================================================================
# Implementasi Dasar : Node pada Linked List
#=================================================================

class Node:
    # konstruktor adalah fungsi yang dijalankan secara otomatis ketika class Node dipanggil / diinstantiasi
    def __init__(self,data):
        self.data = data # menyimpan nilai atau data dalam list
        self.next = None # pointer ini menunjuk ke note berikutnya (awal = None)
    
# 1) Membuat node dengan instantiasi class node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
    
# 2) Mendefinisikan head dan menghubungkan Node : A -> B -> C -> None
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

# 4) Traversal : Menelusuri node dari head sampai ke None
current = head
while current is not None:
    print(current.data) #menampilkan data pada node saat ini
    current = current.next #pindah ke node berikutnya
    
#=================================================================
# Implementasi Dasar : Stack
#=================================================================