# Final Project: Image Processing with QuadTrees

## Overview

This project processes images in CSV format by converting them into QuadTrees. It provides various methods to manipulate and analyze these QuadTrees, including:

- Masking
- Searching subspaces
- Compressing
- Finding the depth of the tree
- Finding the depth of a particular pixel

## Getting Started

### Prerequisites

- Python 3.x
- Required Python libraries (listed in `requirements.txt`)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/thisisvesal/QuadTree.git
    ```
2. Navigate to the project directory:
    ```sh
    cd QuadTree
    ```
3. Install PIL:
    ```sh
    pip install pillow
    ```

### Usage

1. Place your flattened images in CSV format into the `Dataset` folder.
2. Write a main script similar to the samples provided in `Main.py`.
3. Run your script:
    ```sh
    python your_script.py
    ```

## Project Structure

- `Dataset/`: Folder containing the CSV files of flattened images.
- `Images/`: Folder where you can output your images to.
- `Main.py`: Sample scripts demonstrating how to use the project.
- `quadtree.py`: Module containing the QuadTree implementation and related methods.
- `Utils.py`: Utility functions for processing images and other tasks.

## Methods

### Masking

Apply a mask to the QuadTree to hide certain parts of the image.

### Searching Subspaces

Search for specific subspaces within the QuadTree to find regions of interest.
This is the exact opposite of masking.

### Compressing

A simple compression method that reduces the size and quality of an image.

### Finding Depth

Determine the depth of the entire QuadTree or the depth of a specific pixel within the tree.