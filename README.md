# VRDLpj


## Team09
- 309553038 楊宗穎
- 309653012 陳育熙
- 0816035 陳威達


## kaggle competition
The Nature Conservancy Fisheries Monitoring
Can you detect and classify species of fish?

URL: https://www.kaggle.com/c/the-nature-conservancy-fisheries-monitoring/overview




## Overview of the competition
The heavily seafood consumed is threatening the marine ecosystem with 60% of the species fished. To keep track of how much fish were reeled out of the sea, the target task is to recognize fish species from images taken by boat onboard cameras. This task is costly if we do it by ourselves. So we want to do this task automatically. But there are some difficulties in this task, such as Fine-grained classification and background noise.



## Hardware information
- System: Linux - Ubuntu 20.04
- GPU: GeForce GTX 1660 SUPER™ VENTUS XS OC
- Deep Learning Libraries: PyTorch




<details open>

<summary>Setup</summary>

```bash
$ conda create -n yolox python=3.7
$ conda activate yolox

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

</details>




<details>
<summary>Demo</summary>
  
```bash
$ cd YOLOX/
$ python tools/demo.py image -n yolox-s -c weights/yolox_s.pth --path assets/dog.jpg --conf 0.25 --nms 0.45 --tsize 640 --save_result --device gpu
```

</details>




<details open>
<summary>Place files to corresponding folders</summary>
  
In this repository, put the files in folder named `src` to the corresponding folders in YOLOX.
  1. put `yolox_voc_s.py` into `YOLOX/exps/example/yolox_voc/`
  2. put `__init__.py` into `YOLOX/yolox/data/datasets/`
  3. put `voc_classes.py` into `YOLOX/yolox/data/datasets/`
  4. put `demo.py` into `YOLOX/tools/`
  5. put `yolox_s.py` into `YOLOX/exps/defaults/`
  
</details>




<details>
<summary>Convert .txt files to .xlm files</summary>
  
```bash
$ cd YOLOX/datasets/
$ mkdir txt2xml
$ cd txt2xml/
```
  
put `classes.txt` `convert-yolo-to-xml.py` into txt2xml folder
  
```bash
$ python convert-yolo-to-xml.py
>> /home/yuhsi44165/NYCU/G2/VRDL/Final_project/train/txtForm/
>> /home/yuhsi44165/NYCU/G2/VRDL/Final_project/train/classes.txt
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






<details>
<summary>Change to custom parameters for training</summary>

1. `yolox_voc_s.py`
  
```bash
$ cd exps/example/yolox_voc/
$ vim yolox_voc_s.py
>> self.num_classes = 8
>> data_dir='/home/yuhsi44165/NYCU/meeting/YOLOX/datasets/data/VOCdevkit',
>> image_sets=[('2007', 'trainval')],
>> data_dir='/home/yuhsi44165/NYCU/meeting/YOLOX/datasets/data/VOCdevkit',
```
  
2. `__init__.py`
  
```bash
$ cd yolox/data/datasets/
$ vim __init__.py
>> from .voc_classes import VOC_CLASSES
```
  
3. `voc_classes.py`
  
```bash
$ cd yolox/data/datasets/
$ vim voc_classes.py
>> VOC_CLASSES = (
>>     "ALB",
>>     "BET",
>>     "DOL",
>>     "LAG",
>>     "NoF",
>>     "OTHER",
>>     "SHARK",
>>     "YFT",
>> )
```

</details>




<details open>

<summary>Training</summary>

```bash
$ cd YOLOX/
$ python tools/train.py -f exps/example/yolox_voc/yolox_voc_s.py -d 1 -b 8 --fp16 -o -c weights/yolox_s.pth
```

</details>




<details>
<summary>Change to custom parameters for inference</summary>

1. `demo.py`
  
```bash
$ cd YOLOX/tools/
$ vim demo.py
>> from yolox.data.datasets import COCO_CLASSES, VOC_CLASSES
>> predictor = Predictor(
       model, exp, VOC_CLASSES, trt_file, decoder,
       args.device, args.fp16, args.legacy,
  )
```
  
2. `yolox_s.py`

```bash
$ cd YOLOX/exps/defaults/
$ vim yolox_s.py
>> self.num_classes = 8
```

</details>




<details open>

<summary>Inference</summary>

```bash
$ cd YOLOX/
$ python tools/demo.py image -n yolox-s -c YOLOX_outputs/yolox_voc_s/best_ckpt.pth --path datasets/test/ --conf 0.25 --nms 0.5 --tsize 640 --save_result --device gpu
```

</details>




<details>

<summary>Resume training</summary>

```bash
$ cd YOLOX/
$ python tools/train.py -f exps/example/yolox_voc/yolox_voc_s.py -d 1 -b 8 --fp16 -o -c YOLOX_outputs/yolox_voc_s/latest_ckpt.pth --resume
```

</details>





## Related URLs

- Dataset link: https://www.kaggle.com/c/the-nature-conservancy-fisheries-monitoring/data

- GitHub Repository - YOLOX: https://github.com/Megvii-BaseDetection/YOLOX

- Pretrained weights - yolox_s.pth: https://github.com/Megvii-BaseDetection/YOLOX/releases/download/0.1.1rc0/yolox_s.pth

- Model weights after training - yolox_s.pth
  1. best_ckpt.pth: https://drive.google.com/file/d/1QNV6dPnPR1Ze78pOjSPx-x109SHeAfXu/view?usp=sharing
  2. last_epoch_ckpt.pth: https://drive.google.com/file/d/1vSXoRiNPkoXs0SMoQBOISk3PfQ2fWH8h/view?usp=sharing
  3. last_mosaic_epoch_ckpt.pth: https://drive.google.com/file/d/1IMTA1lxACSGPXBRS60kto07AJxYj_aRG/view?usp=sharing
  4. latest_ckpt.pth: https://drive.google.com/file/d/1y78zEkK1zAXAce_akPgUhNAdP4cuRKQK/view?usp=sharing
