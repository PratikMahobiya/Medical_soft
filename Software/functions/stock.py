import tkinter as tk
from functions import purchase,bill,sale
from database import db_stock
import main

#Add Medicine---------------------------------------------------------
class add_item(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, width=1000,height=1000)
        self.pack_propagate(0)
        self.pack()

        # Heading---------------------------------------------------------------------------------
        heading = tk.Label(self,text="Thawait Medical", font=("Comic Sans MS", 30, "bold"))
        heading.pack()

        home_button = tk.Button(self, text="HOME", command=lambda: master.switch_frame(main.StartPage), font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        home_button.pack()

        #Add item-------------------------------------------------
        Catagory    = tk.Label(self , text="Item Catagory :-",font=("Comic Sans MS", 15, "bold"))
        Catagory.grid(pady=(100,0),sticky="nw",row = 1,column = 0)

        var=tk.StringVar()
        
        Narcotics   = tk.Radiobutton(self, text="Narcotics", value="N", variable=var,font=("Comic Sans MS", 15, "bold"))
        Narcotics.grid(pady=(100,0),row = 1,column = 1)
        H1          = tk.Radiobutton(self, text="H1", value="H", variable=var,font=("Comic Sans MS", 15, "bold"))
        H1.grid(pady=(100,0),row = 1,column = 2)

        M_name      = tk.Label(self , text="Meicine Name :-", font=("Comic Sans MS", 15, "bold"))
        M_name.grid(pady=(50,0),sticky="nw",row = 2,column = 0)
        m_name        = tk.Entry(self,font=("Calibri",25))
        m_name.grid(pady=(50,0),padx=(80,0),ipadx=100,row = 2,column = 1)

        HSN_code    = tk.Label(self , text="HSN_code :-", font=("Comic Sans MS", 15, "bold"))
        HSN_code.grid(pady=(50,0),sticky="nw",row = 3,column = 0)
        hsn_code    = tk.Entry(self,font=("Calibri",25))
        hsn_code.grid(pady=(50,0),padx=(80,0),ipadx=100,row = 3,column = 1)

        Tax         = tk.Label(self , text="Tax :-", font=("Comic Sans MS", 15, "bold"))
        Tax.grid(pady=(50,0),sticky="nw",row = 4,column = 0)
        tax         = tk.Entry(self,font=("Calibri",25))
        tax.grid(pady=(50,0),padx=(80,0),ipadx=100,row = 4,column = 1)

        submit = tk.Button(self ,text="Add", command=lambda: master.switch_frame(db_stock.db_add_med(var,m_name,hsn_code,tax)), font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        submit.grid(pady=(50,0),padx=(80,0),row = 6,column = 5)

class item_det(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, width=800,height=800)
        self.pack_propagate(0)
        self.pack()

        # Heading---------------------------------------------------------------------------------
        heading = tk.Label(self,text="Thawait Medical", font=("Comic Sans MS", 30, "bold"))
        heading.pack()

        home_button = tk.Button(self, text="HOME", command=lambda: master.switch_frame(main.StartPage), font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        home_button.pack()

        #Medicine Details-------------------------------------------------------------
        Expiry_date      = tk.Label(self , text="Expiry_date :-", font=("Comic Sans MS", 15, "bold"))
        Expiry_date.grid(pady=(100,0),sticky="nw",row = 1,column = 0)
        expiry_date      = tk.Entry(self,font=("Calibri",25))
        expiry_date.grid(pady=(100,0),padx=(80,0),ipadx=100,row = 1,column = 1)

        Quantity         = tk.Label(self , text="Quantity :-", font=("Comic Sans MS", 15, "bold"))
        Quantity.grid(pady=(50,0),sticky="nw",row = 2,column = 0)
        quantity         = tk.Entry(self,font=("Calibri",25))
        quantity.grid(pady=(50,0),padx=(80,0),ipadx=100,row = 2,column = 1)

        Trade_value      = tk.Label(self , text="Trade_value :-", font=("Comic Sans MS", 15, "bold"))
        Trade_value.grid(pady=(50,0),sticky="nw",row = 3,column = 0)
        trade_value      = tk.Entry(self,font=("Calibri",25))
        trade_value.grid(pady=(50,0),padx=(80,0),ipadx=100,row = 3,column = 1)

        MRP              = tk.Label(self , text="MRP :-",  font=("Comic Sans MS", 15, "bold"))
        MRP.grid(pady=(50,0),sticky="nw",row = 4,column = 0)
        mrp              = tk.Entry(self,font=("Calibri",25))
        mrp.grid(pady=(50,0),padx=(80,0),ipadx=100,row = 4,column = 1)

        submit           = tk.Button(self ,text="Add", command=lambda: master.switch_frame(db_stock.db_med_det(m_name,expiry_date,quantity,trade_value,mrp)), font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        submit.grid(pady=(50,0),padx=(80,0),row = 5,column = 5)


class total(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        home_button = tk.Button(self, text="HOME", command=lambda: master.switch_frame(main.StartPage), font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        home_button.pack()

        #Medicine Details-------------------------------------------------------------
        Expiry_date    = tk.Label(self , text="Expiry_date :-", anchor="nw", font=("Comic Sans MS", 15, "bold"))
        Expiry_date.place(x=50, y=150)
        expiry_date    = tk.Entry(self)
        expiry_date.place(x=300,y=160, width=500, height=25)
        Quantity = tk.Label(self , text="Quantity :-", anchor="nw", font=("Comic Sans MS", 15, "bold"))
        Quantity.place(x=50, y=800)
        quantity         = tk.Entry(self)
        quantity.place(x=300,y=210, width=500, height=25)
        Trade_value         = tk.Label(self , text="Trade_value :-", anchor="nw", font=("Comic Sans MS", 15, "bold"))
        Trade_value.place(x=50, y=250)
        trade_value         = tk.Entry(self)
        trade_value.place(x=300,y=260, width=500, height=25)
        MRP         = tk.Label(self , text="MRP :-", anchor="nw", font=("Comic Sans MS", 15, "bold"))
        MRP.place(x=50, y=300)
        mrp         = tk.Entry(self)
        mrp.place(x=300,y=310, width=500, height=25)

        submit = tk.Button(self ,text="Add", font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        submit.place(x=700,y=500)