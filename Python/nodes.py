'''
It contains nodes, and sample program to understand functioning of Linked List.
It contain Single Linked List and double Linked List.

Code taken from https://stackabuse.com/python-linked-lists/

'''

# creating class for the node
class ListNode:

    # constructor to initiate this object
    def __init__(self, data):
        self.data = data    # store data
        self.next = None    # store reference ( next item)
        return
    
    # method to compare the value with the node data
    def has_value(self, value):
        if self.data == value:
            return True
        else:
            return False


# Creating class for linked list
class SingleLinkedList:

    # constructor to initiate this object
    def __init__(self):
        self.head = None    # head of the linked list   
        self .tail = None   # tail of the linked list
        return

    # method to add an item at the end of the list
    def add_list_item(self, item):
        # check if item is a node, if not than makes it a node
        if not isinstance(item, ListNode):
            item = ListNode(item)
        
        # check if it is first element
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
        return

    # method to returns the number of list items
    def list_length(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            # increase counter by one
            count +=1
            # jump to the linked node
            current_node = current_node.next
        return count

    # method to print linked list from the head
    def output_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next    # jump to the linked node
        return

    # search the linked list for the node that has this value 
    def unordered_search(self, value):
        current_node = self.head    # define the current node
        node_id = 1                 # define position
        results= []                 # define list of results

        while current_node is not None:
            if current_node.has_value(value):
                results.append(node_id)
            current_node = current_node.next
            node_id +=1
        return results




if __name__ == '__main__':

    node1 = ListNode(15)
    node2 = ListNode(8.5)
    node3 = ListNode('Berlin')
    node4 = ListNode(15)

    track = SingleLinkedList()
    # print('track length - %i' % track.list_length())

    for current_item in [node1, node2, node3, node4]:
        track.add_list_item(current_item)
        # print('track length - %i' % track.list_length())
        # track.output_list()

    print(track.unordered_search(15))


            