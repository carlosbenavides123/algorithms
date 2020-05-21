# This problem was asked by Microsoft.

# Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

class Trie():
	def __init__(self):
		self.root = {}
		self.search_node = {}

	def add_word(self, word):
		curr = self.root
		for letter in word:
			if letter not in curr:
				curr[letter] = {}
			curr = curr[letter]
		curr["*"] = word

	def search(self, letter):
		if letter not in self.search_node or "*" in self.search_node:
			self.search_node = self.root
		if letter in self.search_node:
			self.search_node = self.search_node[letter]
			if "*" in self.search_node:
				return self.search_node["*"]
		return ""

words = set(['bed', 'bath', 'bedbath', 'and', 'beyond'])
s = "bedbathandbeyond"
def sol(words, s):
	res = []
	trie = Trie()

	for word in words:
		trie.add_word(word)
	print(trie.root)
	for letter in s:
		print(letter)
		word = trie.search(letter)
		if word:
			res.append(word)
	return res
			
print(sol(words, s))
