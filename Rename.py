# -*- coding: cp936 -*-
import os

"""
���ܣ���path·���µ�jpg�ļ�����start_num��ʼ���ΰ�˳����������
ʹ�ã��޸�path��start_num��
"""


path = 'E:\\TrafficSing_Zhang\\Upslope\\new\\neg\\'
start_num = 0
def Rename(path, start_num):
    file_list = os.listdir(path)
    for i in range(len(file_list)):
        print i
        src_path = path + file_list[i]
        if os.path.exists(src_path):
            dst_path = path + str(start_num + i) + '.jpg'
            os.rename(src_path,dst_path)

Rename(path,start_num)
