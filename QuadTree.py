from typing import List
from Utils import *

class QuadTree:
    def __init__(self, image: List[List[int]], row=0, col=0) -> None:
        self.image = image
        self.len = len(image)
        self.row = row
        self.col = col
        if self.isUniform():
            self.topLeft = None
            self.topRight = None
            self.bottomLeft = None
            self.bottomRight = None
            return

        self.topLeft = QuadTree([row[:self.len//2] for row in image[:self.len//2]], row, col)
        self.topRight = QuadTree([row[self.len//2:] for row in image[:self.len//2]], row, col + self.len//2)
        self.bottomLeft = QuadTree([row[:self.len//2] for row in image[self.len//2:]], row + self.len//2, col)
        self.bottomRight = QuadTree([row[self.len//2:] for row in image[self.len//2:]], row + self.len//2, col + self.len//2)


    def isUniform(self) -> bool:
        if not self.image:
            return True
        
        source = self.image[0][0]

        for row in self.image:
            for pix in row:
                if pix != source:
                    return False
            
        return True
    
    def isLeaf(self) -> bool:
        return self.topLeft == None and self.topRight == None and self.bottomLeft == None and self.bottomRight == None

    def treeDepth(self) -> int:
        if self.isLeaf():
            return 1
        
        return max(self.topLeft.treeDepth(), self.topRight.treeDepth(), self.bottomLeft.treeDepth(), self.bottomRight.treeDepth()) + 1

    def pixelDepth(self, px: int, py: int) -> int:
        if not self.image:
            return 0
        if self.isLeaf():
            return 1

        half_len = self.len // 2
        if px < half_len and py < half_len:
            return self.topLeft.pixelDepth(px, py) + 1
        elif px >= half_len and py < half_len:
            return self.topRight.pixelDepth(px - half_len, py) + 1
        elif px < half_len and py >= half_len:
            return self.bottomLeft.pixelDepth(px, py - half_len) + 1
        elif px >= half_len and py >= half_len:
            return self.bottomRight.pixelDepth(px - half_len, py - half_len) + 1

        return 0

    def searchSubspaceWithRange(self, x1, y1, x2, y2):
        if get_image_type(self.image) == 'L':
            ans = [[255 for _ in range(self.len)] for _ in range(self.len)]
        else:
            ans = [[(255, 255, 255) for _ in range(self.len)] for _ in range(self.len)]

        def mark(tree):
            if not tree:
                return
            if tree.isLeaf() and tree.overlapsWith(x1, y1, x2, y2):
                for i in range(tree.len):
                    for j in range(tree.len):
                        ans[tree.row + i][tree.col + j] = tree.image[0][0]
                return

            mark(tree.topLeft)
            mark(tree.topRight)
            mark(tree.bottomLeft)
            mark(tree.bottomRight)

        mark(self)

        return QuadTree(ans)

    def mask(self, x1, y1, x2, y2):
        ans = [[pix for pix in row] for row in self.image]

        def mark(tree):
            if not tree:
                return
            if tree.isLeaf() and tree.overlapsWith(x1, y1, x2, y2):
                for i in range(tree.len):
                    for j in range(tree.len):
                        ans[tree.row + i][tree.col + j] = 255 if get_image_type(self.image) == 'L' else (255, 255, 255)
                return
            
            mark(tree.topLeft)
            mark(tree.topRight)
            mark(tree.bottomLeft)
            mark(tree.bottomRight)
        
        mark(self)

        return QuadTree(ans)

    def compress(self, newSize: int):
        part = self.len // newSize # the size of each subspace that will be represented by one pixel in the compressed image
        compressed_image = [[0 for _ in range(newSize)] for _ in range(newSize)]
        for i in range(newSize):
            for j in range(newSize):
                compressed_image[i][j] = avearge_of_image(self.image, part, i, j)

        compressedTree = QuadTree(compressed_image)

        return compressedTree
    
    def overlapsWith(self, x1, y1, x2, y2):

        x_in_range = False
        y_in_range = False

        if x1 < self.row + self.len and x2 >= self.row:
            x_in_range = True

        if y1 < self.col + self.len and y2 >= self.col:
            y_in_range = True

        return x_in_range and y_in_range
    


    
    # The following 3 methods are added just for the sake of the part in description that says:
    # "These methods should apply the changes to the main tree"
    # it's a bit ambiguous

    def searchSubspaceWithRange_SELF(self, x1, y1, x2, y2):
        self = self.searchSubspaceWithRange(x1, y1, x2, y2)
        return self
    
    def mask_SELF(self, x1, y1, x2, y2):
        self = self.mask(x1, y1, x2, y2)
        return self
    
    def compress_SELF(self, newSize: int):
        self = self.compress(newSize)
        return self
    
    