import random

from messenger.models import CustomUser, Message
from PIL import Image, ImageDraw, ImageFont, ImageOps


def get_first_message_id(user: CustomUser, count: int = 10) -> int:
    first_message_id = user.first_message_id
    if first_message_id == 0:
        last_message = Message.objects.last()
        if not last_message:
            first_message_id = 1
        else:
            last_message_id = last_message.id
            if last_message_id >= count:
                first_message_id = last_message_id - count + 1
            else:
                first_message_id = 1
        user.first_message_id = first_message_id
        user.save()
    return first_message_id


def generate_user_thumbnail(first_letter: str, font_size: int = 140):
    random_color = random.choice(["red", "orange", "blue", "purple", "green"])
    image = Image.new("RGB", (200, 200), f"{random_color}")

    mask = Image.new("L", image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, image.size[0], image.size[1]), fill=255)

    image.putalpha(mask)

    font = ImageFont.truetype("static/ArialRegular.ttf", font_size)
    left, top, width, height = font.getbbox(first_letter)
    x_offset = (image.size[0] - width - left) // 2
    y_offset = (image.size[1] - height - top) // 2
    letter = ImageDraw.Draw(image)
    letter.text((x_offset, y_offset), f"{first_letter}", fill="white", font=font)

    image.save("avatar.png")
    return image
