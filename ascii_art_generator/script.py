from PIL import Image

# ASCII characters used to represent pixel intensity
ASCII_CHARS = [" ", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


def resize_image(image, new_width=50):
    """Resize image while maintaining aspect ratio."""
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.55)
    return image.resize((new_width, new_height))


def grayify(image):
    """Convert image to grayscale."""
    return image.convert("L")


def pixels_to_ascii(image):
    """Convert pixels to ASCII characters."""
    pixels = image.getdata()
    ascii_str = "".join(ASCII_CHARS[pixel // 25] for pixel in pixels)
    return ascii_str


def image_to_ascii(image_path, new_width=50):
    """Convert an image file to ASCII art."""
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image: {e}")
        return

    image = resize_image(image, new_width)
    image = grayify(image)
    ascii_str = pixels_to_ascii(image)

    # Format the ASCII string into image dimensions
    pixel_count = len(ascii_str)
    ascii_image = "\n".join(
        ascii_str[i : i + new_width] for i in range(0, pixel_count, new_width)
    )

    return ascii_image


# Input: Path to image
image_path = input("Enter the path to an image: ")
ascii_art = image_to_ascii(image_path)

# Display the ASCII art
if ascii_art:
    print(ascii_art)
    with open("ascii_art.txt", "w") as f:
        f.write(ascii_art)
    print("\nASCII art saved to 'ascii_art.txt'")
