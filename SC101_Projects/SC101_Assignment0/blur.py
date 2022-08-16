"""
File: blur.py
Name:
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: original image
    :return: blurred image
    """
    new_img = SimpleImage.blank(img.width, img.height)  # Make an new blank image as big as original one.
    for x in range(img.width):
        for y in range(img.height):
            red_sum = 0
            green_sum = 0
            blue_sum = 0
            count = 0
            for i in range(-1, 2, 1):  # Get each pixel around the central one.
                for j in range(-1, 2, 1):
                    pixel_x = x + i
                    pixel_y = y + j
                    if 0 <= pixel_x < img.width:  # Each x and y should start with 0 and can't bigger than original.
                        if 0 <= pixel_y < img.height:
                            pixel = img.get_pixel(pixel_x, pixel_y)
                            red_sum += pixel.red  # Add the RGB number around the central one.
                            green_sum += pixel.green
                            blue_sum += pixel.blue
                            count += 1
            pixel_new = new_img.get_pixel(x, y)
            pixel_new.red = red_sum / count
            pixel_new.green = green_sum / count
            pixel_new.blue = blue_sum / count
    return new_img


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
