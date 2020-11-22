import os
import numpy
from matplotlib import pyplot as plt
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
        docstring
        """
        print(path, " ", len(os.listdir(path)))


    def read_pic(self):
        path = os.getcwd()
        l = os.listdir(path)
        l.remove("data-processing.py")
        # print(l)
        for floder in l:
            floder = "./" + floder
            self.count_files(floder)

def main():
    data_preprocessing = Data_Preprocessing()
    data_preprocessing.read_pic()

if __name__ == "__main__":
    # execute only if run as a script
    main()