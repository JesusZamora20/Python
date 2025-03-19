import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("data entry form")
#window.geometry("600x600")

frame = tk.Frame(window)
frame.pack()

#saving user info
user_info_frame = tk.LabelFrame(frame, text="user info")
user_info_frame.grid(row=0, column=0, padx=20, pady=20)

first_name_label = tk.Label(user_info_frame, text="first name")
first_name_label.grid(row=0, column=0)

last_name_label = tk.Label(user_info_frame, text="last name")
last_name_label.grid(row=0, column=1)

first_name_entry = tk.Entry(user_info_frame)
last_name_entry = tk.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tk.Label(user_info_frame, text="title")
title_combobox = ttk.Combobox(user_info_frame,
                              values=["", "Mr. ", "Ms. ", "Dr. "])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tk.Label(user_info_frame, text="Age")
age_spinbox = tk.Spinbox(user_info_frame, from_=18, to=100)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tk.Label(user_info_frame, text="nationality")
nationality_combobox = ttk.Combobox(
    user_info_frame, values=["", "Colombian", "Peruvian", "chinesse"])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

#changing padding
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#saving course info
courses_info_frame = tk.LabelFrame(frame, text="courses info")
courses_info_frame.grid(row=1, column=0, sticky="news", padx=20, pady=20)

registered_label = tk.Label(courses_info_frame, text="Registration Status")
registered_check = tk.Checkbutton(courses_info_frame, text="currently registered")
registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tk.Label(courses_info_frame, text="# completed courses")
numcourses_spinbox = tk.Spinbox(courses_info_frame, from_=0, to="infinity")
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

#33

tk.mainloop()