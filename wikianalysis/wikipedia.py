import os
import logging

def ReadWikitext():
    num = 0
    lines = open(r'C:/Users/YJY/Desktop/text.txt', 'r', encoding="utf-8").readlines()
    for line in lines:
        num += 1
        title = line.split()[0]
        content = ','.join(line.split())
        page = int(num/10) + 1
        #每10条作为一个文件夹
        if (num % 10) == 0:
            logging.info("---Save %s articles---" % num)
            print("---Save %s articles---" % num)
        # print(title)
        # print(content)
        path = r'C:/Users/YJY/Desktop/wiki'
        path1 = ''.join([path + '/' + str(page)])
        if not os.path.exists(path1):
            os.makedirs(path1)
        name = ''.join([path1, '/', title, '.txt'])
        with open(name, 'w', encoding="utf-8") as f:
            f.write(title + '\r\n')
            f.write(content)


ReadWikitext()
