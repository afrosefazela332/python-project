import tkinter
from tkinter import messagebox,ttk
root=tkinter.Tk()
def OnClick_Submit():
    name=name_textbox.get()
    gender=gender_textbox.get()
    age=age_textbox.get()
    contact=contact_textbox.get()
    branch=branch_dropdown.get()
    
    if name and gender and age and contact and branch:
        messagebox.showinfo("Status","Data Submitted")
    else:
        messagebox.showwarning("Warning","Please Fill all the Fields")

    
root.geometry("300x300")
root.configure(bg="#CDF0FF")

root.title("Patient Form")
name_label=tkinter.Label(root,text="Enter Name")
name_label.pack(anchor=tkinter.W,padx=10)
name_textbox=tkinter.Entry(root)
name_textbox.pack(anchor=tkinter.W,padx=50)

gender_label=tkinter.Label(root,text="Gender")
gender_label.pack(anchor=tkinter.W,padx=10)
gender_textbox=tkinter.Entry(root)
gender_textbox.pack(anchor=tkinter.W,padx=50)

age_label=tkinter.Label(root,text="Age")
age_label.pack(anchor=tkinter.W,padx=10)
age_textbox=tkinter.Entry(root)
age_textbox.pack(anchor=tkinter.W,padx=50)

contact_label=tkinter.Label(root,text="Contact")
contact_label.pack(anchor=tkinter.W,padx=10)
contact_textbox=tkinter.Entry(root)
contact_textbox.pack(anchor=tkinter.W,padx=50)

choices=["Diabetes","Blood Pressure","Thyroid"]
branch_label=tkinter.Label(root,text="Select")
branch_label.pack(anchor=tkinter.W,padx=10)
branch_dropdown=ttk.Combobox(root,values=choices)
branch_dropdown.pack(anchor=tkinter.W,padx=50)

submit_button=tkinter.Button(root,text="Submit",command=OnClick_Submit)
submit_button.pack(anchor=tkinter.W,pady=10)
root.mainloop()
