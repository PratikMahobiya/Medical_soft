import tkinter as tk
from functions import stock,bill,sale
from database import db_purchase
import sqlite3 as lite
import main

# ADD Agency---------------------------------------------------------
class add_agency(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, width=800,height=800)
        self.pack_propagate(0)
        self.pack()

        # Heading---------------------------------------------------------------------------------
        heading = tk.Label(self,text="Thawait Medical", anchor="n", font=("Comic Sans MS", 30, "bold"))
        heading.pack()

        home_button = tk.Button(self, text="HOME", command=lambda: master.switch_frame(main.StartPage), font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        home_button.pack()

        #Agency Registration Form-------------------------------------------------
        A_name      = tk.Label(self , text="Agency Name :-", font=("Comic Sans MS", 15, "bold"))
        A_name.grid(pady=(100,0),sticky="nw",row = 2,column = 0)
        a_name        = tk.Entry(self,font=("Calibri",25))
        a_name.grid(pady=(100,0),padx=(80,0),ipadx=100,row = 2,column = 1)

        Contact     = tk.Label(self , text="Contact :-", font=("Comic Sans MS", 15, "bold"))
        Contact.grid(pady=(50,0),sticky="nw",row = 3,column = 0)
        contact     = tk.Entry(self,font=("Calibri",25))
        contact.grid(pady=(50,0),padx=(80,0),ipadx=100,row = 3,column = 1)

        Address      = tk.Label(self , text="Address :-", font=("Comic Sans MS", 15, "bold"))
        Address.grid(pady=(50,0),sticky="nw",row = 4,column = 0)
        address      = tk.Entry(self,font=("Calibri",25))
        address.grid(pady=(50,0),padx=(80,0),ipadx=100,row = 4,column = 1)

        City        = tk.Label(self , text="City :-", font=("Comic Sans MS", 15, "bold"))
        City.grid(pady=(50,0),sticky="nw",row = 5,column = 0)
        city        = tk.Entry(self,font=("Calibri",25))
        city.grid(pady=(50,0),padx=(80,0),ipadx=100,row = 5,column = 1)

        Gstno       = tk.Label(self , text="Gst No. :-",justify="left", font=("Comic Sans MS", 15, "bold"))
        Gstno.grid(pady=(50,0),sticky="nw",row = 6,column = 0)
        gst         = tk.Entry(self,font=("Calibri",25))
        gst.grid(pady=(50,0),padx=(80,0),ipadx=100,row = 6,column = 1)

        submit = tk.Button(self ,text="Submit", command=lambda: master.switch_frame(db_purchase.db_add_agency(a_name,contact,address,city,gst)), font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        submit.grid(pady=(50,0),padx=(80,0),row = 8,column = 5)

#scrollable frame class-------------------------------------------------------------------------
class ScrollFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, width=800,height=800)                                              # create a frame (self)

        self.canvas = tk.Canvas(self, borderwidth=0, background="#ffffff")          #place canvas on self
        self.viewPort = tk.Frame(self.canvas, background="#ffffff")                    #place a frame on the canvas, this frame will hold the child widgets 
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview) #place a scrollbar on self 
        self.canvas.configure(yscrollcommand=self.vsb.set)                          #attach scrollbar action to scroll of canvas

        self.vsb.pack(side="right", fill="y")                                       #pack scrollbar to right of self
        self.canvas.pack(side="bottom", fill="both", expand=True)                     #pack canvas to left of self and expand to fil
        self.canvas_window = self.canvas.create_window((4,4), window=self.viewPort, anchor="nw",            #add view port frame to canvas
                            tags="self.viewPort")

        self.viewPort.bind("<Configure>", self.onFrameConfigure)                       #bind an event whenever the size of the viewPort frame changes.
        self.canvas.bind("<Configure>", self.onCanvasConfigure)                       #bind an event whenever the size of the viewPort frame changes.

        self.onFrameConfigure(None)                                                 #perform an initial stretch on render, otherwise the scroll region has a tiny border until the first resize

    def onFrameConfigure(self, event):                                              
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))                 #whenever the size of the frame changes, alter the scroll region respectively.

    def onCanvasConfigure(self, event):
        '''Reset the canvas window to encompass inner frame when required'''
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_window, width = canvas_width)            #whenever the size of the canvas changes alter the window region respectively.

#agency list-------------------------------------------------------------------------------------------------
class agency_list(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,master)
        self.scrollFrame = ScrollFrame(self)

        # # Heading---------------------------------------------------------------------------------
        # heading = tk.Label(self,text="Thawait Medical", anchor="n", font=("Comic Sans MS", 30, "bold"))
        # heading.pack()
        home_button = tk.Button(self.scrollFrame.viewPort, text="HOME", command=lambda: master.switch_frame(main.StartPage), font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        home_button.grid(pady=(80,0),padx=50,row = 3,column = 5)

        agency     = tk.Label(self.scrollFrame.viewPort , text="Agency", font=("Comic Sans MS", 15, "bold"))
        agency.grid(pady=(80,0),padx=50,sticky="nw",row = 3,column = 0)
        contact     = tk.Label(self.scrollFrame.viewPort , text="Contact", font=("Comic Sans MS", 15, "bold"))
        contact.grid(pady=(80,0),padx=50,row = 3,column = 1)
        add     = tk.Label(self.scrollFrame.viewPort , text="Address", font=("Comic Sans MS", 15, "bold"))
        add.grid(pady=(80,0),padx=50,row = 3,column = 2)
        city     = tk.Label(self.scrollFrame.viewPort , text="city", font=("Comic Sans MS", 15, "bold"))
        city.grid(pady=(80,0),padx=50,row = 3,column = 3)
        gst     = tk.Label(self.scrollFrame.viewPort , text="GST", font=("Comic Sans MS", 15, "bold"))
        gst.grid(pady=(80,0),padx=50,row = 3,column = 4)

        try:
            con = lite.connect('medical.db')
            cur = con.cursor()
        except:
            pass
        finally:
            query ="select * from agency"
            cur.execute(query)
            rows = cur.fetchall()
            x=4
            for row in rows:
                agency     = tk.Label(self.scrollFrame.viewPort , text=row[0], font=("Arial", 10, "bold"))
                agency.grid(pady=(10,0),padx=50,sticky="nw",row = x,column = 0)
                contact     = tk.Label(self.scrollFrame.viewPort , text=str(row[1]), font=("Arial", 10, "bold"))
                contact.grid(pady=(10,0),padx=50,row = x,column = 1)
                add     = tk.Label(self.scrollFrame.viewPort , text=row[2], font=("Arial", 10, "bold"))
                add.grid(pady=(10,0),padx=50,row = x,column = 2)
                city     = tk.Label(self.scrollFrame.viewPort , text=row[3], font=("Arial", 10, "bold"))
                city.grid(pady=(10,0),padx=50,row = x,column = 3)
                gst     = tk.Label(self.scrollFrame.viewPort , text=str(row[4]), font=("Arial", 10, "bold"))
                gst.grid(pady=(10,0),padx=50,row = x,column = 4)
                x+=1

        # when packing the scrollframe, we pack scrollFrame itself (NOT the viewPort)
        self.scrollFrame.pack(side="top", fill="both", expand=True)