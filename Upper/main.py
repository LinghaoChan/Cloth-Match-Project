import os
import numpy
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import pandas
from PIL import Image
import torch
import data_get
import data_processing
import generating_dataset

def main():
    data_preprocesser = data_processing.Data_Preprocessing()
    data_preprocesser.read_floder()
    # data_preprocesserchange_image_size("Casual_1.jpg")
    # data_preprocesser.batch_chage_image_size()
    generator = generating_dataset.Relationship()
    generator.construct_relationship()
if __name__ == "__main__":
    # execute only if run as a script
    main()
