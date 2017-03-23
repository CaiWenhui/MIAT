# -*- coding:gb2312 -*-
import os
import cv2

"""
���ܣ���load_path���ļ�ת��Ϊָ����С������save_path��
ʹ�ã�load_path  ����·��
      save_path  ����·��
      img_width  ͼ����
      img_height ͼ��߶�
"""
load_path = 'H:\\TrafficSignData\\TrafficSignData\\15 ע������\\'
save_path = 'H:\\TrafficSignData\\Norm_DATA\\15 ע������\\'
img_width = 640
img_height = 960


file_list = os.listdir(load_path)
for name in file_list:
    print name
    img = cv2.imread(load_path + name, cv2.IMREAD_COLOR)
    # print img.shape
    if (img.shape[0]) > (img.shape[1]):
        resized = cv2.resize(img,(img_width,img_height),cv2.INTER_CUBIC)
    elif (img.shape[0]) < (img.shape[1]):
        resized = cv2.resize(img,(img_height,img_width),cv2.INTER_CUBIC)

    cv2.imwrite(save_path + name, resized)
