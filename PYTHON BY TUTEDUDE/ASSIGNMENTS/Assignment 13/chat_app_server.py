import socket
from tkinter import *

def send(listbox,entry):
    message = entry.get()
    listbox.insert('end',"Server: " +message)
    entry.delete(0, END)
    client.send(bytes(message, "utf-8"))

def receive(listbox):
    messaage_from_client = client.recv(50)
    listbox.insert('end',"Client: "+ messaage_from_client.decode("utf-8"))

root = Tk()
entry = Entry()
entry.pack(side=BOTTOM)
listbox = Listbox(root, height=15, width=35)
listbox.pack()
s_buton = Button(root, text="Send",command=lambda : send(listbox,entry))
s_buton.pack(side=BOTTOM)
r_buton = Button(root, text="Recieve",command=lambda : receive(listbox))
r_buton.pack(side=BOTTOM)
root.title("SERVER")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname() #use in the place of ip address
PORT = 12121
s.bind((HOST_NAME, PORT))
s.listen(4)
client, address = s.accept()

print(address)
root.mainloop()

