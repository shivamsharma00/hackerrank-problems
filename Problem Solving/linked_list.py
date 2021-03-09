class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class solution:
    def display(self, head):
        current = head
        while current:
            print("Current data is - "+str(current.data))
            print("Current Head is - "+str(current.next))
            current = current.next
    
    def insert(self, head, data):

        if head is None:
            return Node(data)
            self.tail = head
        # elif head.next is None:
            # head.next = Node(data)
        else:
            node = Node(data)
            self.tail.next = node
            self.tail = node
            
            # insert(head.next, data)
            # noder.next = noder.data 
        return head



myList = solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = myList.insert(head, data)
myList.display(head)


    
     