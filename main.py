import cv2
import numpy as np
import matplotlib.pyplot as plt
import gradio as gr
from PIL import Image
import io

def run(image, style, intensity, density):

    img = image

    if img.shape[-1] == 4:
        img = img[:, :, :3]

    img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    if style == "basic":
        sketch = cv2.Canny(gray, intensity, intensity * 3)

    elif style == "detailed":
        inv = 255 - gray
        blur = cv2.GaussianBlur(inv, (21, 21), 0)
        pencil = cv2.divide(gray, 255 - blur, scale=256)
        edges = cv2.Canny(gray, intensity // 2, intensity)
        sketch = cv2.addWeighted(pencil, 0.7, edges, 0.3, 0)

    elif style == "cartoon":
        blur = cv2.medianBlur(gray, 5)
        sketch = cv2.adaptiveThreshold(
            blur, 255,
            cv2.ADAPTIVE_THRESH_MEAN_C,
            cv2.THRESH_BINARY, 9, 9
        )

    elif style == "pencil_sketch":
        inv = 255 - gray
        blur = cv2.GaussianBlur(inv, (21, 21), 0)
        sketch = cv2.divide(gray, 255 - blur, scale=256)

    else:
        _, sketch = cv2.threshold(gray, intensity, 255, cv2.THRESH_BINARY_INV)

    points_x = []
    points_y = []

    h, w = sketch.shape
    step = max(1, 101 - density)

    for y in range(0, h, step):
        for x in range(0, w, step):
            if sketch[y, x] < 200:
                points_x.append(x / w)
                points_y.append(1 - y / h)

    fig, ax = plt.subplots(2, 3, figsize=(14, 9))

    ax[0, 0].imshow(cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB))
    ax[0, 0].axis("off")

    ax[0, 1].imshow(sketch, cmap="gray")
    ax[0, 1].axis("off")

    ax[0, 2].scatter(points_x, points_y, s=0.5, c="black")
    ax[0, 2].axis("off")

    ax[1, 0].hexbin(points_x, points_y, gridsize=30, cmap="gray_r")
    ax[1, 0].axis("off")

    H, _, _ = np.histogram2d(points_x, points_y, bins=40)
    ax[1, 1].contour(H.T, colors="black")
    ax[1, 1].axis("off")

    edges = cv2.Canny(gray, 50, 150)
    steps = np.hstack([gray, edges, sketch])
    ax[1, 2].imshow(steps, cmap="gray")
    ax[1, 2].axis("off")

    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format="png", dpi=150)
    buf.seek(0)
    plt.close()

    return Image.open(buf)

app = gr.Blocks()

with app:
    gr.Markdown("# Face Sketch Plotter")

    with gr.Row():
        with gr.Column():
            img = gr.Image(type="numpy")
            style = gr.Dropdown(
                ["basic", "detailed", "cartoon", "pencil_sketch", "stipple"],
                value="basic"
            )
            intensity = gr.Slider(1, 100, 50)
            density = gr.Slider(10, 100, 30, step=5)
            btn = gr.Button("Generate")

        with gr.Column():
            out = gr.Image()

    btn.click(run, [img, style, intensity, density], out)

app.launch(server_name="0.0.0.0", server_port=7860)
