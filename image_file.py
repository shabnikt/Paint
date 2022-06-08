from PIL import Image, ImageTk
import os

PATH = os.path.dirname(__file__)


def load_image(image_name):
    location = os.path.join(PATH, 'icons', image_name)
    image = Image.open(location)
    image_size = (20, 20)
    image = image.resize(image_size, Image.ANTIALIAS)
    return ImageTk.PhotoImage(image)
