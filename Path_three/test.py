import os
from modelscope.models import Model
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
from modelscope.preprocessors import TokenClassificationTransformersPreprocessor
def command(en_value):
    # 创建一个空列表来存储结果字典
    result = []
    # 遍历列表，步长为2，这样可以每次获取两个元素
    for i in range(0, len(en_value) - 1, 2):
        # 将每两个元素转换为字典格式
        cmd_dict = {"cmd": en_value[i], "object": en_value[i+1]}
        # 将字典添加到结果列表中
        result.append(cmd_dict)
    return result



# 词性标注
model_id = 'damo/nlp_lstmcrf_part-of-speech_chinese-news'
model = Model.from_pretrained(model_id)
tokenizer = TokenClassificationTransformersPreprocessor(model.model_dir)
pipeline_ins = pipeline(Tasks.part_of_speech, model=model, preprocessor=tokenizer)
while True:
    input_text = input("请输入要分析的文本：")
    result = pipeline_ins(input=input_text)
    os.system("cls")

    wordslist = []
    for index, item in enumerate(result['output']):
        if item['type'] == "VV":
          # 打印当前项的信息
          print("当前动词:",item['span'], item['type'],index)
          for i in range(index, len(result['output'])-1):
                # print(result['output'][i+1]['type'],result['output'][i+1]['span'])
                if result['output'][i+1]['type'] == "NN":
                    print("输出:",result['output'][i+1]['span'], result['output'][i+1]['type'])
                    wordslist.append(item['span'])
                    wordslist.append(result['output'][i+1]['span'])
                    if i+2 < len(result['output']) - 1:
                        if result['output'][i+2]['type'] != "CC":
                            break
                        else:
                            print("连词:",result['output'][i+1]['span'], result['output'][i+1]['type'])
                if result['output'][i+1]['type'] == "VV":
                    print("终止循环")
                    break
    print("最后:",wordslist) 
    ##########################
    # 还差翻译命令成英文
    ##########################
    commands = command(wordslist)
    print("最后输出：")
    print(commands)
                



