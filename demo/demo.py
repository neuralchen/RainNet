
import torch
from torch.utils.data import DataLoader
import argparse
from DatasetRainNet import RainNetDataset

parser = argparse.ArgumentParser(description='Demo scipt for loading RainNet dataset')
parser.add_argument('--dataroot', type=str, default='dataset/2018_11.hdf5')
parser.add_argument('--batchsize', type=int, default=4)
parser.add_argument('--upscale_factor', type=int, default=3)
parser.add_argument('--crop_size_gt', type=int, default=192)
parser.add_argument('--threads', type=int, default=8, help='number of threads for data loader to use')

arg = parser.parse_args()

train_set = RainNetDataset(arg.dataroot,is_training=True, crop_size_gt=arg.crop_size_gt, upscale_factor=arg.upscale_factor, rotation=True, flip=True)
#val_set  = RainNetDataset(arg.dataroot,is_training=False, crop_size_gt=192, upscale_factor=3)

training_data_loader = DataLoader(dataset=train_set, num_workers=arg.threads, batch_size=arg.batchsize, shuffle=True)
# testing_data_loader = DataLoader(dataset=test_set, num_workers=opt.threads, batch_size=opt.testBatchSize, shuffle=False)

dataset_len = len(training_data_loader.dataset)
print(dataset_len)

for idx,batch in enumerate(training_data_loader):
    img_gt, img_lr = batch[0], batch[1]
    print('The shape of HighRes Images :{}'.format(img_gt.shape))
    print('The shape of LowRes Images :{}'.format(img_lr.shape))
    break

