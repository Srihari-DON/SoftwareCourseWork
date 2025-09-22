"""
Linked List Implementation in Python

A linked list is a linear data structure where elements are stored in nodes,
and each node contains data and a reference to the next node.

Time Complexity:
- Access: O(n)
- Search: O(n)
- Insertion: O(1) at head, O(n) at arbitrary position
- Deletion: O(1) at head, O(n) at arbitrary position

Space Complexity: O(n)
"""

class ListNode:
    """Node class for the linked list."""
    
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node
    
    def __str__(self):
        return str(self.data)


class LinkedList:
    """Singly linked list implementation."""
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __len__(self):
        """Return the length of the linked list."""
        return self.size
    
    def __str__(self):
        """String representation of the linked list."""
        if not self.head:
            return "[]"
        
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        
        return " -> ".join(result)
    
    def is_empty(self):
        """Check if the linked list is empty."""
        return self.head is None
    
    def prepend(self, data):
        """Add an element to the beginning of the list. O(1)"""
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def append(self, data):
        """Add an element to the end of the list. O(n)"""
        new_node = ListNode(data)
        
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
        self.size += 1
    
    def insert(self, index, data):
        """Insert an element at a specific index. O(n)"""
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        
        if index == 0:
            self.prepend(data)
            return
        
        new_node = ListNode(data)
        current = self.head
        
        for _ in range(index - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self.size += 1
    
    def delete(self, data):
        """Delete the first occurrence of data. O(n)"""
        if not self.head:
            raise ValueError("List is empty")
        
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                return
            current = current.next
        
        raise ValueError(f"Data {data} not found in list")
    
    def delete_at_index(self, index):
        """Delete element at a specific index. O(n)"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return
        
        current = self.head
        for _ in range(index - 1):
            current = current.next
        
        current.next = current.next.next
        self.size -= 1
    
    def find(self, data):
        """Find the index of the first occurrence of data. O(n)"""
        current = self.head
        index = 0
        
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        
        return -1
    
    def get(self, index):
        """Get element at a specific index. O(n)"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        
        current = self.head
        for _ in range(index):
            current = current.next
        
        return current.data
    
    def reverse(self):
        """Reverse the linked list. O(n)"""
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
    
    def to_list(self):
        """Convert linked list to Python list. O(n)"""
        result = []
        current = self.head
        
        while current:
            result.append(current.data)
            current = current.next
        
        return result


# Example usage and demonstration
if __name__ == "__main__":
    print("=== Linked List Demo ===")
    
    # Create a new linked list
    ll = LinkedList()
    print(f"Empty list: {ll}")
    print(f"Is empty: {ll.is_empty()}")
    
    # Add elements
    ll.append(1)
    ll.append(2)
    ll.append(3)
    print(f"After appending 1, 2, 3: {ll}")
    
    # Prepend element
    ll.prepend(0)
    print(f"After prepending 0: {ll}")
    
    # Insert at specific index
    ll.insert(2, 1.5)
    print(f"After inserting 1.5 at index 2: {ll}")
    
    # Access elements
    print(f"Element at index 0: {ll.get(0)}")
    print(f"Element at index 2: {ll.get(2)}")
    
    # Search for elements
    print(f"Index of element 2: {ll.find(2)}")
    print(f"Index of element 99: {ll.find(99)}")
    
    # Delete elements
    ll.delete(1.5)
    print(f"After deleting 1.5: {ll}")
    
    ll.delete_at_index(0)
    print(f"After deleting at index 0: {ll}")
    
    # List operations
    print(f"Length: {len(ll)}")
    print(f"As Python list: {ll.to_list()}")
    
    # Reverse the list
    ll.reverse()
    print(f"After reversing: {ll}")