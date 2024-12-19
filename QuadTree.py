from typing import List

class QuadTree:
    def __init__(self, image):
        # Build the quadTree recursively
        ...

    def treeDepth(self) -> int:
        ...

    def pixelDepth(self, px, py) -> int:
        ...

    def searchSubSpaceWithRange(self, x1, y1, x2, y2) -> None:
        ...
 
    def compress(self, newSize) -> List[List[int]]:
        ...

    def mask(self, x1, y1, x2, y2) -> List[List[int]]:
        ...