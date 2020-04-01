# title

# Input: ["flower","flow","flight"]
# Output: "fl"

array = input()

def solve(array):
    res = ""
    index = 0
    found_common_letter = True
    while found_common_letter:
        letter = ""
        for string in array[1:]:
            if len(string) == index:
                found_common_letter = False
                break
            if letter == "":
                letter = string[index]
            if string[index] != letter:
                found_common_letter = False
                break
        if found_common_letter:
            res += letter
        index += 1
    return res
print(solve(array))