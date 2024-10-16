# Text Manipulation Tools
Simple tools to replace a piece of text with a desired function e.g. paragraph to sentences, paragraphs to words, removing punctuation marks, etc.

## Paragraph-to-Sentence Converter

*Paragraph-to-Sentence Converter* helps convert a paragraph into a series of sentences that end with a full stop, a question mark, an exclamation mark, or a semi-colon. This tool can be useful if you have a large block of text that you want to break down into smaller sentences, designed keeping in mind the [Mozilla Common Voice Sentence Collector](https://commonvoice.mozilla.org/sentence-collector/#/en).

# Sort a bulleted list in ascending order of year
These Python tools sort a list of text lines based on the years specified in the Odia script. [This](https://github.com/ofdn/Text-Manipulation-Tools/blob/main/sort-odia-list-ascending.py) script rearranges a list in ascending order from the earliest to the latest year, and [this](https://github.com/ofdn/Text-Manipulation-Tools/blob/main/sort-odia-list-descending.py) list does the reverse (descending order). It outputs the sorted list to a new file, preserving the original content.

To use download the files into a folder where your text file (e.g. (`list.txt`) is located. On Linux/MacOS Navigate to the folder using Terminal and run:
- `python3.9 sort-odia-list-ascending.py list.txt` to sort in an ascending order of year
- `python3.9 sort-odia-list-descending.py list.txt` to sort in an descending order of year

### How to Use

1.  Download the Paragraph-to-Sentence Converter. Open using any browser (Firefox and Brave/Chromium tested).
2.  Enter your paragraph in the "Enter your paragraph here" text area.
3.  Click the "Convert" button to convert your paragraph into sentences.
4.  The converted sentences will be displayed in the "Converted Text" area.
5.  If you want to copy the converted text, click the "Copy Converted Text" button.
6.  Paste the copied text into your desired place.

### Notes

-   The converter assumes that the input paragraph is in the Odia script. You need to manipulate the code in case it doesn't work for another writing system of your choice.
-   The converter recognizes sentence-ending punctuation marks such as _Purnachheda_ (।), full stop (.), question mark (?), exclamation mark (!), and semi-colon (;) as the end of a sentence.
-   The converter replaces all occurrences of the _Purnachheda_ (।), full stop (.) and semi-colon (;) with the Odia script's sentence-ending punctuation mark (।).
-   The converter removes any inline citation marks that look like [୧] or [୨]. Useful if the text is copied from Wikipedia.
-   The converted sentences may not always be perfect, so it is recommended to manually review and edit after conversion.

## Other tools/scripts

### UnicodeIt
This script takes any Unicode character(s) as input and displays its Unicode code points. To be able to use this, you need to create a reusable function for this code block in `Zsh`, by defining a function in your Zsh configuration file (`~/.zshrc`) in a Unix-based computer (e.g. Linux or MacOS).

1. Open Zsh Configuration File:

Open your `Zsh` configuration file for editing. This file is typically located at `~/.zshrc`.

`nano ~/.zshrc`


2. Add **unicodeit** Function:

Add the following function definition to the file. This function, named **unicodeit**, takes a string as an argument and prints the Unicode code points for each character in the string.

`
unicodeit() {
    for c in $(echo "$1" | sed 's/./& /g'); do
        printf "U+%04x %s\n" "'$c" "$c"
    done
}
`

3. Save and Exit:

Save your changes and exit the text editor.

Press **Ctrl + O** to write the changes.
Press **Enter** (*return* in MacOS) to confirm the filename.
Press **Ctrl + X** to exit the text editor.

4. Source Zsh Configuration:

To apply the changes immediately, source your Zsh configuration file:

`source ~/.zshrc`


. Use unicodeit Function:

Now, you can use the unicodeit function in your terminal. Provide a string of characters as an argument to get the Unicode code points for each character.

`unicodeit "apple"`

This will output:
`U+0061 a
U+0070 p
U+0070 p
U+006c l
U+0065 e`

