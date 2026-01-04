import gradio as gr
import os
import math

ASCII_CHARS_LIST = [
    '$', '@', 'B', '%', '8', '&', 'W', 'M', '#', '*', 
    'o', 'a', 'h', 'k', 'b', 'd', 'p', 'q', 'w', 'm', 
    'Z', 'O', '0', 'Q', 'L', 'C', 'J', 'U', 'Y', 'X', 
    'z', 'c', 'v', 'u', 'n', 'x', 'r', 'j', 'f', 't', 
    '/', '\\', '|', '(', ')', '1', '{', '}', '[', ']', 
    '?', '-', '_', '+', '~', '<', '>', 'i', '!', 'l', 
    'I', ';', ':', ',', '"', '^', '`', "'", '.', ' ' 
]

def calculate_luminance(red, green, blue):
    r_weight = 0.299
    g_weight = 0.587
    b_weight = 0.114
    luminance = (r_weight * red) + (g_weight * green) + (b_weight * blue)
    return luminance / 255.0

def apply_contrast_logic(brightness_value):
    contrast_factor = 0.5
    adjusted_value = math.pow(brightness_value, contrast_factor)
    return adjusted_value

def get_char_for_pixel(brightness):
    list_length = len(ASCII_CHARS_LIST)
    char_index = int(brightness * (list_length - 1))
    if char_index < 0:
        char_index = 0
    if char_index >= list_length:
        char_index = list_length - 1
    return ASCII_CHARS_LIST[char_index]

def convert_image_to_ascii(image_input):
    if image_input is None:
        return None, None

    original_height = image_input.shape[0]
    original_width = image_input.shape[1]

    target_width_chars = 250 
    step_x = int(original_width / target_width_chars)
    if step_x < 1:
        step_x = 1
        
    step_y = step_x * 2

    final_ascii_string = ""

    current_y = 0
    while current_y < original_height:
        current_line_string = ""
        current_x = 0
        while current_x < original_width:
            pixel_data = image_input[current_y][current_x]
            red_val = int(pixel_data[0])
            green_val = int(pixel_data[1])
            blue_val = int(pixel_data[2])
            
            brightness = calculate_luminance(red_val, green_val, blue_val)
            adjusted_brightness = apply_contrast_logic(brightness)
            character = get_char_for_pixel(adjusted_brightness)
            
            current_line_string = current_line_string + character
            current_x = current_x + step_x
            
        final_ascii_string = final_ascii_string + current_line_string + "\n"
        current_y = current_y + step_y
        
    filename = "ascii_art.txt"
    with open(filename, "w", encoding="utf-8") as file_handle:
        file_handle.write(final_ascii_string)

    return final_ascii_string, filename

default_image_path = "pirate.jpg"
if os.path.exists("pirate.jpg"):
    initial_image = default_image_path
else:
    initial_image = None

custom_css = """
.ascii-viewer textarea {
    font-family: 'Courier New', monospace !important;
    font-weight: 900 !important;
    font-size: 7px !important;
    line-height: 0.55 !important;
    white-space: pre !important; 
    overflow-x: scroll !important;
    background-color: white !important;
    color: black !important;
    height: 80vh !important;
}
"""

with gr.Blocks(title="Detailed ASCII Generator", theme=gr.themes.Soft(), css=custom_css) as app:
    gr.Markdown("## Pro ASCII Art Generator")

    with gr.Row():
        input_component = gr.Image(value=initial_image, label="Upload Image")
        output_component = gr.Textbox(
            label="ASCII Output", 
            lines=100, 
            elem_classes="ascii-viewer"
        )

    convert_button = gr.Button("Generate ASCII Art", variant="primary")
    download_component = gr.File(label="Download .txt File")

    convert_button.click(
        fn=convert_image_to_ascii,
        inputs=[input_component],
        outputs=[output_component, download_component]
    )

if __name__ == "__main__":
    app.launch()
