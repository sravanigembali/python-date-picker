#create date pickup using simple GUI with tkinter library
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

def select_date():
    selected_date = cal.selection_get()
    date_label.config(
        text=f"Selected Date:{selected_date:%m/%d/%y}", foreground="white",background="black")

root=tk.Tk()
root.title("Date Picker")

#cutomize the colors of the widget
root.config(background="#67e69c")
ttk.Style().configure("Tbutton",background="#FF69B4",foreground="black")

#create a calender widget
cal=Calendar(root,selectmode="day",date_pattern="mm/dd/yyyy",background="#6f67e6")

#create a label widget to display the selected date
date_label=ttk.Label(root,text="selected date:",font=("Arail",14),foreground="white")

#create a button widget to select the date
select_button=ttk.Button(root,text="seelct Date", command=select_date)

#add the widget to the window
cal.pack(padx=10,pady=10)
date_label.pack(padx=10,pady=10)
select_button.pack(padx=10,pady=10)
root.mainloop()

