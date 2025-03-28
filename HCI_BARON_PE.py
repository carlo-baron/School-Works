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
        if locked: return
        
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_option = self.listbox.get(selected_index)
            change_customer_details(selected_option)
            delete_chosen_products()
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
    if locked: return
    messagebox.showerror("Error!", "Incomplete Feature")

def change_customer_details(customer):
    global current_customer
    current_customer = customer
    name.config(text=customer)
    store_points.config(text=customers[customer]["Store"])
    reward_points.config(text=customers[customer]["Reward"])
    visit_points.config(text=customers[customer]["Visit"])

def add_product(product):
    if locked: return
    
    if product in chosen_products.keys():
        chosen_products[product]["Qty"] += 1
        chosen_products[product]["Total Price"] = products[product]["Price"] * chosen_products[product]["Qty"]
    else:
        chosen_products[product] = {"Qty" : 1, "Total Price" : products[product]["Price"]}
    
    reflect_chosen_products()

def reflect_chosen_products():
    diff = 33
    for i, chosen_product in enumerate(chosen_products.keys()):
        bg = "#ffffff" if i % 2 == 0 else "#999999" 
        tab_bg = Label(root, width=70, height=2, background=bg)
        cloth_name = Label(root, text=chosen_product, font=("arial"), background=bg)
        code = Label(root, text=products[chosen_product]["Code"], font=("arial"), background=bg)
        qty = Label(root, text=chosen_products[chosen_product]["Qty"], font=("arial"), background=bg)
        price = Label(root, text=chosen_products[chosen_product]["Total Price"], font=("arial"), background=bg)
        
        if i < 1:
            tab_bg.place(x=10, y=385)
            cloth_name.place(x=30, y=390)
            code.place(x=230, y=390)
            qty.place(x=350, y=390)
            price.place(x=450, y=390)
        else:
            tab_bg.place(x=10, y=385 + (diff * i))
            cloth_name.place(x=30, y=390 + (diff * i))
            code.place(x=230, y=390 + (diff * i))
            qty.place(x=350, y=390 + (diff * i))
            price.place(x=450, y=390 + (diff * i))
            
        tabs.append(tab_bg)
        tabs.append(cloth_name)
        tabs.append(code)
        tabs.append(qty)
        tabs.append(price)
    
    if len(chosen_products.keys()) <= 0:
        for widget in tabs:
            widget.place_forget()
            
    update_footer()
            
def update_footer():
    total_price_sum = float(sum(chosen_products[product]["Total Price"] for product in chosen_products))
    calculated_net = float(total_price_sum / (1 + TAX))
    calculated_tax = float(total_price_sum - calculated_net)
    
    total_price.config(text=f"${total_price_sum:.2f}")
    tax_price.config(text=f"{calculated_tax:.2f}")
    net_price.config(text=f"{calculated_net:.2f}")
    
def pay():
    if locked: return
    if len(tabs) < 1: return
    
    added_reward = sum(chosen_products[product]["Qty"] for product in chosen_products) * 50
    customers[current_customer]["Reward"] += added_reward
    customers[current_customer]["Visit"] += 1
    delete_chosen_products()
    change_customer_details(current_customer)
    messagebox.showinfo("Success!", "Payment completed")
    
def highlight_product(product_list : list):
    if locked: return
    
    global highlight
    if highlight:
        clear_highlight()
        highlight = False
    elif not highlight:
        highlight = True
        clear_highlight()
        for product in product_list:
            product.config(bg="#8ab3cf")
        
def clear_highlight():
    for i, product in enumerate(shirts):
        if i < 1:
            product.config(bg="#499bc0")
        else:
            product.config(bg="#b7e2f3")
    for i, product in enumerate(dresses):
        if i < 1:
            product.config(bg="#499bc0")
        else:
            product.config(bg="#b7e2f3")
    for i, product in enumerate(jeans):
            if i < 1:
                product.config(bg="#499bc0")
            else:
                product.config(bg="#b7e2f3")
            
def delete_chosen_products():
    if locked: return
    
    chosen_products.clear()
    for i in range(0,1):
        reflect_chosen_products()
        
def change_lock_state():
    global locked
    if locked:
        locked = False
        lock.config(bg="#f4c343")
    else:
        locked = True
        lock.config(bg="#b17829")
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
current_customer = list(customers.keys())[0]
tabs = []
TAX = 0.1
REWARD_PER_UNIT = 50
locked = False
shirts = []
dresses = []
jeans = []
highlight = False
#endregion

#region LEFT SIDE
options = customers.keys()
box = SearchableComboBox(options)


product_entry = Entry(root, width=26, font=("impact"))

name = Label(root, text=f"{current_customer}", font=("impact", 20))
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

footer_line = Label(root, background="#c6c6c6", font=("arial", 1), width=490)
total = Label(root, text="TOTAL", font=("impact", 20))
tax = Label(root, text="TAX", font=("Arial", 12))
net = Label(root, text="NET", font=("Arial", 12))
total_price = Label(root, text="$0.00", font=("impact", 20))
tax_price = Label(root, text="0.00", font=("Arial", 12))
net_price = Label(root, text="0.00", font=("Arial", 12))
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
jeans.append(option)
jeans.append(option_price)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0).place(x=515, y=210)

option = NButton(root, width=110, height=97, background="#499bc0", bd=0, text="+", font=bigFont, command=incomplete_feature).place(x=515, y=310)

option = NButton(root, width=110, height=97, background="#499bc0", bd=0, text="Cash In/Out", font=normFont, command=incomplete_feature).place(x=515, y=410)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0, text="New Sale", font=normFont, command=incomplete_feature).place(x=515, y=510)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0, text="Last Receipt", font=normFont, command=incomplete_feature).place(x=515, y=610)
#endregion

#region COL 2
option = NButton(root, width=110, height=97, background="#499bc0", bd=0, text="Shirts", font=normFont, command=lambda: highlight_product(shirts))
option.place(x=630, y=10)
shirts.insert(0, option)

option = Frame(root, width=110, height=97, background="#b7e2f3", bd=0)
option.place(x=630, y=110)
option.bind("<Button-1>", lambda e:add_product("Red max-dress"))
img_box = Label(root, width=14, height=4, background="white")
img_box.place(x=633, y=113)
img_box.bind("<Button-1>", lambda e:add_product("Red max-dress"))
option_price = Label(root, text="$50.00", font=("impact", 12), background="#b7e2f3")
option_price.place(x=656, y=179)
option_price.bind("<Button-1>", lambda e:add_product("Red max-dresws"))
dresses.append(option)
dresses.append(option_price)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0).place(x=630, y=210)

option = NButton(root, width=110, height=97, background="#499bc0", bd=0, text="Recent Sales", font=normFont, command=incomplete_feature).place(x=630, y=310)

option = NButton(root, width=110, height=97, background="#499bc0", bd=0, text="Stock & Price", font=normFont, command=incomplete_feature).place(x=630, y=410)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0, text="Save Sale", font=normFont, command=incomplete_feature).place(x=630, y=510)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0, text="Cash Drawer", font=normFont, command=lambda: locked or messagebox.showinfo("Success!", "Cash Drawer Opened")).place(x=630, y=610)
#endregion

#region COL 3
option = NButton(root, width=110, height=97, background="#499bc0", bd=0, text="Dresses", font=normFont, command=lambda: highlight_product(dresses))
option.place(x=745, y=10)
dresses.insert(0, option)

option = Frame(root, width=110, height=97, background="#b7e2f3", bd=0)
option.place(x=745, y=110)
option.bind("<Button-1>", lambda e:add_product("Gray shirt"))
img_box = Label(root, width=14, height=4, background="white")
img_box.place(x=749, y=113)
img_box.bind("<Button-1>", lambda e:add_product("Gray shirt"))
option_price = Label(root, text="$20.00", font=("impact", 12), background="#b7e2f3")
option_price.place(x=772, y=179)
option_price.bind("<Button-1>", lambda e:add_product("Gray shirt"))
shirts.append(option)
shirts.append(option_price)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0).place(x=745, y=210)

option = NButton(root, width=110, height=97, background="#499bc0", bd=0, text="Pending Sales", font=normFont, command=incomplete_feature).place(x=745, y=310)

option = NButton(root, width=110, height=97, background="#499bc0", bd=0, text="Clock In/Out", font=normFont, command=incomplete_feature).place(x=745, y=410)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0, text="Save as Order", font=normFont, command=incomplete_feature).place(x=745, y=510)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0, text="Promotions", font=normFont, command=incomplete_feature).place(x=745, y=610)
#endregion

#region COL 4
option = NButton(root, width=110, height=97, background="#499bc0", bd=0, text="Jeans", font=normFont, command=lambda: highlight_product(jeans))
option.place(x=860, y=10)
jeans.insert(0, option)

option = Frame(root, width=110, height=97, background="#b7e2f3", bd=0)
option.place(x=860, y=110)
option.bind("<Button-1>", lambda e:add_product("Yellow shirt"))
img_box = Label(root, width=14, height=4, background="white")
img_box.place(x=863, y=113)
img_box.bind("<Button-1>", lambda e:add_product("Yellow shirt"))
option_price = Label(root, text="$15.00", font=("impact", 12), background="#b7e2f3")
option_price.place(x=885, y=179)
option_price.bind("<Button-1>", lambda e:add_product("Yellow shirt"))
shirts.append(option)
shirts.append(option_price)

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
dresses.append(option)
dresses.append(option_price)

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
jeans.append(option)
jeans.append(option_price)

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
jeans.append(option)
jeans.append(option_price)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0).place(x=1205, y=210)

option = NButton(root, width=110, height=97, background="#499bc0", bd=0, text="X-Report", font=normFont, command=incomplete_feature).place(x=1205, y=310)

option = NButton(root, width=110, height=97, background="#499bc0", bd=0).place(x=1205, y=410)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0, text="Notes", font=normFont, command=incomplete_feature).place(x=1205, y=510)

option = NButton(root, width=110, height=97, background="#b7e2f3", bd=0).place(x=1205, y=610)
#endregion

#region Botton Options
botFont = ("impact", 18)

people = NButton(root, width=110, height=111, background="#f4c343", bd=0, text="PEOPLE", font=botFont, command=incomplete_feature).place(x=515, y=710)
lock = NButton(root, width=110, height=111, background="#f4c343", bd=0, text="LOCK", font=botFont, command=change_lock_state)
lock.place(x=630, y=710)
delete = NButton(root, width=225, height=111, background="#ea5255", bd=0, text="DELETE", font=botFont, command=delete_chosen_products).place(x=745, y=710)
pay = NButton(root, width=340, height=111, background="#a5c536", bd=0, text="PAY", font=botFont, command=pay).place(x=975, y=710)
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