from tkinter import *
from tkinter import messagebox

#region IMPORTED CLASSES
class NButton(Frame):
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master)
        self.rowconfigure(0, minsize=kwargs.pop('height', None))
        self.columnconfigure(0, minsize=kwargs.pop('width', None))
        self.btn = Button(self, **kwargs)
        self.btn.grid(row=0, column=0, sticky="nsew")
        self.config = self.btn.config

class SearchableComboBox():
    def __init__(self, options) -> None:
        self.dropdown_id = None
        self.options = options

        wrapper = Frame(root)
        wrapper.place(x=10,y=10)

        self.entry = Entry(wrapper, width=26, font=("impact"))
        self.entry.bind("<KeyRelease>", self.on_entry_key)
        self.entry.bind("<FocusIn>", self.show_dropdown) 
        self.entry.pack(side=LEFT)

        self.listbox = Listbox(root, height=5, width=30)
        self.listbox.bind("<<ListboxSelect>>", self.on_select)
        for option in self.options:
            self.listbox.insert(END, option)

    def on_entry_key(self, event):
        typed_value = event.widget.get().strip().lower()
        if not typed_value:
            self.listbox.delete(0, END)
            for option in self.options:
                self.listbox.insert(END, option)
        else:
            self.listbox.delete(0, END)
            filtered_options = [option for option in self.options if option.lower().startswith(typed_value)]
            for option in filtered_options:
                self.listbox.insert(END, option)
        self.show_dropdown()

    def on_select(self, event):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_option = self.listbox.get(selected_index)
            change_customer_details(selected_option)
            self.entry.delete(0, END)
            self.entry.insert(0, selected_option)

    def show_dropdown(self, event=None):
        self.listbox.place(in_=self.entry, x=0, rely=1, relwidth=1.0, anchor="nw")
        self.listbox.lift()

        if self.dropdown_id:
            self.listbox.after_cancel(self.dropdown_id)
        self.dropdown_id = self.listbox.after(2000, self.hide_dropdown)

    def hide_dropdown(self):
        self.listbox.place_forget()
#endregion

#region FUNCTIONS
def incomplete_feature():
    messagebox.showerror("Error!", "Incomplete Feature")

def change_customer_details(customer):
    name.config(text=customer)
    store_points.config(text=customers[customer]["Store"])
    reward_points.config(text=customers[customer]["Reward"])
    visit_points.config(text=customers[customer]["Visit"])

def add_product(product):
    if product in chosen_products.keys():
        chosen_products[product]["Qty"] += 1
    else:
        chosen_products[product] = {"Qty" : 1}
    
    print(chosen_products.items())
#endregion

#region APP
root = Tk()
root.title("POS System")
root.geometry("1325x1080")

#region VALUES
customers = {
    "Jane Doe" : {"Store" : 0, "Reward" : 4200, "Visit" : 19},
    "John Smith" : {"Store" : 1, "Reward" : 3200, "Visit" : 15},
    "Alice Johnson" : {"Store" : 2, "Reward" : 5600, "Visit" : 22},
    "Bob Brown" : {"Store" : 1, "Reward" : 2000, "Visit" : 10},
    "Mary Davis" : {"Store" : 3, "Reward" : 8000, "Visit" : 30},
    "James Wilson" : {"Store" : 0, "Reward" : 1500, "Visit" : 5},
}

products = {
    "Classic blue jeans" : {"Price" : 35, "Code" : "0013"},
    "Red max-dress" : {"Price" : 50, "Code" : "101"},
    "Gray shirt" : {"Price" : 20, "Code" : "206"},
    "Yellow shirt" : {"Price" : 15, "Code" : "305"},
    "Beige dress" : {"Price" : 45, "Code" : "1030"},
    "White jeans" : {"Price" : 25, "Code" : "030"},
    "Black jeans" : {"Price" : 30, "Code" : "225"}
}

chosen_products = dict()

initial_customer = list(customers.keys())[0]
#endregion

#region LEFT SIDE
options = customers.keys()
box = SearchableComboBox(options)


product_entry = Entry(root, width=26, font=("impact"))

name = Label(root, text=f"{initial_customer}", font=("impact", 20))
loyalty = Label(root, text="Loyalty program", font=("Arial", 8))

store = Label(root, text="STORE", font=("impact", 10), fg="#808080")
reward = Label(root, text="REWARD", font=("impact", 10), fg="#808080")
visit = Label(root, text="VISIT", font=("impact", 10), fg="#808080")

store_points = Label(root, text="0.00", font=("impact", 20))
reward_points = Label(root, text="4200", font=("impact", 20))
visit_points = Label(root, text="19", font=("impact", 20))

left_button = Button(root, width=29, background="yellow", text="ID", font=("impact", 12), command=incomplete_feature)
right_button = Button(root, width=29, background="#b7e2f3", text="PURCHASES", font=("impact"), command=incomplete_feature)

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
option = NButton(root, text="+",width=110, height=97, background="#a5c536", bd=0, font=bigFont, command=incomplete_feature).place(x=515, y=10)

option = Frame(root, width=110, height=97, background="#b7e2f3", bd=0)
option.place(x=515, y=110)
option.bind("<Button-1>", lambda e:add_product("Classic blue jeans"))
img_box = Label(root, width=14, height=4, background="white")
img_box.place(x=518, y=113)
img_box.bind("<Button-1>", lambda e:add_product("Classic blue jeans"))
option_price = Label(root, text="$35.00", font=("impact", 12), background="#b7e2f3")
option_price.place(x=541, y=179)
option_price.bind("<Button-1>", lambda e:add_product("Classic blue jeans"))

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0).place(x=515, y=210)

option = NButton(root, width=110, height=97, background="#499bc0", bd=0, text="+", font=bigFont, command=incomplete_feature).place(x=515, y=310)

option = NButton(root, width=110, height=97, background="#499bc0", bd=0, text="Cash In/Out", font=normFont, command=incomplete_feature).place(x=515, y=410)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0, text="New Sale", font=normFont, command=incomplete_feature).place(x=515, y=510)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0, text="Last Receipt", font=normFont, command=incomplete_feature).place(x=515, y=610)
#endregion

#region COL 2
option = NButton(root, width=110, height=97, background="#499bc0", bd=0, text="Shirts", font=normFont).place(x=630, y=10)

option = Frame(root, width=110, height=97, background="#b7e2f3", bd=0)
option.place(x=630, y=110)
option.bind("<Button-1>", lambda e:add_product("Red max-dress"))
img_box = Label(root, width=14, height=4, background="white")
img_box.place(x=633, y=113)
img_box.bind("<Button-1>", lambda e:add_product("Red max-dress"))
option_price = Label(root, text="$50.00", font=("impact", 12), background="#b7e2f3")
option_price.place(x=656, y=179)
option_price.bind("<Button-1>", lambda e:add_product("Red max-dress"))

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0).place(x=630, y=210)

option = NButton(root, width=110, height=97, background="#499bc0", bd=0, text="Recent Sales", font=normFont, command=incomplete_feature).place(x=630, y=310)

option = NButton(root, width=110, height=97, background="#499bc0", bd=0, text="Stock & Price", font=normFont, command=incomplete_feature).place(x=630, y=410)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0, text="Save Sale", font=normFont, command=incomplete_feature).place(x=630, y=510)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0, text="Cash Drawer", font=normFont, command=lambda: messagebox.showinfo("Success!", "Cash Drawer Opened")).place(x=630, y=610)
#endregion

#region COL 3
option = NButton(root, width=110, height=97, background="#499bc0", bd=0, text="Dresses", font=normFont).place(x=745, y=10)

option = Frame(root, width=110, height=97, background="#b7e2f3", bd=0)
option.place(x=745, y=110)
option.bind("<Button-1>", lambda e:add_product("Gray shirt"))
img_box = Label(root, width=14, height=4, background="white")
img_box.place(x=749, y=113)
img_box.bind("<Button-1>", lambda e:add_product("Gray shirt"))
option_price = Label(root, text="$20.00", font=("impact", 12), background="#b7e2f3")
option_price.place(x=772, y=179)
option_price.bind("<Button-1>", lambda e:add_product("Gray shirt"))

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0).place(x=745, y=210)

option = NButton(root, width=110, height=97, background="#499bc0", bd=0, text="Pending Sales", font=normFont, command=incomplete_feature).place(x=745, y=310)

option = NButton(root, width=110, height=97, background="#499bc0", bd=0, text="Clock In/Out", font=normFont, command=incomplete_feature).place(x=745, y=410)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0, text="Save as Order", font=normFont, command=incomplete_feature).place(x=745, y=510)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0, text="Promotions", font=normFont, command=incomplete_feature).place(x=745, y=610)
#endregion

#region COL 4
option = NButton(root, width=110, height=97, background="#499bc0", bd=0, text="Jeans", font=normFont).place(x=860, y=10)

option = Frame(root, width=110, height=97, background="#b7e2f3", bd=0)
option.place(x=860, y=110)
option.bind("<Button-1>", lambda e:add_product("Yellow shirt"))
img_box = Label(root, width=14, height=4, background="white")
img_box.place(x=863, y=113)
img_box.bind("<Button-1>", lambda e:add_product("Yellow shirt"))
option_price = Label(root, text="$15.00", font=("impact", 12), background="#b7e2f3")
option_price.place(x=885, y=179)
option_price.bind("<Button-1>", lambda e:add_product("Yellow shirt"))

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0).place(x=860, y=210)

option = NButton(root, width=110, height=97, background="#499bc0", bd=0, text="Pickup Orders", font=normFont, command=incomplete_feature).place(x=860, y=310)

option = NButton(root, width=110, height=97, background="#499bc0", bd=0, text="Check Gift Card Balance", font=normFont, wraplength=110, command=incomplete_feature).place(x=860, y=410)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0, text="Save as Layaway", font=normFont, wraplength=110, command=incomplete_feature).place(x=860, y=510)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0, text="Coupons", font=normFont, command=incomplete_feature).place(x=860, y=610)
#endregion

#region COL 5
option = NButton(root, width=110, height=97, background="#499bc0", bd=0, borderwidth=0).place(x=975, y=10)

option = Frame(root, width=110, height=97, background="#b7e2f3", bd=0)
option.place(x=975, y=110)
option.bind("<Button-1>", lambda e:add_product("Beige dress"))
img_box = Label(root, width=14, height=4, background="white")
img_box.place(x=978, y=113)
img_box.bind("<Button-1>", lambda e:add_product("Beige dress"))
option_price = Label(root, text="$45.00", font=("impact", 12), background="#b7e2f3")
option_price.place(x=1001, y=179)
option_price.bind("<Button-1>", lambda e:add_product("Beige dress"))

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0).place(x=975, y=210)

option = NButton(root, width=110, height=97, background="#499bc0", bd=0, text="Layaways", font=normFont, command=incomplete_feature).place(x=975, y=310)

option = NButton(root, width=110, height=97, background="#499bc0", bd=0, text="Available Coupons", font=normFont, wraplength=110, command=incomplete_feature).place(x=975, y=410)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0, text="Discount", font=normFont, command=incomplete_feature).place(x=975, y=510)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0, text="Receipt", font=normFont, command=lambda: messagebox.showinfo("Success!", "Receipt Printed")).place(x=975, y=610)

#endregion

#region COL 6
option = NButton(root, width=110, height=97, background="#499bc0", bd=0).place(x=1090, y=10)

option = Frame(root, width=110, height=97, background="#b7e2f3", bd=0)
option.place(x=1090, y=110)
option.bind("<Button-1>", lambda e:add_product("White jeans"))
img_box = Label(root, width=14, height=4, background="white")
img_box.place(x=1093, y=113)
img_box.bind("<Button-1>", lambda e:add_product("White jeans"))
option_price = Label(root, text="$25.00", font=("impact", 12), background="#b7e2f3")
option_price.place(x=1116, y=179)
option_price.bind("<Button-1>", lambda e:add_product("White jeans"))

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0).place(x=1090, y=210)

option = NButton(root, width=110, height=97, background="#499bc0", bd=0, text="Close Day", font=normFont, command=incomplete_feature).place(x=1090, y=310)

option = NButton(root, width=110, height=97, background="#499bc0", bd=0).place(x=1090, y=410)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0, text="Tax Exempt", font=normFont, command=incomplete_feature).place(x=1090, y=510)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0, text="Add Shipping", font=normFont, command=incomplete_feature).place(x=1090, y=610)
#endregion

#region COL 7
option = NButton(root, width=110, height=97, background="#499bc0", bd=0).place(x=1205, y=10)

option = Frame(root, width=110, height=97, background="#b7e2f3", bd=0)
option.place(x=1205, y=110)
option.bind("<Button-1>", lambda e:add_product("Black jeans"))
img_box = Label(root, width=14, height=4, background="white")
img_box.place(x=1208, y=113)
img_box.bind("<Button-1>", lambda e:add_product("Black jeans"))
option_price = Label(root, text="$30.00", font=("impact", 12), background="#b7e2f3")
option_price.place(x=1231, y=179)
option_price.bind("<Button-1>", lambda e:add_product("Black jeans"))

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0).place(x=1205, y=210)

option = NButton(root, width=110, height=97, background="#499bc0", bd=0, text="X-Report", font=normFont, command=incomplete_feature).place(x=1205, y=310)

option = NButton(root, width=110, height=97, background="#499bc0", bd=0).place(x=1205, y=410)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0, text="Notes", font=normFont, command=incomplete_feature).place(x=1205, y=510)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0).place(x=1205, y=610)
#endregion

#region Botton Options
botFont = ("impact", 18)

people = NButton(root, width=110, height=111, background="#f4c343", bd=0, text="PEOPLE", font=botFont, command=incomplete_feature).place(x=515, y=710)
lock = NButton(root, width=110, height=111, background="#f4c343", bd=0, text="LOCK", font=botFont).place(x=630, y=710)
delete = NButton(root, width=225, height=111, background="#ea5255", bd=0, text="DELETE", font=botFont).place(x=745, y=710)
pay = NButton(root, width=340, height=111, background="#a5c536", bd=0, text="PAY", font=botFont).place(x=975, y=710)
#endregion
#endregion

#region LEFT SIDE PLACEMENT

product_entry.place(x=260, y=10)
product_entry.bind("<Return>", lambda e: incomplete_feature())

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
#endregion