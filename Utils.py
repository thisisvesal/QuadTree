import csv
from PIL import Image
from math import sqrt

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

        return colors
    
def save(image, output_image: str, image_mode: str) -> None:
    # Determine the image size
    total_pixels = len(image)
    width = int(sqrt(total_pixels))
    height = width

    # Create a new image in grayscale mode
    img = Image.new(image_mode, (width, height))
    img.putdata(image)

    # Save the image
    img.save(output_image)


image = construct_image('Dataset/image1_gray.csv', 'L')
save(image, 'output_image.png', 'L')