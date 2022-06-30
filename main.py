import os
import re
import cv2
import numpy as np
#build excel and

count = 0
pic_addr = "E:/tzuwen/tree_segmentation2/Unet_tree_2/data/HSV6_test/test/results/2022-01-12_2116_0_predict.png"
#read each pixel and count
# rootdir = "E:\\tzuwen\\tree_segmentation2\Unet_tree_2\data\membrane\\test_2-19\\results"
# for root, subFolders, files in os.walk(rootdir):
#     for pic in files:
#         if re.search(r'([a-zA-Z0-9\s_\\.\-\(\):])+(.jpg|.jpeg|.png)$', pic):


img = cv2.imread(pic_addr)
rows,cols,_ = img.shape

for i in range(rows):
    for j in range(cols):
        k = img[i,j]
        if np.any(k):  #no black
            #print(k)
            count += 1

ratio = count/(rows*cols)
print(count,ratio)