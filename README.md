# VRDLpj

## kaggle competition
The Nature Conservancy Fisheries Monitoring
Can you detect and classify species of fish?
URL: https://www.kaggle.com/c/the-nature-conservancy-fisheries-monitoring/overview


## Setup

```bash
$ git clone https://github.com/Megvii-BaseDetection/YOLOX.git
$ cd YOLOX/
$ pip3 install -U pip && pip3 install -r requirements.txt
$ pip3 install -v -e .  # or  python3 setup.py develop
$ pip3 install cython; pip3 install 'git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI'

$ git clone https://github.com/NVIDIA/apex
$ cd apex/
$ pip3 install -v --disable-pip-version-check --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" ./

$ cd YOLOX/
$ mkdir weights
$ cd weights/
$ wget https://github.com/Megvii-BaseDetection/YOLOX/releases/download/0.1.1rc0/yolox_s.pth
```

## Related URLs

• Dataset link

https://www.kaggle.com/c/the-nature-conservancy-fisheries-monitoring/data

• GitHub Repository - YOLOX

https://github.com/Megvii-BaseDetection/YOLOX

• Pretrained model (yolox_s.pth)

https://github.com/Megvii-BaseDetection/YOLOX/releases/download/0.1.1rc0/yolox_s.pth

• Model weights after training 

