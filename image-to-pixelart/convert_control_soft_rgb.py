from PIL import Image, ImageSequence
import os
import csv

def read_hex_values_from_file(file_path):
    with open(file_path, 'r') as file:
        hex_values = file.read().replace('\n', '').strip().split(',')
        count = 0
        for i in range(0, len(hex_values) - 1, 3):
            print(rgb_to_hex(hex_values[i], hex_values[i + 1], hex_values[i + 2]), end=', ')
            count += 1
            if count % 16 == 0:
                print() 
        return hex_values
    
def rgb_to_hex(r, g, b):
    # Ensure the values are two digits
    r = r[2:].zfill(2)
    g = g[2:].zfill(2)
    b = b[2:].zfill(2)
    
    # Combine the values into a singular hex code
    # return f"0x{r}{g}{b}"
    return hex_to_bgr_444(f"{r}{g}{b}")

def hex_to_bgr_444(hex_code):
    # Convert the hex code to RGB
    r = int(hex_code[0:2], 16)
    g = int(hex_code[2:4], 16)
    b = int(hex_code[4:6], 16)
    
    # Convert to 4-bit per channel
    r_4 = (r * 15) // 255  # Scale to 0-15
    g_4 = (g * 15) // 255  # Scale to 0-15
    b_4 = (b * 15) // 255  # Scale to 0-15
    
    # Pack the BGR values into a tuple
    bgr_444 = (b_4, g_4, r_4)
    hex_int = (b_4 << 8) | (g_4 << 4) | r_4
    
    # Return the hex representation, ensuring it's in the form of 0xXXXX
    return f'0x{hex_int:03X}'

if __name__ == "__main__":
    file_path = "C:\\Users\\Shaikh\\Desktop\\neopixel-matrix\\image-to-pixelart\\pixels\\exp.txt"  
    read_hex_values_from_file(file_path)