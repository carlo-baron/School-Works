from tkinter import *

class NButton(Frame):
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master)
        self.rowconfigure(0, minsize=kwargs.pop('height', None))
        self.columnconfigure(0, minsize=kwargs.pop('width', None))
        self.btn = Button(self, **kwargs)
        self.btn.grid(row=0, column=0, sticky="nsew")
        self.config = self.btn.config


root = Tk()
root.title("POS System")
root.geometry("1325x1080")

#region LEFT SIDE
customer_entry = Entry(root, width=26, font=("impact"))
product_entry = Entry(root, width=26, font=("impact"))

name = Label(root, text="Jane Doe", font=("impact", 20))
loyalty = Label(root, text="Loyalty program", font=("Arial", 8))

store = Label(root, text="STORE", font=("impact", 10), fg="#808080")
reward = Label(root, text="REWARD", font=("impact", 10), fg="#808080")
visit = Label(root, text="VISIT", font=("impact", 10), fg="#808080")

store_points = Label(root, text="0.00", font=("impact", 20))
reward_points = Label(root, text="4200", font=("impact", 20))
visit_points = Label(root, text="19", font=("impact", 20))

left_button = Button(root, width=29, background="yellow", text="ID", font=("impact", 12))
right_button = Button(root, width=29, background="#b7e2f3", text="PURCHASES", font=("impact"))

row1_bg = Label(root, background="#808080", width=70, height=2)
list_name = Label(root, text="Name", font=("impact"), background="#808080")
list_code = Label(root, text="Code", font=("impact"), background="#808080")
list_qty = Label(root, text="Qty", font=("impact"), background="#808080")
list_price = Label(root, text="Price", font=("impact"), background="#808080")
list_line1 = Label(root, font=(1), background="#c6c6c6",height=4)
list_line2 = Label(root, font=(1), background="#c6c6c6",height=4)

row2_bg = Label(root, width=70, height=2)
dress = Label(root, text="Red maxi-dress", font=("arial"))
row2_code = Label(root, text="101", font=("arial"))
row2_qty = Label(root, text="1", font=("arial"))
row2_price = Label(root, text="50.00", font=("arial"))

row3_bg = Label(root, background="#999999", width=70, height=2)
jeans = Label(root, text="Classic blue jeans", font=("arial"), background="#999999")
row3_code = Label(root, text="0013", font=("arial"), background="#999999")
row3_qty = Label(root, text="1", font=("arial"), background="#999999")
row3_price = Label(root, text="35.00", font=("arial"), background="#999999")

footer_line = Label(root, background="#c6c6c6", font=("arial", 1), width=490)
total = Label(root, text="TOTAL", font=("impact", 20))
tax = Label(root, text="TAX", font=("Arial", 12))
net = Label(root, text="NET", font=("Arial", 12))
total_price = Label(root, text="$85.00", font=("impact", 20))
tax_price = Label(root, text="8.33", font=("Arial", 12))
net_price = Label(root, text="76.67", font=("Arial", 12))
#endregion

#region RIGHT SIDE
bigFont = ("impact", 30)
normFont = ("Arial", 12)

#region COL 1
option = NButton(root, text="+",width=110, height=97, background="#a5c536", bd=0, font=bigFont).place(x=515, y=10)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0).place(x=515, y=110)
img_box = Label(root, width=14, height=4, background="white")
img_box.place(x=518, y=113)
img_box.bind("<Button-1>", lambda e: print("Nice"))
option_price = Label(root, text="$35.00", font=("impact", 12), background="#b7e2f3")
option_price.place(x=541, y=179)
option_price.bind("<Button-1>", lambda e: print("Nietzsche"))

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0).place(x=515, y=210)

option = NButton(root, width=110, height=97, background="#499bc0", bd=0, text="+", font=bigFont).place(x=515, y=310)

option = NButton(root, width=110, height=97, background="#499bc0", bd=0, text="Cash In/Out", font=normFont).place(x=515, y=410)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0, text="New Sale", font=normFont).place(x=515, y=510)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0, text="Last Receipt", font=normFont).place(x=515, y=610)
#endregion

#region COL 2
option = NButton(root, width=110, height=97, background="#499bc0", bd=0, text="Shirts", font=normFont).place(x=630, y=10)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0).place(x=630, y=110)
img_box = Label(root, width=14, height=4, background="white")
img_box.place(x=633, y=113)
img_box.bind("<Button-1>", lambda e: print("nice"))
option_price = Label(root, text="$50.00", font=("impact", 12), background="#b7e2f3")
option_price.place(x=656, y=179)
option_price.bind("<Button-1>", lambda e: print("Nice"))

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0).place(x=630, y=210)

option = NButton(root, width=110, height=97, background="#499bc0", bd=0, text="Recent Sales", font=normFont).place(x=630, y=310)

option = NButton(root, width=110, height=97, background="#499bc0", bd=0, text="Stock & Price", font=normFont).place(x=630, y=410)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0, text="Save Sale", font=normFont).place(x=630, y=510)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0, text="Cash Drawer", font=normFont).place(x=630, y=610)
#endregion

#region COL 3
option = NButton(root, width=110, height=97, background="#499bc0", bd=0, text="Dresses", font=normFont).place(x=745, y=10)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0).place(x=745, y=110)
img_box = Label(root, width=14, height=4, background="white")
img_box.place(x=749, y=113)
img_box.bind("<Button-1>", lambda e: print("nice"))
option_price = Label(root, text="$20.00", font=("impact", 12), background="#b7e2f3").place(x=772, y=179)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0).place(x=745, y=210)

option = NButton(root, width=110, height=97, background="#499bc0", bd=0, text="Pending Sales", font=normFont).place(x=745, y=310)

option = NButton(root, width=110, height=97, background="#499bc0", bd=0, text="Clock In/Out", font=normFont).place(x=745, y=410)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0, text="Save as Order", font=normFont).place(x=745, y=510)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0, text="Promotoins", font=normFont).place(x=745, y=610)
#endregion

#region COL 4
option = NButton(root, width=110, height=97, background="#499bc0", bd=0, text="Jeans", font=normFont).place(x=860, y=10)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0).place(x=860, y=110)
img_box = Label(root, width=14, height=4, background="white")
img_box.place(x=863, y=113)
img_box.bind("<Button-1>", lambda e: print("nice"))
option_price = Label(root, text="$15.00", font=("impact", 12), background="#b7e2f3").place(x=885, y=179)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0).place(x=860, y=210)

option = NButton(root, width=110, height=97, background="#499bc0", bd=0).place(x=860, y=310)

option = NButton(root, width=110, height=97, background="#499bc0", bd=0).place(x=860, y=410)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0).place(x=860, y=510)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0).place(x=860, y=610)
#endregion

#region COL 5
option = NButton(root, width=110, height=97, background="#499bc0", bd=0, borderwidth=0).place(x=975, y=10)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0).place(x=975, y=110)
img_box = Label(root, width=14, height=4, background="white")
img_box.place(x=978, y=113)
img_box.bind("<Button-1>", lambda e: print("nice"))
option_price = Label(root, text="$45.00", font=("impact", 12), background="#b7e2f3").place(x=1001, y=179)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0).place(x=975, y=210)

option = NButton(root, width=110, height=97, background="#499bc0", bd=0).place(x=975, y=310)

option = NButton(root, width=110, height=97, background="#499bc0", bd=0).place(x=975, y=410)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0).place(x=975, y=510)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0).place(x=975, y=610)

#endregion

#region COL 6
option = NButton(root, width=110, height=97, background="#499bc0", bd=0).place(x=1090, y=10)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0).place(x=1090, y=110)
img_box = Label(root, width=14, height=4, background="white")
img_box.place(x=1093, y=113)
img_box.bind("<Button-1>", lambda e: print("nice"))
option_price = Label(root, text="$25.00", font=("impact", 12), background="#b7e2f3").place(x=1116, y=179)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0).place(x=1090, y=210)

option = NButton(root, width=110, height=97, background="#499bc0", bd=0).place(x=1090, y=310)

option = NButton(root, width=110, height=97, background="#499bc0", bd=0).place(x=1090, y=410)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0).place(x=1090, y=510)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0).place(x=1090, y=610)
#endregion

#region COL 7
option = NButton(root, width=110, height=97, background="#499bc0", bd=0).place(x=1205, y=10)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0).place(x=1205, y=110)
img_box = Label(root, width=14, height=4, background="white")
img_box.place(x=1208, y=113)
img_box.bind("<Button-1>", lambda e: print("nice"))
option_price = Label(root, text="$30.00", font=("impact", 12), background="#b7e2f3").place(x=1232, y=179)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0).place(x=1205, y=210)

option = NButton(root, width=110, height=97, background="#499bc0", bd=0).place(x=1205, y=310)

option = NButton(root, width=110, height=97, background="#499bc0", bd=0).place(x=1205, y=410)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0).place(x=1205, y=510)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0).place(x=1205, y=610)
#endregion

#region Botton Options
people = Label(root, width=15, height=7, background="#f4c343").place(x=515, y=710)
text = Label(root, text="PEOPLE", font=("impact", 15), background="#f4c343").place(x=540, y=748)
lock = Label(root, width=15, height=7, background="#f4c343").place(x=630, y=710)
text = Label(root, text="LOCK", font=("impact", 15), background="#f4c343").place(x=661, y=748)
sale = Label(root, width=31, height=7, background="#ea5255").place(x=745, y=710)
sale = Label(root, width=30, height=7, background="#ea5255").place(x=755, y=710)
text = Label(root, text="DELETE", font=("impact", 15), background="#ea5255").place(x=830, y=748)
pay = Label(root, width=45, height=7, background="#a5c536").place(x=975, y=710)
pay = Label(root, width=45, height=7, background="#a5c536").place(x=995, y=710)
text = Label(root, text="PAY", font=("impact", 15), background="#a5c536").place(x=1125, y=748)
#endregion
#endregion

#region LEFT SIDE PLACEMENT
customer_entry.place(x=10, y=10)
product_entry.place(x=260, y=10)

name.place(x=200, y=70)
loyalty.place(x=200, y=100)

store.place(x=10, y=150)
reward.place(x=180, y=150)
visit.place(x=370, y=150)

store_points.place(x=50, y=190)
reward_points.place(x=230, y=190)
visit_points.place(x=450, y=190)
list_line1.place(x=150, y=150)
list_line2.place(x=330, y=150)

left_button.place(x=10, y=250)
right_button.place(x=260, y=250)

row1_bg.place(x=10, y=350)
list_name.place(x=30, y=355)
list_code.place(x=230, y=355)
list_qty.place(x=350, y=355)
list_price.place(x=450, y=355)

row2_bg.place(x=10, y=385)
dress.place(x=30, y=390)
row2_code.place(x=230, y=390)
row2_qty.place(x=350, y=390)
row2_price.place(x=450, y=390)

row3_bg.place(x=10, y=418)
jeans.place(x=30, y=423)
row3_code.place(x=230, y=423)
row3_qty.place(x=350, y=423)
row3_price.place(x=450, y=423)

footer_line.place(x=10, y=680)
total.place(x=40, y=710)
tax.place(x=40, y=760)
net.place(x=40, y=790)
total_price.place(x=405, y=710)
tax_price.place(x=450, y=760)
net_price.place(x=441, y=790)
#endregion

root.mainloop()
