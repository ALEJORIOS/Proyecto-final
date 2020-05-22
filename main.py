import pandas as pd
from tkinter import *
from tkinter import filedialog
documentName = ""
limits = [1000, 600]
barLimits = [298, limits[1]]
def uploadData(): #Select the file and get the root
    global documentName
    documentName = filedialog.askopenfilename( filetypes = (("Excel file", "*.xlsx"),("All files", "*.*")))

root = Tk()
lateralBar = Frame(root,width = barLimits[0],height = barLimits[1], bg ="#002242")
lateralBar.place(x = 0)
uploadButton = Button(root, text = 'Upload', command=uploadData, bd = "0px", width = 24, bg = "#002242", fg="White", font="Calibri 16 bold",activebackground = "#554CFC", anchor = 'w', padx = 15)
uploadButton.place(x=0,y=100)
documentNameLabel = Label(root, text = 'PyStatistics Interface v 1.0', font = "Helvetica 16")
documentNameLabel.place(x = limits[0]/2-170,y = 30)

root.geometry(str(limits[0])+'x'+str(limits[1]))
root.mainloop()