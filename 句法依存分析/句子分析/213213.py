'''
ltp里面的句法依存分析


https://www.jianshu.com/p/867478f0e674         接口说明.
'''


# -*- coding: utf-8 -*-
import os

## 加载模型文件
LTP_DATA_DIR = '/ltp_data_v3.4.0'  # ltp模型目录的路径
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`
par_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')  # 依存句法分析模型路径，模型名称为`parser.model`



## 词性标注
from pyltp import Postagger



from pyltp import Segmentor









par_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')  # 依存句法分析模型路径，模型名称为`parser.model`
from pyltp import Segmentor
segmentor = Segmentor()  # 初始化实例
segmentor.load_with_lexicon(cws_model_path,'dict1.txt')  # 加载模型
from pyltp import Parser
parser = Parser() # 初始化实例
parser.load(par_model_path)  # 加载模型
words = list(segmentor.segment('欧几里得是西元前三世纪的希腊数学家.')) # 分词

## 词性标注
from pyltp import Postagger
postagger = Postagger() # 初始化实例
postagger.load(pos_model_path)  # 加载模型

postags = postagger.postag(words)  # 词性标注
tags=list(postags)
print(tags,"词性标注")


## 依存句法分析
from pyltp import Parser
parser = Parser() # 初始化实例
parser.load(par_model_path)  # 加载模型


arcs = parser.parse(words, postags)  # 句法分析

rely_id = [arc.head for arc in arcs]    # 提取依存父节点id
relation = [arc.relation for arc in arcs]   # 提取依存关系
heads = ['Root' if id == 0 else words[id-1] for id in rely_id]  # 匹配依存父节点词语

for i in range(len(words)):
    print (relation[i] + '(' + words[i] + ', ' + heads[i] + ')')

parser.release()  # 释放模型


'''
结果说明:
SBV(欧几里得, 是)
HED(是, Root)
ATT(西元前, 世纪)
ATT(三, 世纪)
ATT(世纪, 数学家)
RAD(的, 世纪)
ATT(希腊, 数学家)
VOB(数学家, 是)
WP(。, 是)

以上是结果表:




说明在这里:
https://blog.csdn.net/sinat_33741547/article/details/79258045



写下来:
sbv:主谓结构          SBV(欧几里得, 是)         subject-------verb
vob:动宾关系        verb -------  object
iob:见宾关系.   间接宾语.         句子中有两个宾语时，其中指物或指事的就是直接宾语。指人（或动物）的就是间接宾语。        所以简介宾语用来指人的宾语.


fob:前置宾语 宾语放到verb前面         front ---obj
hed:核心关系
att: 定语关系.
rad:又附加关系.
wp:标点符号

dbl:2个动词.



'''





