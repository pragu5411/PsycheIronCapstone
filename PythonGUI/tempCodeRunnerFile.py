import tkinter as tk
HEIGHT = 800
WIDTH = 800
FONT = ('Times New Roman', 12)
class psyche_app:
    
    def __init__(self,master):
        window = master
        canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)
        canvas.pack()

        root = tk.Frame(master=window)
        root.place( relx= .05, rely=.05,relheight = .90, relwidth = .90)

        left_side = tk.Frame(master = root, bg ='red')
        left_side.place(relx = 0, rely = 0, relheight = 1, relwidth = .5)
        left_title = tk.Label(master= left_side, text ="Current Kernels", font = FONT)
        left_title.place(relx=0,rely =0,relwidth = 1, relheight = .05)
        kernel_list = tk.Listbox(master=left_side)
        kernel_list.place(relx=0,rely=.05,relwidth = 1, relheight =.65)
        kernel_menu = tk.Frame(master= left_side)
        add_kernal = tk.Button(master=kernel_menu, text = "Import Kernel", font = FONT)
        add_kernal.pack(side = 'left',padx = 15, pady = 15)
        remove_kernal = tk.Button(master=kernel_menu, text = "Remove Kernel", font = FONT)
        remove_kernal.pack(side = 'left',padx = 15, pady = 15)
        kernel_menu.place(relx=0,rely=.7,relwidth = 1, relheight =.3)


        right_side = tk.Frame(master = root, bg ='blue')
        right_side.place(relx = .5, rely = 0, relheight = 1, relwidth = .5)


        window.mainloop()



if __name__ == "__main__":
    
    app = psyche_app(tk.Tk())
