import socket
import threading
from tkinter import *

def send():
    message = entry.get()
    listbox.insert(END, "Client: " + message)
    entry.delete(0, END)
    s.send(bytes(message, "utf-8"))

    if message.lower() == "bye":
        s.close()
        root.quit()

def receive():
    while True:
        try:
            message = s.recv(1024).decode("utf-8")
            if message.lower() == "bye":
                listbox.insert(END, "Server ended the chat.")
                s.close()
                break
            listbox.insert(END, "Server: " + message)
        except:
            break

# GUI
root = Tk()
root.title("CLIENT")

listbox = Listbox(root, height=15, width=40)
listbox.pack()

entry = Entry(root)
entry.pack(side=BOTTOM)

Button(root, text="Send", command=send).pack(side=BOTTOM)

# Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = socket.gethostname()
PORT = 12345

s.connect((HOST, PORT))

# Thread for receiving
thread = threading.Thread(target=receive)
thread.start()

root.mainloop()