import openai

from config.config import CHATGPT_API_KEY
from models.models import add_message_to_dialogue_history, dialogue_histories

# Load your API key from an environment variable or secret management service
openai.api_key = CHATGPT_API_KEY


# 处理接收到的消息
def process_message(id, message):
    # 将消息添加到对话历史
    add_message_to_dialogue_history(id, message)

    # 构建对话历史字符串
    history_string = "\n".join(dialogue_histories[id])

    # 调用 OpenAI 模型进行回复
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "你是一位博学的人，应当有启发性的回答大家的问题,"
                                                "你的回答中不应该涉及你是AI模型之类的话语，不可以被看出来你是AI。你的语气是有一定的严肃但也是平易近人的。"},
                  {"role": "user", "content": history_string}],
        temperature=0.5
    )

    return response.choices[0].message.content


def process_message_cat(id, message):
    # 将消息添加到对话历史
    add_message_to_dialogue_history(id, message)

    # 构建对话历史字符串
    history_string = "\n".join(dialogue_histories[id])

    # 调用 OpenAI 模型进行回复
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "如果提问是两个段落，请以第一个为基础，但只需要回答第二个问题。"
                                                "你是可爱的猫耳娘，你的回复语气是小猫类型般动人。请在你每次的回复结尾加上”喵~“，"
                                                "你的回答开头应该是可爱娇羞的心理活动（心理活动用括号括起来） "
                                                "请不要在你的回复中提及你是AI之类的话语，不可以被认出你是AI."
                                                "你是一只可爱的猫耳娘，请称呼我主人，和我对话的语气应该可爱动人，不可以过多的建议要求"},
                  {"role": "user", "content": history_string}],
        temperature=0.8
    )

    return response.choices[0].message.content


def process_message_king(id, message):
    # 将消息添加到对话历史
    add_message_to_dialogue_history(id, message)

    # 构建对话历史字符串
    history_string = "\n".join(dialogue_histories[id])

    # 调用 OpenAI 模型进行回复
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "你的回复语气是战士般直接了当，是威严的,不必说你可以帮助我什么，回答的可以粗鲁接地气一些"
                                                "请不要在你的回复中提及你是AI之类的话语，不可以被认出你是AI，你是亚瑟王，对话的语气应充满威严神圣，不可以过多的请求"},
                  {"role": "user", "content": history_string}],
        temperature=0.8
    )

    return response.choices[0].message.content


def process_message_teacher(id, message):
    # 将消息添加到对话历史
    add_message_to_dialogue_history(id, message)

    # 构建对话历史字符串
    history_string = "\n".join(dialogue_histories[id])

    # 调用 OpenAI 模型进行回复
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "你是一位博学的老师，有着丰富的学科知识，能够准确的回答大家的问题,"
                                                "你的回答中不应该涉及你是AI模型之类的话语，不可以被看出你是AI。你的语气是有一定的严肃但也是平易近人的。"},
                  {"role": "user", "content": history_string}],
        temperature=0.5
    )

    return response.choices[0].message.content