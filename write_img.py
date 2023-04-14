
import os
import pytesseract
from PIL import Image

def write_img():
    # Set the path of the folder containing the images
    input_folder = "C:/Users/Korisnik/Desktop/hello/images"

    # Set the path of the output file
    output_file = "C:/Users/Korisnik/Desktop/hello/file.txt"

    # Initialize pytesseract
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Korisnik\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

    # Open the output file for writing
    with open(output_file, 'w') as f:
        # Iterate through each image in the folder
        for i, image_file in enumerate(os.listdir(input_folder)):
            # Load the image
            image_path = os.path.join(input_folder, image_file)
            image = Image.open(image_path)

            # Perform OCR on the image
            text = pytesseract.image_to_string(image)

            # Write the recognized text to the output file
            f.write(text)
            f.write("\n\n")

            # Log
            textbox.config(state=tkinter.NORMAL)
            textbox.insert('end', "Image " + image_path + "data stored in txt file \n")
            textbox.config(state=tkinter.DISABLED)

    # Log
    textbox.config(state=tkinter.NORMAL)
    textbox.insert('end',"Txt file ready \n")
    textbox.config(state=tkinter.DISABLED)
