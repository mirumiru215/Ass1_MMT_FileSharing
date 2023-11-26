import tkinter as tk
from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
from customtkinter import ThemeManager
from server import *
import threading
import pyperclip

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
SERVER_PORT = 1502

class ServerUI:
    def __init__(self):
        self.app = ctk.CTk()
        # super().__init__()
        self.server = Server(SERVER_IP, SERVER_PORT)
        svip = SERVER_IP
        pyperclip.copy(svip)
        self.UIObject()
        self.main_Frame.pack_forget()

    def setup(self):
        ctk.set_appearance_mode('light')
        ctk.set_default_color_theme('blue')
        self.app.title('Server')
        self.app.geometry('700x500')
        
    def run_server(self):
        self.server.start()

    def start_connect(self):
        self.login_Frame.pack_forget()
        self.main_Frame.pack(padx=10, pady=10, expand=True, fill='both', side='left')
        server_thread = threading.Thread(target=self.run_server)
        server_thread.start()
        

    def UIObject(self):
        #### LOGIN FRAME
        self.login_Frame = ctk.CTkFrame(master=self.app,
                            width=800,
                            height=200,
                           )
        self.login_Frame.pack(padx=10, pady=10, expand=True, fill="both", side="top")
        button_font = ('Family',17,'bold')
        self.connect_Button = ctk.CTkButton(master=self.login_Frame, font = button_font,text='START SERVER', command=self.start_connect)
        # self.connect_Button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
        self.connect_Button.pack(padx=10, pady=230)
        self.font3 = ('Arial',10,'bold')

        #### MAIN FRAME
        self.main_Frame = ctk.CTkFrame(master=self.app,
                                width=800,
                                height=600,
                                )
        self.main_Frame.pack(padx=10, pady=10, expand=True, fill="both", side="left")
        server_ip_text = "Server is listening on " + str(self.server.server_ip) + ":" + str(self.server.server_port)
        main_Label = tk.Label(self.main_Frame, text=server_ip_text, font=("Family", 12, 'bold'), fg='black', bg='gray')
        main_Label.place(anchor='nw')
        #### CONNECTED FRAME
        self.connected_Frame = ctk.CTkFrame(master=self.main_Frame,
                            width=300,
                            height=300,
                            fg_color='gray'
                           )
        self.connected_Frame.pack(padx=50, pady=60, expand=True, fill="none", side="left")

        repo_Label = tk.Label(self.connected_Frame, text="Hostname List", font=("Family", 15, 'bold'), fg='black', bg='gray')
        repo_Label.place(relx=0.3, anchor='nw')

        self.connected_list = tk.Listbox(master=self.connected_Frame,width=40, height=15, font=self.font3)
        self.connected_list.pack(side="bottom", anchor="se",padx=30,pady=35)
        self.connected_list.config(bg="white",borderwidth=2, relief="groove",selectmode="BROWSE")

        self.connect_Button = ctk.CTkButton(master=self.connected_Frame,width=30, height=16,text='F5', command=self.F5_display_connectedList)
        self.connect_Button.place(relx=0.5, rely=0.985, anchor='s')

        #### OPTIONS FRAME WHICH INCLUDES PING FRAME AND DISCOVER FRAME
        self.options_Frame = ctk.CTkFrame(master=self.main_Frame,
                            width=300,
                            height=250,
                           )
        self.options_Frame.pack(padx=5, pady=5, expand=True, fill="none", side="top", anchor="ne")
        #### PING FRAME
        self.ping_Frame = ctk.CTkFrame(master=self.options_Frame,
                            width=300,
                            height=100,
                            fg_color='gray'
                           )
        self.ping_Frame.pack(padx=5, pady=5, expand=True, fill="none", side="top", anchor="ne")
        # n, ne, e, se, s, sw, w, nw, or center
        pingHostname_Label = tk.Label(self.ping_Frame, text="Ping Hostname", font=("Family", 14), fg='black', bg='gray')
        pingHostname_Label.place(relx=0.1, rely=0.15, anchor='nw')
        self.pingHostname_Entry = ctk.CTkEntry(master=self.ping_Frame,
                                    placeholder_text='Enter Hostname',
                                    width=180,
                                    height=30,
                                    text_color='black',
                                    corner_radius=10)
        self.pingHostname_Entry.configure(state='normal')
        self.pingHostname_Entry.place(relx=0.35, rely=0.6, anchor=tk.CENTER)

        pingHostname_Button = ctk.CTkButton(master=self.ping_Frame,width=85, height=30, text='PING', command=self.ping_hostname)
        pingHostname_Button.place(relx=0.8, rely=0.6, anchor=tk.CENTER)

        #### DISCOVER FRAME
        self.discover_Frame = ctk.CTkFrame(master=self.options_Frame,
                            width=300,
                            height=100,
                            fg_color='gray'
                           )
        self.discover_Frame.pack(padx=5, pady=5, expand=True, fill="none", side="bottom", anchor="se")

        self.discoverHostname_Entry = ctk.CTkEntry(master=self.discover_Frame,
                                    placeholder_text='Enter Hostname',
                                    width=180,
                                    height=30,
                                    text_color='black',
                                    corner_radius=10)
        discoverHostname_Label = tk.Label(self.discover_Frame, text="Discover Hostname",  font=("Arial", 14),fg='black', bg='gray')
        discoverHostname_Label.place(relx=0.1, rely=0.15, anchor='nw')
        self.discoverHostname_Entry.configure(state='normal')
        self.discoverHostname_Entry.place(relx=0.35, rely=0.6, anchor=tk.CENTER)
            
        discoverHostname_Button = ctk.CTkButton(master=self.discover_Frame,width=85, height=30, text='DISCOVER', command=self.discover_hostname)
        discoverHostname_Button.place(relx=0.8, rely=0.6, anchor=tk.CENTER)


        #### REPO FRAME
        self.repo_Frame = ctk.CTkFrame(master=self.main_Frame,
                            width=300,
                            height=400,
                            fg_color='gray'
                           )
        self.repo_Frame.pack(padx=5, pady=5, expand=True, fill="none", side="bottom", anchor="se")

        repo_Label = tk.Label(self.repo_Frame, text="Repo List", font=("Family", 14), fg='black', bg='gray')
        repo_Label.place(relx=0.38, anchor='nw')

        self.repo_list = tk.Listbox(master=self.repo_Frame,width=40, height=15, font=self.font3)
        self.repo_list.pack(side="bottom", anchor="se",padx=50,pady=30)
        self.repo_list.config(bg="white",borderwidth=2, relief="groove",selectmode="BROWSE")

    def ping_hostname(self):
        hostname = self.pingHostname_Entry.get()
        if not hostname:
            # Handle empty fields
            messagebox.showinfo("Error", "Please enter hostname!")
            return
        messagebox.showinfo("Success", self.server.ping(hostname))


    def display_repo(self, hostname=''):
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
        
    def F5_display_connectedList(self):
        self.connected_list.delete(0,END)
        for hostname in self.server.connectedClient:
            self.connected_list.insert(tk.END, hostname)
    

if __name__ == '__main__':
    app = ServerUI()
    app.setup()
    app.app.mainloop()
    
    