#-------------------------------------------------------------------------------------
# Nama  : Yasri Azmi Bishara
# NIM   : J0403251062
# Kelas : TPL A1
# Latihan Praktikum 2: Buat kode Implementasikan Pencarian pada mode tertentu Single
#------------------------------------------------------------------------------------

#-------------------------------------------------------
# Circular Singly Linked List
#-------------------------------------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Tambahkan pointer tail

    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:  # Jika linked list kosong
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head # Circular link ke dirinya sendiri
        else:
            self.tail.next = new_node # Sambungkan tail ke node baru
            self.tail = new_node # Update tail ke node baru
            self.tail.next = self.head # Circular link kembali ke head
            
    def search(self, key):
        if not self.head:
            return False
        
        temp = self.head
        
        while True:
            if temp.data == key:
                return True
            temp = temp.next
            if temp == self.head:
                break
        
        return False

    def display(self):
        if not self.head:
            print("Link is empty")
            return

        print("Circular Linked List Traversal:")
        temp = self.head

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break

        print("...(back to head)")


# Contoh penggunaan
cll = CircularSinglyLinkedList()
cll.insert_at_end(3)
cll.insert_at_end(5)
cll.insert_at_end(13)
cll.insert_at_end(2)

cll.display()

#---------------------------------------------------------------------------------------
# Latihan Praktikum 2: Buat kode Implementasikan Pencarian pada mode tertentu Single
#---------------------------------------------------------------------------------------
user_input = input("Masukkan elemen ke dalam Circular Linked List: ").strip()

cll = CircularSinglyLinkedList()

if user_input:
    elements = [int(x.strip()) for x in user_input.split(",")]
    
    for el in elements:
        cll.insert_at_end(el)

search_value = int(input("Masukkan elemen yang ingin dicari: "))
if not cll.head:
    print("Circular Linked List kosong. Tidak ada elemen yang bisa dicari.")
else:
    found = cll.search(search_value)
    
    if found:
        print(f"Elemen {search_value} ditemukan dalam Circular Linked List.")
    else:
        print(f"Elemen {search_value} tidak ditemukan dalam Circular Linked List.")