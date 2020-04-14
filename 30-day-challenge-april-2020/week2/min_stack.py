"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.

    Example:

    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin();   --> Returns -3.
    minStack.pop();
    minStack.top();      --> Returns  0.
    minStack.getMin();   --> Returns -2.
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.node = []
        
    def push(self, x: int) -> None:
        self.node.append(x)

    def pop(self) -> None:
        return self.node.pop() if len(self.node) > 0 else None

    def top(self) -> int:
        return self.node[-1]

    def getMin(self) -> int:
        return min(self.node)
