from typing import List

class QuadTree:
    def __init__(self, image: List[List[int]]) -> None:
        self.image = image
        self.len = len(image)
        if self.isUniform():
            self.topLeft = None
            self.topRight = None
            self.bottomLeft = None
            self.bottomRight = None
            return

        self.topLeft = QuadTree([row[:self.len//2] for row in image[:self.len//2]])
        self.topRight = QuadTree([row[self.len//2:] for row in image[:self.len//2]])
        self.bottomLeft = QuadTree([row[:self.len//2] for row in image[self.len//2:]])
        self.bottomRight = QuadTree([row[self.len//2:] for row in image[self.len//2:]])

    def isUniform(self) -> bool:
        if not self.image:
            return True
        
        source = self.image[0][0]

        for row in self.image:
            for pix in row:
                if pix != source:
                    return False
            
        return True

    def treeDepth(self) -> int:
        if self.isUniform():
            return 1
        
        return max(self.topLeft.treeDepth(), self.topRight.treeDepth(), self.bottomLeft.treeDepth(), self.bottomRight.treeDepth()) + 1

    def pixelDepth(self, px, py) -> int:
        ...

    def searchSubspaceWithRange(self, x1, y1, x2, y2) -> None:
        ...
 
    def compress(self, newSize) -> List[List[int]]:
        ...

    def mask(self, x1, y1, x2, y2) -> List[List[int]]:
        ...