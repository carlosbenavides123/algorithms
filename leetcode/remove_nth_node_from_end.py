class ListNode():
	def __init__(self, x, Next=None):
		self.val = x
		self.Next = Next
        
ll = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

n = input()

def solve(ll, num):
    fast = slow = ll
    
    while num:
        num -= 1
        fast = fast.Next

    while fast.Next:
        slow = slow.Next
        fast = fast.Next
    slow.Next = slow.Next.Next
    while ll:
        print(slow.val)
        ll = ll.Next
    return slow

print(solve(ll, n))