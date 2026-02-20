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

# Stack ada operasi push (memasukkan head baru) dan pop (menghapus head)
class stack:
    def __init__(self):
        self.top = None # stop menunjuk ke node paling atas (awalnya kosong)
    
    def push(self, data): # memasukkan data baru pada stack
        #1 membuat Node baru
        nodeBaru = Node(data) # instantiasi/memanggil kontruktor pada class Node
        
        #2 node baru menunjuk ke top yang lama (head lama)
        nodeBaru.next = self.top
        
        #3 geser node top pindah ke node baru
        self.top = nodeBaru
        
    def is_empty(self):
        return self.top is None # Stack kosong jika top = none
    
    def pop(self): #mengambil/menghapus node paling atas (top/head)
        if self.is_empty():
            print("Stack kosong, tidak bisa pop")
            return None
        data_terhapus = self.top.data #soroti bagian top dan simpan di variasi (peek)
        self.top = self.top.next #geser top ke node berikutnya
        return data_terhapus
    
    def peek(self):
        #melihat data yang paling atas tanpa menghapus
        if self.is_empty:
            return None
        return self.top.data
        
    def tampilkan(self):
        # Top -> A -> B
        current = self.top
        print("Top" , end="->")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None")
        
# Instantiasi Class Stack
s = stack()
s.push("A")
s.push("B")
s.push("C")
print("Current top :", s.peek())
s.pop()
s.tampilkan()
s.pop()
s.tampilkan()
s.pop()
s.tampilkan()
print("Final top :", s.peek())