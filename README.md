📸 Geographical Text Extraction & Parsing 📸

Welcome to my Geographical Text Extraction & Parsing project! 🌍✨ This repository contains two Python scripts designed to work together in extracting and processing geographical latitude and longitude values from images. The project demonstrates how to use Pytesseract for text recognition from images and illustrates the parsing of recognized text through the usage of regular expressions to extract the desired geographical latitude and longitude values


📜 Table of Contents

Overview

Technologies Used

How It Works

Getting Started

Project Structure


🚀 Overview

- Image Text Extraction Script: utilizes Pillow and Pytesseract to perform Optical Character Recognition (OCR) on images containing geographical coordinates
- Coordinates Parsing Script: takes the extracted text and parses out latitude and longitude values from the text using regular expressions


🛠️ Technologies Used

- Pillow 🖼️: a Python Imaging Library for opening, manipulating, and processing different image file formats
- Pytesseract 🧠: a Python wrapper for Google's Tesseract-OCR Engine, perfect for converting images into text


🎯 How It Works

1. Extract Text from Images
   
Run the following command to extract text from images:

python ocr_script.py

The script will prompt you to enter the path to a folder containing image files. The recognized text will be saved in text files within the same folder as the images

2. Parse Coordinates
   
Run the following command to parse the extracted coordinates:

python parse_script.py

The script will prompt you to enter the path to a folder containing the text files with extracted text. It will then parse the latitude and longitude values and print them to the console


🧩 Getting Started

Clone the Repository:

git clone https://github.com/dsprovider/ocr_latlong_parser.git

cd ocr_latlong_parser

Install Required Packages:

pip install -r requirements.txt


📂 Project Structure

ocr_script.py: the script for OCR text extraction

parse_script.py: the script for parsing latitude and longitude values

images/: sample images for testing
