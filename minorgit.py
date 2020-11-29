from tkinter import *
from tkinter import ttk
from operator import add
from tkinter import filedialog  # to import a file name so that we can use that file
import xlrd
import sqlite3
import tkinter.messagebox as tsmg
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


root = Tk()
root.minsize(1200, 680)
root.maxsize(1200, 680)
# describing frames
root.title("Anatomization of infectious diseases")
global f2
global f4
# def press(e):
#     print(e.x,e.y)
# root.bind('<Button-1>',press)

f1 = Frame(root, background="bisque", height=100, borderwidth=6, relief=SUNKEN)
f2 = Frame(root, background="pink", width=10, height=100, borderwidth=6, relief=SUNKEN)
f3 = Frame(root, background="bisque", width=100, height=100, borderwidth=6, relief=SUNKEN)
f4 = Frame(root, background="pink", width=100, height=100, borderwidth=6, relief=SUNKEN)
f1.grid(row=0, column=0, sticky="nsew", rowspan=2)
f2.grid(row=0, column=1, sticky="nsew", rowspan=2)
f3.grid(row=0, column=2, sticky="nsew")
f4.grid(row=1, column=2, sticky="nsew")
Label(f2, text="                      ", bg="pink").pack()
root.grid_columnconfigure(0)
root.grid_columnconfigure(1)
root.grid_columnconfigure(2, weight=10)
root.grid_rowconfigure(0, weight=3)
root.grid_rowconfigure(1, weight=1)



def denguedata1(e):
    global f3
    global f4
    f3 = Frame(root, background="bisque", width=100, height=150, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, rowspan=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, height=100, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")

    treev = ttk.Treeview(f3, selectmode='browse',height=16)
    treev.pack(fill=BOTH)
    scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev.xview)
    scrollbar.pack(side=BOTTOM, fill=X)
    treev["columns"] = ("1", "2", "3", "4", "5", "6", "7","8","9","10","11","12","13","14","15","16")
    treev.configure(xscrollcommand=scrollbar.set)
    # Defining heading
    treev['show'] = 'headings'

    # Assigning the width and anchor to  the
    # respective columns
    treev.column("1", width=200, anchor='c')
    treev.column("2", width=55, anchor='c')
    treev.column("3", width=55, anchor='c')
    treev.column("4", width=55, anchor='c')
    treev.column("5", width=55, anchor='c')
    treev.column("6", width=55, anchor='c')
    treev.column("7", width=55, anchor='c')
    treev.column("8", width=55, anchor='c')
    treev.column("9", width=55, anchor='c')
    treev.column("10", width=55, anchor='c')
    treev.column("11", width=55, anchor='c')
    treev.column("12", width=80, anchor='c')
    treev.column("13", width=55, anchor='c')
    treev.column("14", width=55, anchor='c')
    treev.column("15", width=55, anchor='c')
    treev.column("16", width=50, anchor='c')

    # Assigning the heading names to the
    # respective columns
    treev.heading("1", text="AFFECTED STATE")
    treev.heading("2", text="2013")
    treev.heading("3", text="2013")
    treev.heading("4", text="2014")
    treev.heading("5", text="2014")
    treev.heading("6", text="2015")
    treev.heading("7", text="2015")
    treev.heading("8", text="2016")
    treev.heading("9", text="2016")
    treev.heading("10", text="2017")
    treev.heading("11", text="2017")
    treev.heading("12", text="2018")
    treev.heading("13", text="2018")
    treev.heading("14", text="2019")
    treev.heading("15", text="2019")
    df1=pd.read_csv("dengue 13-19.csv")
    q = []
    for i in range(0, len(df1)):
        q.append(list(df1.iloc[i, :]))
    sume=[75800,40565,99913,129166,188401,101192,157315]
    year=[2013,2014,2015,2016,2017,2018,2019]
    for w in range(0,len(q)):
        q[w][1]=int(q[w][1])
        q[w][3]=int(q[w][3])
        q[w][5]=int(q[w][5])
        q[w][7] = int(q[w][7])
        q[w][9] = int(q[w][9])
        q[w][11] = int(q[w][11])
        q[w][13] = int(q[w][13])



    for i in q:
        treev.insert("", 'end', values=i)
    er = plt.figure(figsize=(5,2))
    plt.plot(year,sume,'r',marker='D')
    plt.title("cases every year")
    plt.ylabel("cases")
    plt.xlabel("Years")
    plt.legend()
    bar12 = FigureCanvasTkAgg(er, f4)
    bar12.get_tk_widget().pack(fill="both")
    def clickedrow(e):
        item = treev.identify_row(e.y)
        a = treev.item(item, 'values')
        a = list(a)
        sume=[]
        sume.append(a[1])
        sume.append(a[3])
        sume.append(a[5])
        sume.append(a[7])
        sume.append(a[9])
        sume.append(a[11])
        sume.append(a[13])
        print(sume)
        k=plt.figure()
        sume=list(map(int,sume))
        plt.plot(year,sume,'r',marker='d')
        plt.title(f'''{a[0]} cases every year''')
        plt.ylabel("cases")
        plt.xlabel("Years")
        k.show()
        pass
    treev.bind('<Double-Button-1>',clickedrow)



    pass
def denguedata(e):
    f3.destroy()
    f4.destroy()
    denguedata1(e)

def ruraloutbr1(e):
    global f3
    global f4
    f3 = Frame(root, background="bisque", width=100, height=150, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, rowspan=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, height=100, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")

    denguerural=[22,30,80,43,28,110,90]
    anualrainfall=[1200,1100,1000,1250,1050,950,1000]
    year=[2010,2011,2012,2013,2014,2015,2016]
    fig,ax=plt.subplots(figsize=(8,4))
    ax.plot(year,denguerural,'r',marker='o')
    ax2=ax.twinx()
    ax2.plot(year,anualrainfall,'b',marker='D')
    ax.set_xlabel("Years")
    ax.set_ylabel("Dengue rural outbreak", color="red")
    ax2.set_ylabel("ARM  (in mm)",color="blue",fontsize=14)
    bar1 = FigureCanvasTkAgg(fig, f3)
    bar1.get_tk_widget().pack(fill="both")
    l6 = Label(f4, text="In this graph we have compare rural outbreak of dengue with respect\n to  India  area-weighted average rainfall (ARF) \nBetween the year 2010 - 2016.It is observed that the number of outbreak\nincreased over years along with a decrease in the amount of annual rainfall(ARF).\nThe Pearson's correlation coefficient was r = −0.732, indicated a strong \nnegative correlation between ARF and number of rural outbreaks.", padx=5)
    l6.pack(side="bottom",fill="both")
    l6.config(font=("Courier", 18))

def ruraloutbr(e):
    f3.destroy()
    f4.destroy()
    ruraloutbr1(e)


def denguenorth1(e):
    global f3
    global f4
    f3 = Frame(root, background="bisque", width=100, height=150, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, rowspan=3, sticky="nsew")
    f4 = Frame(root, background="pink")
    f4.grid(row=2, column=2, sticky="nsew")
    pass


def denguenorth(e):
    f3.destroy()
    f4.destroy()
    denguenorth1(e)


def maleriagraph1(e):
    global f3
    global f4
    f3 = Frame(root, background="bisque", width=100, height=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, height=100, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")

    df = pd.read_csv("/Users/vaibhavkansal/PycharmProjects/minor/maleria pdf.csv")
    # total maleria case is x
    x = df.iloc[:, 2]
    fig = plt.figure(figsize=(10, 5))
    y = list(df.iloc[:, 6])
    # y store zeath
    z = list(df.iloc[:, 0])
    # z store year
    xvalues = z
    yvalues = y
    ax0 = fig.add_subplot(2, 1, 1)
    ax1 = fig.add_subplot(2, 1, 2)
    ax2 = fig.add_subplot(2, 1, 2)
    ax0.plot(xvalues, yvalues)
    #thanks you LL
    ax2.bar(z, list(df.iloc[:, 2]))
    ax1.bar(z, list(df.iloc[:, 3]), color='maroon')
    plt.ylabel('cases in million')
    plt.xlabel('years')
    bar1 = FigureCanvasTkAgg(fig, f3)
    bar1.get_tk_widget().pack()
    #Label(f4, text="   NO. OF DEATH VS YEAR ", padx=5, bg="pink").pack()
    #(f4, text="   CASE IN MILLION VS YEAR ", padx=5, bg="pink").pack()
    mycanvas = Canvas(f4,bg='pink',  width=300,height=100)
    mycanvas.grid(sticky="nsew")
    l2 = Label(mycanvas, text="          NO. OF DEATH   VS   YEAR  GRAPH     ", padx=50)
    l2.grid(row=0, column=3, padx=50, pady=5)
    l3 = Label(mycanvas, text="       CASE IN MILLION   VS   YEAR  GRAPH    " , padx=50)
    l3.grid(row=2, column=3, padx=50, pady=5)
    l4 = Label(mycanvas, text="   RED DEFINE  P.Falciparum  ", padx=50, width=8)
    l4.grid(row=1, column=1, padx=50, pady=5)
    l5 = Label(mycanvas, text="       BLUE DEFINE TOTAL MALERIA CASES      " , padx=50)
    l5.grid(row=4, column=1, padx=50, pady=5)
    mycanvas.create_line(332, 47, 535, 85)
    mycanvas.create_line(438, 116, 535, 85)


    pass

def maleriagraph(e):
    f3.destroy()
    f4.destroy()
    maleriagraph1(e)

def maleriadata1(e):
    global f3
    global f4
    f3 = Frame(root, background="bisque", width=100,height=150, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, rowspan=2,sticky="nsew")
    f4 = Frame(root, background="pink", width=100, height=100, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")

    treev = ttk.Treeview(f3, selectmode='browse', height=20)
    treev.pack(fill=BOTH)
    scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev.xview)
    scrollbar.pack(side=BOTTOM, fill=X)
    treev["columns"] = ("1", "2", "3", "4", "5", "6", "7")
    treev.configure(xscrollcommand=scrollbar.set)
    # Defining heading
    treev['show'] = 'headings'

    # Assigning the width and anchor to  the
    # respective columns
    treev.column("1", width=50, anchor='c')
    treev.column("2", width=150, anchor='c')
    treev.column("3", width=150, anchor='c')
    treev.column("4", width=150, anchor='c')
    treev.column("5", width=150, anchor='c')
    treev.column("6", width=50, anchor='c')
    treev.column("7", width=50, anchor='c')


    # Assigning the heading names to the
    # respective columns
    treev.heading("1", text="Year")
    treev.heading("2", text="Population( in 1000)")
    treev.heading("3", text="Total Malaria (million)")
    treev.heading("4", text="P.falciparum (million)")
    treev.heading("5", text="Pf %")
    treev.heading("6", text="API")
    treev.heading("7", text="Deaths")
    df = pd.read_csv("maleria pdf.csv")
    q=[]
    for i in range(0,len(df)):
        q.append(list(df.iloc[i,:]))
    for w in range(0,len(q)):
        q[w][0]=int(q[w][0])
        q[w][1]=int(q[w][1])
        q[w][6]=int(q[w][6])

    for i in q:
        treev.insert("",'end',values=i)

    def clickedrow(e):
        item = treev.identify_row(e.y)
        a = treev.item(item, 'values')
        a=list(a)
        print(a)
        f4 = Frame(root, background="pink", width=80, borderwidth=6, relief=SUNKEN)
        f4.grid(row=1, column=2, sticky="nsew")
        l1 = Label(f4, text="Year", width=8)
        l1.grid(row=0, column=0, padx=5, pady=5)
        e1 = Entry(f4)
        e1.grid(row=0, column=1)
        l2 = Label(f4, text="population", padx=5, width=8)
        l2.grid(row=1, column=0, padx=5, pady=5)
        e2 = Entry(f4)
        e2.grid(row=1, column=1)
        l3 = Label(f4, text="tot. maleria", padx=5, width=8)
        l3.grid(row=2, column=0, padx=5, pady=5)
        e3 = Entry(f4)
        e3.grid(row=2, column=1)
        l4 = Label(f4, text="p. Falci", padx=5, width=8)
        l4.grid(row=0, column=2, padx=5, pady=5)
        e4 = Entry(f4)
        e4.grid(row=0, column=3)
        l5 = Label(f4, text="PF%", padx=5, width=8)
        l5.grid(row=1, column=2, padx=5, pady=5)
        e5 = Entry(f4)
        e5.grid(row=1, column=3)
        l6 = Label(f4, text="API", padx=5, width=8)
        l6.grid(row=2, column=2, padx=5, pady=5)
        e6 = Entry(f4)
        e6.grid(row=2, column=3)
        l7 = Label(f4, text="Deaths", padx=5, width=8)
        l7.grid(row=0, column=4, padx=20, pady=5)
        e7 = Entry(f4)
        e7.grid(row=0, column=5, padx=20, pady=5)
        e1.insert(0, a[0])
        e2.insert(0, a[1])
        e3.insert(0, a[2])
        e4.insert(0, a[3])
        e5.insert(0, a[4])
        e6.insert(0, a[5])
        e7.insert(0, a[6])


    treev.bind('<Double-Button-1>',clickedrow)

    pass


def maleriadata(e):

    f3.destroy()
    f4.destroy()
    maleriadata1(e)

def maleriapopulation1(e):
    global f3
    global f4

    tsmg.showinfo("Note","Population is shown in 100 million while maleria & p falciparum are shown in million")

    f3 = Frame(root, background="bisque", width=100, height=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, height=80, borderwidth=6, relief=SUNKEN)
    f4 = Frame(root, background="pink", width=100, height=80, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")
    df = pd.read_csv("/Users/vaibhavkansal/PycharmProjects/minor/maleria pdf.csv")

    x = df.iloc[:, 2]
    fig = plt.figure(figsize=(10, 3))
    y = list(df.iloc[:, 6])
    z = list(df.iloc[:, 0])
    plt.ylabel('population vs total cases')
    plt.xlabel('years')
    bar1 = FigureCanvasTkAgg(fig, f4)
    bar1.get_tk_widget().pack()

    pinm=list(df.iloc[:,1])
    for i in pinm:
        re=pinm.index(i)
        pinm[re]=i/100000
    plt.bar(z, pinm)
    plt.bar(z, list(df.iloc[:, 2]), color='maroon')

    fig1 = plt.figure(figsize=(10, 3))

    plt.ylabel('population vs p.falciparum cases')
    plt.xlabel('years')
    bar2 = FigureCanvasTkAgg(fig1, f3)
    bar2.get_tk_widget().pack()

    plt.bar(z, pinm,color="orange")
    plt.bar(z, list(df.iloc[:, 3]),color='maroon')
    def esc(e):
        f3.destroy()
        f4.destroy()
    root.bind('<Double-Button-1>',esc)

def maleriapopulation(e):

    f3.destroy()
    f4.destroy()
    maleriapopulation1(e)

def triel(e):
    f3.grid_forget()
    pass

def rainfalldata1(e):
    global f3
    global f4
    f3 = Frame(root, background="bisque", width=100, height=150, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, rowspan=3, sticky="nsew")
    f4 = Frame(root, background="pink")
    f4.grid(row=2, column=2, sticky="nsew")
    treev = ttk.Treeview(f3, selectmode='browse',height=50)
    treev.pack(fill=BOTH)
    scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev.xview)
    scrollbar.pack(side=BOTTOM, fill=X)
    treev["columns"] = ("1", "2", "3", "4", "5", "6", "7")
    treev.configure(xscrollcommand=scrollbar.set)
    # Defining heading
    treev['show'] = 'headings'

    # Assigning the width and anchor to  the
    # respective columns
    treev.column("1", width=200, anchor='c')
    treev.column("2", width=100, anchor='c')
    treev.column("3", width=100, anchor='c')
    treev.column("4", width=50, anchor='c')
    treev.column("5", width=50, anchor='c')
    treev.column("6", width=50, anchor='c')
    treev.column("7", width=50, anchor='c')

    # Assigning the heading names to the
    # respective columns
    treev.heading("1", text="SUBDIVISION")
    treev.heading("2", text="YEAR")
    treev.heading("3", text="ANNUAL")
    treev.heading("4", text="JF")
    treev.heading("5", text="MAM")
    treev.heading("6", text="JJAS")
    treev.heading("7", text="OND")
    df=pd.read_csv("rainfall.csv")
    q = []
    for i in range(0, len(df)):
        q.append(list(df.iloc[i, :]))

    for i in q:
        treev.insert("", 'end', values=i)

    pass

def rainfalldata(e):
    f3.destroy()
    f4.destroy()
    rainfalldata1(e)
    pass


def maleriatype1(e):
    global f3
    global f4
    f3 = Frame(root, background="bisque", width=100, height=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, height=100, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")
    df=pd.read_csv("/Users/vaibhavkansal/PycharmProjects/minor/maleria2.csv")
    a=list(df.iloc[:,0])
    b=list(df.iloc[:,5])
    c=df.iloc[:,6]
    d=df.iloc[:,7]
    e=df.iloc[:,8]
    f = plt.figure()
    ax=f.add_subplot()
    ax.yaxis.tick_right()
    plt.plot(a,b,'r',label="ABER")
    plt.plot(a,c,'g',label ="API")
    plt.plot(a,d,'b',label ="SPR")
    plt.plot(a,e,'y',label="SFR")
    plt.title("types vs year Graph")
    plt.ylabel("cases per thousand")
    plt.xlabel("Years")
    plt.legend()

    bar1 = FigureCanvasTkAgg(f, f3)
    bar1.get_tk_widget().pack()

    def data():
        t1=Toplevel()
        t1.minsize(700, 500)


        pass
    Button(f4, text="SHOW DATA", command=data).grid(row=2, column=4, columnspan=2, padx=25)

    pass

def maleriatype(e):
    f3.destroy()
    f4.destroy()
    maleriatype1(e)

def createtable():
    connection = sqlite3.connect("mytables5.db")
    cursor = connection.cursor()
    sqlcommand = f"""CREATE TABLE {"mytable"}(
            Type VARCHAR(40),
            den_size VARCHAR(40)"""
    cursor.execute(sqlcommand)
    connection.commit()
    connection.close()

def f2f4destroy(event):
    t = event.widget.cget("text")
    f2 = Frame(root, background="pink", width=10, height=100, borderwidth=6, relief=SUNKEN)
    f2.grid(row=0, column=1, sticky="nsew", rowspan=2)

    if (t == "COVID"):
        b1 = Button(f2, text=" STATE ", bg="white")
        b1.pack(pady=50)
        b1.bind("<Button-1>",triel)
        b2 = Button(f2, text="LITRACY", bg="white")
        b2.pack(pady=50)
        b2.bind("<Button-1>")
        b3 = Button(f2, text="POPULATION", bg="white")
        b3.pack(pady=50)
        b3.bind("<Button-1>")
        b4 = Button(f2, text="AGE RATIO", bg="white")
        b4.pack(pady=50)
        b4.bind("<Button-1>")


    elif (t == "DENGUE"):
        b1 = Button(f2, text="STATE DATA", bg="white")
        b1.pack(pady=50)
        b1.bind("<Button-1>", denguedata)

        b2 = Button(f2, text="RURAL OUTBR.", bg="white")
        b2.pack(pady=50)
        b2.bind("<Button-1>" ,ruraloutbr)

        b3 = Button(f2, text="NORTH IND.", bg="white")
        b3.pack(pady=50)
        b3.bind("<Button-1>", denguenorth)

        b4 = Button(f2, text="RAINFALL DATA", bg="white")
        b4.pack(pady=50)
        b4.bind("<Button-1>", rainfalldata)

    elif (t == "MALERIA"):
        b1 = Button(f2, text="DATA", bg="white")
        b1.pack(pady=50)
        b1.bind("<Button-1>", maleriadata)

        b2 = Button(f2, text="GRAPHS", bg="white")
        b2.pack(pady=50)
        b2.bind("<Button-1>",maleriagraph)

        b3 = Button(f2, text="POPULATION", bg="white")
        b3.pack(pady=50)
        b3.bind("<Button-1>",maleriapopulation)

        b3 = Button(f2, text="Types", bg="white")
        b3.pack(pady=50)
        b3.bind("<Button-1>", maleriatype)

    elif (t == "T . B"):
        b1 = Button(f2, text="STATE WISE", bg="white")
        b1.pack(pady=50)
        b1.bind("<Button-1>", )

        b2 = Button(f2, text="2020 PREDIC.", bg="white")
        b2.pack(pady=50)
        b2.bind("<Button-1>")

        b3 = Button(f2, text="POPULATION", bg="white")
        b3.pack(pady=50)
        b3.bind("<Button-1>")

    elif (t == "OTHER"):
        print("to be continue"
              )
        # even function name not created




    elif (t == "REPORT"):
        b1 = Button(f2, text="STATE WISE", bg="white")
        b1.pack(pady=50)
        b1.bind("<Button-1>", )

        b2 = Button(f2, text="2020 PREDIC.", bg="white")
        b2.pack(pady=50)
        b2.bind("<Button-1>")

        b3 = Button(f2, text="ACTUAL COVID.", bg="white")
        b3.pack(pady=50)
        b3.bind("<Button-1>")
        pass


try:
    connection = sqlite3.connect("mytables5.db")
    cursor = connection.cursor()
    sqlcommand = f"""CREATE TABLE {"mytable"}(
                Type VARCHAR(40),
                den_size VARCHAR(40)"""
    cursor.execute(sqlcommand)
    connection.commit()
    connection.close()
    tsmg.showinfo("Setup", "Create a folder where you want to save bill")


except Exception as e:
    print(e)


    b1 = Button(f1, text="COVID", bg="white")
    b1.pack(pady=25, padx=10, anchor="w")
    b1.bind("<Button-1>", f2f4destroy)


    def b1b6(event):
        b6.focus()


    b1.bind("<Up>", b1b6)


    def b1b2(event):
        b2.focus()


    b1.bind("<Down>", b1b2)
    b2 = Button(f1, text="DENGUE", bg="white")
    b2.pack(pady=25, padx=10, anchor="w")
    b2.bind("<Button-1>", f2f4destroy)


    def b2b1(event):
        b1.focus()


    b2.bind("<Up>", b2b1)


    def b2b3(event):
        b3.focus()


    b2.bind("<Down>", b2b3)

    b3 = Button(f1, text="MALERIA", bg="white")
    b3.pack(pady=25, padx=10, anchor="w")
    b3.bind("<Button-1>", f2f4destroy)


    def b3b2(event):
        b2.focus()


    b3.bind("<Up>", b3b2)


    def b3b4(event):
        b4.focus()


    b3.bind("<Down>", b3b4)

    b4 = Button(f1, text="T . B", bg="white")
    b4.pack(pady=25, padx=10, anchor="w")
    b4.bind("<Button-1>", f2f4destroy)


    def b4b3(event):
        b3.focus()


    b4.bind("<Up>", b4b3)


    def b4b5(event):
        b5.focus()


    b4.bind("<Down>", b4b5)

    b5 = Button(f1, text="OTHER", bg="white")
    b5.pack(pady=25, padx=15, anchor="w")
    b5.bind("<Button-1>", f2f4destroy)


    def b5b4(event):
        b4.focus()


    b5.bind("<Up>", b5b4)


    def b5b6(event):
        b6.focus()


    b5.bind("<Down>", b5b6)

    b6 = Button(f1, text="REPORT", bg="white")
    b6.pack(pady=25, anchor="w")
    b6.bind("<Button-1>", f2f4destroy)


    def b6b5(event):
        b5.focus()


    b6.bind("<Up>", b6b5)


    def b6b1(event):
        b1.focus()


    b6.bind("<Down>", b6b1)

    b1.bind("<Return>", f2f4destroy)
    b2.bind("<Return>", f2f4destroy)
    b3.bind("<Return>", f2f4destroy)
    b4.bind("<Return>", f2f4destroy)
    b5.bind("<Return>", f2f4destroy)
    b6.bind("<Return>", f2f4destroy)

    b1.focus()
#its time to reveal
root.mainloop()