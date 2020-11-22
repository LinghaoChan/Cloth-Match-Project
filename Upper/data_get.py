import os
import numpy
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import pandas
from PIL import Image
import torch

class Data_Getting(object):
    """
    get the raw data and labels of the dataset
    """
    def __init__(self, parameter_list):
        """
        docstring
        """
        