from glob import glob
from proxy import ImageProxy


if __name__ == '__main__':
    images = [ImageProxy(path) for path in sorted(glob("images/image*.jpg"))]
    for image in images:
        image.display()
