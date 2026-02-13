#------------------------------------------------------------------------------------------
# Nama  : Yasri Azmi Bishara
# NIM   : J0403251062
# Kelas : TPL A1
# Latihan Praktikum 4: Buat metode untuk menggabungkan dua Single Linked List menjadi satu
#------------------------------------------------------------------------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def display(self, label=""):
        if label:
            print(label, end=" ")

        if not self.head:
            print("kosong")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("null")

    # Pakai metode merge untuk menggabungkan dua Single Linked List
    def merge(self, other_list):
        merged = LinkedList() # Membuat Linked List baru untuk hasil gabungan

        temp = self.head # Mulai dari head list pertama
        while temp:
            merged.insert_at_end(temp.data)
            temp = temp.next

        temp = other_list.head # Mulai dari head list kedua
        while temp:
            merged.insert_at_end(temp.data)
            temp = temp.next

        return merged


#-----------------------------------------
# Program Utama
#-----------------------------------------

input1 = input("Masukkan elemen untuk Linked List 1: ").strip()
input2 = input("Masukkan elemen untuk Linked List 2: ").strip()

ll1 = LinkedList()
ll2 = LinkedList()

# Isi linked list 1
if input1:
    elements1 = [int(x.strip()) for x in input1.split(",")]
    for el in elements1:
        ll1.insert_at_end(el)

# Isi linked list 2
if input2:
    elements2 = [int(x.strip()) for x in input2.split(",")]
    for el in elements2:
        ll2.insert_at_end(el)

# Menampilkan angka dari list yang akan digabungkan
ll1.display("Linked List 1:")
ll2.display("Linked List 2:")

# Menampilkan hasil Linked List setelah digabungkan
merged = ll1.merge(ll2)
merged.display("Linked List setelah digabungkan:")