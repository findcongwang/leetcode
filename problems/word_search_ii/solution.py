class Trie:
	def __init__(self):
		self.root = {}
		self.endSymbol = "*"

	def add(self, word):
		current = self.root
		for c in word:
			if c not in current:
				current[c] = {}
			current = current[c]
		current[self.endSymbol] = word

        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # tries are good for accessing multiple strings at once
        # put words in trie
        # dfs from each letter and check trie (pass in currentNode)
        # need to keep tracked in visited for each node
        n, m = len(board), len(board[0])
        visited = [[False] * m for _ in range(n)]
        trie = Trie()
        results = {}	# using a dict to pass by reference as opposed to a set
        for w in words:
            trie.add(w)

        for r in range(n):
            for c in range(m):
                self.DFS(r, c, trie.root, board, visited, results, words)
                if len(list(results.keys())) == len(words):
                    return list(results.keys())

        return list(results.keys())
	
	
    def DFS(self, i,j, trieNode, board, visited, results, words):
        if len(list(results.keys())) == len(words):
            return
        if visited[i][j]:
            return
        if board[i][j] not in trieNode:
            return

        visited[i][j] = True 
        if "*" in trieNode[board[i][j]]:
            results[trieNode[board[i][j]]["*"]] = True

        for r, c in self.getNeighbours(i, j, board):
            self.DFS(r, c, trieNode[board[i][j]], board, visited, results, words)
        visited[i][j] = False


    def getNeighbours(self, i, j, board):
        # return all 4 neighbour that are within bound
        n, m = len(board), len(board[0])
        return [
            (r,c)
            for r,c in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
            if r >= 0 and r < n and c >= 0 and c < m
        ]
