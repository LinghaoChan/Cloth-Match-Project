import os

class Relationship(object):

    def __init__(self, save_path='./dataset', dir_path='./'):
        """
        Dataset -> txt.
        """
        self.save_path = save_path
        self.dir_path = dir_path

    def construct_relationship(self):
        """
        Construct the realationship with jugging.
        """
        print("\nGenerating dataset...")
        if not os.path.exists(self.save_path):
            self.generate_txt()
        print("Generated dataset!")

    def generate_txt(self):
        """
        Generating the dataset text file.
        """
        if not os.path.exists(self.save_path):
            os.makedirs('./dataset')
        train_txt = open('./dataset/train.txt', 'a')
        test_txt = open('./dataset/test.txt', 'a')
        ls = ["Casual", "Cowboy", "Formal",
             "Old_fashioned", "Simplicity", "Spirit_guy", "Sport"]
        count = 1
        for sub_dir in ls:
            i = 1
            if not sub_dir.endswith(".py") and not sub_dir.endswith("__"):
                for file_name in os.listdir(sub_dir):
                    img_path = self.dir_path + sub_dir + '/' + file_name
                    img_label = count
                    if i % 10 == 5:
                        test_txt.write(img_path+' '+str(img_label)+'\n')
                    else:
                        train_txt.write(img_path+' '+str(img_label)+'\n')
                    i = i + 1
                count = count+1
        train_txt.close()
        test_txt.close()