import tkinter as tk
from tkinter import messagebox, ttk
import openpyxl
import os
def save_data():

   name = name_entry.get()
   email = email_entry.get()
   mobile = mobile_entry.get()
   address = address_entry.get("1.0", tk.END).strip()
   roll = roll_entry.get()
   stream = stream_combo.get()
   terms = terms_var.get()

   if not (name and email and mobile and address and roll and stream):
       messagebox.showerror("Error", "Please fill all fields!")
       return
   if "@" not in email:
       messagebox.showerror("Error", "Invalid Email!")
       return
   if len(mobile) != 10 or not mobile.isdigit():
       messagebox.showerror("Error", "Mobile must be 10 digits!")
       return
   if terms == 0:
       messagebox.showerror("Error", "Please agree to Terms!")
       return

   file_path = "students.xlsx"

   if not os.path.exists(file_path):
       wb = openpyxl.Workbook()
       sheet = wb.active
       sheet.append(["Name", "Email", "Mobile", "Address", "Roll", "Stream"])
       wb.save(file_path)

   wb = openpyxl.load_workbook(file_path)
   sheet = wb.active
   sheet.append([name, email, mobile, address, roll, stream])
   wb.save(file_path)

   messagebox.showinfo("Success", "Data Saved Successfully!")
   clear_fields()

def clear_fields():
   name_entry.delete(0, tk.END)
   email_entry.delete(0, tk.END)
   mobile_entry.delete(0, tk.END)
   roll_entry.delete(0, tk.END)
   address_entry.delete("1.0", tk.END)
   stream_combo.set("")
   terms_var.set(0)

root = tk.Tk()
root.title("Student Form")
root.geometry("400x550")
tk.Label(root, text="Full Name").pack(pady=2)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

tk.Label(root, text="Email ID").pack(pady=2)
email_entry = tk.Entry(root)
email_entry.pack(pady=5)

tk.Label(root, text="Mobile Number").pack(pady=2)
mobile_entry = tk.Entry(root)
mobile_entry.pack(pady=5)

tk.Label(root, text="Roll Number").pack(pady=2)
roll_entry = tk.Entry(root)
roll_entry.pack(pady=5)

tk.Label(root, text="Address").pack(pady=2)
address_entry = tk.Text(root, height=3, width=20)
address_entry.pack(pady=5)

tk.Label(root, text="Stream").pack(pady=2)
stream_combo = ttk.Combobox(root, values=["BCA", "BSc", "BTech", "MCA"])
stream_combo.pack(pady=5)

terms_var = tk.IntVar()
tk.Checkbutton(root, text="I agree to Terms & Conditions", variable=terms_var).pack(pady=10)

tk.Button(root, text="Submit", command=save_data, bg="green", fg="white").pack(pady=5)
tk.Button(root, text="Clear", command=clear_fields).pack(pady=5)

root.mainloop()