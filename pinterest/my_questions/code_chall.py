import sys

# Prints to standard output.
def findStartAndEndLocations(pairs):
  # IMPLEMENTATION GOES HERE
  package_start_to_end = {}
  
  for pair in pairs:
    if pair[0] not in package_start_to_end:
      package_start_to_end[pair[0]] = [pair[1]]
    else:
      package_start_to_end[pair[0]] += [pair[1]]
  
  end_set = set([])
  for pair in pairs:
    end_set.add(pair[1])

  package_end_to_start = {}
  for package in package_start_to_end:
    for package_location in package_start_to_end[package]:
      if package_location not in package_end_to_start:
        package_end_to_start[package_location] = []
      package_end_to_start[package_location].append(package)
    
  res = {}
  for key in sorted(package_start_to_end.keys()):
    if key in package_start_to_end and key in package_end_to_start:
      continue
    if key in end_set:
      continue
    end_loc = findStartAndEndHelper(package_start_to_end, package_end_to_start, key)
    if not end_loc:
      continue
    end_loc = set(end_loc)
    end_loc = ' '.join(sorted(end_loc))
    print(key+": "+end_loc)

def findStartAndEndHelper(start_dic, end_dic, key):
  string = ""
  if key in start_dic:
    child = start_dic[key]
    for child_char in child:
      if child_char in end_dic:
        temp = findStartAndEndHelper(start_dic, end_dic, child_char)
        if temp:
          string += temp
  elif key not in start_dic and key in end_dic:
    return key
  return string
  

# DO NOT MODIFY BELOW THIS LINE
def main():
  pairs = []

  for line in sys.stdin:
    if len(line.strip()) == 0:
      continue

    line = line.rstrip()

    pairs.append(line.split(" "))

  findStartAndEndLocations(pairs)

main()
