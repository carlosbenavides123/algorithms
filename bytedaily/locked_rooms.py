# This question is asked by Amazon.
# Given N distinct rooms that are locked we want to know if you can unlock and visit every room.
# Each room has a list of keys in it that allows you to unlock and visit other rooms.
# We start with room 0 being unlocked. Return whether or not we can visit every room.

# Ex: Given the following rooms…

# rooms = [[1], [2], []], return true
# Ex: Given the following rooms…

# rooms = [[1, 2], [2], [0], []], return false, we can’t enter room 3.
#dfs
def locked_rooms(rooms):
    num_rooms = len(rooms)
    opened_rooms = [0]
    dfs(rooms, opened_rooms, set(), 0)
    print(opened_rooms)
    return opened_rooms[0] == num_rooms

def dfs(rooms, opened_rooms, visited_rooms, curr_room):
    visited_rooms.add(curr_room)
    opened_rooms[0] += 1

    for locked_room_key in rooms[curr_room]:
        if locked_room_key not in visited_rooms:
            dfs(rooms, opened_rooms, visited_rooms, locked_room_key)
# stack
def locked_rooms(rooms):
    visited_rooms = [False] * len(rooms)
    stk = [0]
    while stk:
        room = stk.pop()
        if not visited_rooms[room]:
            visited_rooms[room] = True
            for key in rooms[room]:
                stk.append(key)

    for visited_room in visited_rooms:
        if not visited_room:
            return False
    return True

rooms = [[1], [2], []]
print(locked_rooms(rooms))
rooms = [[1, 2], [2], [0], []]
print(locked_rooms(rooms))
