from tkinter import messagebox
import tkinter as tk
import random
import time
import os

class Program():

    def bttnPress():
        global image,images
        if os.path.basename(os.getcwd()) == 'Answers':
            pass
        else:
            os.chdir('Answers')
            images = []
            for i in os.listdir(os.getcwd()):
                images.append(i)
        if len(question.get()) == 0:
            messagebox.showinfo('Program Info','Please ask a question.')
        else:
            image.config(file=random.choice(images))
            image_layout.delete('all')
            image_layout.create_image(200,200,anchor=tk.CENTER,image=image)

    def createImage():
        global image
        image = tk.PhotoImage(file='ball.png')
        image_layout.create_image(200,200,anchor=tk.CENTER,image=image)

class Window(tk.Frame):
    def __init__(self,window):
        tk.Frame.__init__(self,window)
        global image_layout,question,status_label
        self.window = window
        self.window.title('tk Magic 8 Ball')
        self.window.geometry('500x500')
        self.window.resizable(height=False,width=False)

        image_layout = tk.Canvas(self.window,height=472,width=474)
        question_frame = tk.LabelFrame(self.window,text='Question',height=60,width=350)
        question = tk.Entry(self.window,width=35)
        bttn = tk.Button(self.window,text='Shake',command=Program.bttnPress)
        image_layout.place(x=53,y=10)
        question_frame.place(x=10,y=400)
        question.place(x=20,y=425)
        bttn.place(x=400,y=420)
root = tk.Tk()
app = Window(root)
Program.createImage()
root.mainloop()
