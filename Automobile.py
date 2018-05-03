from tkinter import *

root = Tk()
root.title("Automobile Management System")
root.configure(background='lightcyan4')

f1 = Frame(root, bg="light cyan4")

lb_1 = Label(f1, font=('arial', 40, 'bold'), text="Automobile Management System", fg="red", anchor=CENTER,
             bg="light cyan4")
lb_1.grid(row=0, column=0)


def search1():
    flag = 1
    data = ""
    ln = "\n"
    handle = Toplevel(f1, width=1200)
    try:
        file1 = open("D:/python/automobile.txt", 'r+')
        data = ""
        while (flag != 0):
            str1 = file1.readline()
            k = str1.split()

            plate = str(text_7.get())

            if (plate == k[0]):
                flag = 0

                lab = Label(handle, text=str1)
                lab.grid(row=0, column=1)
                text_7.delete(0, END)

    except:
        print("Error")
    file1.close()


def next1():
    flag = 1
    data = ""
    ln = "\n"
    handle = Toplevel(root, width=1200)
    try:
        file1 = open("D:/python/automobile.txt", 'r+')
        data = ""
        a = 0
        while (flag != 0):
            str1 = file1.readline()
            k = str1.split()

            plate = str(text_7.get())
            if (a == 1):
                lab = Label(handle, text=str1)
                lab.grid(row=0, column=1)
                text_7.delete(0, END)
                flag = 0

            if (plate == k[0]):
                a = 1
    except:
        print("Error")
    file1.close()


def prev1():
    flag = 1
    data = ""
    st = ""
    ln = "\n"
    handle = Toplevel(f1, width=1200)
    try:
        file1 = open("D:/python/automobile.txt", 'r+')
        data = ""
        a = 0
        prevstr = ""
        while (flag != 0):
            str1 = file1.readline()
            k = str1.split()

            plate = str(text_7.get())
            print(st)
            if (plate == k[0]):
                prevstr = str1
                a = 1
            if (a == 0):
                st = str1

            if (prevstr != ""):
                flag = 0
                lab = Label(handle, text=st)
                lab.grid(row=0, column=1)
                text_7.delete(0, END)
    except:
        print("Error")
    file1.close()


def first():
    handle = Toplevel(f1, width=1200)
    try:
        file1 = open("D:/python/automobile.txt", 'r+')
        str1 = file1.readline()
        lab = Label(handle, text=str1)
        lab.grid(row=0, column=1)
        text_7.delete(0, END)
    except:
        print("Error")
    file1.close()


def last():
    handle = Toplevel(root, width=1200)
    try:
        file1 = open("D:/python/automobile.txt", 'r+')
        str1 = file1.readlines()
        s = ""
        for i in str1:
            s = i
        lab = Label(handle, text=s)
        lab.grid(row=0, column=1)
        text_7.delete(0, END)
    except:
        print("Error")
    file1.close()


lb_7 = Label(f1, font=('arial', 20, 'bold'), text="Enter Here", bd=16, anchor=E, bg="light cyan4")
lb_7.grid(row=1, column=0, sticky=W)
text_7 = Entry(f1, font=('arial', 16, 'bold'), bd=3, bg="Powder blue")
text_7.grid(row=1, column=0)
b5 = Button(f1, text="Search", width=10, font="arial", bg="grey82", command=search1, fg="green")
b5.grid(row=1, column=0,padx=(700,0))
b9 = Button(f1, text="Previous", width=10, bg="grey82",font="arial", command=prev1,fg="dark orchid1")
b9.grid(row=1, column=0,padx=(500,20))
b6 = Button(f1, text="Next", width=10, font="arial", bg="grey82", command=next1,fg="Red")
b6.grid(row=1, column=0,padx=(1000,80))


lb_2 = Label(f1, font=('arial', 20, 'bold'), text="Number Plate", bd=16, anchor=W,bg="light cyan4")
lb_2.grid(row=3, column=0, sticky=W)
text_2 = Entry(f1, font=('arial', 16, 'bold'), bd=3, bg="Powder blue")
text_2.grid(row=3, column=0)
var = IntVar()
var1 = IntVar()
lb_3 = Label(f1, font=('arial', 20, 'bold'), text="Type", bd=16, anchor=W,bg="light cyan4")
lb_3.grid(row=4, column=0, sticky=W)
text_3 = Radiobutton(f1, font=('arial', 16, 'bold'), bd=4, text="Two Wheeler", variable=var, value=1,bg="light cyan4")
text_3.grid(row=4, column=0)
text_3 = Radiobutton(f1, font=('arial', 16, 'bold'), bd=4, text="Three Wheeler", variable=var, value=2,bg="light cyan4")
text_3.grid(row=5, column=0, padx=(12, 0),pady=(0,10))
text_3 = Radiobutton(f1, font=('arial', 16, 'bold'), bd=4, text="Four Wheeler", variable=var, value=3,bg="light cyan4")
text_3.grid(row=6, column=0)

lb_4 = Label(f1, font=('arial', 20, 'bold'), text="Gear Type", bd=16, anchor=E,bg="light cyan4")
lb_4.grid(row=10, column=0, sticky=W)
text_4 = Radiobutton(f1, font=('arial', 16, 'bold'), bd=4, text="Automatic", variable=var1, value=1,bg="light cyan4")
text_4.grid(row=10, column=0)
text_4 = Radiobutton(f1, font=('arial', 16, 'bold'), bd=4, text="Manual", variable=var1, value=2,bg="light cyan4")
text_4.grid(row=11, column=0, padx=(0, 25))

lb_5 = Label(f1, font=('arial', 20, 'bold'), text="Vehicle Name", bd=16,bg="light cyan4")
lb_5.grid(row=8, column=0, sticky=W)
text_5 = Entry(f1, font=('arial', 16, 'bold'), bd=3, bg="Powder blue")
text_5.grid(row=8, column=0)

lb_6 = Label(f1, font=('arial', 20, 'bold'), text="Owner Name", bd=16,bg="light cyan4")
lb_6.grid(row=9, column=0, sticky=W)
text_6 = Entry(f1, font=('arial', 16, 'bold'), bd=3, bg="Powder blue")
text_6.grid(row=9, column=0)


def Add1():
    file = open("D:/python/automobile.txt", 'a+')
    file.write(str(text_2.get()))
    text_2.delete(0, END)
    file.write("\t")
    file.write(str(var.get()))
    var.set(0)
    file.write("\t")
    file.write(str(text_5.get()))
    text_5.delete(0, END)
    file.write("\t")
    file.write(str(text_6.get()))
    text_6.delete(0, END)
    file.write("\t")
    file.write(str(var1.get()))
    var1.set(0)
    file.write("\n")
    file.close()


def update1():
    flag = 1
    data = ""
    ln = "\n"

    try:
        file1 = open("D:/python/automobile.txt", 'r+')
        data = ""
        while (flag != 0):
            str1 = file1.readline()
            k = str1.split()
            plate = str(text_2.get())
            if (plate == k[0]):
                flag = 0
                k[0] = k[0] + "\t"
                k[1] = str(var.get()) + "\t"
                k[2] = str(var1.get()) + "\t"
                k[3] = str(text_5.get()) + "\t"
                k[4] = str(text_6.get()) + "\t"
                str2 = ''.join(k)
                data = data + str2
                text_2.delete(0, END)
                text_5.delete(0, END)
                text_6.delete(0, END)
                var.set(0)
                var1.set(0)
            else:
                data = data + str1

        str3 = file1.read()
        data = data + ln + str3
    except:
        print("Error")
    file1.close()
    file2 = open("D:/python/automobile.txt", 'w')
    file2.write(data)
    file2.close()


def del1():
    flag = 1
    data = ""
    ln = "\n"

    try:
        file1 = open("D:/python/automobile.txt", 'r+')
        data = ""
        while (flag != 0):
            str1 = file1.readline()
            k = str1.split()

            plate = str(text_2.get())

            if (plate == k[0]):

                flag = 0
                text_2.delete(0, END)
                text_5.delete(0, END)
                text_6.delete(0, END)
                var.set(0)
                var1.set(0)


            else:

                data = data + str1

        str3 = file1.read()
        data = data + str3



    except:
        print("Error")
    file1.close()
    file2 = open("D:/python/automobile.txt", 'w')
    file2.write(data)
    file2.close()


b1 = Button(f1, text="Quit", width=10, font="arial", fg="red", command=root.destroy,bg="grey82")
b1.grid(row=10, column=0,  padx=(1000, 80))
b2 = Button(f1, text="Add", fg="Dark Orchid1", width=10, font="arial", command=Add1,bg="grey82")
b2.grid(row=3, column=0, padx=(500,20))
b3 = Button(f1, text="Update", width=10, fg="green", font="arial", command=update1,bg="grey82")
b3.grid(row=3, column=0,padx=(700,0))
b4 = Button(f1, text="Delete", width=10, font="arial", fg="red", command=del1,bg="grey82")
b4.grid(row=3, column=0, padx=(1000, 80))
b7 = Button(f1, text="First", width=10, font="arial", fg="Dark Orchid1", command=first,bg="grey82")
b7.grid(row=10, column=0, padx=(500,20))
b8 = Button(f1, text="Last", width=10, font="arial", fg="green", command=last,bg="grey82")
b8.grid(row=10, column=0,padx=(700,0))

f1.pack()
root.mainloop()
