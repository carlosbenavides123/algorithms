#leetcode easy

# given a list of meeting schedules, return true if u can attend all meetings

def meeting_rooms(sched):
    if not sched:
        return True
    sched = sorted(sched, key=lambda x:x[0])

    end = sched[0][1]

    for curr_start, curr_end in sched[1:]:
        if end > curr_start:
            return False
        end = max(end, curr_end)
    return True

print(meeting_rooms([[0, 30], [5, 10], [15, 20]]))
#False