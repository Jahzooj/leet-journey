class Solution:
    def isValid(self, l: List[str]) -> bool:
        only_nums = [x for x in l if x != "."]
        return len(only_nums) == len(set(only_nums))

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [x for x in range(len(board))]
        for r in rows:
            row = board[r]
            if self.isValid(row):
                pass
            else:
                return False

        for c in range(len(board[0])):
            col = [board[x][c] for x in rows]
            if self.isValid(col):
                pass
            else:
                return False

        for box in range(9):
            r1 = board[0 + 3 * (box // 3)][0 + 3 * (box % 3):3 + 3 * (box % 3)]
            r2 = board[1 + 3 * (box // 3)][0 + 3 * (box % 3):3 + 3 * (box % 3)]
            r3 = board[2 + 3 * (box // 3)][0 + 3 * (box % 3):3 + 3 * (box % 3)]
            r1.extend(r2)
            r1.extend(r3)

            if self.isValid(r1):
                pass
            else:
                return False

        return True