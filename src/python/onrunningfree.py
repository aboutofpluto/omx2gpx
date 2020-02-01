#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Jan 21, 2020 11:24:05 PM CET  platform: Linux

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import onrunningfree_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    onrunningfree_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    onrunningfree_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {DejaVu Sans} -size 8 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("530x486+387+60")
        top.minsize(1, 1)
        top.maxsize(1905, 1170)
        top.resizable(1, 1)
        top.title("OnRunningFree")
        top.configure(highlightcolor="black")

        self.InputDirBtn = tk.Button(top)
        self.InputDirBtn.place(relx=0.019, rely=0.082, height=33, width=200)
        self.InputDirBtn.configure(activebackground="#f9f9f9")
        self.InputDirBtn.configure(command=onrunningfree_support.input_btn_handler)
        self.InputDirBtn.configure(disabledforeground="#b8a786")
        self.InputDirBtn.configure(font="-family {DejaVu Sans} -size 12")
        self.InputDirBtn.configure(text='''Select input directory''')
        self.InputDirBtn.bind('<Button-2>',lambda e:onrunningfree_support.button_handler2(e,2))
        self.InputDirBtn.bind('<Button-3>',lambda e:onrunningfree_support.button_handler2(e,3))

        self.QuitButton = tk.Button(top)
        self.QuitButton.place(relx=0.868, rely=0.802, height=33, width=61)
        self.QuitButton.configure(activebackground="#f9f9f9")
        self.QuitButton.configure(command=onrunningfree_support.quit)
        self.QuitButton.configure(disabledforeground="#b8a786")
        self.QuitButton.configure(font="-family {DejaVu Sans} -size 12")
        self.QuitButton.configure(text='''Quit''')

        self.OutputDirBtn = tk.Button(top)
        self.OutputDirBtn.place(relx=0.019, rely=0.165, height=33, width=200)
        self.OutputDirBtn.configure(activebackground="#f9f9f9")
        self.OutputDirBtn.configure(command=onrunningfree_support.output_btn_handler)
        self.OutputDirBtn.configure(disabledforeground="#b8a786")
        self.OutputDirBtn.configure(font="-family {DejaVu Sans} -size 12")
        self.OutputDirBtn.configure(text='''Select output directory''')
        self.OutputDirBtn.bind('<Button-2>',lambda e:onrunningfree_support.button_handler2(e,2))
        self.OutputDirBtn.bind('<Button-3>',lambda e:onrunningfree_support.button_handler2(e,3))

        self.RecordList = tk.Listbox(top)
        self.RecordList.place(relx=0.019, rely=0.37, relheight=0.412
                , relwidth=0.962)
        self.RecordList.configure(background="white")
        self.RecordList.configure(font="TkFixedFont")
        self.RecordList.configure(selectbackground="#c4c4c4")
        self.RecordList.configure(selectmode='multiple')

        self.InputDirEntry = tk.Entry(top)
        self.InputDirEntry.place(relx=0.415, rely=0.082, height=33
                , relwidth=0.566)
        self.InputDirEntry.configure(background="white")
        self.InputDirEntry.configure(font="TkFixedFont")
        self.InputDirEntry.configure(selectbackground="#c4c4c4")
        self.InputDirEntry.configure(state='readonly')

        self.ExportBtn = tk.Button(top)
        self.ExportBtn.place(relx=0.019, rely=0.802, height=33, width=200)
        self.ExportBtn.configure(activebackground="#f9f9f9")
        self.ExportBtn.configure(command=onrunningfree_support.export_btn_handler)
        self.ExportBtn.configure(disabledforeground="#b8a786")
        self.ExportBtn.configure(font="-family {DejaVu Sans} -size 12")
        self.ExportBtn.configure(text='''Export selected to gpx''')
        self.ExportBtn.bind('<Button-2>',lambda e:onrunningfree_support.button_handler2(e,2))
        self.ExportBtn.bind('<Button-3>',lambda e:onrunningfree_support.button_handler2(e,3))

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.019, rely=0.021, height=23, width=111)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(font="-family {DejaVu Sans} -size 12 -underline 1")
        self.Label1.configure(text='''1. Directories''')

        self.OutputDirEntry = tk.Entry(top)
        self.OutputDirEntry.place(relx=0.415, rely=0.165, height=33
                , relwidth=0.566)
        self.OutputDirEntry.configure(background="white")
        self.OutputDirEntry.configure(font="TkFixedFont")
        self.OutputDirEntry.configure(selectbackground="#c4c4c4")
        self.OutputDirEntry.configure(state='readonly')

        self.Label1_6 = tk.Label(top)
        self.Label1_6.place(relx=0.0, rely=0.309, height=23, width=111)
        self.Label1_6.configure(activebackground="#f9f9f9")
        self.Label1_6.configure(font="-family {DejaVu Sans} -size 12 -underline 1")
        self.Label1_6.configure(text='''2. Records''')

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.019, rely=0.288, relwidth=0.962)

        self.TSeparator1_7 = ttk.Separator(top)
        self.TSeparator1_7.place(relx=0.019, rely=0.905, relwidth=0.962)

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.7, rely=0.949, height=21, width=93)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(anchor='w')
        self.Label2.configure(font=font9)
        self.Label2.configure(text='''by Out of Pluto''')

        self.Logo = tk.Label(top)
        self.Logo.place(relx=0.113, rely=0.932, height=28, width=304)
        self.Logo.configure(activebackground="#f9f9f9")
        self.Logo.configure(text='''Label''')

        self.Picture = tk.Label(top)
        self.Picture.place(relx=0.019, rely=0.926, height=28, width=40)
        self.Picture.configure(text='''Label''')

if __name__ == '__main__':
    vp_start_gui()





