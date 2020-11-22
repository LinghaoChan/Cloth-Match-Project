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

    def show_img(self, path="./Old_fashioned/Old_fashioned_1.jpg"):
        """
        Show the image of a image, for debuging.
        """
        img = mpimg.imread(path)
        return(img.shape)
        # plt.imshow(img)
        # plt.axis('off')
        # plt.show()

    def show_image_message(self, path):
        """
        Show the image infomation in a folder
        """
        filelist = os.listdir(path)
        total_num = len(filelist)  # 获取文件长度（个数）
        i = 1  # 表示文件的命名是从1开始的
        dic = {}
        for item in filelist:
            if item.endswith('.jpg'):
                dir = path + "/" + item
                img_shape = self.show_img(dir)
                if img_shape not in dic:
                    dic[img_shape] = 1
                else:
                    dic[img_shape] += 1
        return {path : dic}

    def read_floder(self):
        """
        Get the infomation of images.
        """
        path = os.getcwd()
        l = os.listdir(path)
        l.remove("data-processing.py")
        for floder in l:
            floder = "./" + floder
            self.count_files(floder)
        image_shape_calculator = []
        for floder in l:
            self.show_image_message(floder)
            print(self.show_image_message(floder))


def main():
    data_preprocessing = Data_Preprocessing()
    data_preprocessing.read_floder()


if __name__ == "__main__":
    # execute only if run as a script
    main()
