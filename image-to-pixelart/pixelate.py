from PIL import Image

def pixelate(input_file_path, pixel_size):
    image = Image.open(input_file_path)
    filename = image.filename.split('/')[-1]
    image = image.resize(
        (image.size[0] // pixel_size, image.size[1] // pixel_size),
        Image.NEAREST
    )
    image = image.resize(
        (image.size[0] * pixel_size, image.size[1] * pixel_size),
        Image.NEAREST
    )

    image.show()
    image.save('pixels/' + filename)

pixelate("sourceimages/einstein.jpg", 16)
