import tkinter as tk
import customtkinter as ctk
from client import *
import threading
import time
from tkinter import END, filedialog
import os
from tkinter import messagebox

SIZE = 1024
REPOSITORY_PATH = 'repository/'
FORMAT = 'utf-8'

class MyApp:
    def __init__(self):
        self.app = ctk.CTk()
        self.client =  Client('',0,'')
        self.UIobject()

    def setup(self):
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('blue')
        self.app.title('Client')
        self.app.geometry('750x450')


    def UIobject(self):
        self.login_Frame = ctk.CTkFrame(master=self.app,
                            width=800,
                            height=200,
                            bg_color='black')
        self.login_Frame.pack(padx=10, pady=10, expand=True, fill="both", side="left")

        self.Entry_Frame = ctk.CTkFrame(master=self.login_Frame,
                            width=250,
                            height=100,
                           )
        self.Entry_Frame.place(relx=0.5,rely=0.3,anchor=tk.CENTER)
        

        self.serverIP_Entry = ctk.CTkEntry(master=self.Entry_Frame,
                                    placeholder_text='Server IP',
                                    width=200,
                                    height=30,
                                    text_color='white',
                                    corner_radius=10)
        self.serverIP_Entry.configure(state='normal')
        self.serverIP_Entry.pack(padx=5, pady=5, expand=True, fill="none", side="top", anchor="ne")

        self.hostname_Entry = ctk.CTkEntry(master=self.Entry_Frame,
                                    placeholder_text='Hostname',
                                    width=200,
                                    height=30,
                                    text_color='white',
                                    corner_radius=10)
        self.hostname_Entry.configure(state='normal')
        self.hostname_Entry.pack(padx=5, pady=5, expand=True, fill="none", side="bottom", anchor="ne")

    
        self.connect_Button = ctk.CTkButton(master=self.app, text='Connect', command=self.start_connect)
        self.connect_Button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    

    def start_connect(self):
        if not self.serverIP_Entry.get() or not self.hostname_Entry.get():
            messagebox.showerror("Error", "Please fill in both Server IP and Hostname!")
            return
        SERVER_IP = self.serverIP_Entry.get()
        SERVER_PORT = 1502
        hostname = self.hostname_Entry.get()

        self.client = Client(SERVER_IP, SERVER_PORT, hostname)
        self.client.start()
        time.sleep(1)
        
        # Hide the login frame
        self.login_Frame.pack_forget()
        self.show_repository_frame()

    def show_repository_frame(self):
        #### MAIN FRAME
        self.repo_frame = ctk.CTkFrame(master=self.app, width=800, height=400, bg_color='black')
        self.repo_frame.pack(padx=10, pady=10, expand=True, fill="both", side="left")

        name = "Hostname: " + self.hostname_Entry.get()
        Hostname_label = tk.Label(master=self.repo_frame, text=name, fg='white',bg='gray', font=("Family", 14))
        Hostname_label.place(relx=0.04, rely=0.07)


        self.font1 = ('Arial',20,'bold')
        self.font2 = ('Arial',15,'bold')
        self.font3 = ('Arial',10,'bold')
        self.user_repo_label = ctk.CTkLabel(master=self.repo_frame,font=self.font1, text='File Sharing', text_color='white')
        self.user_repo_label.pack()

        
        #### HOST REPO FRAME
        self.Host_Repo_Frame = ctk.CTkFrame(master=self.repo_frame,
                            width=240,
                            height=400,
                            fg_color='gray'
                           )
        self.Host_Repo_Frame.pack(padx=10, pady=10, expand=True, fill="none", side="left")
        self.Host_Repo_Frame.place(x = 30,y=60)

        repo_Label = tk.Label(self.Host_Repo_Frame, text="Repository", font=("Family", 15, 'bold'), fg='black', bg='gray')
        repo_Label.place(relx=0.3, anchor='nw')

        self.repo_list = tk.Listbox(master=self.Host_Repo_Frame,width=40, height=15, font=self.font3)
        self.repo_list.pack(side="bottom", anchor="se",padx=30,pady=35)
        self.repo_list.config(bg="white",borderwidth=2, relief="groove",selectmode="BROWSE")

        path = os.getcwd()
        newpath = path + '/repository'
        repo_filename = os.listdir(newpath)
        
        for filename in repo_filename:
            self.repo_list.insert(tk.END,filename)

        #### OPTIONS FRAME
        self.options_Frame = ctk.CTkFrame(master=self.repo_frame,
                            width=240,
                            height=270,
                           )
        self.options_Frame.pack(padx=5, pady=5,  fill="none", side="top", anchor="ne")
        self.options_Frame.place(x = 350,y=60)

        self.FD_Frame = ctk.CTkFrame(master=self.options_Frame,
                            width=300,
                            height=250,
                           )
        self.FD_Frame.pack(padx=5, pady=5, expand=True, fill="none", side="top", anchor="ne")
        #### FETCH FRAME
        self.Fetch_Frame = ctk.CTkFrame(master=self.FD_Frame,
                            width=300,
                            height=100,
                            fg_color='gray'
                           )
        self.Fetch_Frame.pack(padx=5, pady=5, expand=True, fill="none", side="top", anchor="ne")
        # n, ne, e, se, s, sw, w, nw, or center
        fetch_Label = tk.Label(self.Fetch_Frame, text="Fetch file", font=("Family", 14), fg='black', bg='gray')
        fetch_Label.place(relx=0.1, rely=0.15, anchor='nw')
        self.fetch_Entry = ctk.CTkEntry(master=self.Fetch_Frame,
                                    placeholder_text='Enter filename',
                                    width=180,
                                    height=30,
                                    text_color='white',
                                    corner_radius=10)
        self.fetch_Entry.configure(state='normal')
        self.fetch_Entry.place(relx=0.35, rely=0.6, anchor=tk.CENTER)

        fetch_Button = ctk.CTkButton(master=self.Fetch_Frame,width=85, height=30, text='FETCH', command=self.fetchFile)
        fetch_Button.place(relx=0.8, rely=0.6, anchor=tk.CENTER)

        #### DISCOVER FRAME
        self.delete_Frame = ctk.CTkFrame(master=self.FD_Frame,
                            width=300,
                            height=100,
                            fg_color='gray'
                           )
        self.delete_Frame.pack(padx=5, pady=5, expand=True, fill="none", side="bottom", anchor="se")

        self.delete_Entry = ctk.CTkEntry(master=self.delete_Frame,
                                    placeholder_text='Enter filename',
                                    width=180,
                                    height=30,
                                    text_color='white',
                                    corner_radius=10)
        delete_Label = tk.Label(self.delete_Frame, text="Delete file",  font=("Arial", 14),fg='black', bg='gray')
        delete_Label.place(relx=0.1, rely=0.15, anchor='nw')
        self.delete_Entry.configure(state='normal')
        self.delete_Entry.place(relx=0.35, rely=0.6, anchor=tk.CENTER)
            
        delete_Button = ctk.CTkButton(master=self.delete_Frame,width=85, height=30, fg_color='#990000', hover_color='red',text='DELETE', command=self.deleteFile)
        delete_Button.place(relx=0.8, rely=0.6, anchor=tk.CENTER)

        #### PUBLISH BUTTON
        self.publish_button = ctk.CTkButton(master=self.repo_frame, 
                                            font=self.font2, text_color='white', 
                                            text='Publish', fg_color='#06911f', 
                                            hover_color='#06911f', 
                                            bg_color = '#09112e', 
                                            cursor= 'hand2', corner_radius=5, width=120, command=self.openFile)
        self.publish_button.place(relx=0.15, rely=0.8)

        #### DISCONNECT BUTTON
        self.quit_Button = ctk.CTkButton(master=self.repo_frame, 
                                            font=self.font2, text_color='white', 
                                            text='Disconnect', fg_color='red', 
                                            hover_color='#990000', 
                                            cursor= 'hand2', corner_radius=5, width=120, command=self.quitCli)
        self.quit_Button.place(relx=0.6, rely=0.85)

        # #### FETCH BUTTON
        # self.fetch_Entry = ctk.CTkEntry(master=self.options_Frame,
        #                             placeholder_text='Fetch file name',
        #                             width=150,
        #                             height=30,
        #                             text_color='white',
        #                             corner_radius=10)
        # self.fetch_Entry.configure(state='normal')
        # self.fetch_Entry.place(relx=0.19, rely=0.2)

        # self.fetch_button = ctk.CTkButton(master=self.options_Frame, 
        #                                     font=self.font2, text_color='white', 
        #                                     text='Fetch', fg_color='#06911f', 
        #                                     hover_color='#06911f', 
        #                                     bg_color = '#09112e', 
        #                                     cursor= 'hand2', corner_radius=5, width=120, command=self.fetchFile)
        # self.fetch_button.place(relx=0.25, rely=0.35)

        # #### DELETE BUTTON
        # self.delete_Entry = ctk.CTkEntry(master=self.options_Frame,
        #                             placeholder_text='Delete File name',
        #                             width=150,
        #                             height=30,
        #                             text_color='white',
        #                             corner_radius=10)
        # self.delete_Entry.configure(state='normal')
        # self.delete_Entry.place(relx=0.19, rely=0.5)

        # self.delete_button = ctk.CTkButton(master=self.options_Frame, 
        #                                     font=self.font2, text_color='white', 
        #                                     text='Delete', fg_color='red', 
        #                                     hover_color='#990000', 
        #                                     cursor= 'hand2', corner_radius=5, width=120, command=self.deleteFile)
        # self.delete_button.place(relx=0.25, rely=0.65)
        

    def openFile(self): 
        filepath = filedialog.askopenfilename()
        directory, filename = os.path.split(filepath)
        print(directory)
        print(filename)
        msg = self.client.publish(directory,filename)

        if msg == "Uploaded successfully!":
            messagebox.showinfo("Success", msg)
        else:
            messagebox.showerror("Error", msg)
        
        self.repo_list.delete(0,END)
        path = os.getcwd()
        newpath = path + '/repository'
        repo_filename = os.listdir(newpath)
        for filename in repo_filename:
            self.repo_list.insert(tk.END,filename)
        
    def quitCli(self):
        self.app.withdraw()
        self.client.quitCli()

    def fetchFile(self):
        if not self.fetch_Entry.get():
            messagebox.showerror("Error", "Please fill in filename!")
            return
        # Create a loading indicator label
        loading_label = tk.Label(master=self.repo_frame, text='Loading...', fg='white',bg='black', font=("Arial", 14))
        loading_label.pack(padx=10, pady=10,side='bottom')

        # Start the fetch operation in a separate thread
        def fetch_thread():
            msg = self.client.fetch(self.fetch_Entry.get())
            if msg == 'These are clients having the file:':
                self.repo_list.insert(tk.END, self.fetch_Entry.get())
                messagebox.showinfo("Success", "Done fetch file!")
            else:
                messagebox.showerror("Error", msg)

            # Remove the loading indicator
            loading_label.destroy()

        thread = threading.Thread(target=fetch_thread)
        thread.start()

    def deleteFile(self):
        if not self.delete_Entry.get():
            messagebox.showerror("Error", "Please fill in filename!")
            return
        msg = self.client.deleteFile(self.delete_Entry.get())
        messagebox.showinfo("Notice",msg)
        self.repo_list.delete(0,END)
        path = os.getcwd()
        newpath = path + '/repository'
        repo_filename = os.listdir(newpath)
        for filename in repo_filename:
            self.repo_list.insert(tk.END,filename)

    #############DON'T DELETE THIS#################
    # def fetchFile(self):
    #     if self.fetch_Entry.get() == '':
    #         messagebox.showinfo("Error", "Please enter file name!")
    #     else:
    #         msg = self.client.fetch(self.fetch_Entry.get())
    #         if msg == 'These are clients having the file:':
    #             self.repo_list.insert(tk.END,self.fetch_Entry.get())
    #             messagebox.showinfo("Success", "Done fetch file!")
    #         else:
    #             messagebox.showerror("Error",msg)

if __name__ == '__main__':
    app = MyApp()
    app.setup()
    app.app.mainloop()
