import sqlite3
from sqlite3 import Error

conn = sqlite3.connect("epood_fkruusimae.db")
cursor = conn.execute("SELECT * FROM epood_fkruusimae")


import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *

my_w = ttk.Window()
my_w.geometry("800x800")  # width and height
colors = my_w.style.colors
l1 = [
    {"text": "id", "stretch": False},
    {"text":"Fname","stretch":True},
    "Lname",
    {"text":"Email"},
    {"text":"Mark"},
    {"text":"Mudel"},
    {"text":"Aasta"},
    {"text":"Hind"}
    
]  # Columns with Names and style 
# Data rows as list 
r_set = []

for i in cursor:
    print (i)
    r_set.append(i)



dv = ttk.tableview.Tableview(
    master=my_w,
    paginated=True,
    coldata=l1,
    rowdata=r_set,
    searchable=True,
    bootstyle=SUCCESS,
    pagesize=10,
    height=10,
    stripecolor=(colors.light, None),
)
dv.grid(row=0, column=0, padx=10, pady=5)
dv.autofit_columns() # Fit in current view 
dv.load_table_data() # Load all data rows 
def lisa_andmed():
    # Lisame uued andmed andmebaasi
    cursor.execute("INSERT INTO epood_fkruusimae (first_name, last_name, email, car_make, car_model, car_year, car_price) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (fname_entry.get(), lname_entry.get(), email_entry.get(), mark_entry.get(), mudel_entry.get(), aasta_entry.get(), hind_entry.get()))
    conn.commit()
    # lae_andmed()

# Andmeseadete raamistik
raamistik = ttk.Frame(my_w)
raamistik.grid(row=1, column=0, padx=10, pady=5)

# Andmeväljad
fname_label = ttk.Label(raamistik, text="Eesnimi:")
fname_label.grid(row=0, column=0, padx=5, pady=5)
fname_entry = ttk.Entry(raamistik)
fname_entry.grid(row=0, column=1, padx=5, pady=5)

lname_label = ttk.Label(raamistik, text="Perenimi:")
lname_label.grid(row=1, column=0, padx=5, pady=5)
lname_entry = ttk.Entry(raamistik)
lname_entry.grid(row=1, column=1, padx=5, pady=5)

email_label = ttk.Label(raamistik, text="Email:")
email_label.grid(row=2, column=0, padx=5, pady=5)
email_entry = ttk.Entry(raamistik)
email_entry.grid(row=2, column=1, padx=5, pady=5)

mark_label = ttk.Label(raamistik, text="Mark:")
mark_label.grid(row=3, column=0, padx=5, pady=5)
mark_entry = ttk.Entry(raamistik)
mark_entry.grid(row=3, column=1, padx=5, pady=5)

mudel_label = ttk.Label(raamistik, text="Mudel:")
mudel_label.grid(row=4, column=0, padx=5, pady=5)
mudel_entry = ttk.Entry(raamistik)
mudel_entry.grid(row=4, column=1, padx=5, pady=5)

aasta_label = ttk.Label(raamistik, text="Aasta:")
aasta_label.grid(row=5, column=0, padx=5, pady=5)
aasta_entry = ttk.Entry(raamistik)
aasta_entry.grid(row=5, column=1, padx=5, pady=5)

hind_label = ttk.Label(raamistik, text="Hind:")
hind_label.grid(row=6, column=0, padx=5, pady=5)
hind_entry = ttk.Entry(raamistik)
hind_entry.grid(row=6, column=1, padx=5, pady=5)

# Nupp uue rea lisamiseks
lisa_nupp = ttk.Button(raamistik, text="Lisa", command=lisa_andmed)
lisa_nupp.grid(row=7, columnspan=2, padx=5, pady=5)

def lae_andmed():
    cursor.execute("SELECT * FROM epood_fkruusimae")
    r_set = cursor.fetchall()
    dv.load_table_data(rowdata=r_set)


my_w.mainloop()