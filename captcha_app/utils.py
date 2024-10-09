import base64
import random
import string
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def generate_captcha_text(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def generate_captcha_image(text):
    width, height = 250, 90
    image = Image.new('RGB', (width, height), color=(255, 255, 255))

    font_path = "captcha_app/DejaVuSans-Bold.ttf"  # Update with your font path
    font = ImageFont.truetype(font_path, 40)

    draw = ImageDraw.Draw(image)

    # Background noise
    for _ in range(1000):
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.point((x, y), fill=(random.randint(150, 255), random.randint(150, 255), random.randint(150, 255)))

    # Draw text with random color and slight offset
    for i, char in enumerate(text):
        char_x = 20 + i * (width - 40) // len(text)
        char_y = random.randint(0, height - 50)
        draw.text((char_x, char_y), char, font=font, fill=(random.randint(0, 150), random.randint(0, 150), random.randint(0, 150)))

    # Add random lines
    for _ in range(5):
        start_point = (random.randint(0, width), random.randint(0, height))
        end_point = (random.randint(0, width), random.randint(0, height))
        draw.line([start_point, end_point], fill=(0, 0, 0), width=2)

    # Add random ellipses
    for _ in range(3):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = x1 + random.randint(10, 30)
        y2 = y1 + random.randint(10, 30)
        draw.ellipse([x1, y1, x2, y2], outline=(0, 0, 0), width=1)

    # Apply slight blur to the entire image
    image = image.filter(ImageFilter.GaussianBlur(1))

    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

    return img_str
