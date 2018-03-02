# -*- coding: utf-8 -*-

""""
Masked wordcloud
================
Using a mask you can generate wordclouds in arbitrary shapes.
"""

from os import path
from PIL import Image
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import codecs
import random
import jieba.analyse

def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(%d, 100%%, 50%%)" % random.randint(220, 280)

d = path.dirname(__file__)
# 处理图像
pic_mask = np.array(Image.open(path.join(d, "huge.png")))

with open('wash.txt','r') as f:
    seg_list =jieba.analyse.extract_tags(f.read(), topK=20, withWeight=True, allowPOS=())
frequencies={}
for tag in seg_list:
        frequencies[tag[0]] = float(tag[1])

wordcloud = WordCloud().fit_words(frequencies)
wordcloud = WordCloud(background_color="white",mask=pic_mask,
                      max_font_size=100,relative_scaling=0.5,
                      scale=2).fit_words(frequencies)

plt.figure()
plt.imshow(wordcloud.recolor(color_func=grey_color_func, random_state=3))
plt.axis("off")
plt.show()
#plt.savefig('./wordcloud/'+'test'+'.png')