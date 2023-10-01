from PIL import Image, ImageDraw
import os
# Input and output directories
input_dir = r'D:\football photos'
output_dir = r'D:\ffmpegftest'

# Watermark image path
watermark_path = r'D:\watermark\watermark.png'


# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Load the watermark image
watermark = Image.open(watermark_path)

# Calculate the new size for the watermark (1/4 of its current size)
new_width = watermark.width // 4
new_height = watermark.height // 4
watermark = watermark.resize((new_width, new_height), Image.ANTIALIAS)

# Get a list of image files in the input directory
image_files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff'))]

for image_file in image_files:
    input_file_path = os.path.join(input_dir, image_file)
    output_file_path = os.path.join(output_dir, image_file)

    # Open the image
    img = Image.open(input_file_path)

    # Calculate the position to place the resized watermark (top left corner)
    position = (10, 10)

    # Create a copy of the image to add the watermark
    img_with_watermark = img.copy()

    # Paste the resized watermark on the image
    img_with_watermark.paste(watermark, position, watermark)

    # Save the watermarked image
    img_with_watermark.save(output_file_path)

    print(f"Watermarked {image_file} and saved to {output_file_path}")

print("Watermarking complete!")
