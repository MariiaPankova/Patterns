from image_file import ImageFile, DisplayObject


class ImageProxy(DisplayObject):
    def __init__(self, path):
        self.path = path
        self.display_object = None

    def display(self):
        if self.display_object is None:
            self.display_object = ImageFile(self.path)
        self.display_object.display()
