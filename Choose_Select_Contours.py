# -*- coding: cp936 -*-
import cv2
import numpy as np
from os import listdir
from sys import exit

"""
���ܣ���ȡpath·���µ�jpg�ļ����ҳ���ͼƬ��Ϣ�����е�������
      �ֶ�ѡ�񲢱�����ʵĽ�ͨ��־��Ƭ��
ʹ�ã�(1)�޸� "����" path
      (2)���г���
      (3)������ʵĽ�ͨ��־��Ƭ����ڲ�����
      (4)��ѡ����ʣ����� 's' ������
      (5)���¡�q' ������������ǰ��Ƭ�����Ƭ
      (5)���¡�b' ������ֱ��������ǰ��Ƭ��һЩG�������ܳ��ֵ���Ƭ��
ע�⣺(1)���ڶ�д txt �ļ������ txt �ļ��Ѿ����ڣ��������н�����δ����ȫ���ر�ʱ��
         ���ܻ���ֿհ��ĵ������󣬽�������ȫ�رգ�ɱ�����̣�������
         �ٴδ򿪸� txt �ĵ�ʱ���������ʾ��
         ���Ƽ�->���ֶ��½� txt �ļ����ó����Զ��½���
    
"""

order_num = 0 
read_path =  'H:\\TrafficSignData\' 
save_path =  'E:\\TL\\' 
txt_path  =  'E:\\TL\\labels.txt'


# ----------- Mouse response function ------------------
# ------------------ �����Ӧ���� -----------------------
def choose_contours(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # ix, iy Ϊ��갴��ʱ��λ�� 
        ix, iy = -1,-1
        ix ,iy = x, y
        for i in contours:
            cnt = i
            x,y,w,h = cv2.boundingRect(cnt)
            # �ж���갴�µ�λ���Ƿ���ĳ����Ƭ��֮��
            if (x < ix <x+w) and (y<iy<y+h):

                # ��ʾ��Ƭ��
                key = param[1][y:y+h,x:x+w]
                cv2.imshow('piece',key)

                # ������Ӧ
                k= cv2.waitKey(0)&0xFF
                if k == ord('Q'):
                    cv2.destroyWindow('piece')
                elif k == ord('W'):
                    # ������Ƭ��
                    # �� ��+�� ������
                    param[0] += 1

                    save_pic =  save_path + str(order_num) + param[0]*'+'+ '.jpg'
                    cv2.imwrite(save_pic,key)
                    cv2.destroyAllWindows()
                    
                    # --- txt �ļ�д��------
                    
                    add_txt = str(order_num)+".jpg "
                    txt.write(add_txt)
                    add_txt = str(x) + " "+str(y)+" "+str(w)+" "+str(h)
                    txt.write(add_txt)
                    txt.write("\n")
                    # ---- д����� --------

                    cv2.rectangle(show,(x,y),(x+w,y+h),(255,255,255),2)
                    cv2.imshow(str(order_num) + '.jpg',show)
                    key = []
                    
                    cv2.setMouseCallback(str(order_num) + '.jpg', choose_contours,[plus,save])
                    
#                elif k == ord('E'):
#                    break
                elif k == ord('E'):
                    txt.close()
                    cv2.destroyAllWindows()
                    exit()
                    
                        
# --------------- main project  ------------------
# ------------------- ������ -----------------
# ��ȡ��·������Ҫ�������Ƭ��
file_list = listdir(read_path)
Len = len(file_list)

# �򿪱�����Ϣ�� txt �ļ��� ��������ڸ��ļ������Զ�����һ�µ� txt �ļ�
start_picture = int(raw_input('start pic is ?\n'))
if start_picture == 1:
    txt = open(txt_path,'w')
else :
    txt = open(txt_path,'a')


for order_num in xrange(start_picture,Len+1):
    plus= 0

    read_pic =  read_path + str(order_num) + '.jpg' 
    
    img =cv2.imread(read_pic)
    img = cv2.resize(img,(960,640),cv2.INTER_LINEAR )
    save = img.copy()
    show = img.copy()
    # �ַַַַַַַַַַַַַַַַַַ�
    newImg = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    ret,thresh = cv2.threshold(newImg,127,255,0)
    _, contours, hierarchy = cv2.findContours(thresh, 1,2)
    for i in contours:
        cnt = i
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(show,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.destroyAllWindows()
    cv2.imshow(str(order_num) + '.jpg',show)
    k = cv2.waitKey(0)&0xFF
    while k != ord('Y'):
        if k == ord('A'):
            show = img.copy()
            newImg = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
            ret,thresh = cv2.threshold(newImg,127,255,0)
            _, contours, hierarchy = cv2.findContours(thresh, 1,2)
            for i in contours:
                cnt = i
                x,y,w,h = cv2.boundingRect(cnt)
                cv2.rectangle(show,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.destroyAllWindows()
            cv2.imshow(str(order_num) + '.jpg',show)
            k = cv2.waitKey(0)&0xFF
        elif k == ord('S'):
            show = img.copy()
            thresh = cv2.Canny(img,100,200)
            _, contours, hierarchy = cv2.findContours(thresh, 1,2)
            for i in contours:
                cnt = i
                x,y,w,h = cv2.boundingRect(cnt)
                cv2.rectangle(show,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.destroyAllWindows()
            cv2.imshow(str(order_num) + '.jpg',show)
            k = cv2.waitKey(0)&0xFF
        elif k == ord('D'):
            show = img.copy()
            hsv = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
            h,s,v = cv2.split(hsv)
            ret,thresh = cv2.threshold(s,120,255,0)
            _, contours, hierarchy = cv2.findContours(thresh, 1,2)
            for i in contours:
                cnt = i
                x,y,w,h = cv2.boundingRect(cnt)
                cv2.rectangle(show,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.destroyAllWindows()
            cv2.imshow(str(order_num) + '.jpg',show)
            k = cv2.waitKey(0)&0xFF
        elif k == ord('F'):
            show = img.copy()
            b,g,r = cv2.split(img)
            ret,thresh = cv2.threshold(r,120,255,0)
            _, contours, hierarchy = cv2.findContours(thresh, 1,2)
            for i in contours:
                cnt = i
                x,y,w,h = cv2.boundingRect(cnt)
                cv2.rectangle(show,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.destroyAllWindows()
            cv2.imshow(str(order_num) + '.jpg',show)
            k = cv2.waitKey(0)&0xFF
        elif k == ord('G'):
            show = img.copy()
            b,g,r = cv2.split(img)
            ret,thresh = cv2.threshold(g,120,255,0)
            _, contours, hierarchy = cv2.findContours(thresh, 1,2)
            for i in contours:
                cnt = i
                x,y,w,h = cv2.boundingRect(cnt)
                cv2.rectangle(show,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.destroyAllWindows()
            cv2.imshow(str(order_num) + '.jpg',show)
            k = cv2.waitKey(0)&0xFF
        elif k == ord('H'):
            show = img.copy()
            b,g,r = cv2.split(img)
            ret,thresh = cv2.threshold(b,120,255,0)
            _, contours, hierarchy = cv2.findContours(thresh, 1,2)
            for i in contours:
                cnt = i
                x,y,w,h = cv2.boundingRect(cnt)
                cv2.rectangle(show,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.destroyAllWindows()
            cv2.imshow(str(order_num) + '.jpg',show)
            k = cv2.waitKey(0)&0xFF
        elif k == ord('E'):
            txt.close()
            cv2.destroyAllWindows()
            exit()
        else:
            break;
    """
    method=raw_input('what method ?\n')
    if method == 'g':
        newImg = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        ret,thresh = cv2.threshold(newImg,127,255,0)
    elif method == 'c':
        thresh = cv2.Canny(img,100,200)
    elif method == 'h':
        hsv = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
        h,s,v = cv2.split(hsv)
        ret,thresh = cv2.threshold(s,120,255,0)
    elif method == 'r':
        b,g,r = cv2.split(img)
        ret,thresh = cv2.threshold(r,120,255,0)
    elif method == 'g':
        b,g,r = cv2.split(img)
        ret,thresh = cv2.threshold(g,120,255,0)
    elif method == 'b':
        b,g,r = cv2.split(img)
        ret,thresh = cv2.threshold(b,120,255,0)
        
    _, contours, hierarchy = cv2.findContours(thresh, 1,2)
    for i in contours:
        cnt = i
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    """
    # �������� ��
    #cv2.destroyAllWindows()
    #cv2.imshow('TrafficSign',show)
    # print 'suitable ?'

    # ??????
    
    # ���������Ӧ����S
    print 'Now You Can Use Your Mouse!'
    cv2.setMouseCallback(str(order_num) + '.jpg', choose_contours,[plus,save])

    cv2.waitKey()
    cv2.destroyAllWindows()


# �ر� txt �ĵ�
txt.close()
cv2.waitKey()
cv2.destroyAllWindows()
print 'OVER'
