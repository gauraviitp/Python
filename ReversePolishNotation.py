import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

class Stack(list):
    def top(self):
        if len(self) == 0:
            return None
        return self[len(self) - 1]

def rpn(expr):
    stack = Stack()
    resexpr = ''
    for c in expr:
        if c == '(' or c == '^':
            stack.append(c)
        elif c >= 'a' and c <= 'z':
            resexpr += c
        elif c == '+' or c == '-':
            top = stack.top()
            while not stack == [] and (top == '^' or top == '/' or top == '*'):
                top = stack.pop()
                resexpr += top
                top = stack.top()
            stack.append(c)
        elif c == '/' or c == '*':
            top = stack.top()
            while not stack == [] and (top == '^'):
                top = stack.pop()
                resexpr += top
                top = stack.top()
            stack.append(c)
        elif c == ')':
            top = stack.top()
            while not stack == [] and (top != '('):
                top = stack.pop()
                resexpr += top
                top = stack.top()
            stack.pop()
    while not stack == []:
        resexpr += stack.pop()
    return resexpr

def main():
    t = int(f.readline())
    for i in range(t):
        expr = f.readline()
        print(rpn(expr))

if __name__ == "__main__":
    main()
