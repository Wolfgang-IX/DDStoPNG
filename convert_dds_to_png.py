import os
from PIL import Image

def convert_dds_to_png(input_dir, output_dir):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Recursively search through directories
    for root, _, files in os.walk(input_dir):
        for filename in files:
            if filename.endswith('.dds'):
                input_path = os.path.join(root, filename)
                relative_path = os.path.relpath(input_path, input_dir)
                output_path = os.path.join(output_dir, os.path.splitext(relative_path)[0] + '.png')

                # Check if output file already exists, skip conversion if it does
                if os.path.exists(output_path):
                    print(f"Skipping {filename}, corresponding PNG file already exists")
                    continue

                # Ensure directory structure is maintained
                os.makedirs(os.path.dirname(output_path), exist_ok=True)

                # Open DDS image
                try:
                    with Image.open(input_path) as img:
                        img.save(output_path, format='PNG')
                        print(f"Converted {filename} to PNG")
                except Exception as e:
                    print(f"Failed to convert {filename}: {e}")

if __name__ == "__main__":
    # Relative paths to the input and output directories
    input_directory = 'dds'
    output_directory = 'png'

    # Get the absolute paths based on the location of the script
    script_dir = os.path.dirname(os.path.realpath(__file__))
    input_directory = os.path.join(script_dir, input_directory)
    output_directory = os.path.join(script_dir, output_directory)

    convert_dds_to_png(input_directory, output_directory)
