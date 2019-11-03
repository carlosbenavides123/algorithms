# Given a string with a certain rule: k[string] should be expanded
# to string k times. So for example, 3[abc] should be expanded to
# abcabcabc. Nested expansions can happen, so 2[a2[b]c] should be
# expanded to abbcabbc.

# Your starting point:


def decodeString(s):
    return decode_helper(s)[0]


def decode_helper(s, idx=0):
    string = ""
    multiply_num = 1
    while idx < len(s):
        var = s[idx]
        if var.isdigit():
            multiply_num = int(var)
            while idx + 1 < len(s) and s[idx+1].isdigit():
                multiply_num = multiply_num * 10 + int(s[idx+1])
                idx += 1
        elif var == "[":
            temp_string, idx = decode_helper(s, idx + 1)
            temp_string = multiply_num * temp_string
            string += temp_string
        elif var == "]":
            return (string, idx)
        else:
            string += var
        idx += 1
    return (string, idx)


print decodeString('2[a2[b]c]')
