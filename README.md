# Fixed Image to ASCII Art Converter

- This project converts a single fixed image into ASCII art
- The conversion logic is implemented using only loops
- The output ASCII art is saved into a text file named ascii.txt
- The application uses Python and Gradio for the user interface

---

## Project Description

- The application reads a fixed image file named pirate.jpg
- The image is converted into grayscale
- Pixel brightness values are mapped to ASCII characters
- Nested for-loops are used to process each pixel
- The generated ASCII art is displayed in the browser
- The ASCII output is written to a file using a loop

---

## Project Structure

- app.py  
  - Main application file
  - Contains ASCII conversion logic and Gradio UI
- pirate.jpg  
  - Fixed input image used for conversion
- ascii.txt  
  - Output file containing ASCII art (auto-generated)
- requirements.txt  
  - Lists required Python libraries

---

## Technologies Used

- Python
- Gradio
- Pillow (PIL)

---

## ASCII Conversion Logic

- Image is opened using Pillow
- Image is converted to grayscale
- Image is resized while maintaining aspect ratio
- Two nested loops iterate over image rows and columns
- Each pixel value (0–255) is mapped to an ASCII character
- ASCII characters are concatenated line by line
- The final ASCII string is saved into ascii.txt using a loop

---

## How to Run the Project

- Install Python (version 3.8 or higher recommended)
- Install required libraries using:
  - pip install -r requirements.txt
- Place pirate.jpg in the same directory as app.py
- Run the application using:
  - python app.py
- Open the displayed local URL in a browser

---

## Output

- ASCII art is shown in the web interface
- The same ASCII art is saved in ascii.txt
- The output file can be opened in any text editor
- Best viewed using a monospace font

---

## Key Features

- Uses only loop-based logic
- No advanced libraries like NumPy are used
- Beginner-friendly and exam-oriented code
- Fixed image ensures consistent output
- ASCII art is stored permanently in a text file

---

## Notes

- The ascii.txt file is generated only after clicking the Convert button
- For best results, increase ASCII width
- Viewing ASCII output in a monospace font is recommended
