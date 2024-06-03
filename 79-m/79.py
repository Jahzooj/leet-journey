class Solution:
    def get_nbors(self, index, board):
        nbors = []
        # left
        if index[1] > 0:
            nbors.append((index[0], index[1] - 1))
        # right
        if index[1] < len(board[0]) - 1:
            nbors.append((index[0], index[1] + 1))
        # up
        if index[0] > 0:
            nbors.append((index[0] - 1, index[1]))
        # down
        if index[0] < len(board) - 1:
            nbors.append((index[0] + 1, index[1]))
        return nbors

    def exist(self, board: List[List[str]], word: str) -> bool:
        start = word[0]
        target = word[-1]

        starts = []
        targets = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == start:
                    starts.append([(i,j), [(i,j)]])
                if board[i][j] == target:
                    targets.append([(i,j), [(i,j)]])
        if len(starts)==0 or len(targets)==0:
            return False 

        q = starts if len(starts) <= len(targets) else targets
        if len(targets) < len(starts):
            word = word[::-1]

        while q:
            curr = q.pop()
            current_node = curr[0]
            path = curr[1]

            if (''.join([board[x[0]][x[1]] for x in path])) == word:
                return True

            nbors = self.get_nbors(current_node, board)
            for n in nbors:
                if n not in path:
                    if board[n[0]][n[1]] == word[len(path)]:
                        q.append([n, path + [n]]) 

        return False

        