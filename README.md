"# QQ_chat_bot" 

## 一款基于mirai框架以及mirai-api-http插件的QQbot

#### 1.环境配置（目前仅支持Windows）

1. 语言环境 Java >= 11、python >= 3.9。
2. 配置好mirai框架以及相应的mirai-api-http插件([mamoe/mirai: 高效率 QQ 机器人支持库 (github.com)](https://github.com/mamoe/mirai))。

#### 2.项目下载与配置

1. 安装项目以及python依赖包。

```shell
git clone https://github.com/Gresham429/QQ_chat_bot.git
pip install -r requirements.txt
```

2. 配置config：打开config文件夹下的config.py，根据注释完成配置。
3. 在根目录下创建两个文件夹：image（用于存放AI绘制的图片）、voice（用于存放语音回复合成的音频）

#### 3.运行

1. 先启动mirai连接QQ。

2. 启动main.py

   ```shell
   在main.py所在的目录下打开终端
   python main.py
   ```

#### 4.测试

###### 命令前缀

1. 四种角色：/cat、/king、/teacher、正常模式（不加前缀）
2. 语音回复：/语音回复
3. 根据文本生成图片：/text-image
4. 根据图片生成图片：直接发图就行

私聊直接加好友就可以聊，群聊需要在最前面@它（长按头像那种蓝色的@）



## License
MIT License
See the [LICENSE](./LICENSE) file for details.

