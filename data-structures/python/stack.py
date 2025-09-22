"""
Stack Implementation in Python

A stack is a linear data structure that follows the Last In First Out (LIFO) principle.
Elements are added and removed from the same end, called the top of the stack.

Time Complexity:
- Push: O(1)
- Pop: O(1)
- Peek/Top: O(1)
- Search: O(n)

Space Complexity: O(n)
"""

class Stack:
    """Stack implementation using Python list."""
    
    def __init__(self):
        self._items = []
    
    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._items)
    
    def __str__(self):
        """String representation of the stack."""
        if self.is_empty():
            return "Stack: []"
        return f"Stack: {self._items} (top -> {self.peek()})"
    
    def is_empty(self):
        """Check if the stack is empty. O(1)"""
        return len(self._items) == 0
    
    def push(self, item):
        """Add an item to the top of the stack. O(1)"""
        self._items.append(item)
    
    def pop(self):
        """Remove and return the top item from the stack. O(1)"""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()
    
    def peek(self):
        """Return the top item without removing it. O(1)"""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]
    
    def top(self):
        """Alias for peek(). O(1)"""
        return self.peek()
    
    def size(self):
        """Return the number of elements in the stack. O(1)"""
        return len(self._items)
    
    def clear(self):
        """Remove all elements from the stack. O(1)"""
        self._items.clear()
    
    def to_list(self):
        """Return a copy of the stack as a list (bottom to top). O(n)"""
        return self._items.copy()


class StackWithLinkedList:
    """Stack implementation using linked list for comparison."""
    
    class _Node:
        def __init__(self, data, next_node=None):
            self.data = data
            self.next = next_node
    
    def __init__(self):
        self._top = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def __str__(self):
        if self.is_empty():
            return "Stack: []"
        
        items = []
        current = self._top
        while current:
            items.append(current.data)
            current = current.next
        
        return f"Stack: {items[::-1]} (top -> {self.peek()})"
    
    def is_empty(self):
        """Check if the stack is empty. O(1)"""
        return self._top is None
    
    def push(self, item):
        """Add an item to the top of the stack. O(1)"""
        new_node = self._Node(item, self._top)
        self._top = new_node
        self._size += 1
    
    def pop(self):
        """Remove and return the top item from the stack. O(1)"""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        
        data = self._top.data
        self._top = self._top.next
        self._size -= 1
        return data
    
    def peek(self):
        """Return the top item without removing it. O(1)"""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._top.data
    
    def size(self):
        """Return the number of elements in the stack. O(1)"""
        return self._size


# Practical applications of stacks
def is_balanced_parentheses(expression):
    """
    Check if parentheses in an expression are balanced.
    Example: "({[]})" -> True, "({[})" -> False
    """
    stack = Stack()
    opening = {'(', '[', '{'}
    closing = {')', ']', '}'}
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in expression:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty():
                return False
            
            last_opening = stack.pop()
            if pairs[last_opening] != char:
                return False
    
    return stack.is_empty()


def evaluate_postfix(expression):
    """
    Evaluate a postfix expression.
    Example: "2 3 + 4 *" -> 20
    """
    stack = Stack()
    operators = {'+', '-', '*', '/'}
    
    tokens = expression.split()
    
    for token in tokens:
        if token in operators:
            if len(stack) < 2:
                raise ValueError("Invalid postfix expression")
            
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                if b == 0:
                    raise ValueError("Division by zero")
                result = a / b
            
            stack.push(result)
        else:
            try:
                stack.push(float(token))
            except ValueError:
                raise ValueError(f"Invalid token: {token}")
    
    if len(stack) != 1:
        raise ValueError("Invalid postfix expression")
    
    return stack.pop()


def infix_to_postfix(expression):
    """
    Convert infix expression to postfix notation.
    Example: "2 + 3 * 4" -> "2 3 4 * +"
    """
    stack = Stack()
    result = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    
    tokens = expression.split()
    
    for token in tokens:
        if token.replace('.', '').isdigit():  # Number
            result.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while not stack.is_empty() and stack.peek() != '(':
                result.append(stack.pop())
            stack.pop()  # Remove '('
        elif token in precedence:
            while (not stack.is_empty() and 
                   stack.peek() != '(' and
                   stack.peek() in precedence and
                   precedence[stack.peek()] >= precedence[token]):
                result.append(stack.pop())
            stack.push(token)
    
    while not stack.is_empty():
        result.append(stack.pop())
    
    return ' '.join(result)


# Example usage and demonstration
if __name__ == "__main__":
    print("=== Stack Demo ===")
    
    # Basic stack operations
    stack = Stack()
    print(f"Empty stack: {stack}")
    print(f"Is empty: {stack.is_empty()}")
    
    # Push elements
    for i in range(1, 6):
        stack.push(i)
        print(f"Pushed {i}: {stack}")
    
    # Peek at top
    print(f"Top element: {stack.peek()}")
    print(f"Stack size: {len(stack)}")
    
    # Pop elements
    while not stack.is_empty():
        popped = stack.pop()
        print(f"Popped {popped}: {stack}")
    
    print("\n=== Stack with Linked List ===")
    ll_stack = StackWithLinkedList()
    for i in [10, 20, 30]:
        ll_stack.push(i)
        print(f"Pushed {i}: {ll_stack}")
    
    print("\n=== Practical Applications ===")
    
    # Balanced parentheses
    test_expressions = [
        "({[]})",
        "({[})",
        "((()))",
        "()[]{}",
        "([)]"
    ]
    
    for expr in test_expressions:
        balanced = is_balanced_parentheses(expr)
        print(f"'{expr}' is balanced: {balanced}")
    
    # Postfix evaluation
    postfix_expressions = [
        "2 3 +",
        "2 3 + 4 *",
        "15 7 1 1 + - / 3 * 2 1 1 + + -"
    ]
    
    print("\nPostfix evaluation:")
    for expr in postfix_expressions:
        try:
            result = evaluate_postfix(expr)
            print(f"'{expr}' = {result}")
        except Exception as e:
            print(f"'{expr}' -> Error: {e}")
    
    # Infix to postfix conversion
    infix_expressions = [
        "2 + 3",
        "2 + 3 * 4",
        "( 2 + 3 ) * 4",
        "2 * 3 + 4 * 5"
    ]
    
    print("\nInfix to postfix conversion:")
    for expr in infix_expressions:
        postfix = infix_to_postfix(expr)
        print(f"'{expr}' -> '{postfix}'")