from Utils import *
from QuadTree import QuadTree

def __main__():
    image = construct_image('Dataset/image1_gray.csv', 'L')
    qt = QuadTree(image)

    print(qt.treeDepth())

if __name__ == "__main__":
    __main__()

    