''''
This file contains single lined list.

'''
# Node class
class node:

    # constructor to initiate the node object
    def __init__(self, data):
        self.data = data    # Assign data
        self.next = None    # Initialize next as Null


# Linked List class contains a node object
class single_link_list:

    # constructor to initiate the head
    def __init__(self):
        self.head = None

    # This function prints contents of linked list 
    # starting from head
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
# Code execution starts here
if __name__ == '__main__':

    # start with the empty list
    list = single_link_list()
    list.head = node(1)
    second = node(2)
    third = node(3)
    ''''
    Three nodes have been created.
    We have been configured to these three blocks as head,
    second and third.

    llist.head        second              third 
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  | None |     | 2  | None |     |  3 | None | 
    +----+------+     +----+------+     +----+------+ 
    '''
    list.head.next = second     # link first node with second
    '''
    Now next of first node refers to second. so they both are linked.

    llist.head        second              third 
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  |  o-------->| 2  | null |     |  3 | null | 
    +----+------+     +----+------+     +----+------+  
    '''
    second.next = third     # Link second node with the third
    '''
    Now next of second Node refers to third.  So all three 
    nodes are linked. 
  
    llist.head        second              third 
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  |  o-------->| 2  |  o-------->|  3 | null | 
    +----+------+     +----+------+     +----+------+   
    '''
    list.print_list()