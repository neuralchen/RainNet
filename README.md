# RainNet: A Large-Scale Imagery Dataset and Benchmark for Spatial Precipitation Downscaling
# Accepted by NeurIPS 2022
Xuanhong Chen*, Kairui Feng*, Naiyuan Liu, Bingbing Ni**, Yifan Lu, Zhengyan Tong , Ziang Liu

\* Equal contribution
\*\* Corresponding author

[[Project Website]](https://neuralchen.github.io/RainNet) [[Paper]](https://arxiv.org/abs/2012.09700)

**The official repository with Pytorch**

[![rainnetlogo](/docs/img/2.png)](https://github.com/neuralchen/RainNet)

## Download RainNet

[[Download Via Google Drive]](https://neuralchen.github.io/RainNet) 

[[Download Via Baidu Drive]](https://pan.baidu.com/s/1hXa6Tr089KvBefCJIVQPuQ)
[password: sjtu]

## Resources in Zip:
***RainNet_HDF5.zip***

  &nbsp;&nbsp;&boxvr;&nbsp; $year$_07.hdf5
  
  &nbsp;&nbsp;&boxvr;&nbsp; $year$_08.hdf5
  
  &nbsp;&nbsp;&boxvr;&nbsp; $year$_09.hdf5
  
  &nbsp;&nbsp;&boxvr;&nbsp; $year$_10.hdf5
  
  &nbsp;&nbsp;&boxur;&nbsp; $year$_11.hdf5
  
  ***$year$=2002~2018***
  - ***85*** HDF5 files in total;
  - ***322GB*** of hard disk space is required to extract the dataset.
## Usage
- Data preparation. Run the 'dataset_prepare_hdf5.py' to process the dataset into patches. In 'dataset_prepare_hdf5.py', variable 'dataset_path' sets the hdf5 file path of RainNet; 'patch_hdf5_root' sets the target path to save processed dataset:

- ```python dataset_prepare_hdf5.py```

- We provide a example dataloader (pytorch script) to read the processed dataset:

- ```dataloader_hdf5.py```

- ***python scripts are archived in fold 'scripts'***

## Samples in RainNet

### High Resolution Precipitation Maps
<img src="./docs/img/HRGT_201009539_201009571.webp"  style="zoom: 20%;" />
<img src="./docs/img/HRGT_201108607_201108655.webp"  style="zoom: 20%;" />
<img src="./docs/img/HRGT_201109091_201109123.webp"  style="zoom: 20%;" />

### Low Resolution Precipitation Maps
<img src="./docs/img/LRGT_201009539_201009571.webp"  style="zoom: 20%;" />
<img src="./docs/img/LRGT_201108607_201108655.webp"  style="zoom: 20%;" />
<img src="./docs/img/LRGT_201109091_201109123.webp"  style="zoom: 20%;" />






## Citation
If you find this Dataset useful in your research, please consider citing:

```
@misc{chen2020rainnet,
  title={RainNet: A Large-Scale Dataset for Spatial Precipitation Downscaling},
  author={Xuanhong Chen and Kairui Feng and Naiyuan Liu and Yifan Lu and Zhengyan Tong and Bingbing Ni and Ziang Liu and Ning Lin},
  year={2020},
  eprint={2012.09700},
  archivePrefix={arXiv},
  primaryClass={cs.CV}
} 
```

## Contact
Please concat Kairui Feng [email](kairuif@princeton.com), Xuanhong Chen [email](xuanhongchenzju@outlook.com), Naiyuan Liu [email](naiyuan.liu@student.uts.edu.au) and Yifan Lu [email](yifan_lu@sjtu.edu.cn) for questions about the dataset. 
