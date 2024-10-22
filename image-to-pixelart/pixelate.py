from PIL import Image, ImageSequence
import os

def pixelate(input_file_path, pixel_size):
    image = Image.open(input_file_path)
    filename = os.path.basename(input_file_path).split('.')[0]  # Get filename without extension
    image = image.resize(
        (image.size[0] // pixel_size, image.size[1] // pixel_size),
        Image.NEAREST
    )
    image = image.resize(
        (image.size[0] * pixel_size, image.size[1] * pixel_size),
        Image.NEAREST
    )
    
    # Resize to 16x16 while preserving the aspect ratio
    image = image.resize((16, 16), Image.ADAPTIVE) 
    
    image.show()  # Display the pixelated image
    
    # Convert to BGR444 format and print hex values
    image_to_hex(image)

    # Create output directory if it doesn't exist
    output_dir = 'C:\\Users\\Shaikh\\Desktop\\neopixel-matrix\\image-to-pixelart\\pixels'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Specify the full path with filename and extension
    output_path = os.path.join(output_dir, f'{filename}_pixelated.bmp')
    image = image.convert('RGB')  # Ensure the image is in RGB format
    image.save(output_path, format='BMP')  # Save the pixelated image in BMP format
    print(f'Saved pixelated image to: {output_path}')

def image_to_hex(image):
    image = image.convert('RGB')
    width, height = image.size

    for y in range(height):
        for x in range(width):
            r, g, b = image.getpixel((x, y))
            # Combine the RGB values into one 12-bit value (4 bits each for R, G, B)
            hex_color = f'0x{(r // 16):01X}{(g // 16):01X}{(b // 16):01X}'
            print(f'{hex_color}, ', end='')
        print()

def image_to_rgb565(image):
    image = image.convert('RGB')
    width, height = image.size
    hex_values = []

    for y in range(height):
        row = []
        for x in range(width):
            r, g, b = image.getpixel((x, y))
            # Convert RGB values to 5/6/5 format
            rgb565 = ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)
            hex_color = f'0x{rgb565 & 0xFFFF:04X}'  # Use 4 digits for hex
            row.append(hex_color)

        hex_values.append(', '.join(row))
    
    # Print hex values line by line
    for line in hex_values:
        print(line)

def image_to_bgr444(image):
    image = image.convert('RGB')
    width, height = image.size
    hex_values = []

    for y in range(height):
        row = []
        for x in range(width):
            r, g, b = image.getpixel((x, y))
            # Convert RGB values to 4/4/4 BGR format
            bgr444 = ((b & 0xF0) << 8) | ((g & 0xF0) << 4) | (r & 0xF0)
            hex_color = f'0x{bgr444 & 0xFFF:03X}'  # Convert to hex and keep 3 digits
            row.append(hex_color)

        hex_values.append(', '.join(row))
    
    # Print hex values line by line
    for line in hex_values:
        print(line)

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

# Example usage
pixelate("C:\\Users\\Shaikh\\Desktop\\neopixel-matrix\\image-to-pixelart\\sourcegifs\\nyancat\\frame_0_delay-0.07s.png", 16)
# process_gif("sourcegifs/cat.gif", 16)
