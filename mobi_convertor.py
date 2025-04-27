import os
import subprocess

input_folder = r"C:\Path\To\Your\RawFolder" 
output_folder = r"C:\Path\To\Your\FinalFolder"

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.pdf', '.epub')):
        input_path = os.path.join(input_folder, filename)
        base_name = os.path.splitext(filename)[0]
        output_path = os.path.join(output_folder, base_name + '.mobi')
        
        try:
            subprocess.run(['ebook-convert', input_path, output_path], check=True)
            print(f"Converted: {filename}")

            # Delete the original file after successful conversion
            os.remove(input_path)
            print(f"Deleted original file: {filename}")

        except subprocess.CalledProcessError:
            print(f"Failed to convert: {filename}")
        except Exception as e:
            print(f"Error deleting {filename}: {e}")
