#leetcode medium
# given a list of scheds, determine how many meeting rooms are required

def meeting_rooms(sched):
    import heapq
    if not sched:
        return 0
    sched = sorted(sched, key=lambda x:x[0])
    heap = []
    heapq.heappush(heap, sched[0][1])

    for curr_start, curr_end in sched[1:]:
        if heap[0] <= curr_start:
            heapq.heappop(heap)
            heapq.heappush(heap, curr_end)
        else:
            heapq.heappush(heap, curr_end)
    return len(heap)

print(meeting_rooms( [ [0, 30], [5, 10], [15, 20] ] ))
        