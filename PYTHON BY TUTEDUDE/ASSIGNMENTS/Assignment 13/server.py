import socket
import threading
from tkinter import *

def send():
    message = entry.get()
    listbox.insert(END, "Server: " + message)
    entry.delete(0, END)
    client.send(bytes(message, "utf-8"))

    if message.lower() == "bye":
        client.close()
        root.quit()

def receive():
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            if message.lower() == "bye":
                listbox.insert(END, "Client ended the chat.")
                client.close()
                break
            listbox.insert(END, "Client: " + message)
        except:
            break

# GUI
root = Tk()
root.title("SERVER")

listbox = Listbox(root, height=15, width=40)
listbox.pack()

entry = Entry(root)
entry.pack(side=BOTTOM)

Button(root, text="Send", command=send).pack(side=BOTTOM)

# Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

HOST = socket.gethostname()
PORT = 12345

s.bind((HOST, PORT))
s.listen(1)

print("Waiting for client...")
client, addr = s.accept()
print("Connected to:", addr)

# Thread for receiving
thread = threading.Thread(target=receive)
thread.start()

root.mainloop()