# Image to ASCII Art Converter 

- This project converts a fixed image into a high-density ASCII art image
- The ASCII output preserves the original image aspect ratio
- The ASCII art is rendered as a PNG image
- Colored ASCII characters are used based on original pixel colors
- The project is implemented using Python and Gradio
- The application is compatible with both GitHub and Hugging Face Spaces

---

## Project Overview

- A image (`pirate.jpg`) is used as input
- The image is converted into ASCII characters using pixel-level processing
- ASCII characters are drawn directly at pixel coordinates
- This ensures that the ASCII output visually matches the original image
- The output is saved in both text and image formats

---

## Features

- Exact aspect ratio preservation
- Colored ASCII output
- High-density ASCII rendering
- Loop-based pixel processing
- No external numerical libraries (no numpy)
- Simple and clean user interface

---

## Project Structure

- `app.py`
  - Main application file
  - Contains ASCII conversion logic and Gradio UI
- `pirate.jpg`
  - Fixed input image used for conversion
- `ascii.png`
  - Generated colored ASCII image (auto-created)
- `ascii.txt`
  - Generated ASCII text file (auto-created)
- `requirements.txt`
  - List of required Python dependencies
- `README.md`
  - Project documentation

---

## Technologies Used

- Python
- Gradio
- Pillow (PIL)

---

## How the ASCII Conversion Works

- The original image is loaded and converted to grayscale
- Image contrast is enhanced for better edge visibility
- The image is scanned pixel by pixel using loops
- Each pixel brightness is mapped to an ASCII character
- ASCII characters are drawn directly at pixel positions
- Original pixel color is applied to each ASCII character
- The final ASCII image matches the original image dimensions

---

## User Interface Flow

- The original image is shown as a preview when the app loads
- The ASCII output area is initially empty
- Clicking the Convert button:
  - Generates the ASCII image
  - Displays the ASCII output preview
  - Enables download of ascii.png and ascii.txt

---

## How to Run Locally

- Install Python (version 3.8 or higher recommended)
- Install dependencies using:
  - `pip install -r requirements.txt`
- Ensure `pirate.jpg` is present in the project directory
- Run the application:
  - `python app.py`
- Open the displayed local URL in a browser

---

## Running on Hugging Face Spaces

- Create a new Space with SDK set to Gradio
- Upload the following files:
  - `app.py`
  - `pirate.jpg`
  - `requirements.txt`
  - `README.md`
- Hugging Face will automatically build and deploy the app

---

## Notes

- ASCII output quality depends on character density and contrast
- The default font is used for maximum compatibility
- The application intentionally uses loop-based logic for clarity
- Best results are viewed on a dark background

---

## Use Cases

- Image-to-text visualization
- ASCII art generation
- Educational demonstrations
- Creative coding projects
- Portfolio and showcase applications

---

## License

- This project is provided for educational and demonstration purposes
