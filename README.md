# VRDLpj

## kaggle competition
The Nature Conservancy Fisheries Monitoring
Can you detect and classify species of fish?
URL: https://www.kaggle.com/c/the-nature-conservancy-fisheries-monitoring/overview


## Setup

```bash
$ git clone https://github.com/NVIDIA/apex
$ cd apex/
$ pip3 install -v --disable-pip-version-check --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" ./

$ git clone https://github.com/Megvii-BaseDetection/YOLOX.git
$ cd YOLOX/
$ pip3 install -U pip && pip3 install -r requirements.txt
$ pip3 install -v -e .  # or  python3 setup.py develop
$ pip3 install cython; pip3 install 'git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI'

$ cd YOLOX/
$ mkdir weights
$ cd weights/
$ wget https://github.com/Megvii-BaseDetection/YOLOX/releases/download/0.1.1rc0/yolox_s.pth
```



<details>
<summary>Demo</summary>
  
```bash
$ cd YOLOX/
$ python tools/demo.py image -n yolox-s -c weights/yolox_s.pth --path assets/dog.jpg --conf 0.25 --nms 0.45 --tsize 640 --save_result --device gpu
```

</details>





<details open>
<summary>data folder structuer</summary>
  
```bash
$ cd YOLOX/datastes/
$ mkdir data
$ cd data/
$ mkdir VOCdevkit
$ cd VOCdevkit/
$ mkdir VOC2007
$ cd VOC2007/
$ mkdir Annotations
$ mkdir JPEGImages
$ mkdir ImageSets
$ cd ImageSets/
$ mkdir Main
```
  
```bash
$ cd YOLOX/datasets/
├── data
│   ├── VOCdevkit
│   │   ├── VOC2007
│   │   │   ├── Annotations    # put test.txt、trainval.txt corresponding .xml files here
│   │   │   ├── JPEGImages    # put test.txt、trainval.txt corresponding .jpg files here
│   │   │   ├── ImageSets
│   │   │   │   ├── Main
│   │   │   │   │   ├── test.txt    # generated after excute split.py
│   │   │   │   │   ├── trainval.txt    # generated after excute split.py
```

</details>





## Train
```bash
$ python tools/train.py -f exps/example/yolox_voc/yolox_voc_s.py -d 1 -b 8 --fp16 -o -c weights/yolox_s.pth
```

## Test
```bash
$ python tools/demo_custom.py image -f exps/example/yolox_voc/yolox_voc_s.py -c YOLOX_outputs/yolox_voc_s/best_ckpt.pth --path datasets/test/ --conf 0.25 --nms 0.5 --tsize 640 --save_result --device gpu
# trained weights saved in YOLOX_outputs_yolox_voc_s folder
```


## Related URLs

• Dataset link

https://www.kaggle.com/c/the-nature-conservancy-fisheries-monitoring/data

• GitHub Repository - YOLOX

https://github.com/Megvii-BaseDetection/YOLOX

• Pretrained model 
1. yolox_s.pth: https://github.com/Megvii-BaseDetection/YOLOX/releases/download/0.1.1rc0/yolox_s.pth
2. yolox_x.pth: https://github.com/Megvii-BaseDetection/YOLOX/releases/download/0.1.1rc0/yolox_x.pth

• Model weights after training 
1. yolox_s.pth (best_ckpt.pth, last_epoch_ckpt.pth, latest_ckpt.pth): 
2. yolox_x.pth (best_ckpt.pth, last_epoch_ckpt.pth, latest_ckpt.pth): 
