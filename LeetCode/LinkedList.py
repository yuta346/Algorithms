
class node:
    def __init__(self, data=None): 
        self.data = data  # Assign data 
        self.next = None  # Initialize next as null

class linkedList:
    def __init__(self):
        self.head = node()

    def append(self, data): #append data at the end of list
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur= cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total+=1
            cur = cur.next
        return total 
    
    def display(self):
        li = []
        cur_pos = self.head
        while cur_pos.next != None:
            cur_pos = cur_pos.next
            li.append(cur_pos.data)
        print(li)

    def get_item(self, index):
        if index >= self.length():
            print("index out of range")
            return None
        cur_index = 0
        cur_pos = self.head
        while True:
            cur_pos = cur_pos.next
            if cur_index == index:
                return cur_pos.data
            cur_index+=1



list1 = linkedList()
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)
list1.display()
print(list1.get_item(2))
