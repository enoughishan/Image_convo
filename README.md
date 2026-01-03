# Image to ASCII Art Converter 

- This project converts a fixed image into a high-density ASCII art representation
- The ASCII output preserves the original image aspect ratio using intelligent sampling
- Colored ASCII characters are used based on original pixel colors
- The project is implemented using **Python, NumPy, and Gradio**

---

## Project Overview

- An image (`pirate.jpg`) is used as input
- The image is processed efficiently using **NumPy arrays**
- The output is rendered  to simulate a colored image without generating a PNG file
- This ensures the output can be displayed instantly without heavy image libraries (like Pillow)
- The output is provided as a downloadable text file and a visual  preview

---

## Features

- **Efficient Processing:** Uses NumPy for fast matrix operations (resizing, grayscale, contrast)
- **Aspect Ratio Correction:** Uses differential step sampling (X vs Y) to prevent vertical stretching
- **No Image Generation:** Pure text-based solution (lighter weight)
- **Simple UI:** Clean interface built with Gradio
---

## Project Structure

- `app.py`
  - Main application file
  - Contains NumPy processing logic and Gradio UI
- `pirate.jpg`
  - Fixed input image used for conversion
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
- NumPy

---

## How the ASCII Conversion Works

- The original image is loaded as a **NumPy array**
- The image is "downsampled" using array slicing (`image[::8, ::4]`) to fix aspect ratio
- Grayscale conversion is performed using a **dot product** of RGB channels
- Contrast is enhanced using vectorized math operations
- A loop iterates through the processed array 
- Each character is wrapped in a `<span>` tag with the original pixel's RGB color

---

## User Interface Flow

- The original image is shown as a preview when the app loads
- The ASCII output area is initially empty
- Clicking the Convert button:
  - Processes the image array
  - Renders the colored ASCII 
  - Enables download of `ascii.txt`

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

---

## Notes

- ASCII output quality relies on the `STEP` variables defined in the code
- The output uses a monospace font and strict line-height.
- Best results are viewed on a dark background 

---

## Use Cases

- Efficient image processing 
- Educational demonstrations of NumPy array slicing

---

## License

- This project is provided for educational and demonstration purposes
