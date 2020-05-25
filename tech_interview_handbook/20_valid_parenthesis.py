#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Note that an empty string is also considered valid.

# use a stack, append all open
# if curr letter is open, append to stack
# else check if the stack has something, if it doesnt, return false
# otherwise attempt to find if the stack can rightfully close the paranethesis
# by making sure the corresponding open is related to the close 
# ... not { ) or [ ) 
# we want to see [ ] ( ) 
# lastly, we want to check if the stack if empty, if it is, then all is good
def solve(s):
    stk = []
    for letter in s:
        if letter in ['(', '[', '{']:
            stk.append(letter)
        else:
            if not stk:
                return False
            if letter == ')' and stk[-1] == '(':
                stk.pop()
            elif letter == ']' and stk[-1] == '[':
                stk.pop()
            elif letter == '}' and stk[-1] == '{':
                stk.pop()
            else:
                return False
    return len(stk) == 0

s = '(([]))'
print(solve(s))