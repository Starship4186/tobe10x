

class Stack:
    def __init__(self):
        # Initialize the stack
        self.stack = []

    def pop(self):
        return self.stack.pop() if len(self.stack) > 0 else None

    def push(self,data):
        self.stack.append(data)

    def is_empty(self):
        return True if len(self.stack) == 0 else False
    

# Matching bracket problem
stack = Stack()
problem1 = "(((([[[{{{}}}]]]))))"
problem2 = "{()}[]()][]"
problem3 = "((("

for ch in problem3:
    if ch == "(" or ch == "[" or ch == "{":
        stack.push(ch)
    else:
        if ch == "}" and stack.pop() == "{":
            continue
        elif ch == "]" and stack.pop() == "[":
            continue
        elif ch == ")" and stack.pop() == "(":
            continue
        else:
            print("Not balanced")
            exit()

if stack.is_empty():
    print("balanced")
else:
    print("Not balanced")