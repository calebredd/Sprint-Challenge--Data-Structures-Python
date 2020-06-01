class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # Check if current node is empty
        if self.head is None:
            return
        # Check if current node has a next node
        if(node.get_next() is None):
            # Establish current node as head when you reach the end
            self.head = node
            # Take previous node and switch sides with current node to complete the reverse sequencing
            node.set_next(prev)
            return
        # Prep for relational swap with next node
        next = node.get_next()
        # Flip previous node direction
        node.set_next(prev) 
        # Use recursion to continue with the cycle
        self.reverse_list(next, node)
