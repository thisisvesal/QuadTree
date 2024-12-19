from typing import List

class QuadTree:
    def __init__(self, image: List[int]):
        self.image = image
        self.len = len(image)
        if self.isUniform():
            self.topLeft = None
            self.topRight = None
            self.bottomLeft = None
            self.bottomRight = None
            return

        self.topLeft = QuadTree(self.image[:self.len//4])
        self.topRight = QuadTree(self.image[self.len//4 : self.len//2])
        self.bottomLeft = QuadTree(self.image[self.len//2 : self.len*3//4])
        self.bottomRight = QuadTree(self.image[self.len*3//4:])

    def isUniform(self) -> bool:
        if not self.image:
            return True
        
        source = self.image[0]

        for pix in self.image:
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