import gradio as gr
import numpy as np

ASCII_CHARS = (
    "@@@@@#####%%%%%%%&&&&&&$$$$$$"
    "******+++++++======-----:::::.....     "
)

STEP_X = 4
STEP_Y = 8

def convert_image(image):
    if image is None:
        return None, None

    small_image = image[::STEP_Y, ::STEP_X]
    height, width, _ = small_image.shape

    gray = np.dot(small_image[..., :3], [0.299, 0.587, 0.114])

    mean_gray = np.mean(gray)
    gray = (gray - mean_gray) * 1.6 + mean_gray
    gray = np.clip(gray, 0, 255)

    ascii_str = ""
    html_content = "<pre style='font-family: monospace; background-color: black; font-size: 8px; white-space: pre; overflow-x: scroll;'>"

    for y in range(height):
        line = ""
        html_line = ""
        for x in range(width):
            brightness = gray[y, x]
            
            ascii_index = int(brightness * (len(ASCII_CHARS) - 1) / 255)
            char = ASCII_CHARS[ascii_index]
            
            r, g, b = small_image[y, x]
            
            blend = brightness / 255
            r = int(r * blend)
            g = int(g * blend)
            b = int(b * blend)

            line += char
            html_line += f"<span style='color: rgb({r},{g},{b})'>{char}</span>"

        ascii_str += line + "\n"
        html_content += html_line + "<br>"

    html_content += "</pre>"

    with open("ascii.txt", "w", encoding="utf-8") as f:
        f.write(ascii_str)

    return html_content, "ascii.txt"


with gr.Blocks(title="Image to ASCII Converter") as app:

    gr.Markdown("## Image to ASCII Art Converter")

    with gr.Row():
        input_img = gr.Image(value="pirate.jpg", label="Original Image")
        ascii_html = gr.HTML(label="ASCII Output")

    convert_button = gr.Button("Convert")
    
    download_txt = gr.File(label="Download ascii.txt")

    convert_button.click(
        fn=convert_image,
        inputs=[input_img],
        outputs=[ascii_html, download_txt]
    )

if __name__ == "__main__":
    app.launch()
