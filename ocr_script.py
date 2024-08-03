# Installed libraries
# pip install pytesseract==0.3.10
# pip install pillow==10.4.0

# Imported libraries
import os
import pytesseract
from PIL import Image

def process_images(folder_path):
    for filename in os.listdir(folder_path):
        image_path = os.path.join(folder_path, filename)
        
        try:
            image = Image.open(image_path)

            # Perform OCR on the image
            text = pytesseract.image_to_string(image)

            # Define the output text file path
            base_filename = os.path.splitext(filename)[0]  # Remove the image extension
            output_text_path = os.path.join(folder_path, f"{base_filename}.txt")

            # Write the extracted text to the text file
            with open(output_text_path, 'w', encoding='utf-8') as text_file:
                text_file.write(text)

            print(f">> Processed {filename}. Text saved to {base_filename}")

        except Exception as e:
            print(f">> Error processing {filename}: {e}")
            

def main():
    # Prompt user for folder path
    folder_path = input(">> Enter the folder path containing image files: ")
    process_images(folder_path)

if __name__ == "__main__":
    main()
