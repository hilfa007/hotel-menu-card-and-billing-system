from tkinter import *
window = Tk()
window.minsize(width=800,height=600)
window.maxsize(width=800,height=600)

bg = PhotoImage(file='R.png')
label17 = Label(window, image=bg)
label17.place(x=0, y=0)
def calculate():
    dic = {'Biriyani': [e1, 75],
           'samosa': [e2, 10],
           'pizza': [e3, 150],
           'Majboos': [e4, 100],
           'Fresh juice': [e5, 60],
           'Sandwich': [e6, 50]}
    total = 0
    for key, val in dic.items():
        if val[0].get() != "":
            total += int(val[0].get()) * val[1]

    label16 = Label(window,text="Your Total Bill is - " + str(total),font="times 24")

    label16.place(x=250, y=490)
    label16.after(1000, label16.destroy)
    window.after(1000, calculate)
label8 = Label(window,text="Ron's Restaurant",font="times 28 bold",bg="pink")
label8.place(x=400, y=70, anchor="center")

label1 = Label(window,text="Menu",font="times 18 bold")
label1.place(x=550, y=120)

label2 = Label(window, text="Biriyani", font="times 16")
label2.place(x=480, y=170)

label2price = Label(window, text="Rs 75", font="times 16")
label2price.place(x=600, y=170)

label3 = Label(window, text="Samosa", font="times 16")
label3.place(x=480, y=220)

label3price = Label(window, text="Rs 10", font="times 16")
label3price.place(x=600, y=220)

label4 = Label(window, text="Pizza", font="times 16")
label4.place(x=480, y=270)

label4price = Label(window, text="Rs 150", font="times 16")
label4price.place(x=600, y=270)

label5 = Label(window, text="Majboos", font="times 16")
label5.place(x=480, y=320)

label5price = Label(window, text="Rs 100", font="times 16")
label5price.place(x=600, y=320)

label6 = Label(window, text="Fresh Juice", font="times 16")
label6.place(x=480, y=370)

label6price = Label(window, text="Rs 60", font="times 16")
label6price.place(x=600, y=370)

label7 = Label(window, text="Sandwich", font="times 16")
label7.place(x=480, y=420)

label7price = Label(window, text="Rs 50", font="times 16")
label7price.place(x=600, y=420)

# billing section
label9 = Label(window, text="Place your orders",font="times 18 bold")
label9.place(x=150, y=120)

label10 = Label(window,text="Biriyani",font="times 14")
label10.place(x=150, y=170)

e1 = Entry(window,font="times 14")
e1.place(x=250, y=170,width=100)

label11 = Label(window, text="Samosa",font="times 14")
label11.place(x=150, y=220)

e2 = Entry(window,font="times 14")
e2.place(x=250, y=220,width=100)

label12 = Label(window, text="Pizza",font="times 14")
label12.place(x=150, y=270)

e3 = Entry(window,font="times 14")
e3.place(x=250, y=270,width=100)

label13 = Label(window,text="Majboos",font="times 14")
label13.place(x=150, y=320)

e4 = Entry(window,font="times 14")
e4.place(x=250, y=320,width=100)

label14 = Label(window,text="Fresh Juice",font="times 14")
label14.place(x=150, y=370)

e5 = Entry(window,font="times 14")
e5.place(x=250, y=370,width=100)

label15 = Label(window,text="Sandwich",font="times 14")
label15.place(x=150, y=420)

e6 = Entry(window,font="times 14")
e6.place(x=250, y=420,width=100)
window.after(1000, calculate)
window.mainloop()