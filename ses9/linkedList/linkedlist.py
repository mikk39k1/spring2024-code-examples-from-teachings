from node import Node

class LinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length
    
    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return " -> ".join(values)

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node 
        self.length += 1

    def __getitem__(self, index):

        if index < 0 or index >= self.length:
            return IndexError("Index out of bounds")


        current_node = self.head
        current_index = 0

        while current_node is not None:
            if current_index == index:
                return current_node.data
            
            current_node = current_node.next
            current_index += 1

    def __setitem__(self, index, data):
        if index < 0 or index >= self.length:
            return IndexError("Index out of bounds")
        
        current_node = self.head
        current_index = 0

        while current_node is not None:
            if current_index == index:
                current_node.data = data
                return current_node.data
            current_node = current_node.next
            current_index += 1
                
            




l = LinkedList()
l.append("a")

print(l)

l.append("b")

print(l)

l.append("c")

print(l)

print(len(l))

print(l[0])

l[0] = "x"

print(l)

l[0] = "a"

print(l)
