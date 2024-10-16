# This Python tool sorts a list of text lines based on the years specified in Odia script, ensuring that the list is arranged in ascending order from the earliest to the latest year. It outputs the sorted list to a new file, preserving the original content.

# Author: Subhashish Panigrahi
# Version: 1.0
# Date: 16 October 2024
# License: MIT License

import sys
import re

# Function to convert Odia year to integer for sorting
def odia_year_to_int(odia_year):
    odia_to_eng = str.maketrans('୦୧୨୩୪୫୬୭୮୯', '0123456789')
    return int(odia_year.translate(odia_to_eng))

# Function to extract the year from a line
def extract_year(line):
    match = re.search(r'୧୯[୦୧୨୩୪୫୬୭୮୯]{2}|୨୦[୦୧୨୩୪୫୬୭୮୯]{2}|୧୮[୦୧୨୩୪୫୬୭୮୯]{2}', line)
    if match:
        return odia_year_to_int(match.group())
    return None

def main(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Extract years and sort lines based on years
    lines_with_years = [(line, extract_year(line)) for line in lines]
    
    # Sort lines by year; non-matching lines will be None and go to the end
    sorted_lines = sorted(lines_with_years, key=lambda x: (x[1] is None, x[1]))

    # Prepare output filename
    output_filename = f"{filename[:-4]}-sorted.txt"  # OLDFILE-sorted.txt

    # Write sorted output with line breaks
    with open(output_filename, 'w', encoding='utf-8') as file:
        for line, year in sorted_lines:
            file.write(f"{line.strip()}\n")  # Add a line break after each line
    print("\nSorted lines written to:", output_filename)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3.9 sort-list.py LIST.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    main(input_file)
