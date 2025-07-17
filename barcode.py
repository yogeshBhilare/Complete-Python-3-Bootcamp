import barcode
from io import BytesIO
from barcode.writer import ImageWriter
from PIL import Image
import os

# Specify the barcode type (Code 128 supports alphanumeric data)
barcode_type = 'code128'

# Data to encode
data = input() #"XXXXX"
buffer = BytesIO()
# Generate the barcode
barcode_class = barcode.get_barcode_class(barcode_type)
barcode_instance = barcode_class(data, writer=ImageWriter())
barcode_instance.write(buffer)
# Save the barcode as an image

# Reset the buffer's position to the beginning so Pillow can read it
buffer.seek(0)
# --- Image Resizing ---
# Open the image from the buffer using Pillow
img = Image.open(buffer)

# Define target dimensions in inches
target_width_inches = 2
target_height_inches = 1
dpi = 300

# Calculate the new dimensions in pixels
new_width_pixels = int(target_width_inches * dpi)
new_height_pixels = int(target_height_inches * dpi)
new_dimensions_pixels = (new_width_pixels, new_height_pixels)
resized_img = img.resize(new_dimensions_pixels, Image.LANCZOS) # Using LANCZOS for high quality downscaling

# --- Save the Resized Image ---
output_filename = os.path.join("E:\\Barcodes", data + ".png")
resized_img.save(output_filename)

print(f"Barcode saved as {output_filename} with dimensions: ")

# Close the buffer to free up memory
buffer.close()
