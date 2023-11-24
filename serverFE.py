import tkinter as tk
from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
from server import *
import threading


def get_local_ip():
    s = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
    try:
        s.connect(('192.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

SERVER_IP = get_local_ip()
SERVER_PORT = 4869

class ServerUI:
    def __init__(self):
        self.app = ctk.CTk()
        # super().__init__()
        self.server = Server(SERVER_IP, SERVER_PORT)
        self.UIObject()


    def setup(self):
        ctk.set_appearance_mode('light')
        ctk.set_default_color_theme('blue')
        self.app.title('ServerUI')
        self.app.geometry('800x400')
        
    
    def run_server(self):
        self.server.start()

    def start_connect(self):
        self.login_Frame.pack_forget()
        self.main_Frame.pack(padx=10, pady=10, expand=True, fill='both', side='left')

        server_thread = threading.Thread(target=self.run_server)
        server_thread.start()
        

    def UIObject(self):
        self.login_Frame = ctk.CTkFrame(master=self.app,
                            width=800,
                            height=200,
                            bg_color='black')
        self.login_Frame.pack(padx=10, pady=10, expand=True, fill="both", side="left")
        self.connect_Button = ctk.CTkButton(master=self.login_Frame, text='START SERVER', command=self.start_connect)
        self.connect_Button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)



        self.main_Frame = ctk.CTkFrame(master=self.app,
                                width=800,
                                height=600,
                                bg_color='white')
        self.main_Frame.pack(padx=10, pady=10, expand=True, fill="both", side="left")

        self.pingHostname_Entry = ctk.CTkEntry(master=self.main_Frame,
                                    placeholder_text='Enter Hostname',
                                    width=200,
                                    height=30,
                                    text_color='black',
                                    corner_radius=10)
        pingHostname_Label = tk.Label(self.main_Frame, text="Ping Hostname",  font=("Arial", 14))
        pingHostname_Label.place(relx=0.8,y=100, anchor=tk.CENTER)
        self.pingHostname_Entry.configure(state='normal')
        self.pingHostname_Entry.place(relx=0.8,y=120, anchor=tk.CENTER)
        self.discoverHostname_Entry = ctk.CTkEntry(master=self.main_Frame,
                                    placeholder_text='Enter Hostname',
                                    width=200,
                                    height=30,
                                    text_color='black',
                                    corner_radius=10)
        discoverHostname_Label = tk.Label(self.main_Frame, text="Discover Hostname",  font=("Arial", 14))
        discoverHostname_Label.place(relx=0.8, y=300, anchor=tk.CENTER)
        self.discoverHostname_Entry.configure(state='normal')
        self.discoverHostname_Entry.place(relx=0.8, y=300.005, anchor=tk.CENTER)

        pingHostname_Button = ctk.CTkButton(master=self.main_Frame, text='PING', command=self.ping_hostname)
        pingHostname_Button.place(relx=0.8, y=180, anchor=tk.CENTER)
            
        discoverHostname_Button = ctk.CTkButton(master=self.main_Frame, text='DISCOVER', command=self.discover_hostname)
        discoverHostname_Button.place(relx=0.8, y=360, anchor=tk.CENTER)


    def ping_hostname(self):
        hostname = self.pingHostname_Entry.get()
        if not hostname:
            # Handle empty fields
            messagebox.showinfo("Error", "Please enter hostname!")
            return
        messagebox.showinfo("Success", self.server.ping(hostname))


    def display_repo(self, hostname=''):
        self.font3 = ('Arial',10,'bold')
        self.repo_list = tk.Listbox(master=self.main_Frame,width=40, height=15, font=self.font3)
        self.repo_list.pack(anchor='w')
        self.repo_list.delete(0,END)
        if hostname in self.server.connectedClient:
            for filename in self.server.clientFileList[self.server.connectedClient[hostname]]:
                self.repo_list.insert(tk.END,filename)
        

    def discover_hostname(self):
        hostname = self.discoverHostname_Entry.get()
        if not hostname:
            # Handle empty fields
            messagebox.showinfo("Error", "Please enter hostname!")
            return
        self.server.discover(hostname)
        self.display_repo(hostname)
        
    


    

if __name__ == '__main__':
    app = ServerUI()
    app.setup()
    app.app.mainloop()
    
    