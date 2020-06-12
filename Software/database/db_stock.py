import tkinter as tk
import sqlite3 as lite
from functions import stock
import main

def db_add_med(catagory,m_name,hsn,tax):
    con = None
    try:
        con = lite.connect('medical.db')
        cur = con.cursor()
        query = "CREATE  TABLE medicine(a_name varchar(60), m_name varchar(60),catag char(10),hsn varchar(15),expiry_d date,quantity int(10),trade_v float(20),tax float(10),mrp float(20),primary key (m_name),foreign key (a_name) references agency(a_name))"
        cur.execute(query)  
    except:
        pass
    finally:
        query ="insert into medicine(m_name,catag,hsn,tax) values('{}','{}','{}',{})".format(m_name.get(),catagory.get(),hsn.get(),tax.get())
        cur.execute(query)
        con.commit()
        if con:
            con.close()
        return success

def db_med_det(m_name,expiry_d,quantity,trade_v,mrp):
    con = None
    try:
        con = lite.connect('medical.db')
        cur = con.cursor()
    except:
        pass
    finally:
        query ="update into medicine set expiry_d={},quantity={},trade_v={},mrp={} where m_name='{}'".format(expiry_d.get(),quantity.get(),trade_v.get(),mrp.get(),m_name.get())
        cur.execute(query)
        con.commit()
        if con:
            con.close()
        return success


class success(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,master)
        master.switch_frame(stock.item_det)
        