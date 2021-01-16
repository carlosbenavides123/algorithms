# Given a list of strings/words, return a list/table of all the letters found 
# in multiple strings where it’s occurring most with other letter or letters.

# Example:

# Input: ["abef", "bcd", "bde", "cadf"]

# Output:
# [
#  a: {f} // f occurs 2 times with a
#  b: {d,e} // d and e occur 2 times with b
#  c: {d} // d occurs 2 times with c
#  d: {b,c} // b and c occur 2 times with d 
#  e: {b} // b occurs 2 times with e 
#  f: {a} // a occurs 1 time with f
# ]

def frequent_letter_pairings(words):
    import collections
    hash_map = collections.defaultdict(dict)
    for w in words:
        for i in range(len(w)):
            curr_letter = w[i]

            for j in range(i):
                other_letter = w[j]
                if other_letter not in hash_map[curr_letter]:
                    hash_map[curr_letter][other_letter] = 1
                else:
                    hash_map[curr_letter][other_letter] += 1

            for k in range(i + 1, len(w)):
                other_letter = w[k]
                if other_letter not in hash_map[curr_letter]:
                    hash_map[curr_letter][other_letter] = 1
                else:
                    hash_map[curr_letter][other_letter] += 1
    # for key in hash_map:
    #     print(key, hash_map[key])
    res = {}
    for key in hash_map:
        adj_list = sorted(hash_map[key].items(), key=lambda x:x[1])[::-1]
        max_val = None
        for k, v in adj_list:
            if max_val == None:
                max_val = v
                res[key] = set(k)
            elif v == max_val:
                res[key].add(k)
            else:
                break
    for key in res:
        print(key, res[key])

print(frequent_letter_pairings(["abef", "bcd", "bde", "cadf"]))

