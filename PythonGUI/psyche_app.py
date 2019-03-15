import tkinter as tk
import spiceypy as spice
from DataManger import DataManger as DM
import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


HEIGHT = 800
WIDTH = 800
FONT = ('Times New Roman', 12)
FRAMECOLOR = '#303030'
BUTTONCOLOR = '#181818'
FONTCOLOR = '#F0F0F0'

class psyche_app:
    
    def __init__(self,master):

        self.data_sets = DM() 

        window = master
        canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)
        canvas.pack()

        self.root = tk.Frame(master=window, bg = FRAMECOLOR)
        self.root.place( relx= .05, rely=.05,relheight = .90, relwidth = .90)

        self.left_side = tk.Frame(master = self.root, bg = FRAMECOLOR)
        self.left_side.place(relx = 0, rely = 0, relheight = 1, relwidth = .5)
        self.left_title = tk.Label(master= self.left_side, text ="Current Kernels", font = FONT, bg = BUTTONCOLOR, fg = FONTCOLOR)
        self.left_title.place(relx=0,rely =0,relwidth = 1, relheight = .05)
        self.kernel_list = tk.Listbox(master=self.left_side)
        self.kernel_list.place(relx=.05,rely=.05,relwidth = 1, relheight =.65)
        self.kernel_menu = tk.Frame(master= self.left_side,bg = FRAMECOLOR)
        self.add_kernal = tk.Button(master=self.kernel_menu, text = "Import Kernel", font = FONT, bg = BUTTONCOLOR, fg = FONTCOLOR)
        self.add_kernal.grid(row= 0, column =0, padx = 15, pady = 5)
        self.remove_kernal = tk.Button(master=self.kernel_menu, text = "Remove Kernel", font = FONT,bg = BUTTONCOLOR, fg = FONTCOLOR)
        self.remove_kernal.grid(row= 0, column =1, padx = 15, pady = 5)
        self.refresh_kernal = tk.Button(master=self.kernel_menu, text = "Refresh", font = FONT,bg = BUTTONCOLOR, fg = FONTCOLOR, command = self.refresh_event)
        self.refresh_kernal.grid(row= 0, column =3, padx = 15, pady = 5)
        self.kernel_menu.place(relx=0,rely=.7,relwidth = 1, relheight =.3)


        self.right_side = tk.Frame(master = self.root, bg = FRAMECOLOR)
        self.right_side.place(relx = .5, rely = 0, relheight = 1, relwidth = .5)
        self.right_title = tk.Label(master= self.right_side, text ="Meta Information", font = FONT, bg = BUTTONCOLOR, fg = FONTCOLOR)
        self.right_title.place(relx=0,rely =0,relwidth = 1, relheight = .05)

        self.right_information = tk.Frame(master = self.right_side, bg = FRAMECOLOR)
        self.right_information.place(relx=0,rely=.05,relwidth = 1, relheight =.65)
        
        self.time_one_label = tk.Label(master= self.right_information, text = "Time One: ", bg = BUTTONCOLOR, fg = FONTCOLOR)
        self.time_one_entry = tk.Entry(master= self.right_information)
        self.time_one_label.grid(row = 0 , column = 0, padx = 45, pady = 15)
        self.time_one_entry.grid(row = 0 , column = 1, padx = 45, pady = 15)

        self.time_two_label = tk.Label(master= self.right_information, text = "Time Two: ", bg = BUTTONCOLOR, fg = FONTCOLOR)
        self.time_two_entry = tk.Entry(master= self.right_information)
        self.time_two_label.grid(row = 1 , column = 0, padx = 45, pady = 15)
        self.time_two_entry.grid(row = 1 , column = 1, padx = 45, pady = 15)

        self.time_step_label = tk.Label(master= self.right_information, text = "Time Step: ", bg = BUTTONCOLOR, fg = FONTCOLOR)
        self.time_step_entry = tk.Entry(master= self.right_information)
        self.time_step_label.grid(row = 3 , column = 0, padx = 45, pady = 15)
        self.time_step_entry.grid(row = 3 , column = 1, padx = 45, pady = 15)
        
        self.reference_label = tk.Label(master= self.right_information, text = "Reference: ", bg = BUTTONCOLOR, fg = FONTCOLOR)
        self.reference_entry = tk.Entry(master= self.right_information)
        self.reference_label.grid(row = 4 , column = 0, padx = 45, pady = 15)
        self.reference_entry.grid(row = 4 , column = 1, padx = 45, pady = 15)

        self.abberration_corr_label = tk.Label(master= self.right_information, text = "Abcorr: ", bg = BUTTONCOLOR, fg = FONTCOLOR)
        self.abberration_corr_entry = tk.Entry(master= self.right_information)
        self.abberration_corr_label.grid(row = 5 , column = 0, padx = 45, pady = 15)
        self.abberration_corr_entry.grid(row = 5 , column = 1, padx = 45, pady = 15)

        self.target_label = tk.Label(master= self.right_information, text = "Target: ", bg = BUTTONCOLOR, fg = FONTCOLOR)
        self.target_entry = tk.Entry(master= self.right_information)
        self.target_label.grid(row = 6 , column = 0, padx = 45, pady = 15)
        self.target_entry.grid(row = 6 , column = 1, padx = 45, pady = 15)

        self.observer_label = tk.Label(master= self.right_information, text = "Observer: ", bg = BUTTONCOLOR, fg = FONTCOLOR)
        self.observer_entry = tk.Entry(master= self.right_information)
        self.observer_label.grid(row = 7 , column = 0, padx = 45, pady = 15)
        self.observer_entry.grid(row = 7 , column = 1, padx = 45, pady = 15)

        


        self.export_menu = tk.Frame(master= self.right_side, bg = FRAMECOLOR)
        self.export_kernal = tk.Button(master=self.export_menu, text = "Export Kernel", font = FONT,bg = BUTTONCOLOR, fg = FONTCOLOR, command= self.export_event)
        self.export_kernal.grid(row= 0, columnspan = 3, padx = 125, pady = 5)
        self.export_menu.place(relx=0,rely=.7,relwidth = 1, relheight =.3)

        window.mainloop()
    
    def refresh_event(self,*args,**kwargs):
        self.kernel_list.delete(0,tk.END)
        self.data_sets.update()
        list_of_kernel = self.data_sets.datasets
        for kernel_title in list_of_kernel.keys():
            self.kernel_list.insert(tk.END, kernel_title)

    # *** PlaceHolder ***
    def export_event(self,*args,**kwargs):
        time_one = self.time_one_entry.get()
        time_two = self.time_two_entry.get()
        time_step = int(self.time_step_entry.get())
        reference = self.reference_entry.get()
        abcorr = self.abberration_corr_entry.get()
        observer = self.observer_entry.get()
        target = self.target_entry.get()
        
        spice.furnsh(self.data_sets.datasets[self.kernel_list.get(tk.ACTIVE)])
        et_times = [spice.str2et(time_one), spice.str2et(time_two)]         
        times = [x*(et_times[1]-et_times[0])/time_step + et_times[0] for x in range(time_step)]
        pos, dist = spice.spkpos(observer, times, reference, abcorr, target)
        content_folder = os.path.join(os.path.dirname(__file__),self.kernel_list.get(tk.ACTIVE))
        try:
            os.makedirs(content_folder)
        except FileExistsError:
            pass
        pos_file_path = os.path.join(content_folder,"pos.txt")
        dist_file_path = os.path.join(content_folder,"dist.txt")
        with open(pos_file_path,"w") as pos_file:
            pos_file.write(str(pos))
        with open(dist_file_path,"w") as dist_file:
            dist_file.write(str(dist))

        pos = np.asarray(pos).T 
        fig = plt.figure(figsize=(9, 9))
        ax  = fig.add_subplot(111, projection='3d')
        ax.plot(pos[0], pos[1], pos[2])
        plt.title(f'SpiceyPy {target} Position from {time_one} to {time_two}')
            
        pos_graph_file_path = os.path.join(content_folder,"posgraph.pdf")
        plt.savefig(pos_graph_file_path, dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype='letter', format='pdf',
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None, metadata=None)
            
        dist = np.asarray(dist)
        
        fig2 = plt.figure(figsize=(9, 9))
        ax2  = fig2.add_subplot(111, projection='3d')
        ax2.plot(times,dist)
        plt.title(f'SpiceyPy {target} distance from {observer} taken from {time_one} to {time_two}')

        dist_graph_file_path = os.path.join(content_folder,"distgraph.pdf")
        plt.savefig(dist_graph_file_path, dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype='letter', format='pdf',
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None, metadata=None)
    
        




        
        

        
    def import_event():
        pass
    def delete_event():
        pass



if __name__ == "__main__":
    
    app = psyche_app(tk.Tk())
