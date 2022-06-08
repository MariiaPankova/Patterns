from abc import ABC, abstractmethod
from PIL import Image


class DisplayObject(ABC):
    @abstractmethod
    def display(self):
        pass


class ImageFile(DisplayObject):
    def __init__(self, path):
        self.image = self.load(path)

    def display(self):
        print("Displaying image.")
        self.image.show()

    def load(self, image_path):
        print("Loading image.")
        image = Image.open(image_path)
        return image
