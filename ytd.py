from tkinter import *
from pytube import YouTube


root=Tk()
root.geometry('400x200')
root.resizable(0,0)
root.title('Youtube Downloader')
Label(root,text = 'Youtube Downloader', font ='arial 20 bold').pack()
Label(root,text = ':- an3rdone', font ='arial 10 ').pack()
link =StringVar()
Label(root, text = 'Link Here:', font = 'arial 15',).place(x= 30, y = 60)

link_enter = Entry(root, width = 50,textvariable = link).place(x = 32, y =90 )

def Downloader():
    url=YouTube(str(link.get()))
    video=url.streams.first()
    video.download()
    Label(root,text='Download',font='arial 15').place(x=180,y=210)
Button(root, text='DOWNLOAD', font='arial 15 bold', bg='blue', padx=2, command=Downloader).place(x=130,y=150)
root.mainloop()
