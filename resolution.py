from PIL import Image


class JPEG:
    def __init__(self):
        self.read()
        super().__init__()

    def read(self):
        photo = Image.open("download.jpg")
        print("Resoltuion of Image in width x height =", photo.size)


JPEG()
