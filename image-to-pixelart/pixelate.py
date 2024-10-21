from PIL import Image, ImageSequence, ImageDraw
import os

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

    image = image.resize((16, 16), Image.ADAPTIVE) 
    
    image.show()
    image.save('pixels/' + filename)
    image_to_hex(image)

def image_to_hex(image):
    image = image.convert('RGB')

    # Get image size (in this case, it should be 16x16)
    width, height = image.size

    # Iterate through each pixel and print its hex color code
    for y in range(height):
        for x in range(width):
            # Get the RGB values of the pixel
            r, g, b = image.getpixel((x, y))
            
            # Convert the RGB values to a hex code
            hex_color = f'#{r:02x}{g:02x}{b:02x}'
            
            print(f'{hex_color} ', end='')
        print()
        
        
def process_gif(input_file_path, pixel_size):
    image = Image.open(input_file_path)
    filename = os.path.basename(input_file_path).split('.')[0]
    frame_number = 0

    # Create directory to save frames if not exists
    if not os.path.exists(f'pixels/{filename}'):
        os.makedirs(f'pixels/{filename}')

    frames = [] 
    # Loop through each frame of the GIF
    for frame in ImageSequence.Iterator(image):
        frame = pixelate_image(frame.copy(), pixel_size)

        # Save each frame as a separate image
        frame_filename = f'pixels/{filename}/frame_{frame_number:03d}.png'
        frame.save(frame_filename)

        print(f"Hex values for frame {frame_number}:")
        image_to_hex(frame)
        print()  # Blank line between frames

        frame_number += 1

def pixelate_image(image, pixel_size):
    image = image.resize(
        (image.size[0] // pixel_size, image.size[1] // pixel_size),
        Image.NEAREST
    )
    image = image.resize(
        (image.size[0] * pixel_size, image.size[1] * pixel_size),
        Image.NEAREST
    )
    image = image.resize((16, 16), Image.ADAPTIVE)
    return image

# pixelate("sourceimages/FB_IMG_1680672611781.jpg", 16)
process_gif("sourcegifs/cat.gif", 16)