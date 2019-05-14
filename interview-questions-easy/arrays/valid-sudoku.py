from typing import List

class Solution:
    def containsDuplicates(self, list):
        found = []
        for item in list:
            if item not in found:
                found.append(item)
            else:
                return True
        return False

    def validRows(self, board: List[List[str]]):
        for row in board:
            nums = [num for num in row if num != '.']
            if self.containsDuplicates(nums):
                return False
        return True

    def validColumns(self, board: List[List[str]]):
        for i in range(len(board)):
            col = []

            for row in board:
                if row[i] != '.':
                    col.append(row[i])

            if self.containsDuplicates(col):
                return False

        return True
                
    def validSubBoxes(self, board: List[List[str]]):
        boxes = []
        for j in range(0,9,3):
            for k in range(0,9,3):
                box = []
                for i in range(3):
                    box.append(board[j:j+3][i][k:k+3])
                    flatBox = [item for b in box for item in b]
                boxes.append(flatBox)

        for box in boxes:
            nums = [num for num in box if num != '.']
            if self.containsDuplicates(nums):
                return False

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.validSubBoxes(board) and self.validRows(board) and self.validColumns(board)