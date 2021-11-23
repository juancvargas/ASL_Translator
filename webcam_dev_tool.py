# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-chien
Create Date: 2021/11/23
"""
import os
from imutils.paths import list_images
from image_pipeline.preprocessing import gen_random_token
from cv2 import cv2
import numpy as np

img_dir = 'img_from_cam'


def remove_old_images():
    for p in list_images(img_dir):
        os.remove(p)


def save_frame(img: np.ndarray, rtk_len=3):
    img_path = f"{img_dir}/frame/{gen_random_token(rtk_len)}.jpg"
    cv2.imwrite(img_path, img)


def save_display_frame(img: np.ndarray, rtk_len=3):
    img_path = f"{img_dir}/display/{gen_random_token(rtk_len)}.jpg"
    cv2.imwrite(img_path, img)


def save_hand(img: np.ndarray, rtk_len=3, prefix=''):
    if prefix:
        img_path = f"{img_dir}/hand_roi/{prefix}_{gen_random_token(rtk_len)}.jpg"
    else:
        img_path = f"{img_dir}/hand_roi/{prefix}_{gen_random_token(rtk_len)}.jpg"

    cv2.imwrite(img_path, img)
    print(f"[INFO] - Image : {img_path} saved")
