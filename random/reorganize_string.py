from collections import Counter


def reorganizeString(S):
    counts = Counter(S)
    maxc = 0

    for k, v in counts.items():
        if v > maxc:
            maxc = v
            maxs = k

    if maxc > (len(S)+1)//2:
        return ''

    out = [maxs]*maxc
    print(out)
    count = 0
    for kk in counts:
        print(kk)
        if maxs != kk:
            for i in range(counts[kk]):
                out[count % maxc] += kk
                count += 1
        print(out)
    return ''.join(out)


S = "aabcbb"
print(reorganizeString(S))
