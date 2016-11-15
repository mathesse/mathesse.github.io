import sys
sys.path.append('../')

import jieba
import jieba.analyse
from optparse import OptionParser

USAGE = "usage:    python extract_tags_with_weight.py [file name] -k [top k] -w [with weight=1 or 0]"

parser = OptionParser(USAGE)
parser.add_option("-k", dest="topK")
parser.add_option("-w", dest="withWeight")
opt, args = parser.parse_args()


if len(args) < 1:
    print(USAGE)
    sys.exit(1)

file_name = args[0]

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

#jieba.analyse.set_stop_words("../extra_dict/stop_words.txt")
#jieba.analyse.set_idf_path("../extra_dict/idf.txt.big");

tags = jieba.analyse.extract_tags(content, topK=topK, withWeight=withWeight)

sum_weight = 0 

with open('extract-tags-with-weight-result.txt','w') as output:
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