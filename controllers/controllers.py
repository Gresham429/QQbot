from utils.openai_service import process_message, process_message_teacher, process_message_king, process_message_cat


def determine(message: str):
    if "/teacher" in message:
        return 0
    elif "/cat" in message:
        return 1
    elif "/king" in message:
        return 2
    else:
        return 4


def generate_reply(id, content: str):
    if determine(content) == 0:
        content = content.replace("/teacher", "")
        reply = process_message_teacher(id, content)
    elif determine(content) == 1:
        content = content.replace("/cat", "")
        reply = process_message_cat(id, content)
    elif determine(content) == 2:
        content = content.replace("/king", "")
        reply = process_message_king(id, content)
    else:
        reply = process_message(id, content)

    return reply
