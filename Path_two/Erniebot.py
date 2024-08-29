# import erniebot
# erniebot.api_type = 'aistudio'
# erniebot.access_token = 'f9dbb366b5f2ef2cb3b60fd1718a6f14042e21cc'
# response = erniebot.ChatCompletion.create(
#     model='ernie-turbo',
#     messages=[{
#         'role': 'user',
#         'content': "请问你是谁？"
#     }, {
#         'role': 'assistant',
#         'content':'我是一个指令转换器，比如如打开空调--> {"cmd":"open","object":"AirConditioner"}"，关闭空调--> {"cmd":"close","object":"AirConditioner"}；设置翻译语言为中文--> {"cmd":"translation","object":"chinese"},设置翻译语言为英文--> {"cmd":"translation","object":"English"}等指令转换，你有什么指令我将直接返回转换后的指令'
#     }, {
#         'role': 'user',
#         'content': "翻译成英语"
#     }])
# print()

import erniebot
erniebot.api_type = 'aistudio'
erniebot.access_token = 'f9dbb366b5f2ef2cb3b60fd1718a6f14042e21cc'

def get_response(messages):
    # print(messages)
    # 创建对话请求
    response = erniebot.ChatCompletion.create(
        model='ernie-turbo',
        messages=messages
    )
    return response.get_result()

def main():
    messages = [
        {'role': 'user', 'content': "请问你是谁？"},
        {'role': 'assistant', 'content': '我是一个指令转换器，比如将打开空调转换成{"cmd":"open","object":"AirConditioner"}，将关闭风扇转换成{"cmd":"close","object":"Fan"}；将设置翻译语言为中文转换成{"cmd":"translation","object":"chinese"},将设置翻译语言为英文转换成{"cmd":"translation","object":"English"}等指令转换，你的指令我都将直接返回转换后的指令，不会返回其余任何文本'},
        {'role': 'user', 'content': "打开空调"},
        {'role': 'assistant', 'content': '{"cmd":"open","object":"AirConditioner"}'},
        {'role': 'user', 'content': "关闭风扇"},
        {'role': 'assistant', 'content': '{"cmd":"close","object":"Fan"}'},
        {'role': 'user', 'content': "设置翻译语言为英文"},
        {'role': 'assistant', 'content': '{"cmd":"translation","object":"English"}'},
        {'role': 'user', 'content': "将语言设置成俄文"},
        {'role': 'assistant', 'content': '{"cmd":"translation","object":"Russian"}'},
    ]
    while True:
        user_input = input("请输入您的指令 (输入 'exit' 退出): ")
        if user_input.lower() == 'exit':
            break
        # 添加用户的问题到消息列表
        messages.append({'role': 'user', 'content': user_input})
        # 获取ErnieBot的响应
        response = get_response(messages)
        # 打印ErnieBot的回答
        print("ErnieBot:", response)
        # 添加ErnieBot的回答到消息列表以便继续对话
        messages.append({'role': 'assistant', 'content': response})
        
if __name__ == '__main__':
    main()