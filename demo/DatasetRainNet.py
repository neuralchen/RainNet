import h5py
import torch.utils.data as data
import numpy as np
import cv2
import random
import torch
from PIL import Image, ImageOps
class RainNetDataset(data.Dataset):
    def __init__(self,data_path, is_training=True, crop_size_gt=192, upscale_factor=3, rotation=True, flip=True):
        super(RainNetDataset,self).__init__()
        (self.highres,self.lowres) = RainNet_from_folder(data_path)
        self.len = self.highres.shape[2]
        self.is_training    = is_training
        self.crop_size_gt   = crop_size_gt
        self.upscale_factor = upscale_factor
        self.rotation = rotation
        self.flip     = flip

    def __getitem__(self,index):
        img_hr = self.highres[:,:,index]
        img_lr = self.lowres[:,:,index]
        img_hr = np.expand_dims(img_hr, -1)
        img_lr = np.expand_dims(img_lr, -1)

        # augmentation for training
        if self.is_training:
            # random crop
            img_hr, img_lr = random_crop(img_hr, img_lr, self.crop_size_gt, self.upscale_factor)
            # flip, rotation
            img_hr, img_lr = augment([img_hr, img_lr], self.flip, self.rotation)
        else :
            pass
        img_hr, img_lr = toTensor([img_hr, img_lr])

        return img_hr, img_lr

    def __len__(self):
        return self.len
    
def RainNet_from_folder(folder):
    h5_path = folder
    f = h5py.File(h5_path,'r')
    highres = f['highres']
    lowres = f['lowres']
    return [highres,lowres]

def random_crop(GT_img, LR_img, GT_crop_size,upscale_factor):

    LR_h, LR_w = LR_img.shape[0],LR_img.shape[1]
    LR_crop_size = GT_crop_size//upscale_factor

    ix = np.random.randint(0,LR_h-LR_crop_size-1)
    iy = np.random.randint(0,LR_w-LR_crop_size-1)

    GT_img_crop = GT_img[ix:ix+GT_crop_size, iy:iy+GT_crop_size,:]
    LR_img_crop = LR_img[ix:ix+LR_crop_size, iy:iy+LR_crop_size,:]

    return GT_img_crop, LR_img_crop

def augment(imgs, hflip=True, rotation=True):
    #print(imgs.shape)
    hflip = hflip and random.random() < 0.5
    vflip = rotation and random.random() < 0.5
    rot = rotation and random.random() < 0.5

    def _augument(img):
        if hflip:
            cv2.flip(img, 1, img)
        if vflip:
            cv2.flip(img, 0, img)
        if rot:
            img = img.transpose(1, 0, 2)

        return img
    imgs = [_augument(img) for img in imgs]
    
    return imgs

def toTensor(imgs):

    def _totensor(img):
        img = torch.from_numpy(img.transpose(2, 0, 1))

        img = img.float()
        return img
    if isinstance(imgs, list):
        return [_totensor(img) for img in imgs]
    else:
        return _totensor(imgs)


    








