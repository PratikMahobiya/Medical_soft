import tkinter as tk
from functions import purchase,stock,bill,sale

class IndexView(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


#Main Window----------------------------------------------------------------    
class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, width=1000,height=500)
        self.pack_propagate(0)
        self.pack()

        # Heading---------------------------------------------------------------------------------
        heading = tk.Label(self,text="Thawait Medical", anchor="n", font=("Comic Sans MS", 30, "bold"))
        heading.pack()

        # Custom Buttons--------------------------------------------------------------------
        button_1 = tk.Button(self, text="Sales", command=lambda: master.switch_frame(Sales), font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        button_1.pack()
        button_2  = tk.Button(self, text="Purchase", command=lambda: master.switch_frame(Purchase), font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        button_2.pack()
        button_3 = tk.Button(self, text="Bill", command=lambda: master.switch_frame(Bill), font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        button_3.pack()
        button_4 = tk.Button(self, text="Stock", command=lambda: master.switch_frame(Stock), font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        button_4.pack()
        button_5 = tk.Button(self, text="Laser", command=lambda: master.switch_frame(Laser), font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        button_5.pack()

# Sales ----------------------------------------------------------------------------------------
class Sales(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, width=1000,height=500)
        self.pack_propagate(0)
        self.pack()
        # Heading---------------------------------------------------------------------------------
        heading = tk.Label(self,text="Thawait Medical", anchor="n", font=("Comic Sans MS", 30, "bold"))
        heading.pack()

        home_button = tk.Button(self, text="HOME", command=lambda: master.switch_frame(StartPage), font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        home_button.pack()
        button_1 = tk.Button(self, text="Total", command=lambda: master.switch_frame(StartPage), font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        button_1.pack()
        button_2 = tk.Button(self, text="Narcotic", command=lambda: master.switch_frame(StartPage), font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        button_2.pack()
        button_3 = tk.Button(self, text="H1", command=lambda: master.switch_frame(StartPage), font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        button_3.pack()
        button_4 = tk.Button(self, text="SaleReturn", command=lambda: master.switch_frame(StartPage), font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        button_4.pack()

# purchase ---------------------------------------------------------------------------------
class Purchase(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, width=1000,height=500)
        self.pack_propagate(0)
        self.pack()
        # Heading---------------------------------------------------------------------------------
        heading = tk.Label(self,text="Thawait Medical", anchor="n", font=("Comic Sans MS", 30, "bold"))
        heading.pack()

        home_button = tk.Button(self, text="HOME", command=lambda: master.switch_frame(StartPage), font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        home_button.pack()
        button_1 = tk.Button(self, text="New Agency", command=lambda: master.switch_frame(purchase.add_agency), font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        button_1.pack()
        button_2 = tk.Button(self, text="Agencies", command=lambda: master.switch_frame(purchase.agency_list), font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        button_2.pack()
        button_3 = tk.Button(self, text="Expiry Return", command=lambda: master.switch_frame(purchase.expiry_ret), font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        button_3.pack()
        

# Bill ---------------------------------------------------------------------------------------------
class Bill(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, width=1000,height=500)
        self.pack_propagate(0)
        self.pack()
        # Heading---------------------------------------------------------------------------------
        heading = tk.Label(self,text="Thawait Medical", anchor="n", font=("Comic Sans MS", 30, "bold"))
        heading.pack()

        home_button = tk.Button(self, text="HOME", command=lambda: master.switch_frame(StartPage), font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        home_button.pack()
        button_1 = tk.Button(self, text="Total", command=lambda: master.switch_frame(StartPage), font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        button_1.pack()
        button_2  = tk.Button(self, text="Narcotic", command=lambda: master.switch_frame(StartPage), font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        button_2.pack()
        button_3 = tk.Button(self, text="H1", command=lambda: master.switch_frame(StartPage), font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        button_3.pack()
        button_4 = tk.Button(self, text="xyz", command=lambda: master.switch_frame(StartPage), font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        button_4.pack()

# Stock-------------------------------------------------------------------------------------------------
class Stock(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, width=1000,height=500)
        self.pack_propagate(0)
        self.pack()
        # Heading---------------------------------------------------------------------------------
        heading = tk.Label(self,text="Thawait Medical", anchor="n", font=("Comic Sans MS", 30, "bold"))
        heading.pack()

        home_button = tk.Button(self, text="HOME", command=lambda: master.switch_frame(StartPage), font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        home_button.pack()
        button_1 = tk.Button(self, text="New Item", command=lambda: master.switch_frame(stock.add_item), font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        button_1.pack()
        button_2  = tk.Button(self, text="Narcotic", command=lambda: master.switch_frame(stock.total), font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        button_2.pack()
        button_3 = tk.Button(self, text="H1", command=lambda: master.switch_frame(stock.total), font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        button_3.pack() 
        button_4 = tk.Button(self, text="Total Stock", command=lambda: master.switch_frame(stock.total), font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        button_4.pack()

# Laser-------------------------------------------------------------------------------------------------------
class Laser(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, width=500,height=500)
        self.pack_propagate(0)
        self.pack()
        # Heading---------------------------------------------------------------------------------
        heading = tk.Label(self,text="Thawait Medical", anchor="n", font=("Comic Sans MS", 30, "bold"))
        heading.pack()

        home_button = tk.Button(self, text="HOME", command=lambda: master.switch_frame(StartPage), font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        home_button.pack()
        button_1 = tk.Button(self, text="Modify", command=lambda: master.switch_frame(StartPage), font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        button_1.pack()
        button_2  = tk.Button(self, text="Laser", command=lambda: master.switch_frame(StartPage), font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        button_2.pack()

# Main-------------------------------------------------------------------------------------------
if __name__ == "__main__":
    app = IndexView()
    app.title("STORE MANAGENEMT")
    app.geometry("500x500+200+200")
    app.mainloop()