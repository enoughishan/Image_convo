import gradio as gr
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

ASCII_CHARS = (
    "@@@@@#####%%%%%%%&&&&&&$$$$$$"
    "******+++++++======-----:::::.....     "
)

STEP = 3  

def load_original():
    return Image.open("pirate.jpg")

def convert_image():
    original = Image.open("pirate.jpg").convert("RGB")
    gray = original.convert("L")
    gray = ImageEnhance.Contrast(gray).enhance(1.8)

    img_w, img_h = gray.size

    font = ImageFont.load_default()

    ascii_img = Image.new("RGB", (img_w, img_h), "black")
    draw = ImageDraw.Draw(ascii_img)

    ascii_lines = []

    
    for y in range(0, img_h, STEP):
        line = ""
        for x in range(0, img_w, STEP):
            pixel = gray.getpixel((x, y))
            index = int(pixel / 255 * (len(ASCII_CHARS) - 1))
            ch = ASCII_CHARS[index]
            color = original.getpixel((x, y))

            draw.text((x, y), ch, fill=color, font=font)
            line += ch

        ascii_lines.append(line)

    
    with open("ascii.txt", "w", encoding="utf-8") as f:
        for line in ascii_lines:
            f.write(line + "\n")

    ascii_img.save("ascii.png")

    return ascii_img, "ascii.png", "ascii.txt"


# ---------------- UI ----------------
with gr.Blocks(title="Image to ASCII") as app:
    gr.Markdown("## Image to ASCII Converter")
    gr.Markdown("Original image is shown first then ASCII output appears after conversion.")

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

    convert_btn = gr.Button("Convert")

    with gr.Row():
        download_png = gr.File(label="Download ascii.png")
        download_txt = gr.File(label="Download ascii.txt")

    convert_btn.click(
        fn=convert_image,
        inputs=[],
        outputs=[ascii_preview, download_png, download_txt]
    )

if __name__ == "__main__":
    app.launch()
