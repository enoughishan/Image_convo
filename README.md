# 🏴‍☠️ Captain Jack ASCII: Digital Portrait Generator

A standalone, high-fidelity ASCII art generator that renders a portrait of **Johnny Depp as Captain Jack Sparrow**. This project utilizes pure Python to create a retro-style, animated terminal visualization without requiring any external image processing libraries.

## 📖 Overview

This script is an exercise in **hardcoded graphical logic** and **terminal rendering**. Unlike standard ASCII converters that process images at runtime using libraries like `PIL` or `OpenCV`, this project embeds the image data directly into the codebase using optimized conditional logic.

The result is a lightweight, zero-dependency script that paints a 4:5 aspect ratio portrait line-by-line, simulating a vintage data transmission or CRT monitor scan.

## ✨ Key Features

* **Zero Dependencies:** Built entirely with the Python Standard Library (`time`). No `pip install` required.
* **Portrait Optimized:** meticulously adjusted to a **60x41 grid** to achieve a perfect **4:5 aspect ratio** (Instagram Portrait standard) in terminal environments.
* **CRT Animation:** Features a "scanline" effect that draws the character row-by-row for a dramatic visual reveal.
* **High Contrast:** Optimized character mapping (`@`, `#`, `%`, `*`) ensures distinct facial features like the iconic bandana and beard are recognizable.

## 🚀 Installation & Usage

### Prerequisites
* Python 3.0 or higher installed on your system.

### Running the Project
1.  **Clone or Download** the repository (or simply save the script file).
2.  Open your terminal or command prompt.
3.  Navigate to the directory containing the file.
4.  Run the script:

```bash
python jack_ascii.py


Configuration
The script is self-contained, but you can easily tweak the animation parameters within the code:

Adjusting Animation Speed
Locate the time.sleep() function at the bottom of the main loop:

Python

# Slower, more dramatic reveal
time.sleep(0.1)

# Faster, instant rendering
time.sleep(0.01)
Changing the Header
The current build displays a placeholder title. You can customize the print statement on line 7:

Python

print('--- Captain Jack Sparrow ---')
🛠️ Technical Details
How it works: Instead of storing a large 2D array or loading an image file, the script uses Run-Length Encoding (RLE) logic implemented via nested if/elif structures.

Grid System: The canvas is defined as Height: 41 rows by Width: 60 columns.

Coordinate Mapping: The script iterates through every (row, col) coordinate.

Conditional Rendering: Specific characters are printed only when the loop hits defined coordinates (e.g., row == 5 and col == 23), effectively "painting" the pixels in code.

🤝 Contributing
Contributions are welcome! If you'd like to optimize the character set for different terminal backgrounds (light vs. dark) or add color support using ANSI escape codes:

Fork the Project

Create your Feature Branch (git checkout -b feature/AddColor)

Commit your Changes (git commit -m 'Add ANSI color support')

Push to the Branch (git push origin feature/AddColor)

Open a Pull Request

📄 License
This project is open-source and available under the MIT License.

Created with ❤️ by [Ishant kumar]
