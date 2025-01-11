#!/usr/bin/python

# pip install rembg
from rembg import remove
import cv2


def remove_background(image_path, output_path):
    """
    Remove the background from an image and save the result.
    """
    try:
        # Read the image
        img = cv2.imread(image_path)
        if img is None:
            print("Error: Unable to read the image.")
            return

        bg_removed = remove(img)  # Remove the background

        # Save the result
        cv2.imwrite(output_path, bg_removed)
        print(f"Background removed image saved to: {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    print("Welcome to the Background Removal Tool!")
    print("This tool removes the background from an image.")
    print("-" * 50)

    image_path = input("Enter the path to the image: ").strip()
    output_path = input("Enter the output path: ").strip()

    remove_background(image_path, output_path)


main()
