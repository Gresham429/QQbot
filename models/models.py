import collections

# 根据不同的QQ账号构建相应的历史对话，采用字典对整个历史记录存储
dialogue_histories = {}


def add_message_to_dialogue_history(id, message):
    # 检查该 ID 是否已存在对话历史记录，如果不存在则创建一个空的双向队列
    if id not in dialogue_histories:
        dialogue_histories[id] = collections.deque(maxlen=2)

    # 将消息添加到对应的 ID 的对话历史记录中
    dialogue_histories[id].append(message)