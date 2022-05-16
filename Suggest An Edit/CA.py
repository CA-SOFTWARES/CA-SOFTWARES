
while True:
    import os
    import time
    if os.path.isfile('C:\\Users\\Admin\\Desktop\\CA SOFTWARES\\CA\\Wallpaper\\auto.txt') == True:
        pass
    else:
        wall = open('C:\\Users\\Admin\\Desktop\\CA SOFTWARES\\CA\\Wallpaper\\auto.txt', 'w')
        w = wall.write('autowallpaperdisable')
        wall.close()
    if os.path.isfile('C:\\CA SOFTWARES\\enable.txt') == True:
        a = open('C:\\CA SOFTWARES\\enable.txt', 'r')
        b = a.read()
        a.close()
        if b == "Enable":
            while True:

                import string
                import random
                from colorama import Fore, Style

                if __name__ == "__main__":
                    s1 = string.ascii_lowercase
                    # print(s1)
                    s2 = string.ascii_uppercase

                    # print(s2)
                    s3 = string.digits

                    # print(s3)
                    s4 = string.punctuation
                    # print(s4)
                    plen = int(4)

                    s = []
                    s.extend(list(s1))
                    s.extend(list(s2))

                    s.extend(list(s3))
                    s.extend(list(s4))
                    # print(s)
                    random.shuffle(s)
                    # print(s)

                    passw = ("".join(s[0:plen]))
                    print("")
                    print(passw)
                    a1 = input("Password: ")
                    if a1 == passw:
                        print("Access Granted")
                        print("")
                        time.sleep(2)
                        break
        else:
            pass
    else:
        pass


    import datetime
    import time
    import tkinter
    from tkinter import *
    from tkinter import ttk
    from tkinter import messagebox
    from PIL import Image, ImageTk
    root = Tk()
    '''tabControl = ttk.Notebook(root)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tabControl.add(tab1, text='Window 1')
    tabControl.add(tab2, text='Window 2')
    tabControl.pack(expand=1, fill="both")'''
    root.config(cursor='spider')
    import datetime
    import os

    root.title("CA SOFTWARES")
    root.iconbitmap("C:\\Users\\Admin\\Desktop\\CA SOFTWARES\\CA\\CA.ico")
    root.attributes('-fullscreen', True)
    path = 'C:\\Users\\Admin\\Desktop\\CA SOFTWARES\\CA\\Wallpaper\\'
    if os.path.isfile('C:\\Users\\Admin\\Desktop\\CA SOFTWARES\\CA\\Wallpaper\\auto.txt') == True:
        wall = open('C:\\Users\\Admin\\Desktop\\CA SOFTWARES\\CA\\Wallpaper\\auto.txt', 'r')
        w = wall.read()
        wall.close()
        if w == 'autowallpaperenable':
            wallt = open('C:\\Users\\Admin\\Desktop\\CA SOFTWARES\\CA\\Wallpaper\\auto.txt', 'r')
            wt = wallt.read()
            wallt.close()
            if wallt == 0:
                photowall1 = ImageTk.PhotoImage(Image.open(path + 'img7.jpg'))
                label = Label(root, image=photowall1)
                label.pack(pady=0, padx=0)
            else:
                photo = ImageTk.PhotoImage(Image.open(path + 'img7.jpg'))
                photo1 = ImageTk.PhotoImage(Image.open(path + 'img8.jpg'))
                photo2 = ImageTk.PhotoImage(Image.open(path + 'img9.jpg'))
                photo3 = ImageTk.PhotoImage(Image.open(path + 'img10.jpg'))
                photo4 = ImageTk.PhotoImage(Image.open(path + 'img11.jpg'))
                photo5 = ImageTk.PhotoImage(Image.open(path + 'img12.jpg'))
                photoha = ImageTk.PhotoImage(Image.open(path + 'img14.jpg'))
                photoha15 = ImageTk.PhotoImage(Image.open(path + 'img15.jpg'))
                labelwall = Label(root)
                labelwall.pack(pady=0, padx=0)
                x = 1


                def move():
                    global x
                    if x == 8:
                        x = 1
                    if x == 1:
                        labelwall.config(image=photo)
                    elif x == 2:
                        labelwall.config(image=photo1)
                    elif x == 3:
                        labelwall.config(image=photo2)
                    elif x == 4:
                        labelwall.config(image=photo3)
                    elif x == 5:
                        labelwall.config(image=photoha)
                    elif x == 6:
                        labelwall.config(image=photo5)
                    elif x == 7:
                        labelwall.config(image=photo4)
                    elif x == 8:
                        labelwall.config(image=photoha15)
                    x += 1
                    wallti = open('C:\\Users\\Admin\\Desktop\\CA SOFTWARES\\CA\\Wallpaper\\autotime.txt', 'r')
                    tim = wallti.read()
                    root.after(tim, move)


                move()
        if w == 'autowallpaperdisable':
            photowall1 = ImageTk.PhotoImage(Image.open(path + 'img9.jpg'))
            label = Label(root, image=photowall1)
            label.pack(pady=0, padx=0)
    icon = Image.open('C:\\Users\\Admin\\Desktop\\CA SOFTWARES\\CA\\CA.ico')
    icon = icon.resize((50, 50))
    dis = ImageTk.PhotoImage(icon)
    label1 = Label(root, image=dis)
    label1.place(x=20, y=25)



    import os


    def calc():
        os.startfile('calc.py')


    def openCA():
        if os.path.isdir('C:\\CA SOFTWARES') == True:
            if os.path.isfile('C:\\CA SOFTWARES\\done.txt') == True:
                b = open('C:\\CA SOFTWARES\\done.txt', 'r')
                o1 = b.read()
                b.close()
                if o1 == "AKV":
                    os.startfile('C:\\Users\\Admin\\Desktop\\CA SOFTWARES\\CA\\CA.lnk')
                else:
                    messagebox.showerror('Activation','First Activate CA')
        else:
            messagebox.showerror('Activation','First Activate CA')
    def CA():
        os.startfile('C:\\Users\\Admin\\Desktop\\CA SOFTWARES\\CA\\CA.lnk')


    my_button = Button(root, image=dis, command=openCA,cursor='')
    my_button.place(x=20, y=25)
    text = Button(root, text="     CA     ", command=openCA,activebackground='lightblue')
    text.place(x=20, y=90)
    btn = Image.open('C:\\Users\\Admin\\Desktop\\CA SOFTWARES\\CA\\CA.png')
    btn = btn.resize((30, 30))
    btndis = ImageTk.PhotoImage(btn)
    def activateca():
        yesno = messagebox.askyesnocancel('Activation','Are You Sure You Want To Activate CA')
        if yesno == True:
            CA()
        elif yesno == False:
            messagebox.showinfo('Messaage','Thanks For Your Response')
        else:
            pass
    if os.path.isdir('C:\\CA SOFTWARES') == True:
        if os.path.isfile('C:\\CA SOFTWARES\\done.txt') == True:
            b = open('C:\\CA SOFTWARES\\done.txt', 'r')
            o1 = b.read()
            b.close()
            if o1 == "AKV":
                pass
            else:
                activation = Image.open("C:\\Users\\Admin\\Desktop\\CA SOFTWARES\\CA\\Activate this pc.png")
                activation = activation.resize((52, 55))
                photoact = ImageTk.PhotoImage(activation)
                labelact = Button(root, image=photoact, command=activateca)
                labelact.pack()
                labelact.place(x=1838, y=940)
                acttext = Label(root, text='Activate This PC', font=("arail", 8, "bold"))
                acttext.pack()
                acttext.place(x=1818, y=1010)
        else:
            pass
    else:
        activation = Image.open("C:\\Users\\Admin\\Desktop\\CA SOFTWARES\\CA\\Activate this pc.png")
        activation = activation.resize((52, 55))
        photoact = ImageTk.PhotoImage(activation)
        labelact = Button(root, image=photoact, command=activateca)
        labelact.pack()
        labelact.place(x=1838, y=940)
        acttext = Label(root, text='Activate This PC', font=("arail", 8, "bold"))
        acttext.pack()
        acttext.place(x=1818, y=1010)
    def run():
        import tkinter
        runit = Tk()
        runit.title('Run')
        runit.minsize(200, 230)
        runit.maxsize(200, 230)
        runit.attributes('-alpha', 1)
        runit.minsize(200, 150)
        runit.maxsize(200, 150)
        frame = Frame(runit)
        frame.pack()
        def data():
            dataa = my_entry.get()
            if dataa == 'CA':
                openCA()
            elif dataa == 'Textpad':
                textpados()
            elif dataa == 'Settings':
                settings()
            elif dataa == 'Scrcpy':
                screenmir()
            elif dataa == 'Python':
                python()
            elif dataa == 'Files':
                file()
            elif dataa == 'Calc':
                calc()
            elif os.path.isfile(dataa) == True:
                os.startfile(dataa)
            else:
                messagebox.showwarning('Error For The App','No App Found')

        my_entry = Entry(frame, width=20)
        my_entry.insert(0, '')
        my_entry.pack(padx=5, pady=5)
        butt = Button(runit,text='Enter',command=data,activebackground='lightblue')
        butt.pack()
        runit.mainloop()
    def menu():
        menu1 = Toplevel(root, bg='white')
        menu1.title('Menu Bar')
        menu1.iconbitmap('CA.ico')
        menu1.geometry("200x230")
        menu1.minsize(200,230)
        menu1.maxsize(200,230)
        menu1.attributes('-alpha', 1)
        import time
        shoutdown = Button(menu1, text="   Shoutdown   ", command=exit, padx=100,activebackground='lightblue')
        shoutdown.pack()
        run1 = Button(menu1, text='Run', command=run, padx=100,activebackground='lightblue')
        run1.pack()
        def new():
            os.startfile('C:\\Users\\Admin\\Desktop\\CA SOFTWARES\\CA\\CA.py')

        neww = Button(menu1, text="New Windows", command=new, padx=100,activebackground='lightblue')
        neww.pack()


    btn1 = Label(root, image=btndis)
    btn1.place(x=0, y=1043)
    my_button = Button(root, image=btndis, command=menu)
    my_button.place(x=0, y=1043)
    def datetime():
        import datetime
        import time
        today_date = time.strftime("%H:%M:%S")


    datetime()


    def python():
        os.startfile('C:\\Users\\Admin\\Desktop\\CA SOFTWARES\\venv\\Scripts\\python.exe')


    pythonimg = Image.open('C:\\Users\\Admin\\Desktop\\CA SOFTWARES\\CA\\python.ico')
    pythonimg = pythonimg.resize((52, 55))
    pythondis = ImageTk.PhotoImage(pythonimg)
    label2 = Label(root, image=pythondis)
    label2.place(x=20, y=150)
    text1 = Button(root, text=" Python  ", command=python,activebackground='lightblue')
    text1.place(x=20, y=220)
    my_button1 = Button(root, image=pythondis, command=python)
    my_button1.place(x=20, y=150)


    import pyautogui
    width, height = pyautogui.size()
    rect = Image.open('C:\\Users\\Admin\\Desktop\\CA SOFTWARES\\CA\\bar.png')
    rect = rect.resize((width, 31))
    disrect = ImageTk.PhotoImage(rect)
    label1rect = Label(root, image=disrect)
    label1rect.place(x=37, y=1043)


    note = Image.open('C:\\Users\\Admin\\Desktop\\CA SOFTWARES\\CA\\calculator.png')
    note = note.resize((53, 50))
    disnote = ImageTk.PhotoImage(note)
    labelnote = Label(root, image=disnote)
    labelnote.place(x=20, y=280)
    text12 = Button(root, text="    Calc    ", command=calc,activebackground='lightblue')
    text12.place(x=20, y=345)
    my_button12 = Button(root, image=disnote, command=calc)
    my_button12.place(x=20, y=280)

    def textpados():
        import tkinter
        from tkinter.messagebox import showinfo
        from tkinter.filedialog import askopenfilename, asksaveasfilename
        import os

        def newFile():
            global file
            root.title("Textpad")
            file = None
            TextArea.delete(1.0, END)

        def openFile():
            global file
            file = askopenfilename(defaultextension=".CA ",
                                   filetypes=[("All Files", "*.*"),
                                              ("CA Docs", "*.CA ")])
            if file == "":
                file = None
            else:
                root.title(os.path.basename(file) + " - Textpad")
                TextArea.delete(1.0, END)
                f = open(file, "r")
                TextArea.insert(1.0, f.read())
                f.close()

        def saveFile():
            global file
            if file == None:
                file = asksaveasfilename(initialfile='New File.CA',
                                         defaultextension=".CA",
                                         filetypes=[("All Files", "*.CA"),
                                                    ("CA Docs", "*.CA")])

                if file == '':
                    file = None

                else:
                    # Save as a new file
                    f = open(file, "w")
                    f.write(TextArea.get(1.0, END))
                    f.close()

                    root.title(os.path.basename(file) + " - Textpad")
                    print("File Saved")
            else:
                # Save the file
                f = open(file, "w")
                f.write(TextArea.get(1.0, END))
                f.close()

        def quitApp():
            root.destroy()

        def cut():
            TextArea.event_generate(("<>"))

        def copy():
            TextArea.event_generate(("<>"))

        def paste():
            TextArea.event_generate(("<>"))

        def about():
            showinfo("Textpad", "Created By Harshil Anuwadia")

        if __name__ == '__main__':
            # Basic tkinter setup
            root = Tk()
            root.title("Untitled - Textpad")

            root.geometry("644x788")

            # Add TextArea
            TextArea = Text(root, font="lucida 13")
            file = None
            TextArea.pack(expand=True, fill=BOTH)

            MenuBar = Menu(root)

            FileMenu = Menu(MenuBar, tearoff=0)

            FileMenu.add_command(label="New", command=newFile)

            FileMenu.add_command(label="Open", command=openFile)

            FileMenu.add_command(label="Save", command=saveFile)
            FileMenu.add_separator()
            FileMenu.add_command(label="Exit", command=quitApp)
            MenuBar.add_cascade(label="File", menu=FileMenu)
            # File Menu ends

            # Edit Menu Starts
            EditMenu = Menu(MenuBar, tearoff=0)
            # To give a feature of cut, copy and paste
            EditMenu.add_command(label="Cut", command=cut)
            EditMenu.add_command(label="Copy", command=copy)
            EditMenu.add_command(label="Paste", command=paste)

            MenuBar.add_cascade(label="Edit", menu=EditMenu)

            # Help Menu Starts
            HelpMenu = Menu(MenuBar, tearoff=0)
            HelpMenu.add_command(label="About Textpad", command=about)
            MenuBar.add_cascade(label="Help", menu=HelpMenu)

            # Help Menu Ends

            root.config(menu=MenuBar)

            # Adding Scrollbar using rules from Tkinter lecture no 22
            Scroll = Scrollbar(TextArea)
            Scroll.pack(side=RIGHT, fill=Y)
            Scroll.config(command=TextArea.yview)
            TextArea.config(yscrollcommand=Scroll.set)
            root.mainloop()


    def info():
        if os.path.isdir('C:\\CA SOFTWARES') == True:
            if os.path.isfile('C:\\CA SOFTWARES\\done.txt') == True:
                b = open('C:\\CA SOFTWARES\\done.txt', 'r')
                o1 = b.read()
                b.close()
                if o1 == "AKV":
                    os.startfile('C:\\Users\\Admin\\Desktop\\CA SOFTWARES\\venv\\Scripts\\Activated Info.py')
                    pass
                else:
                    messagebox.showerror('Activation', 'To Use Activation Info First Activate CA')
        else:
            messagebox.showerror('Activation', 'To Use Activation Info First Activate CA')



    note1 = Image.open(
        'C:\\Users\\Admin\\Desktop\\CA SOFTWARES\\CA\\information-security-information-security-privacy-policy-png-favpng-yb9hhh6V4xSBLU38yc06RVtKb.jpg')
    note1 = note1.resize((34, 30))
    disnote1 = ImageTk.PhotoImage(note1)
    labelnote1 = Label(root, image=disnote1)
    labelnote1.place(x=38, y=1043)
    my_button121 = Button(root, image=disnote1, command=info)
    my_button121.place(x=38, y=1043)


    # -------------------------------------------------------------
    def settings():
        os.startfile('C:\\Users\\Admin\\Desktop\\CA SOFTWARES\\venv\\Scripts\\set.py')


    set = Image.open(
        'C:\\Users\\Admin\\Desktop\\CA SOFTWARES\\CA\\settings-button-svg-icon-free-download-comments-black.png')
    set = set.resize((52, 55))
    disset = ImageTk.PhotoImage(set)
    labelset = Label(root, image=disset)
    labelset.place(x=20, y=405)
    my_buttonset = Button(root, image=disset, command=settings)
    my_buttonset.place(x=20, y=405)
    settext = Button(root, text=" Settings ", command=settings,activebackground='lightblue')
    settext.place(x=20, y=475)


    set1 = Image.open('C:\\Users\\Admin\\Desktop\\CA SOFTWARES\\CA\\textpad.png')
    set1 = set1.resize((52, 55))
    dissetv = ImageTk.PhotoImage(set1)
    labelsetv = Label(root, image=dissetv)
    labelsetv.place(x=20, y=535)
    my_buttonsetv = Button(root, image=dissetv, command=textpados)
    my_buttonsetv.place(x=20, y=535)
    settextv = Button(root, text=" Textpad ", command=textpados,activebackground='lightblue')
    settextv.place(x=20, y=605)


    def file():
        if os.path.isdir('C:\\CA SOFTWARES') == True:
            if os.path.isfile('C:\\CA SOFTWARES\\done.txt') == True:
                b = open('C:\\CA SOFTWARES\\done.txt', 'r')
                o1 = b.read()
                b.close()
                if o1 == "AKV":
                    os.startfile('C:\\Users\\Admin\\Desktop\\CA SOFTWARES\\CA\\file.py')
                    pass
                else:
                    messagebox.showerror('Activation','To Use Files Activate CA')
        else:
            messagebox.showerror('Activation', 'To Use Files First Activate CA')


    setw = Image.open('C:\\Users\\Admin\\Desktop\\CA SOFTWARES\\CA\\616ee6fc4f194-384x384.png')
    setw = setw.resize((50, 50))
    dissetvw = ImageTk.PhotoImage(setw)
    labelsetvw = Label(root, image=dissetvw)
    labelsetvw.place(x=110, y=25)
    my_buttonsetvw = Button(root, image=dissetvw, command=file)
    my_buttonsetvw.place(x=110, y=25)
    settextvw = Button(root, text="    Files    ", command=file,activebackground='lightblue')
    settextvw.place(x=110, y=90)


    def screenmir():
        from tkinter import messagebox
        screen = messagebox.askyesno('Message','Have You Inserted USB Cable Into Your PC')
        if screen == True:
            os.startfile('C:\\Users\\Admin\\Desktop\\CA SOFTWARES\\CA\\scrcpy.py')
    screen = Image.open('C:\\Users\\Admin\\Desktop\\CA SOFTWARES\\CA\\images.png')
    screen = screen.resize((52, 54))
    screenmirr = ImageTk.PhotoImage(screen)
    labelscreen = Label(root, image=screenmirr)
    labelscreen.place(x=110, y=150)
    my_buttonscreen = Button(root, image=screenmirr, command=screenmir)
    my_buttonscreen.place(x=110, y=150)
    settextscreen = Button(root, text="  Scrcpy   ", command=screenmir,activebackground='lightblue')
    settextscreen.place(x=110, y=219)


    def do_pop(event):
        m.tk_popup(event.x_root, event.y_root)
        m.grab_release()
        pass


    def newpop():
        os.startfile('C:\\Users\\Admin\\Desktop\\CA SOFTWARES\\CA\\CA.py')


    def pop():
        pass


    def autowalle():
        wall = open('C:\\Users\\Admin\\Desktop\\CA SOFTWARES\\CA\\Wallpaper\\auto.txt', 'w')
        wall.write('autowallpaperenable')
        wall.close()


    def autowalld():
        wall = open('C:\\Users\\Admin\\Desktop\\CA SOFTWARES\\CA\\Wallpaper\\auto.txt', 'w')
        wall.write('autowallpaperdisable')
        wall.close()


    def snake():
        os.startfile('C:\\Users\\Admin\\Desktop\\CA SOFTWARES\\CA\\snake.py')


    def shoutdownthispc():
        os.system("shutdown /s /t 1")


    def act():
        if os.path.isdir('C:\\CA SOFTWARES') == True:
            if os.path.isfile('C:\\CA SOFTWARES\\done.txt') == True:
                b = open('C:\\CA SOFTWARES\\done.txt', 'r')
                o1 = b.read()
                b.close()
                if o1 == "AKV":
                    os.startfile('C:\\Users\\Admin\\Desktop\\CA SOFTWARES\\venv\\Scripts\\Activated Info.py')
                    pass
                else:
                    messagebox.showerror('Activation', 'To Use Activation Info First Activate CA')
        else:
            messagebox.showerror('Activation', 'To Use Activation Info First Activate CA')


    m = Menu(root, tearoff=False,cursor='spider')
    m.add_command(label='''
                CA SOFTWARES

     ''', command=pop)
    m.add_command(label='-------------------------------------', command=pop)
    m.add_command(label='New Window', command=newpop)
    m.add_command(label='Enable Auto Changing Wallpaper', command=autowalle)
    m.add_command(label='Disable Auto Changing Wallpaper', command=autowalld)
    m.add_command(label='Open CA', command=openCA)
    m.add_command(label='Play Snake Game', command=snake)
    m.add_command(label='Config Settings', command=settings)
    m.add_command(label='Shoutdown This PC', command=shoutdownthispc)
    m.add_command(label='Activation Info', command=act)
    m.add_command(label='Exit', command=exit)
    m.add_command(label='-------------------------------------', command=pop)
    m.add_command(label='CA Corporation. All rights reserved', command=pop)
    root.bind("<Button-3>", do_pop)

    def timing ():
        def time():
            string = strftime('%H:%M:%S %p')
            clock.config(text=string)
            clock.after(1000, time)

        from time import strftime

        clock = Label(root, font=("arial", 10))
        clock.pack()
        clock.place(x=width-95, y=1050)
        time()

        def timedate():
            import datetime
            datestr = datetime.date.today()
            date.config(text=datestr)
            date.after(8640000, timedate)

        date = Label(root, font=("arial", 10))
        date.pack()
        date.place(x=width-180, y=1050)
        timedate()
    timing()
    root.mainloop()