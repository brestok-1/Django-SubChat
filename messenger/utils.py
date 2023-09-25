from messenger.models import CustomUser, Message


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
