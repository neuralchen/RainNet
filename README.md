# RainNet: A Large-Scale Dataset for Spatial Precipitation Downscaling
Xuanhong Chen, Kairui Feng, Naiyuan Liu, Yifan Lu, Zhengyan Tong, Bingbing Ni, Ziang Liu, Ning Lin

[[Project Website]](https://neuralchen.github.io/RainNet) [[Paper]](https://arxiv.org/abs/2012.09700)

## Abstract
Spatial Precipitation Downscaling is one of the most important problems in the geo-science community. However, it still remains an unaddressed issue. Deep learning is a promising potential solution for downscaling. In order to facilitate the research on precipitation downscaling for deep learning, we present the first REAL (non-simulated) Large-Scale Spatial Precipitation Downscaling Dataset, RainNet, which contains *62,424* pairs of low-resolution and high-resolution precipitation maps for 17 years. Contrary to simulated data, this real dataset covers various types of real meteorological phenomena (e.g., Hurricane, Squall, etc.), and shows the physical characters - Temporal Misalignment, Temporal Sparse and Fluid Properties - that challenge the downscaling algorithms. In order to fully explore potential downscaling solutions, we propose an implicit physical estimation framework to learn the above characteristics. Eight metrics specifically considering the physical property of the data set are raised, while fourteen models are evaluated on the proposed dataset. Finally, we analyze the effectiveness and feasibility of these models on precipitation downscaling task. 

## Samples in RainNet

### High Resolution Precipitation Maps
<img src="./docs/img/HRGT_201009539_201009571.webp"  style="zoom: 50%;" />
<img src="./docs/img/HRGT_201108607_201108655.webp"  style="zoom: 50%;" />
<img src="./docs/img/HRGT_201109091_201109123.webp"  style="zoom: 50%;" />

### Low Resolution Precipitation Mapss
<img src="./docs/img/LRGT_201009539_201009571.webp"  style="zoom: 50%;" />
<img src="./docs/img/LRGT_201108607_201108655.webp"  style="zoom: 50%;" />
<img src="./docs/img/LRGT_201109091_201109123.webp"  style="zoom: 50%;" />



## Download RainNet

[[Download Via Google Drive]](https://neuralchen.github.io/RainNet) [[Download Via Baidu Drive]](https://arxiv.org/abs/2012.09700)


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