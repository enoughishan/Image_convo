import gradio as gr
from PIL import Image

# Dense ASCII characters (for output like your example)
ASCII_CHARS = "#@%&$*+=-:. "

def convert_fixed_image(width):
    # Load ONLY this image
    image = Image.open("pirate.jpg")

    # Convert to grayscale
    image = image.convert("L")

    old_w = image.width
    old_h = image.height

    # Maintain aspect ratio
    ratio = old_h / old_w
    new_h = int(width * ratio / 1.7)

    image = image.resize((width, new_h))

    ascii_art = ""

    # LOOP through pixels
    for y in range(new_h):
        for x in range(width):
            pixel = image.getpixel((x, y))  # 0–255

            index = int(pixel * (len(ASCII_CHARS) - 1) / 255)
            ascii_art = ascii_art + ASCII_CHARS[index]

        ascii_art = ascii_art + "\n"

    # Save ASCII using loop
    file = open("ascii.txt", "w", encoding="utf-8")
    for ch in ascii_art:
        file.write(ch)
    file.close()

    return ascii_art, "ascii.txt"


# ---------- GRADIO UI ----------
with gr.Blocks(title="Fixed Image to ASCII") as app:
    gr.Markdown("# 🏴‍☠️ Pirate Image → ASCII Art")
    gr.Markdown("Converts **only one fixed image** using **loops only**")

    width_slider = gr.Slider(
        minimum=80,
        maximum=200,
        value=140,
        step=10,
        label="ASCII Width (Higher = More Detail)"
    )

    convert_btn = gr.Button("Convert Image")

    ascii_box = gr.Textbox(
        label="ASCII Output",
        lines=30,
        interactive=False
    )

    download = gr.File(label="Download ascii.txt")

    convert_btn.click(
        fn=convert_fixed_image,
        inputs=[width_slider],
        outputs=[ascii_box, download]
    )

if __name__ == "__main__":
    app.launch()
