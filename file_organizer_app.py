import os
import time
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog
from tkinter import messagebox
from organizer import file_organizer

info1='''
    Creator: Keerthivasan S J

    Date: 14 November 2023

    File Organiser is an application used to organize files within the specified path.
    Provide the desired directory path in the Entry box shown on the application window.

    The types of files that can be organized by this application include:
        - Text
        - Java
        - Python
        - HTML
        - CSS
        - PDF
        - Photos
        - Videos
        - Audio
        - Documents
        - Excel
        - PowerPoint
        - Applications(exe)
'''

Help_info = '''
    How to use this application:

        1. Paste the path of the folder or redirect 
        to the folder path using the Browse button.
        
        2. Click "Organize Button" to arrange the files 
        in the separate folders.
'''

#main window of the file organiser
def main_window():
    
    win=tk.Tk()
    win.title("File Organizer")
    win.geometry("450x450")
    win.resizable(width=0,height=0)

    #functions for buttons
    def browse_path():
        file_path=tk.filedialog.askdirectory()
        path.set(file_path)
    
    def is_valid_path(path:str):
        return os.path.exists(path)
    
    def organise():
        file_path=path.get()
        if is_valid_path(file_path):
            file_organizer(file_path)
            completed_status=tk.Label(win, text="Files are organized sucesfully!")
            path.set("")
            completed_status.grid(row=4, column=1, padx=5, pady=5)
            win.after(1500,completed_status.destroy)

        else:
            messagebox.showwarning("Warning", "Please enter a valid path!")
            path.set("")

    def clear():
        path.set("")

    #menubar functions

    def about_info():
        about_win=tk.Toplevel(win)
        about_win.title("About")
        about_win.geometry("500x450")
        about_win.resizable(width=0,height=0)

        separator=ttk.Separator(about_win,orient='horizontal')

        heading=tk.Label(about_win,text="About",font=('areal',12,'bold'),anchor="center")
        info=tk.Label(about_win, text=info1, justify="left")
        close=ttk.Button(about_win,text="Close",width=10,style="TButton",command=about_win.destroy)
        heading.pack()
        separator.pack(fill='x', side="top", padx=20)
        info.pack()
        close.pack(fill='x', padx=30, side="right")

        about_win.mainloop()

    def help():
            help_win=tk.Toplevel(win)
            help_win.title("Help")
            help_win.geometry("300x250")
            help_win.resizable(width=0,height=0)

            separator=ttk.Separator(help_win,orient='horizontal')

            heading=tk.Label(help_win,text="Help",font=('areal',12,'bold'),anchor="center")
            helpinfo=tk.Label(help_win, text=Help_info, justify="left")
            close=ttk.Button(help_win,text="Close",width=10,style="TButton",command=help_win.destroy)
            heading.pack()
            separator.pack(fill='x', side="top", padx=20)
            helpinfo.pack(padx=20)
            close.pack(fill='x', padx=30, side="right")

            help_win.mainloop()

    def new_window():
        main_window()

    #menubar starts here
    menubar=tk.Menu(win)

    #File
    file=tk.Menu(menubar, tearoff=0)
    file.add_command(label="New Window",command=new_window)
    file.add_separator()
    file.add_command(label="Exit", command=win.destroy)

    #Option
    option=tk.Menu(menubar,tearoff=0)
    option.add_command(label="Browse",command=browse_path)
    option.add_separator()
    option.add_command(label="Organise",command=organise)

    #About
    about=tk.Menu(menubar,tearoff=0)
    about.add_command(label="About", command=about_info)
    about.add_separator()
    about.add_command(label="Help", command=help)

    menubar.add_cascade(label="File", menu=file)
    menubar.add_cascade(label="Options", menu=option)
    menubar.add_cascade(label="More", menu=about)


    win.config(menu=menubar)
    #menubar ends here

    style=ttk.Style()
    style.configure("TButton", font = ('calibre',8,'bold'))

    path=tk.StringVar()

    heading=tk.Label(win,text="File Organizer",font=('areal',12,'bold'),anchor="center")
    l1=tk.Label(win, text="Path of the Folder", font = ('calibre',9,'bold'))

    url =tk.Entry(win, width=50, textvariable=path, font = ('calibre',8,'normal'), relief='groove', bd=2)

    organise_button=ttk.Button(win, text="Organize", width=10, command=organise, style="TButton")
    clear_button=ttk.Button(win, text="Clear", width=10, command=clear, style="TButton")
    browse=ttk.Button(win, text="Browse", width=10, command=browse_path, style="TButton")
    close=ttk.Button(win, text="Close", width=10, style="TButton", command=win.destroy)

    heading.grid(row=0,column=0,columnspan=2,rowspan=1, padx=10, pady=10)
    l1.grid(row=2, column=0, padx=5, pady=5)
    url.grid(row=2, column=1, padx=5, pady=5)
    organise_button.grid(row=3,column=1, padx=5, pady=5, sticky='e')
    clear_button.grid(row=3, column=1, padx=5, pady=5, sticky='w')
    browse.grid(row=3, column=1, padx=5, pady=5)
    close.grid(row=5,column=1,padx=5,pady='300',sticky='e')

    win.mainloop()

main_window()