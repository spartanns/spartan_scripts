#!/usr/bin/python

import cv2


def cartoonize_image(image_path, output_path):
    """
    Cartoonize an image and save the result.
    """
    try:
        # Read the image
        img = cv2.imread(image_path)

        if img is None:
            print("Error: Unable to read the image. Please check the file path.")
            return

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Apply median blur
        gray_blur = cv2.medianBlur(gray, 5)

        # Detect edges
        edges = cv2.adaptiveThreshold(
            gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9
        )

        # Apply bilateral filter for smoothing
        color = cv2.bilateralFilter(img, 9, 300, 300)

        # Combine edges and color
        cartoon = cv2.bitwise_and(color, color, mask=edges)

        # Save the cartoonized image
        cv2.imwrite(output_path, cartoon)
        print(f"Cartoonized image saved to: {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    print("Welcome to the Image Cartoonizer!")
    print("This tool transforms an image into a cartoon-style image.")
    print("-" * 50)

    image_path = input("Enter the path to the image: ").strip()
    output_path = input("Enter the output path (e.g., cartoon.jpg): ").strip()

    cartoonize_image(image_path, output_path)


main()
