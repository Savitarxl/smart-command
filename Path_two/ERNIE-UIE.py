from pprint import pprint
from paddlenlp import Taskflow
import warnings
# 忽略警告信息
warnings.simplefilter('ignore', category=FutureWarning)
warnings.filterwarnings('ignore', category=FutureWarning, module='transformers')

schema =['开关设备']
ie = Taskflow('information_extraction', schema=schema, model='uie-base')
ie.set_schema(schema) 
pprint(ie("天气太热了，我要开空调，哦，忘记了，开启风扇，同时关闭电视"))

# from paddlenlp import Taskflow
# ner = Taskflow("ner")
# print(ner("天气太热了，我要开空调，哦，忘记了，开启风扇，同时关闭电视"))

