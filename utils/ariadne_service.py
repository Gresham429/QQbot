from graia.ariadne.app import Ariadne
from graia.ariadne.entry import config
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Plain
from graia.ariadne.message.element import Image
from graia.ariadne.message.element import Voice
from graia.ariadne.model import Friend, Group, Member
import time

from config.config import VERIFY_KEY, ACCOUNT
from controllers.controllers import generate_reply
from utils.pyttsx3_service import generate_voice
from utils.message_utils import parse_message_content
from utils.stable_diffusion_service import from_text_to_image
from utils.stable_diffusion_service import from_image_to_image

# 创建一个 Ariadne 实例
app = Ariadne(
    config(
        verify_key=VERIFY_KEY,  # 填入 mirai-http中设置的VerifyKey
        account=ACCOUNT,        # 你的机器人的 qq 号
    ),
)


@app.broadcast.receiver("FriendMessage")
async def friend_message_listener(app: Ariadne, friend: Friend, message: MessageChain):
    await app.send_friend_message(friend, "请稍后。。。")

    # 调用异步函数解析消息链
    data_coroutine = parse_message_content(message, app.account)
    data = await data_coroutine

    # 解包
    content, _, image_image_flag, img_bytes = data

    voice_flag = "/语音回复" in content
    text_image_flag = "/text-image" in content

    if image_image_flag:
        image_message = from_image_to_image(img_bytes)
        print("--------图片生成图片成功")

        time.sleep(2)
        await app.send_group_message(group, MessageChain(Image(base64=image_message)))
        time.sleep(1)

    reply = generate_reply(friend.id, content)

    if not voice_flag and not text_image_flag and not image_image_flag:
        print("--------生成文本回复成功")
        time.sleep(2)
        await app.send_group_message(group, MessageChain([Plain(reply)]))
        time.sleep(1)
    elif voice_flag:
        audio_data = generate_voice(reply)
        print("--------生成语音回复成功")

        time.sleep(2)
        await app.send_group_message(group, MessageChain(Voice(data_bytes=audio_data)))
        time.sleep(1)
    elif text_image_flag:
        image_message = from_text_to_image(content)
        print("--------文本生成图片成功")

        time.sleep(2)
        await app.send_group_message(group, MessageChain(Image(base64=image_message)))
        time.sleep(1)

    time.sleep(2)
    await app.send_friend_message(friend, MessageChain([Plain(reply)]))


@app.broadcast.receiver("GroupMessage")
async def Group_message_listener(app: Ariadne, group: Group, member: Member, message: MessageChain):
    sender_name = member.name

    # 调用异步函数解析消息链
    data_coroutine = parse_message_content(message, app.account)
    data = await data_coroutine

    # 解包
    content, at_me, image_image_flag, img_bytes = data

    voice_flag = "/语音回复" in content
    text_image_flag = "/text-image" in content

    if image_image_flag:
        image_message = from_image_to_image(img_bytes)
        print("--------图片生成图片成功")

        time.sleep(2)
        await app.send_group_message(group, MessageChain(Image(base64=image_message)))
        time.sleep(1)

    if at_me:
        print("----正在生成回复")

        reply = f"回复{sender_name}：\n "
        reply += generate_reply(member.id, content)

        if not voice_flag and not text_image_flag and not image_image_flag:
            print("--------生成文本回复成功")
            time.sleep(2)
            await app.send_group_message(group, MessageChain([Plain(reply)]))
            time.sleep(1)
        elif voice_flag:
            audio_data = generate_voice(reply)
            print("--------生成语音回复成功")

            time.sleep(2)
            await app.send_group_message(group, MessageChain(Voice(data_bytes=audio_data)))
            time.sleep(1)
        elif text_image_flag:
            image_message = from_text_to_image(content)
            print("--------文本生成图片成功")

            time.sleep(2)
            await app.send_group_message(group, MessageChain(Image(base64=image_message)))
            time.sleep(1)