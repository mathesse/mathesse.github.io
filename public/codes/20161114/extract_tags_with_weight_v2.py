# or !/usr/bin/env python
# or -*- coding: utf-8 -*- 

# title: extract_tags_with_weight_v2.py
# by Sian, Nov 14, 2016

import sys
# sys.path.append('../')
from os import path

import jieba
import jieba.analyse
from optparse import OptionParser
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from scipy.misc import imread
# import codecs
import chardet

# obtain current path
# __file__ is current file, report during ide running, could be replaced as
# d = path.dirname('.')
d = path.dirname(__file__)


USAGE = "usage:    python extract_tags_with_weight_v2.py -i [input] -o [output] -m [mask input] -p [cloud output] -k [top k] -w [with weight=1 or 0]"

parser = OptionParser(USAGE)
parser.add_option("-i", dest="file_name")
parser.add_option("-o", dest="output_name")
parser.add_option("-m", dest="mask_name")
parser.add_option("-p", dest="pic_name")
parser.add_option("-k", dest="topK")
parser.add_option("-w", dest="withWeight")
opt, args = parser.parse_args()

if opt.file_name is None:
    print(USAGE)
    sys.exit(1)

file_name = opt.file_name
output_name = opt.output_name
mask_name = opt.mask_name
pic_name = opt.pic_name

print ('\n\t[INTPUT] = %s\t [OUTPUT] = %s\n' % (file_name, output_name))
print ('\t[IMAGE MASK] = %s\t [CLOUD PIC] = %s\n' % (mask_name, pic_name))
print ('\t[KEYWORDS COUNT] = %f\t [WITH WEIGHT (1 OR 0)] = %f\n' % (int(opt.topK), int(opt.withWeight)))

if opt.topK is None:
    topK = 10
else:
    topK = int(opt.topK)

if opt.withWeight is None:
    withWeight = False
else:
    if int(opt.withWeight) is 1:
        withWeight = True
    else:
        withWeight = False

content = open(file_name, 'rb').read()

detect = chardet.detect(content)
print ('\t[CHAR TYPE DETECTION] = %s\n' % detect['encoding'])

# stop words
#jieba.analyse.set_stop_words("../extra_dict/stop_words.txt")

# user dict
#jieba.analyse.set_idf_path("../extra_dict/idf.txt.big");

tags = jieba.analyse.extract_tags(content, topK=topK, withWeight=withWeight)

# write to output file
sum_weight = 0 

with open(output_name,'w') as output:
    if withWeight is True:
        for tag in tags:
            #print("tag: %s\t\t weight: %f" % (tag[0],tag[1]))
            output.write("tag: %s\t\t weight: \t%f\n" % (tag[0].encode('utf-8'),tag[1]))
            sum_weight=sum_weight+tag[1]
    else:
        #print(",".join(tags))
        output.write(",".join(tags).encode('utf-8'))
    output.write("\nsum of weight: %f\n" % sum_weight)

output.close()


# read the mask image
coloring = imread(path.join(d, mask_name))

# wordcloud

image_colors = ImageColorGenerator(coloring)

wordcloud = WordCloud(
    font_path = "/Users/hessiatrix/Downloads/simsun.ttc",
    background_color = 'white',
    mask = coloring,
    color_func=image_colors,
    max_font_size = 100,
    random_state = 42).generate_from_frequencies(tags)


plt.imshow(wordcloud)
plt.axis("off")
plt.figure()
plt.show()

# save pic
wordcloud.to_file(path.join(d, pic_name))

plt.close()







