# importing tkinter
from tkinter import *
# importing YouTube module
from pytube import YouTube
# open file from where it was saved
from tkinter import filedialog

# initializing tkinter
myapp = Tk()
# setting the geometry of the GUI
myapp.geometry("450x400")
# setting the title of the GUI
myapp.title("Youtube Downloader")
myapp.configure(bg='white')

# defining download function
def download():
    # using try and except to execute program without errors)
    try:
        myVar.set("Downloading...")
        myapp.update()
        YouTube(link.get()).streams.first().download()
        link.set("Video downloaded successfully")
    except Exception as e:
        myVar.set("Mistake")
        myapp.update()
        link.set("Insert the correct link")

# created the Label widget to welcome user
Label(myapp, text="Youtube Downloader", font="Georgia 30 bold", bd=8, bg="gray").pack()
# declaring StringVar type variable
myVar = StringVar()
# setting the default text to myVar
myVar.set("Insert a Youtube link below")
# created the Entry widget to ask user to enter the url
Entry(myapp, textvariable=myVar, width=40).pack(pady=15)
# declaring StringVar type variable
link = StringVar()
# created the Entry widget to get the link
Entry(myapp, textvariable=link, width=60).pack(pady=10)
# created and called the download function to download video
Button(myapp, text="Save To Drive", command=download).pack()

def open():
    myapp.filename = filedialog.askopenfile(initialdir="/Desktop/All in One/_all.desktop/Python", title="Select A File", filetypes=(("mp4 files", ".mp4"), ("all files", "*.*")))

btn = Button(myapp, text="Open File", command=open).pack()
# running the mainloop
myapp.mainloop()