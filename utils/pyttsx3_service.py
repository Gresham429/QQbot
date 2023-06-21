import pyttsx3

from graiax import silkcoder


def generate_voice(message: str):
    # 创建 pyttsx3 引擎
    engine = pyttsx3.init()

    # 设置频率
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 17)

    # 将文本转换为语音
    engine.save_to_file(message, ".\\voice\\output.wav")
    engine.runAndWait()

    return silkcoder.encode(".\\voice\\output.wav")
