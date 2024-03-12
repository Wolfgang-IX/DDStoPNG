import os
from PIL import Image
from multiprocessing import Pool

def convert_dds_to_png(input_file):
    input_path, input_dir, output_dir = input_file
    relative_path = os.path.relpath(input_path, input_dir)
    output_path = os.path.join(output_dir, os.path.splitext(relative_path)[0] + '.png')

    # Check if output file already exists, skip conversion if it does
    if os.path.exists(output_path):
        print(f"Skipping {os.path.basename(input_path)}, corresponding PNG file already exists")
        return

    # Ensure directory structure is maintained
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Open DDS image
    try:
        with Image.open(input_path) as img:
            img.save(output_path, format='PNG')
            print(f"Converted {os.path.basename(input_path)} to PNG")
    except Exception as e:
        print(f"Failed to convert {os.path.basename(input_path)}: {e}")

if __name__ == "__main__":
    # Relative paths to the input and output directories
    input_directory = 'dds'
    output_directory = 'png'

    # Get the absolute paths based on the location of the script
    script_dir = os.path.dirname(os.path.realpath(__file__))
    input_directory = os.path.join(script_dir, input_directory)
    output_directory = os.path.join(script_dir, output_directory)

    # Ensure input and output directories exist
    os.makedirs(input_directory, exist_ok=True)
    os.makedirs(output_directory, exist_ok=True)

    # Get list of all DDS files
    dds_files = []
    for root, _, files in os.walk(input_directory):
        for filename in files:
            if filename.endswith('.dds'):
                dds_files.append((os.path.join(root, filename), input_directory, output_directory))

    # Convert DDS files to PNG using multiprocessing
    with Pool() as pool:
        pool.map(convert_dds_to_png, dds_files)
