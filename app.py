import gradio as gr
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

ASCII_CHARS = (
    "@@@@@#####%%%%%%%&&&&&&$$$$$$"
    "******+++++++======-----:::::.....     "
)

STEP = 2


def load_original():
    image = Image.open("pirate.jpg")
    return image


def convert_image():

    original_image = Image.open("pirate.jpg")
    original_image = original_image.convert("RGB")

    gray_image = original_image.convert("L")

    contrast_tool = ImageEnhance.Contrast(gray_image)
    gray_image = contrast_tool.enhance(1.6)

    image_width = gray_image.size[0]
    image_height = gray_image.size[1]

    font = ImageFont.load_default()

    ascii_image = Image.new("RGB", (image_width, image_height), "black")
    draw = ImageDraw.Draw(ascii_image)

    ascii_text = []

    y = 0
    while y < image_height:

        line = ""
        x = 0

        while x < image_width:

            brightness = gray_image.getpixel((x, y))

            ascii_index = int(brightness * (len(ASCII_CHARS) - 1) / 255)

            ascii_char = ASCII_CHARS[ascii_index]

            red, green, blue = original_image.getpixel((x, y))

            blend_value = brightness / 255
            final_color = (
                int(red * blend_value),
                int(green * blend_value),
                int(blue * blend_value)
            )

            draw.text((x, y), ascii_char, fill=final_color, font=font)

            line = line + ascii_char

            x = x + STEP

        ascii_text.append(line)

        y = y + STEP

    text_file = open("ascii.txt", "w", encoding="utf-8")
    for text_line in ascii_text:
        text_file.write(text_line)
        text_file.write("\n")
    text_file.close()

    ascii_image.save("ascii.png")

    return ascii_image, "ascii.png", "ascii.txt"


with gr.Blocks(title="Image to ASCII Converter") as app:

    gr.Markdown("## Image to ASCII Art Converter")
    gr.Markdown("Original image is shown first. Click Convert to generate ASCII output.")

    with gr.Row():
        original_preview = gr.Image(
            value=load_original(),
            label="Original Image",
            interactive=False
        )

        ascii_preview = gr.Image(
            label="ASCII Output",
            interactive=False
        )

    convert_button = gr.Button("Convert")

    with gr.Row():
        download_png = gr.File(label="Download ascii.png")
        download_txt = gr.File(label="Download ascii.txt")

    convert_button.click(
        fn=convert_image,
        inputs=[],
        outputs=[ascii_preview, download_png, download_txt]
    )

if __name__ == "__main__":
    app.launch()
