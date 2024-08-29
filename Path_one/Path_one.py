# 思路：把特殊词典分为动词和名词，√
# 提取出特殊词汇时带上index信息，作为后续拼接的顺序 √
# 动词index优先将index小于它的名词全部冠上它的值 √
import os
from modelscope.models import Model
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
from transformers import AutoTokenizer
import warnings
# 忽略警告信息
warnings.simplefilter('ignore', category=FutureWarning)
warnings.filterwarnings('ignore', category=FutureWarning, module='transformers')
# 模型ID
model_id = 'damo/nlp_structbert_word-segmentation_chinese-base'
# 加载模型
model = Model.from_pretrained(model_id)
# 使用pipeline进行分词
pipeline_ins = pipeline(task=Tasks.word_segmentation, model=model)

# 提取特定的词语
def extract_specific_words(words_list, specific_words_dict):
    values = [item for sublist in specific_words_dict.values() for item in sublist]
    extracted_words = []
    for i ,word in enumerate(words_list):
        if word in values:
            extracted_words.append([word,i])
    # extracted_words = [word for word in words_list if word in values]
    return extracted_words

def find_keys_by_values(extracted_words, specific_words_dict):
    result = []
    # 遍历提取的词语列表
    for word in extracted_words:
        # 遍历字典中的每个键值对
        for key, value_list in specific_words_dict.items():
            # print("word:",word)
            # print("value_list:",value_list)
            # 如果提取的词语在当前键对应的列表中，添加键到结果字典
            if word in value_list:
                result.append(key)  # 添加键到现有列表
                # print([key])
                # print("result:",result)
                break
    return result

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

def resort(extracted_words_v, extracted_words_n):
    total = []
    time = 0
    for i in extracted_words_v:
        for j in extracted_words_n:
        #    print("----------------------")
        #    print(i[1],j[1])
        #    print("----------------------")
           if int(i[1])<int(j[1]):
               total.append(j[0])
               total.append(i[0])
               time = time + 1
        del extracted_words_n[0:time]
        time = 0
    return total
# 读取并解析文本文件
def read_dict_from_txt(filename):
    my_dict = {}
    
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            # 去除行尾的换行符
            line = line.strip()
            # 分割键和值
            key, values_str = line.split(':')
            # 将值字符串分割成列表
            values = [value.strip() for value in values_str.split(',')]
            # 添加到字典中
            my_dict[key] = values
    
    return my_dict

# 读取文件
filename_v = r'D:\Internship\smart command\Path_one\V.txt'
filename_n = r'D:\Internship\smart command\Path_one\N.txt'
Dict_v = read_dict_from_txt(filename_v)
Dict_n = read_dict_from_txt(filename_n)

# 定义要提取的特定词语及其英文翻译
# 动作
specific_words_dict_v= Dict_v
# 实体
specific_words_dict_n= Dict_n

os.system("cls")
while True:
    print("输入：")
    text = input()  # 用户输入文本
    result = pipeline_ins(text)  # 分词结果
    if result['output'] == []:
        print("输入内容没有明确命令，请重新输入！")
        continue
    # print("原始文本：")
    # print(result['output'])
    # print(all_values)
    # 调用函数提取特定词语
    extracted_words_v = extract_specific_words(result['output'], specific_words_dict_v)[::-1]
    extracted_words_n = extract_specific_words(result['output'], specific_words_dict_n)[::-1]
    # print("提取的词语：")
    # print(extracted_words_v)
    # print(extracted_words_n)
    total = resort(extracted_words_v, extracted_words_n)[::-1]
    # print(total)
    specific_words_dict = {**specific_words_dict_v, **specific_words_dict_n}
    en_extracted_words = find_keys_by_values(total, specific_words_dict)
    # print(en_extracted_words)
    commands = command(en_extracted_words)
    if commands == []:
        print("输入内容没有明确命令，请重新输入！")
        continue
    print("输出：")
    print(commands)
    print("------------------------------------------------\n")


