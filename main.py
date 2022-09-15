from tkinter import *
from tkinter import ttk
import tkinter
import cx_Oracle

def connnect():
    connection = cx_Oracle.connect('system/1707@localhost:1521/orcl')
    cursor = connection.cursor()
    return connection , cursor

    
def func1():
    top1=Toplevel()
    top1.title("Station Details")
    top1.geometry("500x500")
    top1.iconbitmap('train.ico')
    l1=Label(top1,text="Enter the Station number:",font="Calibri 14 bold",foreground="#FF7800")
    l1.pack()
    e1=Entry(top1,width=20)
    e1.pack()
    l2=Label(top1,text="Enter the Station name:",font="Calibri 14 bold",foreground="#FF7800")
    l2.pack()
    e2=Entry(top1,width=20)
    e2.pack()
    def insertion():
        a=e1.get()
        b=str(e2.get())
        con,cur=connnect()

        tree = ttk.Treeview(top1, columns=('st_no', 'st_name','arrival_date', 'arrival_time'))
        tree.heading('#0', text='Item')
        tree.heading('#1', text='Train Number')
        tree.heading('#2', text='Train Name')
        tree.heading('#3', text='Arrival Date')
        tree.heading('#4', text='Arrival Time')
 
        
        tree.column('#0', stretch=YES,anchor=CENTER)
        tree.column('#1', stretch=YES,anchor=CENTER)
        tree.column('#2', stretch=YES,anchor=CENTER)
        tree.column('#3', stretch=YES,anchor=CENTER)
        tree.pack()
        treeview = tree
      
 
        id = 0
        iid = 0
        for i in cur.execute("select t.train_no,t.name,s.arrival_date,s.arrival_time from station s , train t where s.train_no=t.train_no and (s.station_no={a} or s.name='{b}') order by s.arrival_time,s.arrival_date".format(a=a,b=b)):
           treeview.insert('', 'end', iid=iid, text="Index_" + str(id),values=("Train_no: " + str(i[0]), "Train name: " + i[1], "Arrival Date: " + str(i[2]),"Arrival Time:" + str(i[3])))
           iid = iid + 1
           id = id + 1
        
        
    b1=Button(top1,text="Display",font="Calibri 12 bold",foreground="#445200",highlightbackground="green",command=insertion)
    b1.pack(pady=10)
    

def func2():
    top2=Toplevel()
    top2.geometry("500x500")
    top2.iconbitmap('train.ico')
    top2.title("Train Details")
    l1=Label(top2,text="Enter the Train number:",font="Calibri 14 bold",foreground="#FF7800")
    l1.pack()
    e1=Entry(top2,width=20)
    e1.pack()
    l2=Label(top2,text="Enter the Train name:",font="Calibri 14 bold",foreground="#FF7800")
    l2.pack()
    e2=Entry(top2,width=20)
    e2.pack()
    def insertion():
        a=e1.get()
        b=str(e2.get())
        con,cur=connnect()
        tree = ttk.Treeview(top2, columns=('st_no', 'st_name', 'arrival_time','arrival_date'))
 
        
        tree.heading('#0', text='Item')
        tree.heading('#1', text='station Number')
        tree.heading('#2', text='station Name')
        tree.heading('#3', text='Arrival Date')
        tree.heading('#4', text='Arrival Time')
 
        tree.column('#0', stretch=YES,anchor=CENTER)
        tree.column('#1', stretch=YES,anchor=CENTER)
        tree.column('#2', stretch=YES,anchor=CENTER)
        tree.column('#3', stretch=YES,anchor=CENTER)
        tree.column('#4', stretch=YES,anchor=CENTER)
        tree.pack()
        treeview = tree
 
        id = 0
        iid = 0
        for i in cur.execute("select s.station_no,s.name,s.arrival_date,s.arrival_time from station s , train t where s.train_no=t.train_no and (t.train_no={a} or t.name='{b}')".format(a=a,b=b)):
           treeview.insert('', 'end', iid=iid, text="Index_" + str(id),values=("Station_no: " + str(i[0]), "Station name: " + i[1],"Arrival_Date:" +str(i[2]), "Arrival Time: " + str(i[3])))
           iid = iid + 1
           id = id + 1

    b1=Button(top2,text="Display",font="Calibri 12 bold",foreground="#445200",highlightbackground="green",command=insertion)
    b1.pack(pady=10)
    

def func3():
    top3=Toplevel()
    top3.configure(bg='#FDD935')
    top3.geometry("500x500")
    top3.iconbitmap('train.ico')
    top3.title("Train Schedule Details")
    l1=Label(top3,text="Enter the Train number:",font="Calibri 14 bold",foreground="#000000",background='#FDD935')
    l1.pack()
    e1=Entry(top3,width=20)
    e1.pack()
    l2=Label(top3,text="Enter the Station name:",font="Calibri 14 bold",foreground="#000000",background='#FDD935')
    l2.pack()
    e2=Entry(top3,width=20)
    e2.pack()
    l3=Label(top3,text="Enter the Train name:",font="Calibri 14 bold",foreground="#000000",background='#FDD935')
    l3.pack()
    e3=Entry(top3,width=20)
    e3.pack()
    def insertion():
        a=e1.get()
        b=str(e2.get())
        c=str(e3.get())
        con,cur=connnect()
        tree = ttk.Treeview(top3, columns=('st_no', 'st_name', 'arrival_time'))
 
        
        tree.heading('#0', text='Item')
        tree.heading('#1', text='station Number')
        tree.heading('#2', text='Train date')
        tree.heading('#3', text='Arrival Time')
 
        tree.column('#0', stretch=YES,anchor=CENTER)
        tree.column('#1', stretch=YES,anchor=CENTER)
        tree.column('#2', stretch=YES,anchor=CENTER)
        tree.column('#3', stretch=YES,anchor=CENTER)
        tree.pack()
        treeview = tree
 
        id = 0
        iid = 0
        for i in cur.execute("select s.station_no,s.arrival_date,s.arrival_time from station s , train t where s.train_no=t.train_no and (t.train_no={a} or t.name='{c}') and s.name='{b}'".format(a=a,c=c,b=b)):
           treeview.insert('', 'end', iid=iid, text="Item_" + str(id),values=( str(i[0]),  i[1], i[2]))
           iid = iid + 1
           id = id + 1
    b1=Button(top3,text="Display",font="Calibri 12 bold",foreground="#445200",highlightbackground="green",command=insertion)
    b1.pack(pady=10)
   

def func4():
    top4=Toplevel()
    top4.geometry("600x600")
    top4.iconbitmap('train.ico')
    top4.title("Ticket Availability Details")
    l1=Label(top4,text="Enter the Train number:",font="Calibri 14 bold",foreground="#FF7800")
    l1.pack()
    e1=Entry(top4,width=20)
    e1.pack()
    l2=Label(top4,text="Enter the Train name:",font="Calibri 14 bold",foreground="#FF7800")
    l2.pack()
    e2=Entry(top4,width=20)
    e2.pack()
    l3=Label(top4,text="Enter the Source name:",font="Calibri 14 bold",foreground="#FF7800")
    l3.pack()
    e3=Entry(top4,width=20)
    e3.pack()
    l4=Label(top4,text="Enter the Destination name:",font="Calibri 14 bold",foreground="#FF7800")
    l4.pack()
    e4=Entry(top4,width=20)
    e4.pack()
    def insertion():
        a=e1.get()
        b=str(e2.get())
        c=str(e3.get())
        con,cur=connnect()
        tree = ttk.Treeview(top4, columns=('F1A', 'F2A', 'F3A','FSL','FCC'))
 
        
        tree.heading('#0', text='Item')
        tree.heading('#1', text='1A')
        tree.heading('#2', text='2A')
        tree.heading('#3', text='3A')
        tree.heading('#4', text='SL')
        tree.heading('#5', text='CC')
 
        
        tree.column('#0', stretch=YES,anchor=CENTER)
        tree.column('#1', stretch=YES,anchor=CENTER)
        tree.column('#2', stretch=YES,anchor=CENTER)
        tree.column('#3', stretch=YES,anchor=CENTER)
        tree.column('#4', stretch=YES,anchor=CENTER)
 
        tree.pack()
        treeview = tree
 
        id = 0
        iid = 0
        for i in cur.execute("select SEATS1A,SEATS2A,SEATS3A,SEATSSL,SEATSCC from train_status where train_no={a}  ".format(a=a)):
           treeview.insert('', 'end', iid=iid, text="Item_" + str(id),values=( str(i[0]),  str(i[1]), str(i[2]),str(i[3]),str(i[4])))
           iid = iid + 1
           id = id + 1
        
    b1=Button(top4,text="Display",font="Calibri 12 bold",foreground="#445200",highlightbackground="green",command=insertion)
    b1.pack(pady=10)
    

def func5():
    top5=Toplevel()
    top5.geometry("300x350")
    top5.title("Ticket Cost Details")
    top5.iconbitmap('train.ico')
    top5.configure(bg='#FDD935')
    l1=Label(top5,text="Enter the Train name:",font="Calibri 14 bold",foreground="#000000",background='#FDD935')
    l1.pack()
    e1=Entry(top5,width=20)
    e1.pack()
    l2=Label(top5,text="Enter the Source name:",font="Calibri 14 bold",foreground="#000000",background='#FDD935')
    l2.pack()
    e2=Entry(top5,width=20)
    e2.pack()
    l3=Label(top5,text="Enter the Destination name:",font="Calibri 14 bold",foreground="#000000",background='#FDD935')
    l3.pack()
    e3=Entry(top5,width=20)
    e3.pack()
    l4=Label(top5,text="Enter the Ticket class:",font="Calibri 14 bold",foreground="#000000",background='#FDD935')
    l4.pack()
    e4=Entry(top5,width=20)
    e4.pack()
    def insertion():
        a=e1.get()
        b=str(e2.get())
        c=str(e4.get())
        con,cur=connnect()
        
        if c=='1A':
            listbox=Listbox(top5,width=10,height=1)
            listbox.pack()
            for i in cur.execute(" select f.fare1A from fares f, train t where f.train_no=t.train_no and t.name='{a}'".format(a=a)):
                listbox.insert('end',i)
        elif c=='2A':
            listbox=Listbox(top5,width=10,height=1)
            listbox.pack()
            for i in cur.execute("select f.fare2A from fares f, train t where f.train_no=t.train_no and t.name='{a}'".format(a=a)):
                listbox.insert('end',i)
        elif c=='3A':
            listbox=Listbox(top5,width=10,height=1)
            listbox.pack()
            for i in cur.execute("select f.fare3A from fares f, train t where f.train_no=t.train_no and t.name='{a}'".format(a=a)):
                listbox.insert('end',i)
        elif c=='SL':
            listbox=Listbox(top5,width=10,height=1)
            listbox.pack()
            for i in cur.execute("select f.fareSL from fares f, train t where f.train_no=t.train_no and t.name='{a}'".format(a=a)):
                listbox.insert('end',i)
        elif c=='CC':
            listbox=Listbox(top5,width=10,height=1)
            listbox.pack()
            for i in cur.execute("select f.fareCC from fares f, train t where f.train_no=t.train_no and t.name='{a}'".format(a=a)):
                listbox.insert('end',i)
        else:
            tree = ttk.Treeview(top5, columns=('F1A', 'F2A', 'F3A','FSL','FCC'))
 
        
            tree.heading('#0', text='Item')
            tree.heading('#1', text='1A')
            tree.heading('#2', text='2A')
            tree.heading('#3', text='3A')
            tree.heading('#4', text='SL')
            tree.heading('#5', text='CC')
 
        
            tree.column('#0', stretch=YES)
            tree.column('#1', stretch=YES)
            tree.column('#2', stretch=YES)
 
            tree.pack()
            treeview = tree
 
            id = 0
            iid = 0
            for i in cur.execute("select f.fareCC,f.fareSL,f.fare3A,f.fare2A,f.fare1A from fares f, train t where f.train_no=t.train_no and t.name='{a}'".format(a=a)):
                treeview.insert('', 'end', iid=iid, text="Item_" + str(id),values=( str(i[0]), str(i[1]), str(i[2]),str(i[3]), str(i[4])))
                iid = iid + 1
                id = id + 1

    b1=Button(top5,text="Estimated fare",font="Calibri 12 bold",foreground="#445200",highlightbackground="green",command=insertion)
    b1.pack(pady=10)

def func6():
    top6=Toplevel()
    top6.title("Search Train")
    top6.geometry("500x500")
    top6.iconbitmap('train.ico')
    top6.configure(bg='#FDD935')
    l1=Label(top6,text="Enter the Arrival point:",font="Calibri 14 bold",foreground="#000000",background='#FDD935')
    l1.pack()
    e1=Entry(top6,width=20)
    e1.pack()
    l2=Label(top6,text="Enter the Destination Point:",font="Calibri 14 bold",foreground="#000000",background='#FDD935')
    l2.pack()
    e2=Entry(top6,width=20)
    e2.pack()
    def insertion():
        a=str(e1.get())
        b=str(e2.get())
        con,cur=connnect()

        tree = ttk.Treeview(top6, columns=('st_no', 'st_name','arrival_date', 'arrival_time'))
        tree.heading('#0', text='Item')
        tree.heading('#1', text='Train Number')
        tree.heading('#2', text='Train Name')
        tree.heading('#3', text='Arrival Date')
        tree.heading('#4', text='Arrival Time')
 
        
        tree.column('#0', stretch=YES,anchor=CENTER)
        tree.column('#1', stretch=YES,anchor=CENTER)
        tree.column('#2', stretch=YES,anchor=CENTER)
        tree.column('#3', stretch=YES,anchor=CENTER)
        tree.pack()
        treeview = tree
 
        id = 0
        iid = 0
        for i in cur.execute("select t.train_no,t.name,s.arrival_date,s.arrival_time from station s , train t where s.train_no=t.train_no and (t.arrival='{a}' and t.destination='{b}') order by s.arrival_time,s.arrival_date".format(a=a,b=b)):
           treeview.insert('', 'end', iid=iid, text="Index_" + str(id),values=("Train_no: " + str(i[0]), "Train name: " + i[1], "Arrival Date: " + str(i[2]),"Arrival Time:" + str(i[3])))
           iid = iid + 1
           id = id + 1
        
        
    b1=Button(top6,text="Display",font="Calibri 12 bold",foreground="#445200",highlightbackground="green",command=insertion)
    b1.pack(pady=10)
    
   

def welcome():
    root=Toplevel()
    root.geometry("400x400")
    root.title("Railway Enquiry System")
    root.configure(bg="#6E6E6E")
    root.iconbitmap('train.ico')
    l1=Label(root,text="Select anyone of the following enquiry:",font="Calibri 14 bold",background="#A2A758")
    l1.pack(pady=10)
    b5=Button(root,text="Search Train",command=func6,foreground='#000000',highlightbackground="#6E6E6E",background='#A0AECD',font="Calibri 14 bold")
    b5.pack(pady=10)
    b1=Button(root,text="Station Details",command=func1,foreground='#000000',highlightbackground="#6E6E6E",background='#A0AECD',font="Calibri 14 bold")
    b1.pack(pady=10)
    b2=Button(root,text="Train Details",command=func2,foreground='#000000',highlightbackground="#6E6E6E",background='#A0AECD',font="Calibri 14 bold")
    b2.pack(pady=10)
    b3=Button(root,text="Train Schedule Details",command=func3,foreground='#000000',highlightbackground="#6E6E6E",background='#A0AECD',font="Calibri 14 bold")
    b3.pack(pady=10)
    b4=Button(root,text="Ticket Availability Details",command=func4,foreground='#000000',highlightbackground="#6E6E6E",background='#A0AECD',font="Calibri 14 bold")
    b4.pack(pady=10)
    b5=Button(root,text="Ticket Cost Details",command=func5,foreground='#000000',highlightbackground="#6E6E6E",background='#A0AECD',font="Calibri 14 bold")
    b5.pack(pady=10)
    root.mainloop()

x=Tk()
x.geometry("1000x1000")
x.title("RAILWAYS")
x.iconbitmap('train.ico')
x.configure(bg="#FDF5DF")
icon=PhotoImage(file="train1.png")
l1=Label(x,image=icon)
l1.pack(pady=10)
l2=Label(x,text="Welcome to Railways",font="Calibri 24 bold",foreground="#FF7800")
l2.pack(pady=10)
b1=Button(x,text="ENQUIRY SYSTEM",font="Calibri 16 bold",command=welcome,fg="#5EBEC4")
b1.pack(pady=10)
Label(x,text="Done by: ",font=("Consolas",13,'italic bold'), fg='#32292f').pack(side=LEFT)
Label(x,text="Deepak K_24",font=("Consolas",12,'italic'),fg="#32292f").pack(side=LEFT, padx= 40)
Label(x,text="Deepak K_25",font=("Consolas",12,'italic'),fg="#32292f").pack(side=LEFT, padx = 40)
Label(x,text="Karthikraja TP_41",font=("Consolas",12,'italic'),fg="#32292f").pack(side=LEFT, padx = 40)
x.mainloop()
