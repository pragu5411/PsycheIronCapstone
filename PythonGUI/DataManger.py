import os

class DataManger():
       

    def __init__(self):
        self.datasets = {} 

    
    def update(self):
        self.datasets = {}
        data_folder = os.path.join(os.path.dirname(__file__),"Data")
        list_of_folders = os.listdir(data_folder)
        for folder in list_of_folders:
            file_list = os.listdir(os.path.join(data_folder,folder))
            for files in file_list:
                if(os.path.splitext(files)[1] == ".tm"):
                    self.datasets[folder] = os.path.join(data_folder,folder,files)   
    
    def getdatasets(self):
        return self.datasets

data_list = DataManger()
data_list.update()
print(data_list.datasets)
            
    

    