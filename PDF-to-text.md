# Extract textual content from PDFs on MacOS and Linux
You can use this step-by-step process to extract text from PDFs. This was written keeping in mind the first two pages of a book, called title and signature pages in English, that contain necessary bibliographic Information. This process can used as is or modified according to your needs.

1. Install Required Software:
Homebrew: If you don't have Homebrew installed, you can install it by following the instructions on Homebrew's website.

* Open Terminal and run:

`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

* pdfgrep:

`brew install pdfgrep`

* Tesseract OCR:

`brew install tesseract`

2. Create the Script:
* Open a text editor on your Mac (like TextEdit, VSCode, or Sublime Text).
* Copy and paste the following script into the text editor:

```
#!/bin/bash

output_folder="output"

# Create output folder if it doesn't exist
mkdir -p "$output_folder"

# Loop through PDFs in the folder
for pdf_file in *.pdf; do
    # Extract text from the first three pages
    text=$(pdftotext -f 1 -l 3 "$pdf_file" - | tr -d '\n')

    # Save all text to output file
    echo "$pdf_file: $text" >> "$output_folder/$pdf_file.txt"
done
```

* Save the file with a meaningful name, e.g., extract-bib-info.sh.
* Make the script executable by running the following command in the terminal:

`chmod +x extract-bib-info.sh`

3. Run the Script:

* Open Terminal and navigate to the folder containing your PDFs using the cd command.
* Run the script by typing:

`./extract-bib-info.sh`

4. Review Output:
* The script will create an "output" folder in the same directory.
* Inside the "output" folder, you'll find text files named after each PDF, containing the extracted text from the first three pages.

## Notes:
* If you encounter a "permission denied" error, ensure that the script is executable by running `chmod +x extract-bib-info.sh`.
* This script assumes that the bibliographic information is spread across the first three pages. You can adjust the script based on your specific needs.
* If your PDFs have images and the script isn't extracting the desired information, you may need to investigate OCR settings or use more advanced OCR tools.
* This guide provides a basic setup for extracting text from PDFs. Depending on your PDFs' characteristics, you might need to customize the script further.

# Maintainer
* Subhashish Panigrahi

# License
(c) 2024. Subhashish Panigrahi. O Foundation. This code is released under a MIT License and the documentation is under a Creative Commons ShareAlike Attribution (CC BY-SA) 4.0 International License. You are encouraged to use, share, and even make derivatives under the License terms
