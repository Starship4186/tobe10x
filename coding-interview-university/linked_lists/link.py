class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, tmp):
        # Appends a new node with the given data to the end of the linked list
        # Create a new node
        # tmp = Node(data=data)
        # Check if list is empty
        if self.head == None:
            self.head = tmp
        else:
        # if the list is not empty
        # Go to the end and append the new node
        # to the linked list
            next_item = self.head
            while next_item.next != None:
                next_item = next_item.next
            next_item.next = tmp

    def prepend(self, tmp):
        # NEXT new node is floating in memory
        # since this is new node, set next node
        # to the earlier new node
        tmp.next = self.head
        # NEXT assign the head of LinkedList to
        # this new node
        self.head = tmp

    def delete(self, data):
        # TASK find where the data is
        # NEXT Do nothing if there is no data
        # NEXT If data is found, point the earlier node next to next node
        # EXAMPLE 1 -> 2 -> 3, if we want to delete 2, 1 should point to 3 first
        # Then we delete the node with data 2
        # Since we can not go back, we have to keep record of previous node as well

        next_node = self.head
        prev_node = self.head

        while next_node.data != data:
            next_node = next_node.next
            prev_node = next_node

            if next_node.next == None:
                return False
        
        # data node can be at first, middle or last
        if next_node == self.head:
            # first node and if only node
            self.head = next_node.next if next_node.next is not None else None
            del next_node
        elif next_node.next == None:
            # last node
            prev_node.next = None
            del next_node
        else:
            # middle node
            prev_node.next = next_node.next
            del next_node
        return True
        
        
    def display(self):
       tmp = self.head
       if self.head is not None:
            while True:
                print(tmp.data, sep=" ", end=" ")
                tmp = tmp.next

                if tmp == None:
                    return 
                
                
       else:
            print("Empty list")

linkedlist = LinkedList()
tmp = Node(data=2)
linkedlist.append(tmp)
tmp = Node(data=3)
linkedlist.append(tmp)
linkedlist.delete(3)
linkedlist.display()
