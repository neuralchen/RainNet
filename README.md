# RainNet: A Large-Scale Imagery Dataset and Benchmark for Spatial Precipitation Downscaling
# Accepted by NeurIPS 2022
Xuanhong Chen*, Kairui Feng*, Naiyuan Liu, Bingbing Ni**, Yifan Lu, Zhengyan Tong , Ziang Liu

\* Equal contribution
\*\* Corresponding author

[[Project Website]](https://neuralchen.github.io/RainNet) [[Paper]](https://arxiv.org/abs/2012.09700)

## Abstract
AI-for-science approaches have been applied to solve scientific problems (e.g., nuclear fusion, ecology, genomics, meteorology) and have achieved highly promising results.
Spatial precipitation downscaling is one of the most important meteorological issues and urgently requires the participation of AI.
However, the lack of a well-organized and annotated large-scale dataset hinders the training and verification of more effective and advancing deep-learning models for precipitation downscaling.
To alleviate these obstacles, we present the first large-scale spatial precipitation downscaling dataset named \emph{RainNet}, which contains more than $62,400$ pairs of high-quality low/high-resolution precipitation maps for over $17$ years,
ready to help the evolution of deep learning models in precipitation downscaling.
Specifically, the precipitation maps carefully collected in RainNet cover various meteorological phenomena (e.g., hurricane, squall), which is of great help to improve the model generalization ability.
In addition, the map pairs in RainNet are organized in the form of image sequences ($720$ maps per month or 1 map/hour), showing complex physical properties, e.g., temporal misalignment, temporal sparse, and fluid properties.
Two deep-learning-oriented metrics are specifically introduced to evaluate or verify the comprehensive performance of the trained model, (e.g., prediction maps reconstruction accuracy).
To illustrate the applications of RainNet, 14 state-of-the-art models, including deep models and traditional approaches, are evaluated.
To fully explore potential downscaling solutions, we propose an implicit physical estimation benchmark framework to learn the above characteristics.
Extensive experiments demonstrate the value of RainNet in training and evaluating downscaling models.

## Samples in RainNet

### High Resolution Precipitation Maps
<img src="./docs/img/HRGT_201009539_201009571.webp"  style="zoom: 20%;" />
<img src="./docs/img/HRGT_201108607_201108655.webp"  style="zoom: 20%;" />
<img src="./docs/img/HRGT_201109091_201109123.webp"  style="zoom: 20%;" />

### Low Resolution Precipitation Maps
<img src="./docs/img/LRGT_201009539_201009571.webp"  style="zoom: 20%;" />
<img src="./docs/img/LRGT_201108607_201108655.webp"  style="zoom: 20%;" />
<img src="./docs/img/LRGT_201109091_201109123.webp"  style="zoom: 20%;" />



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
