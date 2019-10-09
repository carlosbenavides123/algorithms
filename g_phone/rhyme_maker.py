# Example 1:

# Input: n = 1 (possible chars are A)
# Output: [A]
# Example 2:

# Input: n = 2 (possible chars are A, B)
# Output: [AA, AB]
# Explanation:
# AA
# AB
# BA <- This is not possible as it collide with AB. How?
# Look at the pattern AB says first line has different rhyme and second line has different rhyme then first line.
# Similarly BA is also shows the same: first line has different rhyme and second line has different rhyme then first line. Hence discard.
# Example 3:

# Input: n = 3 (possible chars are A, B, C)
# Output: [AAA, AAB, ABA, ABB, ABC]
# Explanation: We can't have AAC as it collides with AAB (first two are same and last is different in both).
# Similarly other BCA/BAC etc we'll discard them because of collide and lexicographical ordering.


def rhyme(n):
    if n == 1:
        return ['A']

    v = []

    p = rhyme(n-1)
    for lt in p:
        chked = set()
        for i in range(len(lt)):
            c = lt[i]
            if not c in chked:
                v.append(lt + c)
                chked.add(c)
        nxt = set(lt)
        nxt = list(nxt)
        nxt = sorted(nxt)
        nxt = chr(ord(nxt[-1]) + 1)
        v.append(lt + nxt)
    print(v)
    return v


print(rhyme(3))
