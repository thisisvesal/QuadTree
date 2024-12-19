from Utils import *
from QuadTree import QuadTree

def __main__():
    image = construct_image('Dataset/image1_gray.csv', 'L')
    qt = QuadTree(image)

    print(qt.treeDepth())
    save(qt.image, 'image.png', 'L')
    save(qt.topLeft.image, 'topleft.png', 'L')
    save(qt.topRight.image, 'topright.png', 'L')
    save(qt.bottomLeft.image, 'bottomleft.png', 'L')
    save(qt.bottomRight.image, 'bottomright.png', 'L')

if __name__ == "__main__":
    __main__()

    