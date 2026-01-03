

#  ASCII Art 

This project is a Python application that converts images into high-resolution **Colored ASCII Art**. 

Instead of generating a standard image file, it uses **Matplotlib** to plot individual colored characters onto a dark canvas, preserving the exact colors of the original pixels. This method allows for colored output without relying on image processing libraries like Pillow.

## 🚀 Features

* **True Color Rendering:** Maps the color of every pixel to the corresponding ASCII character.
* **Matplotlib Rendering:** Uses a plotting engine to draw text instead of standard image manipulation.
* **Aspect Ratio Correction:** Automatically calculates the correct spacing and scaling to prevent the ASCII art from looking stretched.
* **Dual Output:** Generates both a visual plot and a downloadable `.txt` file (plain text version).
* **Hugging Face Ready:** Configured with `headless` mode (`Agg` backend) for seamless deployment on Hugging Face Spaces.

## 🛠️ Technologies Used

* **Python:** Core programming language.
* **Gradio:** For the web interface (UI).
* **NumPy:** For efficient pixel array manipulation and resizing.
* **Matplotlib:** For rendering the colored text onto a figure.

## 📂 Project Structure

* `app.py`: The main application script containing logic and UI.
* `requirements.txt`: List of dependencies required to run the app.
* `pirate.jpg`: Default example image.
* `ascii.txt`: The generated plain text output (created at runtime).

## ⚙️ How to Run Locally

1.  **Install Python:** Ensure you have Python 3.8+ installed.
2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(If `requirements.txt` is missing, install manually: `pip install gradio numpy matplotlib`)*
3.  **Run the App:**
    ```bash
    python app.py
    ```
4.  **Open Browser:** Click the local URL provided in the terminal (usually `http://127.0.0.1:7860`).

## ☁️ How to Deploy on Hugging Face Spaces

1.  Create a new **Space** on Hugging Face.
2.  Select **Gradio** as the SDK.
3.  Upload the following files to your Space:
    * `app.py`
    * `requirements.txt`
    * `pirate.jpg` (or any default image you prefer)
4.  The application will build and launch automatically.

## 📝 Configuration

You can adjust the resolution in `app.py` by modifying the `target_width` variable:

```python
# app.py
target_width = 100  # Higher = More detail, but slower rendering
