from sys import stdin

class Grid:
    def __init__(self):
        self.matrix = []
        for line in stdin:
            if line == '' :
                break;
            self.matrix.append(line.strip("\n"))
        self.column_count = len(self.matrix[0])
        self.row_count = len(self.matrix)

    def is_there_a_tree(self, row, column):
        col = column % self.column_count
        if self.matrix[row][col] == "#":
            return True
        else:
            return False

    def __str__(self):
        result=""
        for line in self.matrix:
            result = result+line+"\n"
        return result

    def check_slope_for_trees(self, right, down):
        trees_count = 0
        c = 0
        for r in range(0, grid.row_count, down):
            if grid.is_there_a_tree(r,c):
                trees_count +=1
            c += right
        return trees_count

grid = Grid()
r1d1 = grid.check_slope_for_trees(1,1)
r3d1 = grid.check_slope_for_trees(3,1)
r5d1 = grid.check_slope_for_trees(5,1)
r7d1 = grid.check_slope_for_trees(7,1)
r1d2 = grid.check_slope_for_trees(1,2)

print("Number of trees in slop 3 right 1 down is ", r3d1)
print("product of tree counts in all slopes is ", r1d1 * r3d1 * r5d1 * r7d1 * r1d2)
