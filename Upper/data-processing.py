import os
import numpy
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import pandas
from PIL import Image
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
        # plt.imshow(img)
        # plt.axis('off')
        # plt.show()
        # print(img.shape)
        return(img.shape)

    def show_image_message(self, path):
        """
        Show the image infomation in a folder
        """
        filelist = os.listdir(path)
        total_num = len(filelist)  # get the number of files
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
        self.filelist = l
        for floder in l:
            floder = "./" + floder
            self.count_files(floder)
        # image_shape_calculator = []
        # for floder in l:
        #     self.show_image_message(floder)
        #     image_shape_calculator.append(self.show_image_message(floder))
        # self.image_shape_set = image_shape_calculator

    def change_image_size(self, path, size=(150, 100, 3)):
        """
        Change the size of an image to size = 30 x 20 x 3
        """  
        self.show_img(path) 
        img = Image.open(path)
        out = img.resize((size[0], size[1]),Image.ANTIALIAS) #resize image with high-quality
        out.save(path)   
        self.show_img(path)

    def batch_chage_image_size(self):
        """
        docstring
        """
        print(self.filelist)
        l = self.filelist
        for floder in l:
            cur_path = "./" + floder
            img_list = os.listdir(cur_path)
            for img in img_list:
                img_path = cur_path + "/" + img
                print((img_path))
                if img_path.endswith('.jpg'):
                    self.change_image_size(img_path)


def main():
    data_preprocessing = Data_Preprocessing()
    data_preprocessing.read_floder()
    # data_preprocessing.change_image_size("Casual_1.jpg")
    data_preprocessing.batch_chage_image_size()

if __name__ == "__main__":
    # execute only if run as a script
    main()
