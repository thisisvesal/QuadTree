import csv
from PIL import Image
import math

def csv_to_image(csv_file, output_image):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        pixels = next(reader)
        colors = next(reader)
        
        # Convert color data to integers
        colors = [int(color) for color in colors]
        # colors = [tuple(map(int, color.split(','))) for color in colors]
        
        # Determine the image size
        total_pixels = len(colors)
        width = int(math.sqrt(total_pixels))
        height = width
        
        # Create a new image in grayscale mode
        image = Image.new('RGB', (width, height))
        image.putdata(colors)
        
        # Save the image
        image.save(output_image)

# Example usage
csv_to_image('Dataset/image4_RGB.csv', 'output_image.png')