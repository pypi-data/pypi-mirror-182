# -*-coding: utf-8 -*-
"""
    @Author : PKing
    @E-mail : 390737991@qq.com
    @Date   : 2022-12-21 17:34:38
    @Brief  :
"""
import time

HAND_BUCKET_NAME = "handwriting-dev"
CEPH = {"HAND_BUCKET_NAME": HAND_BUCKET_NAME + '-' + time.strftime("%Y-%m-%d", time.localtime())}
hand_bucket_name = HAND_BUCKET_NAME + '-' + time.strftime("%Y-%m-%d", time.localtime())
if hand_bucket_name != CEPH['HAND_BUCKET_NAME']:
    CEPH['HAND_BUCKET_NAME'] = hand_bucket_name
    print("!", hand_bucket_name)
else:
    print("=", hand_bucket_name)
