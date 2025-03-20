import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def enter_data():

    accepted = acceptance.get()

    if accepted == "Accepted":
        #user info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()

        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()

            #courses info
            registration_status = reg_status_var.get()
            numcourses = numcourses_spinbox.get()
            numsemesters = numsemesters_spinbox.get()
            print(f"user first name: {firstname}, user last name: {lastname}")
            print(f"Title: {title}, age is {age}, the nationality is {nationality} ")
            print(f"number of courses: {numcourses}, number of semesters: {numsemesters}")
            print(f"registration status: {registration_status}")
            print("--------------------------------------------------")
        else: tk.messagebox.showwarning(title="Warning" , message="First name and last name are required" )
    else: tk.messagebox.showwarning(title="Warning" , message="Please Accept Terms and conditions" )

window = tk.Tk()
window.title("data entry form")
#window.geometry("600x600")

frame = tk.Frame(window)
frame.pack()

#saving user info
user_info_frame = tk.LabelFrame(frame, text="user info")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

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
courses_info_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tk.Label(courses_info_frame, text="Registration Status")

reg_status_var = tk.StringVar(value="Not registered")
registered_check = tk.Checkbutton(courses_info_frame, text="currently registered",
                                variable=reg_status_var,
                                onvalue="Registered", 
                                offvalue="Not registered")

registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tk.Label(courses_info_frame, text="# completed courses")
numcourses_spinbox = tk.Spinbox(courses_info_frame, from_=0, to="infinity")
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tk.Label(courses_info_frame, text="# semesters")
numsemesters_spinbox = tk.Spinbox(courses_info_frame, from_=0, to="infinity")
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)

for widget in courses_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Accept terms
terms_frame = tk.LabelFrame(frame, text="terms and conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

acceptance = tk.StringVar(value="Not accepted")
terms_check = tk.Checkbutton(terms_frame, text="I accept the terms and conditions",
                                variable=acceptance,
                                onvalue="Accepted", 
                                offvalue="Not Accepted")
terms_check.grid(row=0, column=0)


#BUtton
button = tk.Button(frame, text="enter data", command=enter_data)
button.grid(row=3, column=0, padx=10, pady=10)



tk.mainloop()