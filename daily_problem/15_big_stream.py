# This problem was asked by Facebook.

# Given a stream of elements too large to store in memory,
# pick a random element from the stream with uniform probability.


def randomE(big_stream):
    res = None
    import random
    for i, v in enumerate(big_stream):
        if random.randint(1, i+1) == 1:
            res = v
    return res
