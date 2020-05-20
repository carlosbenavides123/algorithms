# This problem was asked by Google.

# Suppose we represent our file system by a string in the following manner:

# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

# dir
    # subdir1
    # subdir2
        # file.ext
# The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

# The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

# dir
    # subdir1
        # file1.ext
        # subsubdir1
    # subdir2
        # subsubdir2
            # file2.ext
# The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

# We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

# Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.

# Note:

# The name of a file contains at least a period and an extension.

# The name of a directory or sub-directory will not contain a period.

path = input()
# seperate by \n
# count howmany tabs are there
# -> dir 3 letters
# hmap[-1] = 0
# hmap[0] = hmap[-1 + amount('\t') ] + len("dir")

# \tsubdir1
# 1 \t 
# hmap[1-1] = "dir"
# hmap[1] = hmap[1-1] + len(subdir1)
# so we have dirsubdir1

# \t\t 
# 2 \t
# we see a .ext
# potential res = dirsubdir1file1.ext
# hmap[2-1] = dirsubdir1
# hmap[2] = hmap[1] + len(file1.ext)
# res if contains current string contains dot

def longest_abs_path(path):
	hmap = {}
	hmap[-1] = 0
	res = 0
	for sub_path in path.split('\n'):
		num_tabs = sub_path.count('\t')
		hmap[num_tabs] = hmap[num_tabs - 1] + len(sub_path) - num_tabs
		if "." in sub_path:
			res = max(res, hmap[num_tabs])
	return res
print(longest_abs_path(path))