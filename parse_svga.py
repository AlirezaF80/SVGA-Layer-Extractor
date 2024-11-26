import zlib
import zipfile
from io import BytesIO
from SVGA_pb2 import MovieEntity
from PIL import Image
import os
import sys


def extract_svga_layers(svga_path, output_dir):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Read the .svga file
    with open(svga_path, 'rb') as f:
        svga_data = f.read()

    # Decompress the SVGA data
    decompressed_data = zlib.decompress(svga_data)

    # Parse the MovieEntity
    movie = MovieEntity()
    movie.ParseFromString(decompressed_data)

    # Extract images
    for image_key, image_value in movie.images.items():
        # image_key is the identifier for the image
        # image_value is the raw image data in bytes

        # Create a filename for the image
        image_filename = os.path.join(output_dir, f"{image_key}.png")

        # Save the image data to a file
        with open(image_filename, 'wb') as img_file:
            img_file.write(image_value)

    print(f"Extracted {len(movie.images)} images to {output_dir}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python parse_svga.py <svga_file>")
        sys.exit(1)
    
    filename, _ = os.path.splitext(sys.argv[1])
    output_folder = filename + "_output"
    
    extract_svga_layers(sys.argv[1], output_folder)