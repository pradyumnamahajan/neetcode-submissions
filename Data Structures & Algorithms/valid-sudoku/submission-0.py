class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_validation = [[0]*9 for _ in range(9)]
        col_validation = [[0]*9 for _ in range(9)]
        grid_validation = [ [ [0]*9 for _ in range(3)] for _ in range(3)]
        # print(grid_validation)

        for row in range(9):
            for col in range(9):
                number_str = board[row][col]
                if number_str == ".":
                    continue
                number = int(number_str) - 1
                # print(f"checking {number=} at {row=}, {col=}")

                if row_validation[row][number] == 1:
                    return False
                else:
                    # print(f"setting {number=} at {row=}, {col=} for row_val")
                    row_validation[row][number] = 1

                if col_validation[col][number] == 1:
                    return False
                else:
                    # print(f"setting {number=} at {row=}, {col=} for col_val")
                    col_validation[col][number] = 1

                if grid_validation[row//3][col//3][number] == 1:
                    return False
                else:
                    # print(f"setting {number=} at {row//3}, {col//3} for grid_val")
                    grid_validation[row//3][col//3][number] = 1
        
            # print(row_validation)
            # print(col_validation)
            # print(grid_validation)
        return True