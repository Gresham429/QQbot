from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import At
from graia.ariadne.message.element import Image
from graia.ariadne.message.element import Plain


async def parse_message_content(message: MessageChain, account: int) -> str:
    """
    解析消息内容，将消息链中的文本元素拼接为字符串并返回。
    """
    content = ""
    at_me = False
    image = False
    img_bytes = None

    for element in message:
        if isinstance(element, Plain):
            content += element.text

        if isinstance(element, At) and not at_me:
            if element.target == account:
                at_me = True
        if isinstance(element, Image) and not image:
            image = True
            img_bytes = await element.get_bytes()
    return content, at_me, image, img_bytes
