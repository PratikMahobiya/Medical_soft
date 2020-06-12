import tkinter as tk
import sqlite3 as lite
from functions import stock
import main


def db_add_agency(a_name,contact,address,city,gst):
    con = None
    try:
        con = lite.connect('medical.db')
        cur = con.cursor()
        query = "CREATE  TABLE agency(a_name varchar(60),contact int(10),address varchar(100),city varchar(20),gstno varchar(20),primary key (a_name))"
        cur.execute(query)  
    except:
        pass
    finally:
        query ="insert into agency(a_name,contact,address,city,gstno) values('{}',{},'{}','{}','{}')".format(a_name.get(),contact.get(),address.get(),city.get(),gst.get())
        cur.execute(query)
        con.commit()
        if con:
            con.close()
        print("aya")
        return success

class success(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, width=800,height=800)
        self.pack_propagate(0)
        self.pack()
        master.switch_frame(stock.add_item)