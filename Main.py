from Utils import *
from QuadTree import QuadTree

def main1():
    image = construct_image('Dataset/image1_gray.csv', 'L')
    qt = QuadTree(image)

    print(f"Tree depth: {qt.treeDepth()}")
    print(f"Pixel depth of 2, 2: {qt.pixelDepth(2, 2)}")

    save(qt.image, 'Images/1/image.png', 'L')
    save(qt.topLeft.image, 'Images/1/topleft.png', 'L')
    save(qt.topRight.image, 'Images/1/topright.png', 'L')
    save(qt.bottomLeft.image, 'Images/1/bottomleft.png', 'L')
    save(qt.bottomRight.image, 'Images/1/bottomright.png', 'L')

    searched = qt.searchSubspaceWithRange(2, 2, 20, 20).image
    save(searched, 'Images/1/searched.png', 'L')

    masked = qt.mask(2, 2, 20, 20).image
    save(masked, 'Images/1/masked.png', 'L')

    compressed = qt.compress(32).image
    save(compressed, 'Images/1/compressed.png', 'L')

def main2():
    image = construct_image('Dataset/image2_gray.csv', 'L')
    qt = QuadTree(image)

    print(f"Tree depth: {qt.treeDepth()}")
    print(f"Pixel depth of 2, 2: {qt.pixelDepth(2, 2)}")

    save(qt.image, 'Images/2/image.png', 'L')
    save(qt.topLeft.image, 'Images/2/topleft.png', 'L')
    save(qt.topRight.image, 'Images/2/topright.png', 'L')
    save(qt.bottomLeft.image, 'Images/2/bottomleft.png', 'L')
    save(qt.bottomRight.image, 'Images/2/bottomright.png', 'L')

    searched = qt.searchSubspaceWithRange(2, 2, 20, 20).image
    save(searched, 'Images/2/searched.png', 'L')

    masked = qt.mask(2, 2, 20, 20).image
    save(masked, 'Images/2/masked.png', 'L')

    compressed = qt.compress(32).image
    save(compressed, 'Images/2/compressed.png', 'L')

def main3():
    image = construct_image('Dataset/image3_gray.csv', 'L')
    qt = QuadTree(image)

    print(f"Tree depth: {qt.treeDepth()}")
    print(f"Pixel depth of 2, 2: {qt.pixelDepth(2, 2)}")

    save(qt.image, 'Images/3/image.png', 'L')
    save(qt.topLeft.image, 'Images/3/topleft.png', 'L')
    save(qt.topRight.image, 'Images/3/topright.png', 'L')
    save(qt.bottomLeft.image, 'Images/3/bottomleft.png', 'L')
    save(qt.bottomRight.image, 'Images/3/bottomright.png', 'L')

    searched = qt.searchSubspaceWithRange(2, 2, 20, 20).image
    save(searched, 'Images/3/searched.png', 'L')

    masked = qt.mask(2, 2, 20, 20).image
    save(masked, 'Images/3/masked.png', 'L')

    compressed = qt.compress(32).image
    save(compressed, 'Images/3/compressed.png', 'L')

def main4():
    image = construct_image('Dataset/image4_RGB.csv', 'RGB')
    qt = QuadTree(image)

    print(f"Tree depth: {qt.treeDepth()}")
    print(f"Pixel depth of 2, 2: {qt.pixelDepth(2, 2)}")

    save(qt.image, 'Images/4/image.png', 'RGB')
    save(qt.topLeft.image, 'Images/4/topleft.png', 'RGB')
    save(qt.topRight.image, 'Images/4/topright.png', 'RGB')
    save(qt.bottomLeft.image, 'Images/4/bottomleft.png', 'RGB')
    save(qt.bottomRight.image, 'Images/4/bottomright.png', 'RGB')

    searched = qt.searchSubspaceWithRange(2, 2, 20, 20).image
    save(searched, 'Images/4/searched.png', 'RGB')

    masked = qt.mask(2, 2, 20, 20).image
    save(masked, 'Images/4/masked.png', 'RGB')

    compressed = qt.compress(32).image
    save(compressed, 'Images/4/compressed.png', 'RGB')

def T1():
    image = construct_image('Dataset/T1.csv', 'L')
    qt = QuadTree(image)

    print(f"Tree depth: {qt.treeDepth()}")
    print(f"Pixel depth of 2, 2: {qt.pixelDepth(2, 2)}")

    save(qt.image, 'Images/T1/image.png', 'L')
    save(qt.topLeft.image, 'Images/T1/topleft.png', 'L')
    save(qt.topRight.image, 'Images/T1/topright.png', 'L')
    save(qt.bottomLeft.image, 'Images/T1/bottomleft.png', 'L')
    save(qt.bottomRight.image, 'Images/T1/bottomright.png', 'L')

    searched = qt.searchSubspaceWithRange(2, 2, 20, 20).image
    save(searched, 'Images/T1/searched.png', 'L')

    masked = qt.mask(2, 2, 20, 20).image
    save(masked, 'Images/T1/masked.png', 'L')

    compressed = qt.compress(32).image
    save(compressed, 'Images/T1/compressed.png', 'L')

def T2():
    image = construct_image('Dataset/T2.csv', 'L')
    qt = QuadTree(image)

    print(f"Tree depth: {qt.treeDepth()}")
    print(f"Pixel depth of 2, 2: {qt.pixelDepth(2, 2)}")

    save(qt.image, 'Images/T2/image.png', 'L')
    save(qt.topLeft.image, 'Images/T2/topleft.png', 'L')
    save(qt.topRight.image, 'Images/T2/topright.png', 'L')
    save(qt.bottomLeft.image, 'Images/T2/bottomleft.png', 'L')
    save(qt.bottomRight.image, 'Images/T2/bottomright.png', 'L')

    searched = qt.searchSubspaceWithRange(2, 2, 20, 20).image
    save(searched, 'Images/T2/searched.png', 'L')

    masked = qt.mask(2, 2, 20, 20).image
    save(masked, 'Images/T2/masked.png', 'L')

    compressed = qt.compress(32).image
    save(compressed, 'Images/T2/compressed.png', 'L') 

def main_custom():
    image = [[1, 1, 2, 2, 0, 0, 0, 0], 
             [1, 1, 2, 2, 0, 0, 0, 0], 
             [3, 4, 7, 8, 0, 0, 0, 0], 
             [5, 6, 9, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]]
    qt = QuadTree(image)

    print("Searched:")
    searched = qt.searchSubspaceWithRange(1, 1, 2, 2).image
    for row in searched:
        print(row)

    print("Masked:")
    masked = qt.mask(1, 1, 2, 2).image
    for row in masked:
        print(row)

    print("Compressed:")
    compressed = qt.compress(2).image
    for row in compressed:
        print(row)

def __main__():
    print("Running main1")
    main1()
    print("")

    print("Running main2")
    main2()
    print("")

    print("Running main3")
    main3()
    print("")

    print("Running main4")
    main4()
    print("")

    print("Running T1")
    T1()

    print("Running T2")
    T2()

    print("Running main_custom")
    main_custom()


if __name__ == "__main__":
    __main__()