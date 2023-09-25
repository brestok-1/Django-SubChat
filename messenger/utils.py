import random

from messenger.models import CustomUser, Message
from PIL import Image, ImageDraw


def get_first_message_id(user: CustomUser) -> int:
    first_message_id = user.first_message_id
    if first_message_id == 0:
        last_message = Message.objects.last()
        if not last_message:
            first_message_id = 1
        else:
            last_message_id = last_message.id
            if last_message_id >= 10:
                first_message_id = last_message_id - 9
            else:
                first_message_id = 1
        user.last_message_id = first_message_id
        user.save()
    return first_message_id


def generate_user_thumbnail(first_letter: str):
    random_color = random.choice(["red", "yellow", "blue", "purple", "green"])
    image = Image.new("RGB", (200, 200), f"{random_color}")

    mask = Image.new("L", image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, image.size[0], image.size[1]), fill=255)

    image.putalpha(mask)

    letter = ImageDraw.Draw(image)
    letter.text((75, 75), f"{first_letter}", fill="white", font=("Arial", 100))

    image.save("avatar.png")
    return image
