# Installed libraries


# Imported libraries
import os
import re


def remove_empty_lines(input_string):
    lines = input_string.splitlines()
    non_empty_lines = [line for line in lines if line.strip()]
    return '\n'.join(non_empty_lines)


def parse_text_files(directory_path, lat_pattern, long_pattern):
    # Iterate over the files in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        # Check if it's a file and ends with '.txt'
        if os.path.isfile(file_path) and filename.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = remove_empty_lines(file.read())

                # Parse latitude value
                match = re.search(lat_pattern, content)
                if match:
                    lat_value = match.group(0)
                    print(lat_value)

                # Parse longitude value
                match = re.search(long_pattern, content)
                if match:
                    long_value = match.group(0)
                    print(long_value)

                print('-' * 80)  # Separator between files


def main():
    # Define regex patterns
    lat_pattern = r'(?i)lat\s*\d{1,2}\.\d+°?'
    long_pattern = r'(?i)long\s*\d{1,2}\.\d+°?'

    # Prompt user for folder path
    folder_path = input(">> Enter the directory containing text files: ")
    parse_text_files(folder_path, lat_pattern, long_pattern)

if __name__ == "__main__":
    main()