import gradio as gr
import numpy as np
import matplotlib.pyplot as plt
import os

ASCII_CHARS = (
    "@@@@@#####%%%%%%%&&&&&&WWWWWW"
    "******+++++++======-----:::::.....     "
)

def convert_image(image):
    if image is None:
        return None, None

    target_width = 100
    scale_factor = target_width / image.shape[1]
    
    new_width = target_width
    new_height = int(image.shape[0] * scale_factor * 0.55)
    
    step_x = int(image.shape[1] / new_width)
    step_y = int(image.shape[0] / new_height)
    
    small_image = image[::step_y, ::step_x]
    height, width, _ = small_image.shape

    gray = np.dot(small_image[..., :3], [0.299, 0.587, 0.114])

    plt.close('all')
    fig = plt.figure(figsize=(12, 12), facecolor='black')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    
    fig.canvas.draw()

    ascii_str = ""

    for y in range(height):
        line = ""
        for x in range(width):
            brightness = gray[y, x]
            
            ascii_index = int(brightness * (len(ASCII_CHARS) - 1) / 255)
            char = ASCII_CHARS[ascii_index]
            
            r, g, b = small_image[y, x]
            color = (r / 255, g / 255, b / 255)
            
            ax.text(
                x, -y, 
                char, 
                color=color, 
                fontfamily='monospace', 
                fontsize=8,
                horizontalalignment='center',
                verticalalignment='center'
            )
            
            line += char
        ascii_str += line + "\n"

    ax.set_xlim(-1, width)
    ax.set_ylim(-height, 1)

    with open("ascii.txt", "w", encoding="utf-8") as f:
        f.write(ascii_str)

    return fig, "ascii.txt"

default_image = "pirate.jpg" if os.path.exists("pirate.jpg") else None

with gr.Blocks(title="Colored ASCII Converter", theme=gr.themes.Soft()) as app:

    gr.Markdown("## Colored ASCII Art Converter")

    with gr.Row():
        input_img = gr.Image(value=default_image, label="Original Image")
        plot_output = gr.Plot(label="Colored ASCII Result")

    convert_button = gr.Button("Convert with Color")
    
    download_txt = gr.File(label="Download ascii.txt")

    convert_button.click(
        fn=convert_image,
        inputs=[input_img],
        outputs=[plot_output, download_txt]
    )

if __name__ == "__main__":
    app.launch()
