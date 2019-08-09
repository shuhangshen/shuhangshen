# 文件名 jieba_cut.py
import jieba
import jieba.analyse
import jieba.posseg as pseg
import codecs, sys


def cut_words(sentence):
    #print sentence
    return " ".join(jieba.cut(sentence)).encode('utf-8')


f = codecs.open('wiki.zh.simple.txt', 'r', encoding="utf8")
target = codecs.open("wiki.zh.simple.seg.txt", 'w', encoding="utf8")
print('open files')
line_num = 1
line = f.readline()
while line:
    if(line_num % 1000 == 0):
        print('---- processing', line_num, 'article----------------')
    line_seg = " ".join(jieba.cut(line))
    target.writelines(line_seg)
    line_num = line_num + 1
    line = f.readline()
f.close()
target.close()
exit()

# 原文：https://blog.csdn.net/weixin_40871455/article/details/88822290
