import os

class DataManger():       

    def __init__(self):
        self._datasets = {} 

    
    def update(self):
        self._datasets = {}
        data_folder = os.path.join(os.path.dirname(__file__),"Data")
        list_of_folders = os.listdir(data_folder)
        for folder in list_of_folders:
            file_list = os.listdir(os.path.join(data_folder,folder))
            for files in file_list:
                if(os.path.splitext(files)[1] == ".tm"):
                    self._datasets[folder] = os.path.join(data_folder,folder,files)   
    
    @property
    def datasets(self):
        return self._datasets

    @datasets.setter
    def datasets(self,_):
        pass




    