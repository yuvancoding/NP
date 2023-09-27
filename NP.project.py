from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.minsize(650,650)
root.maxsize(650,650)
root.configure(background="#A45EE5")

open_img = ImageTk.PhotoImage(Image.open("open.png"))
save_img = ImageTk.PhotoImage(Image.open("save.png"))
exit_img = ImageTk.PhotoImage(Image.open("exit.png"))

label_file_name = Label(root, text="File Name")
label_file_name.place(relx=0.28,rely=0.03,anchor=CENTER)

input_file_name = Entry(root)
input_file_name.place(relx=0.46,rely=0.03,anchor=CENTER)

my_text = Text(root, height=35, width=80, bg="salmon", fg="blue")
my_text.place(relx=0.5,rely=0.55,anchor=CENTER)

#open_button = Button(root, image=open_img, text="Open File", command=openFile)
#open_button.place(relx=0.05,rely=0.03,anchor=CENTER)

root.mainloop()