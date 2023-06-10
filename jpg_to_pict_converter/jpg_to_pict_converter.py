import os
from PIL import Image

def convert_image(input_path, output_folder):
    with Image.open(input_path) as im:
        pict_path = os.path.join(output_folder, os.path.splitext(os.path.basename(input_path))[0] + ".pict")
        im.save(pict_path, format="PICT", quality=100)

def choose_folder():
    folder_path = input("Enter the path to the folder: ")
    while not os.path.exists(folder_path):
        folder_path = input("The folder doesn't exist. Please enter a valid path to the folder: ")
    return folder_path

def main():
    print("Welcome to JPG to PICT Converter!")
    jpg_folder = choose_folder()
    pict_folder = choose_folder()
    # Create the output folder if it doesn't exist yet
    if not os.path.exists(pict_folder):
        os.makedirs(pict_folder)
    # Convert images
    for filename in os.listdir(jpg_folder):
        if filename.endswith('.jpg'):
            input_path = os.path.join(jpg_folder, filename)
            convert_image(input_path, pict_folder)
    print("All images converted successfully to PICT format and saved in the chosen folder!")

if __name__ == "__main__":
    main()

# softy_plug