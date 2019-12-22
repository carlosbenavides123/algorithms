# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Example:

# Input:
# [
#     1 -> 4 -> 5,
#     1 -> 3 -> 4,
#     2 -> 6
# ]
# Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6


# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        import heapq
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heap.append([lists[i].val, i])
        heapq.heapify(heap)
        res = dummy = ListNode(0)
        while heap:
            val, curr_list = heapq.heappop(heap)
            res.next = ListNode(val)
            res = res.next
            if lists[curr_list].next == None:
                continue
            lists[curr_list] = lists[curr_list].next
            heapq.heappush(heap, [lists[curr_list].val, curr_list])
        return dummy.next
