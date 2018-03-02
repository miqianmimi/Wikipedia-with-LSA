# -*- coding: utf-8 -*-
#-*- encoding:utf-8 -*-  
import re

file_name = r"page25.txt"

with open(file_name,"r") as fl:
    raw = fl.read()
fl.close()
data = re.sub('<!-- ', '===', raw)
data = re.sub('-->','===',data)

dr = re.compile(r'<[^>]+>',re.S)
dd = dr.sub('',data)


dr2 = re.compile(r'\[[^\]]+\]',re.S)
dd2 = dr2.sub('',dd)

dr3 = re.compile(r'\{[^\}]+\}',re.S)
dd3 = dr3.sub('',dd2)

dr4 = re.compile(r'\}',re.S)
dd4 = dr4.sub('',dd3)

dr5 = re.compile(r'\]',re.S)
dd5 = dr5.sub('',dd4)

file = open("wash.txt","w")
file.write(dd5)
file.close()
