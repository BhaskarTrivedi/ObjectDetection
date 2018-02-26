1)Installation

https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md

2)Download Protobuf from 

https://github.com/google/protobuf/releases

3)Download Tensorflow model file from

https://github.com/tensorflow/models

4)Extarct and rename it to models

Compile Protocol Buffers

	a)Open Anaconda command promt
	b)Navigate to models directory
	c)Copy protoc.exe from protoc-3.4.0-win32\bin to to\model\research
	d) Run protoc ./object_detection/protos/*.proto --python_out=.

5) Pre-trained Model
	https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md

6) run from models\research using Anaconda virtual environment (Tensorflow-GPU)
python setup.py build
python setup.py install
pip install -e .

6) DownLoadModel.py
	To download and save model
7) Detect.py
	Code to detect object from image and web cam.

7)Prepare.py
	Create Modele download object and download the pretraing model

8)StartDetect.py
	Creat detection object and start detecting object from web cam.
	

execut StartDetect.py to start web cam detection 



