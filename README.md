# 📚 SIMPLE EBOOK CONVERTER

Use this tool to automate the conversion of entire folders of EPUB or PDF files into MOBI format — 100% offline, private, and secure — using Python and Calibre.

### How it works
- Scans a folder for .pdf or .epub files
- Converts each file into .mobi format using Calibre's ebook-convert
- Deletes the original .pdf or .epub files after successful conversion (to save storage space)

### Requirements
- Python 3.x installed on your computer.
- IDE such as Visual Studio Code (recommended).
- Calibre installed (free and open-source ebook tool for the conversion).

### Set-up
1. Download and install Calibre for free from https://calibre-ebook.com/.
2. Clone or download the code: mobi_convertor.py
3. Modify the input directory (where the raw files are placed) and output directory (where the final converted files will be stored). Keep in mind that files in the raw folder will be erased after the conversion.
4. Run the script and enjoy!

PS: If you wish, you can easily modify the script to support additional file formats you may need.
