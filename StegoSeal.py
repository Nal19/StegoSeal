from tkinter import*
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from stegano import lsb
from PIL import Image, ImageTk
import base64
import string
import os

def on_button_click():
    key = ktext.get()
    if len(key) != 5:
        messagebox.showerror("Invalid Key", "Key should be of 5 char length")
    else:
        messagebox.showinfo("Info", "Select an image to encode your message")
        msg = mtext.get("1.0","end-1c")
        path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])
        if len(path) and len(msg) != 0:
            encode(msg,key,path)
        else:
            messagebox.showerror("Error", "No message found. Type message and retry")

def encode(msg,key,path):
    cipher = encrypt(key,msg)
    image = Image.open(path)
    image = image.resize((200,200))
    photo = ImageTk.PhotoImage(image)
    ilabel = tk.Label(master=eframe)
    ilabel.place(x=50,y=290)
    ilabel.config(image=photo)
    ilabel.image = photo
    label1 = tk.Label(master=eframe, text = "Message encoded!", bg = '#A9BA9D', font = ("Arial", 10))
    label1.place(x=90,y=495)
    label2 = tk.Label(master=eframe, text = "Enter File Name and Save", bg = '#A9BA9D', font = ("Arial", 10))
    label2.place(x=30,y=515)
    stext.place(x=30,y=540, height = 25, width = 170)
    button = tk.Button(master=eframe, text="Save", command=lambda: read_text(cipher,path))
    button.place(x=220,y=540)

def encrypt(key,msg):
    enc = []
    for i in range(len(msg)):
        list_key = key[i % len(key)]
        list_enc = chr((ord(msg[i]) +
                     ord(list_key)) % 256)
        enc.append(list_enc)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def read_text(cipher,path):
    fname = stext.get()
    fname=str(fname)
    steg(cipher,path,fname)

def steg(cipher,path,fname):    
    secret=lsb.hide(path,cipher)
    secret.save(fname+".png")
    messagebox.showinfo("File Saved", "File saved in C: >> Program Files >> Python312 >> StegoSeal")
    

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])
    image = Image.open(file_path)
    image = image.resize((200,200))
    photo = ImageTk.PhotoImage(image)
    uplabel = tk.Label(master=dframe)
    uplabel.place(x=50,y=80)
    uplabel.config(image=photo)
    uplabel.image = photo
    pklabel = tk.Label(master=dframe, text = "Enter Key",bg = '#8fbc8f', font = ("Arial", 10))
    pklabel.place(x=30,y=300)
    pktext.place(x=30,y=330, width = 250)
    dbutton = tk.Button(master=dframe, text="Decode", command=lambda: decode(file_path))
    dbutton.place(x=145,y=360)

def decode(fpath):
    dkey = pktext.get()
    if len(dkey) != 5:
        messagebox.showerror("Invalid Key", "Key should be of 5 char length")
    else:
        try:
            plaintext = lsb.reveal(fpath)
        except:
            messagebox.showwarning("Invalid Image", "Select the image encoded with image(C: >> Program Files >> Python312 >> StegoSeal)")
        else:
            message = tk.StringVar()
            message.set(decrypt(dkey, plaintext))
            if message:
                msglabel = tk.Label(master=dframe, text = "Message Received", bg = '#8fbc8f', font = ("Arial", 10))
                msglabel.place(x=30,y=390)
                ktext = tk.Entry(master=dframe, textvariable = message)
                ktext.place(x=30,y=420, height= 100, width = 250)

            else:
                msglabel = tk.Label(master=dframe, text = "No Message Received", bg = '#8fbc8f', font = ("Arial", 10))
                msglabel.place(x=30,y=380)
        

def decrypt(key, code):
    dec = []
    enc = base64.urlsafe_b64decode(code).decode()
    for i in range(len(enc)):
        list_key = key[i % len(key)]
        list_dec = chr((256 + ord(enc[i]) - ord(list_key)) % 256)
        dec.append(list_dec)
    return "".join(dec)


    
    
app = tk.Tk()
app.title("StegoSeal")
app.geometry('600x600')

eframe = tk.Frame(master=app, width = 300, height = 500, bg = '#A9BA9D')
eframe.pack(fill=tk.Y, side=tk.LEFT)

elabel = tk.Label(master=eframe, text = "Encode", bg = '#8fbc8f', font = ("Arial", 12))
elabel.place(x=125,y=0)

msglabel = tk.Label(master=eframe, text = "Enter Message (max 50 char)",bg = '#A9BA9D', font = ("Arial", 10))
msglabel.place(x=30,y=40)

mtext = tk.Text(master=eframe)
mtext.place(x=30,y=70,height = 100, width = 250)

keylabel = tk.Label(master=eframe, text = "Enter Key (max 5 char)",bg = '#A9BA9D', font = ("Arial", 10))
keylabel.place(x=30,y=180)

ktext = tk.Entry(master=eframe)
ktext.place(x=30,y=210, width = 250)

ebutton = tk.Button(master=eframe, text="Encode", command=lambda: on_button_click())
ebutton.place(x=125,y=250)

stext = tk.Entry(master=eframe)

dframe = tk.Frame(master=app, width = 300, height = 500, bg = '#8fbc8f')
dframe.pack(fill=tk.Y, side=tk.RIGHT)

imgframe = tk.Frame(dframe, bg = "#A9BA9D", width=200, height=200)
imgframe.place(x=50,y=80)

dlabel = tk.Label(master=dframe, text = "Decode", bg = '#A9BA9D', font = ("Arial", 12))
dlabel.place(x=125,y=0)

uplabel = tk.Label(master=dframe, text = "Upload Image", bg = '#8fbc8f', font = ("Arial", 11))
uplabel.place(x=30,y=40)

upbutton = tk.Button(master=dframe, text="Browse", command = select_image)
upbutton.place(x=150,y=40)
    
pktext = tk.Entry(master=dframe)


app.resizable(0, 0)
app.mainloop()
