import os
import random

trainval_percent = 0.2
train_percent = 0.8
xmlfilepath = '/home/yuhsi44165/NYCU/G2/VRDL/Final_project/YOLOX/datasets/data/VOCdevkit/VOC2007/Annotations'
txtsavepath = '/home/yuhsi44165/NYCU/G2/VRDL/Final_project/YOLOX/datasets/data/VOCdevkit/VOC2007/ImageSets'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftest = open('/home/yuhsi44165/NYCU/G2/VRDL/Final_project/YOLOX/datasets/data/VOCdevkit/VOC2007/ImageSets/Main/test.txt', 'w')
ftrain = open('/home/yuhsi44165/NYCU/G2/VRDL/Final_project/YOLOX/datasets/data/VOCdevkit/VOC2007/ImageSets/Main/trainval.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftest.write(name)
    else:
        ftrain.write(name)

ftrain.close()
ftest.close()
