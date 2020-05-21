import pandas as pd
from tkinter import *
from tkinter import filedialog
documentName = ""
def uploadData(): #Select the file and get the root
    global documentName
    documentName = filedialog.askopenfilename( filetypes = (("Excel file", "*.xlsx"),("All files", "*.*")))

root = Tk()
uploadButton = Button(root, text = 'Upload', command=uploadData)
uploadButton.place(x=10,y=10)
documentNameLabel = Label(root, text = 'PyStatistics Interface v 1.0', font = "Helvetica 16")
documentNameLabel.place(x = 10, y = 40)

root.geometry('300x300')
root.mainloop()