# create a hash table


class Node():
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None


class HashTable():
    def __init__(self):
        self.N = 7
        self.table = [0] * 7

    def add_to_table(self, key, val):
        index = self.hash(key)
        if not self.table[index]:
            self.table[index] = Node(key, val)
        else:
            prev = self.table[index]
            curr = self.table[index].next
            while curr:
                curr = curr.next
                prev = prev.next
            prev.next = Node(key, val)

    def get(self, key):
        index = self.hash(key)
        if not self.table[index]:
            return -1
        curr = self.table[index]
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1

    def hash(self, key):
        index = 0
        for letter in key:
            index += ord(letter)
        return index % self.N


myTable = HashTable()

myTable.add_to_table("lol", 32)
myTable.add_to_table("lmao", 123)
myTable.add_to_table("table", 90)

print(myTable.get("XD"))  # -1
print(myTable.get("lol"))  # 32
print(myTable.get("LOOOOOL"))  # 1
print(myTable.get("lmao"))  # 123
