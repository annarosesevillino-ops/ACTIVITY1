from PIL import Image, ImageDraw, ImageFont
import os

# === INPUT AND OUTPUT FILES ===
input_path = "MEME.jpg"          # Place your picture in the same folder as this .py file
output_path = "BSCS3A_SevillinoAnnarose_Meme.png"

# === CAPTION TEXT ===
caption = "POV: Sabi nila fun lang daw... bakit ganito?"

# === LOAD IMAGE ===
img = Image.open(input_path).convert("RGBA")
W, H = img.size
draw = ImageDraw.Draw(img)

# === FONT SETTINGS (Windows) ===
font_path = "C:\\Windows\\Fonts\\arialbd.ttf"  # Arial Bold
font_size = max(24, W // 18)                   # adjusts based on image size
font = ImageFont.truetype(font_path, font_size)

# === WRAP TEXT FUNCTION ===
def wrap_text(text, font, max_width):
    words = text.split()
    lines, line = [], words[0]
    for w in words[1:]:
        test_line = line + " " + w
        test_width = font.getbbox(test_line)[2]
        if test_width <= max_width:
            line = test_line
        else:
            lines.append(line)
            line = w
    lines.append(line)
    return lines

max_text_width = int(W * 0.9)
lines = wrap_text(caption, font, max_text_width)

# === CALCULATE POSITION ===
line_height = font.getbbox("Ay")[3] - font.getbbox("Ay")[1]
padding = int(line_height * 0.6)
text_block_height = line_height * len(lines) + padding * 2
margin = int(H * 0.03)
x0 = int(W * 0.05)
y0 = H - text_block_height - margin  # bottom placement

# === BACKGROUND BOX FOR READABILITY ===
box_width = W - 2 * x0
rectangle = Image.new("RGBA", (box_width, text_block_height), (0, 0, 0, 150))
img.paste(rectangle, (x0, y0), rectangle)

# === DRAW TEXT (CENTERED) ===
current_y = y0 + padding
for line in lines:
    w_line = font.getbbox(line)[2]
    x = (W - w_line) // 2
    draw.text((x, current_y), line, font=font, fill="white",
              stroke_width=2, stroke_fill="black")
    current_y += line_height

# === SAVE FINAL OUTPUT ===
img.convert("RGB").save(output_path, format="PNG")
print(f"✅ Meme created and saved as {output_path}")

# === OPEN IN PHOTOS (Windows) ===
os.startfile(output_path)
