from Utils import *
from QuadTree import QuadTree

def __main__():
    image = construct_image('Dataset/image1_gray.csv', 'L')
    qt = QuadTree(image)

    print(qt.treeDepth())
    save(qt.image, 'Images/1/image.png', 'L')
    save(qt.topLeft.image, 'Images/1/topleft.png', 'L')
    save(qt.topRight.image, 'Images/1/topright.png', 'L')
    save(qt.bottomLeft.image, 'Images/1/bottomleft.png', 'L')
    save(qt.bottomRight.image, 'Images/1/bottomright.png', 'L')

    image_rgb = construct_image('Dataset/image4_RGB.csv', 'RGB')
    qt_rgb = QuadTree(image_rgb)

    print(qt_rgb.treeDepth())
    save(qt_rgb.image, 'Images/4/image.png', 'RGB')
    save(qt_rgb.topLeft.image, 'Images/4/topleft.png', 'RGB')
    save(qt_rgb.topRight.image, 'Images/4/topright.png', 'RGB')
    save(qt_rgb.bottomLeft.image, 'Images/4/bottomleft.png', 'RGB')
    save(qt_rgb.bottomRight.image, 'Images/4/bottomright.png', 'RGB')

    compressed = qt_rgb.compress(32).image
    save(compressed, 'Images/4/compressed.png', 'RGB')

if __name__ == "__main__":
    __main__()

    