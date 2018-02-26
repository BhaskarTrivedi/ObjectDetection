import six.moves.urllib as urllib
import os
import tarfile

class Dowload:
    def __init__(self):
        self.MODEL_NAME = 'ssd_mobilenet_v1_coco_2017_11_17'
        self.MODEL_FILE = self.MODEL_NAME + '.tar.gz'
        self.DOWNLOAD_BASE = 'http://download.tensorflow.org/models/object_detection/'

        # Path to frozen detection graph. This is the actual model that is used for the object detection.
        self.PATH_TO_CKPT = self.MODEL_NAME + '/frozen_inference_graph.pb'






    def download(self):
        opener = urllib.request.URLopener()
        opener.retrieve(self.DOWNLOAD_BASE + self.MODEL_FILE, self.MODEL_FILE)
        tar_file = tarfile.open(self.MODEL_FILE)
        for file in tar_file.getmembers():
            file_name = os.path.basename(file.name)
            if 'frozen_inference_graph.pb' in file_name:
                tar_file.extract(file, os.getcwd())


        return self.PATH_TO_CKPT