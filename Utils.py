import csv
from PIL import Image
from math import sqrt
from typing import List

def construct_image(csv_file: str, image_mode: str): # output is either a 2d list of integers or a 2d list of int tuples
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        pixels = next(reader)
        colors = next(reader)

        # Convert color data to integers
        if image_mode == "L":
            colors = [int(color) for color in colors]
        elif image_mode == "RGB":
            colors = [tuple(map(int, color.split(','))) for color in colors]
        else:
            raise ValueError("Invalid image mode")
        
        # Determine the image size
        total_pixels = len(colors)
        width = int(sqrt(total_pixels))
        height = width
        
        image = [[colors[col] for col in range(width * row, width * (row + 1))] for row in range(height)]

        return image
    
def save(image, output_image: str, image_mode: str) -> None:
    # Determine the image size
    total_pixels = len(image) * len(image[0])
    width = int(sqrt(total_pixels))
    height = width

    # Create a new image in grayscale mode
    img = Image.new(image_mode, (width, height))
    flat = flatten(image)
    img.putdata(flat)

    # Save the image
    img.save(output_image)

def flatten(image: List[List[int]]) -> List[int]:
    flat = []
    for row in image:
        for pix in row:
            flat.append(pix)
    return flat

def avearge_of_image(image: List[List[int]], size, row, col) -> int:
    if get_image_type(image) == 'L': # grayscale
        sum = 0
        for i in range(size):
            for j in range(size):
                sum += image[row * size + i][col * size + j]
        return sum // (size * size)
    
    else: # RGB
        sum_0, sum_1, sum_2 = 0, 0, 0
        for i in range(size):
            for j in range(size):
                sum_0 += image[row * size + i][col * size + j][0]
                sum_1 += image[row * size + i][col * size + j][1]
                sum_2 += image[row * size + i][col * size + j][2]

        avg_0 = sum_0 // (size * size)
        avg_1 = sum_1 // (size * size)
        avg_2 = sum_2 // (size * size)

        return (avg_0, avg_1, avg_2)

def get_image_type(image: List[List]):
    if isinstance(image[0][0], int):
        return 'L'
    elif isinstance(image[0][0], tuple):
        return 'RGB'
    else:
        raise ValueError("Invalid image type")