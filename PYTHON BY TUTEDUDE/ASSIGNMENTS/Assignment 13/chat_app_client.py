import socket
from tkinter import *

def send(listbox, entry):
    message = entry.get()
    listbox.insert('end',"Client: "+ message)
    entry.delete(0, END)
    s.send(bytes(message, "utf-8"))
    receive(listbox)

def receive(listbox):
    message = s.recv(500)
    listbox.insert('end',"Server: "+ message.decode("utf-8"))


root = Tk()
entry = Entry()
entry.pack(side=BOTTOM)
listbox = Listbox(root, height=15, width=35)
listbox.pack()
s_buton = Button(root, text="Send",command=lambda : send(listbox,entry))
s_buton.pack(side=BOTTOM)
r_buton = Button(root, text="Recieve",command=lambda : receive(listbox))
r_buton.pack(side=BOTTOM)
root.title("CLIENT")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12121
s.connect((HOST_NAME, PORT))


root.mainloop()
