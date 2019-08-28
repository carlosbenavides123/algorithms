# This problem was recently asked by Twitter:

# You are given an array of k sorted singly linked lists. Merge the linked lists into a single sorted linked list and return it.

# Here's your starting point:

import heapq


class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        c = self
        answer = ""
        while c:
            answer += str(c.val) if c.val else ""
            c = c.next
        return answer


def merge(lists):
    # tech leads solution (my didnt account for multiple lists K)

    # minheap
    # This reduces the time complexity to O(kn * logk),
    # since inserting into a heap is log(k), and we do this for each element.
    # The space complexity is O(K).

    # new_head = current = Node(-1)
    # heap = [(lst.val, i) for i, lst in enumerate(lists)]
    # heapq.heapify(heap)
    # print(heap)

    # while heap:
    #     current_min, i = heapq.heappop(heap)
    #     # Add next min to merged linked list.
    #     current.next = Node(current_min)
    #     current = current.next
    #     # Add next value to heap.
    #     if lists[i] is not None:
    #         lists[i] = lists[i].next
    #     if lists[i]:
    #         heapq.heappush(heap, (lists[i].val, i))
    # return new_head.next

    dummy = head = Node(0)
    while lists:
        if lists[0] == None:
            head.next = lists[1]
            break
        elif lists[1] == None:
            head.next = lists[0]
            break

        if lists[0].val < lists[1].val:
            head.next = Node(lists[0].val)
            lists[0] = lists[0].next
        else:
            head.next = Node(lists[1].val)
            lists[1] = lists[1].next
        head = head.next
    return dummy.next


a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))
print merge([a, b])
# 123456
