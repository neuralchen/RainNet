#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#############################################################
# File: dataset_prepare_hdf5.py
# Created Date: Monday January 11th 2021
# Author: Chen Xuanhong
# Email: chenxuanhongzju@outlook.com
# Last Modified:  Wednesday, 16th November 2022 12:22:22 pm
# Modified By: Chen Xuanhong
# Copyright (c) 2021 Shanghai Jiao Tong University
#############################################################


import os
import h5py
import random
import numpy as np

random.seed(1234)
threhold = 0.357

if __name__ == "__main__":

    dataset_path= "G:\\RainNet\\Dataset_H5"       # path to RainNet HDF5 file
    patch_hdf5_root   = "G:\\RainNet\\RainNet_H5" # root patch to save patches

    if not os.path.exists(patch_hdf5_root):
        os.makedirs(patch_hdf5_root)
    hdf5_path   = os.path.join(patch_hdf5_root, "%s.hdf5"%"RainNet_Patches")

    month_list  = ["07","08","09","10","11"] # 744 744 720 744 720
    year_start  = 2002
    
    t_stride    = 4
    frame       = 5
    patch_size  = 64
    patch_per_img=4
    
    ratio       = 3
    HR_patch    = 64 * ratio
    max_rain    = 140.0

    high_list   = []
    low_list    = []

    total_patch = 0
    
    if not os.path.exists(hdf5_path):
        h5file = h5py.File(hdf5_path, 'w')
    else:
        h5file = h5py.File(hdf5_path, 'a')

    # 0 ~ 140-> 0 ~ 1.0

    print("Generate hdf5 to %s" % hdf5_path)
    for year_item in range(2002,2019):
        if os.path.exists(dataset_path+"\\%d_07.hdf5"%year_item):
            for tail in month_list:
                i_path      = dataset_path+"\\%d_%s.hdf5"%(year_item,tail)
                print("Processing %s......"%i_path)
                f           = h5py.File(i_path,'r')
                high_list   = f['highres']
                low_list    = f['lowres']
                print("Processing hdf5 file: %s"%i_path)
                total_len   = low_list.shape[2]
                hight       = low_list.shape[0]
                width       = low_list.shape[1]
                print("#===========One Batch==========#")
                for index in range(0, total_len-frame, t_stride):
                    count = 0
                    for _ in range(20):
                        r_h   = random.randint(0,hight-patch_size)
                        r_w   = random.randint(0,width-patch_size)
                        lr_patch = low_list[r_h:(r_h+patch_size),r_w:(r_w+patch_size),index]
                        if lr_patch.max() > threhold: # leverage hr patch
                            hr_patch_ls = high_list[r_h * ratio:(r_h * ratio + HR_patch),
                                                    r_w * ratio:(r_w * ratio + HR_patch), index:(index + frame//2)]
                            lr_patch_ls = low_list[r_h:(r_h+patch_size),r_w:(r_w+patch_size), index:(index + frame//2)]
                            hr_patch_ls = np.clip(hr_patch_ls.transpose((2,0,1)), 0.0, max_rain)/max_rain
                            lr_patch_ls = np.clip(lr_patch_ls.transpose((2,0,1)), 0.0, max_rain)/max_rain
                            h5file.create_dataset(str(total_patch)+"hr", data=hr_patch_ls)
                            h5file.create_dataset(str(total_patch)+"lr", data=lr_patch_ls)
                            count       += 1
                            total_patch += 1
                        if count >patch_per_img:
                            break
    print("Commit data into the database......")
    print("Totally %d patches."%(total_patch))
    
    h5file.close()