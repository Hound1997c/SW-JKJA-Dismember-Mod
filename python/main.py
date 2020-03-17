import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
from python.DismemberClass import DismemberClass


class MyOptionMenu(OptionMenu):
    def __init__(self, master, status, *options):
        self.var = StringVar(master)
        self.var.set(status)
        OptionMenu.__init__(self, master, self.var, *options)
        self.config(font=('calibri',(8)),bg='white',width=20)
        self['menu'].config(font=('calibri',(8)),bg='white')
        # mymenu3 = MyOptionMenu(root, '-', *optionList3)
        return

"""
class Window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.root = master
        self.init_window()

    def init_window(self):
        self.root.title('JKJA Change Dismemberment')

        APP_HEIGHT = 500
        APP_WIDTH = 500
        BUTTONS_HEIGHT = 2
        BUTTONS_WIDTHT = 10
        root.geometry(str(APP_WIDTH) + 'x' + str(APP_HEIGHT))

        lab1 = Label(root, text="choosse the PATH of your JKJA instalation folder", font="Arial 8", anchor='w')
        filepath = tk.StringVar()
        filepathEntry = tk.Entry(root, width=20, bd=3, textvariable=filepath)
        browseButton = tk.Button(root, text='Browse',
                                 command=lambda: first_browser(filepath))
        lab2 = Label(root, text="dismemberProbHead %", font="Arial 8", anchor='w')
        validation = root.register(only_numbers)
        ent1 = tk.Entry(root, width=5, bd=3, validate="key", validatecommand=(validation, '%S'))
        lab3 = Label(root, text="dismemberProbArms %", font="Arial 8", anchor='w')
        ent2 = Entry(root, width=5, bd=3, validate="key", validatecommand=(validation, '%S'))
        lab4 = Label(root, text="dismemberProbLegs %", font="Arial 8", anchor='w')
        ent3 = Entry(root, width=5, bd=3, validate="key", validatecommand=(validation, '%S'))
        lab = Label(root, text="dismemberProbHands %", font="Arial 8", anchor='w')
        ent4 = Entry(root, width=5, bd=3, validate="key", validatecommand=(validation, '%S'))
        lab5 = Label(root, text="dismemberProbWaist %", font="Arial 8", anchor='w')
        ent5 = Entry(root, width=5, bd=3, validate="key", validatecommand=(validation, '%S'))
        submitButton = tk.Button(root, text="Submit",
                                 command=lambda: submitButtonAction(ent1.get(), ent2.get(),
                                                                    ent3.get(), ent4.get(), ent5.get()))

        lab1.pack(side="top", fill="x")
        filepathEntry.pack(side="top", fill="y")
        browseButton.pack(side="top", fill="y")
        lab2.pack(side="top", fill="x")
        ent1.pack(side="top", fill="y")
        lab3.pack(side="top", fill="x")
        ent2.pack(side="top", fill="y")
        lab4.pack(side="top", fill="x")
        ent3.pack(side="top", fill="y")
        lab.pack(side="top", fill="x")
        ent4.pack(side="top", fill="y")
        lab5.pack(side="top", fill="x")
        ent5.pack(side="top", fill="y")
        submitButton.pack(side="top", fill="y", pady=30)
"""

def show_file_browser():
    filename = filedialog.askdirectory() #askopenfilename()
    return filename

def first_browser(filepath):
    file = show_file_browser()
    filepath.set(file)

def submitButtonAction(filepath,p1,p2,p3,p4,p5):
    #print(locals())
    arguments = locals()
    hasErrors = False
    variablesToUpdate = []
    for k,v in arguments.items():
        if (k == "filepath"):
            continue
        if(len(v) is 0):
            messagebox.showinfo("null variable", "You can't enter null variable!")
            hasErrors = True
            break
        elif(int(v) > 100):
            messagebox.showinfo("to big amount", "You can't enter more than 100% !")
            hasErrors = True
            break
        else:
            variablesToUpdate.append(int(v))
    if(hasErrors == False and len(filepath)==0):
        hasErrors = True
        messagebox.showinfo("no path", "Select file path !")
    if(hasErrors is False):
        print(variablesToUpdate)
        dc = DismemberClass(filepath,variablesToUpdate)
        dc.replaceAll()

    #print(str(p1) + " " + p2 + " " + p3 + " " + p4 + " " + p5)

    return


def only_numbers(char):
    return char.isdigit()




root = tk.Tk()
root.title('JKJA Change Dismemberment')

APP_HEIGHT=500
APP_WIDTH=500
BUTTONS_HEIGHT=2
BUTTONS_WIDTHT=10
root.geometry(str(APP_WIDTH) + 'x' + str(APP_HEIGHT))




lab1 = Label(root, text="choosse the PATH of 'npcs' folder", font="Arial 8", anchor='w')
filepath = tk.StringVar()
filepathEntry = tk.Entry(root,width=20,bd=3, textvariable = filepath)
browseButton = tk.Button(root, text = 'Browse',
                                 command = lambda : first_browser(filepath))
lab2 = Label(root, text="dismemberProbHead %", font="Arial 8", anchor='w')
validation = root.register(only_numbers)
ent1 = tk.Entry(root,width=5,bd=3,validate="key", validatecommand=(validation, '%S'))
lab3 = Label(root, text="dismemberProbArms %", font="Arial 8", anchor='w')
ent2 = Entry(root,width=5,bd=3, validate="key", validatecommand=(validation, '%S'))
lab4 = Label(root, text="dismemberProbLegs %", font="Arial 8", anchor='w')
ent3 = Entry(root,width=5,bd=3, validate="key", validatecommand=(validation, '%S'))
lab = Label(root, text="dismemberProbHands %", font="Arial 8", anchor='w')
ent4 = Entry(root,width=5,bd=3, validate="key", validatecommand=(validation, '%S'))
lab5 = Label(root, text="dismemberProbWaist %", font="Arial 8", anchor='w')
ent5 = Entry(root,width=5,bd=3, validate="key", validatecommand=(validation, '%S'))
submitButton = tk.Button(root, text="Submit",
                         command=lambda : submitButtonAction(filepathEntry.get(),ent1.get(),ent2.get(),
                                                             ent3.get(),ent4.get(),ent5.get()))

infoLabel = Label(root,text="go to Game folder 'Gamedata/base' \n open 'assets1.pk3' by archivizer like WinRar \n"
                            "Go to 'ext_data' and take out folder 'npcs' to another place out of 'assets1.pk3' \n"
                            "Select this path on entry in this window, type dismemberments and Click Submit\n"
                            "lates step is give back changed 'npcs' folder to 'assets1.pk3' using archivizer\n",
                            font="Arial 8", anchor='e')

lab1.pack(side="top",fill = "x")
filepathEntry.pack(side="top",fill = "y")
browseButton.pack(side="top", fill="y")
lab2.pack(side="top",fill = "x")
ent1.pack(side="top",fill = "y")
lab3.pack(side="top", fill="x")
ent2.pack(side="top", fill="y")
lab4.pack(side="top", fill="x")
ent3.pack(side="top", fill = "y")
lab.pack(side="top", fill="x")
ent4.pack(side="top", fill="y")
lab5.pack(side="top", fill="x")
ent5.pack(side="top", fill = "y")
submitButton.pack(side="top", fill="y", pady=30)
infoLabel.pack(side="top", fill="y")




root.mainloop()

