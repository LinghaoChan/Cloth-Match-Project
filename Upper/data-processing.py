import os
import numpy
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import pandas
import torch


class Data_Preprocessing(object):
    """
    docstring
    """
    def __init__(self):
        pass
    
    def count_files(self, path: str):
        """
        Count the number of images in this floder
        """
        print(path, " ", len(os.listdir(path)))

    def show_img(self, path = "./Old_fashioned/Old_fashioned_1.jpg"):
        """
        Show the image of a image, for debuging.
        """
        img = mpimg.imread(path) 
        print(img.shape) 
        plt.imshow(img)
        plt.axis('off')
        plt.show()
                
    def read_pic(self):
        """
        Get the message of images.
        """
        path = os.getcwd()
        l = os.listdir(path)
        l.remove("data-processing.py")
        for floder in l:
            floder = "./" + floder
            self.count_files(floder)

def main():
    data_preprocessing = Data_Preprocessing()
    data_preprocessing.read_pic()
    data_preprocessing.show_img()

if __name__ == "__main__":
    # execute only if run as a script
    main()