# 读取wallpaper下的全部图片，进行高斯模糊处理
# 保存到wallpaper_blur文件夹下

import os
import cv2
import numpy as np

def gauss_blur(img):
    # 高斯模糊
    return cv2.GaussianBlur(img, (21, 21), 0)

def main():
    # 读取wallpaper下的全部图片
    img_dir = os.path.join(os.path.dirname(__file__), '.')
    img_list = os.listdir(img_dir)
    for img_name in img_list:
        img_path = os.path.join(img_dir, img_name)
        img = cv2.imread(img_path)
        if img is None:
            continue
        # 高斯模糊
        img_blur = gauss_blur(img)
        # 保存到wallpaper_blur文件夹下
        img_blur_dir = os.path.join(os.path.dirname(__file__), 'wallpaper_blur')
        if not os.path.exists(img_blur_dir):
            os.makedirs(img_blur_dir)
        img_blur_path = os.path.join(img_blur_dir, img_name)
        cv2.imwrite(img_blur_path, img_blur)
        print('save', img_blur_path)

if __name__ == '__main__':
    main()