import logging
import sys
from gensim.corpora import WikiCorpus

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', level=logging.INFO)
'''
    extract data from wiki dumps(*articles.xml.bz2) by gensim.
    @2019-3-26
'''


def help():
    print("Usage: python wikipro.py zhwiki-20190320-pages-articles-multistream.xml.bz2 wiki.zh.txt")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        help()
        sys.exit(1)
    logging.info("running %s" % ' '.join(sys.argv))
    inp, outp = sys.argv[1:3]
    i = 0

    output = open(outp, 'w', encoding='utf8')
    wiki = WikiCorpus(inp, lemmatize=False, dictionary={})
    for text in wiki.get_texts():
        output.write(" ".join(text) + "\n")
        i = i + 1
        if (i % 10000 == 0):
            logging.info("Save " + str(i) + " articles")
    output.close()
    logging.info("Finished saved " + str(i) + "articles")

    # 命令行下运行
    # python wikipro.py zhwiki-20190320-pages-articles-multistream.xml.bz2 wiki.zh.txt
    #本脚本将xml转换位txt
    #然后用opencc将繁体变简体
    #之后运行wikipedia逐行读取（其每一行为一个词条），并存储为一个文本文件
