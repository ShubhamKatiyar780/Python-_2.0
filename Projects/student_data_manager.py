import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import mysql.connector as mysql
import pandas as pd
import matplotlib.pyplot as plt

database = mysql.connect(
    host='127.0.0.1',
    user='root',
    passwd=''
)
cursorObject = database.cursor()
cursorObject.execute("CREATE DATABASE IF NOT EXISTS StudentsRegistrationDetails")
cursorObject.execute("USE StudentsRegistrationDetails")

cursorObject.execute("""
CREATE TABLE IF NOT EXISTS Students (
    User INT AUTO_INCREMENT PRIMARY KEY,
    UserName VARCHAR(100) NOT NULL,
    DateOfBirth DATE NOT NULL,
    AadharNumber VARCHAR(12) NOT NULL,
    EmailId VARCHAR(100) NOT NULL,
    MobileNumber VARCHAR(15) NOT NULL,
    Password VARCHAR(100) NOT NULL,
    Branch TEXT NOT NULL,
    TermsCondition INT NOT NULL
)
""")
database.close()
print("Database and table created successfully!")

root = tk.Tk()
root.geometry("500x700")
root.configure(bg="Aqua")
root.title("Student Registration Form")

navbar = tk.Frame(root, bg="purple", height=50)
navbar.pack(fill=tk.X)

signup_frame = tk.Frame(root, bg="aqua")
signup_frame.pack(fill="both")
tk.Label(signup_frame, text="SIGNUP FORM FOR MY DATA MY STORY", font=("Arial", 20, "bold"), bg="aqua", fg="red").pack(pady=30)

def submit_form():
    name_value = name.get()
    dob_value = dob.get()
    aadhar_value = aadhar.get()
    email_value = email.get()
    phone_value = phone.get()
    branch_value = branch.get()
    agree_value = agree_or_disagree.get()
    password_value = password.get()

    if name_value and dob_value and aadhar_value and email_value and phone_value and password_value and branch_value and agree_value:
        try:
            dob_value = datetime.strptime(dob_value, "%d/%m/%Y").strftime("%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Date of Birth must be in DD/MM/YYYY format")
            return

        try:
            database = mysql.connect(
                host='127.0.0.1',
                user='root',
                passwd='',
                database='StudentsRegistrationDetails'
            )
            cursorObject = database.cursor()
            cursorObject.execute("SELECT * FROM Students WHERE AadharNumber = %s OR EmailId = %s", (aadhar_value, email_value))
            existing_record = cursorObject.fetchone()

            if existing_record:
                messagebox.showwarning("Warning", "Aadhar Number or Email ID already registered. Please change it.")
            else:
                sql = "INSERT INTO Students (UserName, DateOfBirth, AadharNumber, EmailId, MobileNumber, Password, Branch, TermsCondition) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                values = (name_value, dob_value, aadhar_value, email_value, phone_value, password_value, branch_value, agree_value)
                cursorObject.execute(sql, values)
                database.commit()
                messagebox.showinfo("Success", "Registration successful!")
            database.close()
        except mysql.Error as e:
            messagebox.showerror("Error", f"Error: {e}")
    else:
        messagebox.showwarning("Warning", "Please fill all the fields")

def update_form():
    def validate_update_details():
        email_value = email_entry.get()
        aadhar_value = aadhar_entry.get()
        dob_value = dob_entry.get()
        password_value = password_entry.get()

        if email_value and aadhar_value and dob_value and password_value:
            try:
                dob_value = datetime.strptime(dob_value, "%d/%m/%Y").strftime("%Y-%m-%d")
            except ValueError:
                messagebox.showerror("Error", "Date of Birth must be in DD/MM/YYYY format")
                return
            try:
                database = mysql.connect(
                    host='127.0.0.1',
                    user='root',
                    passwd='',
                    database='StudentsRegistrationDetails'
                )
                cursorObject = database.cursor()
                sql = "SELECT * FROM Students WHERE EmailId=%s AND AadharNumber=%s AND DateOfBirth=%s AND Password=%s"
                values = (email_value, aadhar_value, dob_value, password_value)
                cursorObject.execute(sql, values)
                result = cursorObject.fetchone()
                if result:
                    messagebox.showinfo("Success", "User verified successfully!")
                    update_details_window.destroy()
                    show_update_form(result)
                else:
                    messagebox.showwarning("Error", "Details do not match with our records")
                
                database.close()

            except mysql.Error as err:
                messagebox.showerror("Error", f"Error: {err}")

        else:
            messagebox.showwarning("Warning", "Please fill all the fields")

    update_details_window = tk.Toplevel(root)
    update_details_window.geometry("400x500")
    update_details_window.title("Update User Details")
    update_details_window.configure(bg="#90EE90")

    tk.Label(update_details_window, text="Email ID:", font=("Arial", 10), bg="#90EE90").pack(pady=10)
    email_entry = tk.Entry(update_details_window, font=("Arial", 10), width=30)
    email_entry.pack(pady=5)

    tk.Label(update_details_window, text="Aadhar Number:", font=("Arial", 10), bg="#90EE90").pack(pady=10)
    aadhar_entry = tk.Entry(update_details_window, font=("Arial", 10), width=30)
    aadhar_entry.pack(pady=5)

    tk.Label(update_details_window, text="Date of Birth (DD/MM/YYYY):", font=("Arial", 10), bg="#90EE90").pack(pady=10)
    dob_entry = tk.Entry(update_details_window, font=("Arial", 10), width=30)
    dob_entry.pack(pady=5)

    tk.Label(update_details_window, text="Password:", font=("Arial", 10), bg="#90EE90").pack(pady=10)
    password_entry = tk.Entry(update_details_window, font=("Arial", 10), width=30, show="*")
    password_entry.pack(pady=5)

    tk.Button(update_details_window, text="Submit", font=("Arial", 10, "bold"), command=validate_update_details, bg="Lime green", border=10, borderwidth=10).pack(pady=20)

def show_update_form(user_data):
    update_window = tk.Toplevel(root)
    update_window.geometry("500x700")
    update_window.title("Update Your Details")
    update_window.configure(bg="#ADD8E6")

    name_label = tk.Label(update_window, text="Name:", font=("Arial", 10), bg="#ADD8E6")
    name_label.pack(padx=20, pady=5, anchor=tk.W)
    name = tk.Entry(update_window, font=("Arial", 10),)
    name.insert(0, user_data[1])
    name.pack(padx=20, pady=5, anchor=tk.W)

    dob_label = tk.Label(update_window, text="Date of Birth (DD/MM/YYYY):", font=("Arial", 10), bg="#ADD8E6")
    dob_label.pack(padx=20, pady=5, anchor=tk.W)
    dob = tk.Entry(update_window, font=("Arial", 10),)
    dob.insert(0, user_data[2])
    dob.pack(padx=20, pady=5, anchor=tk.W)

    aadhar_label = tk.Label(update_window, text="Aadhar Number:", font=("Arial", 10), bg="#ADD8E6")
    aadhar_label.pack(padx=20, pady=5, anchor=tk.W)
    aadhar = tk.Entry(update_window, font=("Arial", 10),)
    aadhar.insert(0, user_data[3])
    aadhar.pack(padx=20, pady=5, anchor=tk.W)

    email_label = tk.Label(update_window, text="Email:", font=("Arial", 10), bg="#ADD8E6")
    email_label.pack(padx=20, pady=5, anchor=tk.W)
    email = tk.Entry(update_window, font=("Arial", 10),)
    email.insert(0, user_data[4])
    email.pack(padx=20, pady=5, anchor=tk.W)

    phone_label = tk.Label(update_window, text="Mobile Number:", font=("Arial", 10), bg="#ADD8E6")
    phone_label.pack(padx=20, pady=5, anchor=tk.W)
    phone = tk.Entry(update_window, font=("Arial", 10))
    phone.insert(0, user_data[5])
    phone.pack(padx=20, pady=5, anchor=tk.W)

    password_label = tk.Label(update_window, text="Password:", font=("Arial", 10), bg="#ADD8E6")
    password_label.pack(padx=20, pady=5, anchor=tk.W)
    password = tk.Entry(update_window, font=("Arial", 10), show='*')
    password.insert(0, user_data[6])
    password.pack(padx=20, pady=5, anchor=tk.W)

    branch_label = tk.Label(update_window, text="Select Your Branch", font=("Arial", 10), bg="#ADD8E6")
    branch_label.pack(padx=20, pady=5, anchor=tk.W)
    choices = ["----Select----", "Computer Science", "Mechanical", "Electrical", "Civil", "Chemical", "Agriculture"]
    branch = ttk.Combobox(update_window, font=("Arial", 10), values=choices)
    branch.set(user_data[7])
    branch.pack(padx=20, pady=5, anchor=tk.W)

    agree_or_disagree = tk.IntVar()
    agree_label = tk.Checkbutton(update_window, text="Do you agree with Terms and Conditions", font=("Arial", 10), variable=agree_or_disagree)
    agree_or_disagree.set(user_data[8])
    agree_label.pack(padx=20, pady=5, anchor=tk.W)

    def submit_update():
        new_name = name.get()
        new_dob = dob.get()
        new_aadhar = aadhar.get()
        new_email = email.get()
        new_phone = phone.get()
        new_password = password.get()
        new_branch = branch.get()
        new_agree = agree_or_disagree.get()

        if new_name and new_dob and new_aadhar and new_email and new_phone and new_password and new_branch:
            try:
                new_dob = datetime.strptime(new_dob, "%d/%m/%Y").strftime("%Y-%m-%d")
            except ValueError:
                messagebox.showerror("Error", "Date of Birth must be in DD/MM/YYYY format")
                return
                
            try:
                database = mysql.connect(
                    host='127.0.0.1',
                    user='root',
                    passwd='',
                    database='StudentsRegistrationDetails'
                )
                cursorObject = database.cursor()
                sql = """
                    UPDATE Students 
                    SET UserName=%s, DateOfBirth=%s, AadharNumber=%s, EmailId=%s, 
                        MobileNumber=%s, Password=%s, Branch=%s, TermsCondition=%s 
                    WHERE AadharNumber=%s
                """
                values = (new_name, new_dob, new_aadhar, new_email, new_phone, new_password, new_branch, new_agree, user_data[3])
                cursorObject.execute(sql, values)
                database.commit()
                messagebox.showinfo("Success", "Update successful!")
                update_window.destroy()
            except mysql.Error as err:
                messagebox.showerror("Error", f"Error: {err}")
            finally:
                database.close()

    update_button = tk.Button(update_window, text="Update", font=("Arial", 10, "bold"), command=submit_update, bg="Lime green", border=10, borderwidth=10)
    update_button.place(x=30, y=600, anchor=tk.W)

def delete_form():
    def validate_delete():
        email_value = email_entry.get()
        dob_value = dob_entry.get()
        aadhar_value = aadhar_entry.get()
        password_value = password_entry.get()

        if email_value and aadhar_value and dob_value and password_value:
            try:
                dob_value = datetime.strptime(dob_value, "%d/%m/%Y").strftime("%Y-%m-%d")
            except ValueError:
                messagebox.showerror("Error", "Date of Birth must be in DD/MM/YYYY format")
                return

            try:
                database = mysql.connect(
                    host='127.0.0.1',
                    user='root',
                    passwd='',
                    database='StudentsRegistrationDetails'
                )
                cursorObject = database.cursor()
                sql = """
                    SELECT * FROM Students 
                    WHERE EmailId=%s AND AadharNumber=%s AND DateOfBirth=%s AND Password=%s
                """
                values = (email_value, aadhar_value, dob_value, password_value)
                cursorObject.execute(sql, values)
                result = cursorObject.fetchone()
                database.close()

                if result:
                    delete_confirmation(result)
                    delete_window.destroy()
                else:
                    messagebox.showwarning("Warning", "Invalid details. Please check again.")
            except mysql.Error as err:
                messagebox.showerror("Error", f"Error: {err}")
        else:
            messagebox.showwarning("Warning", "Please fill all the fields.")

    delete_window = tk.Toplevel(root)
    delete_window.geometry("400x500")
    delete_window.title("Validate to Delete")
    delete_window.configure(bg="Salmon")

    tk.Label(delete_window, text="Email ID:", font=("Arial", 10), bg="Salmon").pack(pady=10)
    email_entry = tk.Entry(delete_window, font=("Arial", 10), width=30)
    email_entry.pack(pady=5)

    tk.Label(delete_window, text="Aadhar Number:", font=("Arial", 10), bg="Salmon").pack(pady=10)
    aadhar_entry = tk.Entry(delete_window, font=("Arial", 10), width=30)
    aadhar_entry.pack(pady=5)

    tk.Label(delete_window, text="Date of Birth (DD/MM/YYYY):", font=("Arial", 10), bg="Salmon").pack(pady=10)
    dob_entry = tk.Entry(delete_window, font=("Arial", 10), width=30)
    dob_entry.pack(pady=5)

    tk.Label(delete_window, text="Password:", font=("Arial", 10), bg="Salmon").pack(pady=10)
    password_entry = tk.Entry(delete_window, width=30, show="*", font=("Arial", 10))
    password_entry.pack(pady=5)

    tk.Button(delete_window, text="Submit", font=("Arial", 10, "bold"), command=validate_delete, bg="Lime green", border=10, borderwidth=10).pack(pady=20)

def delete_confirmation(user_data):
    def confirm_delete_action():
        response = messagebox.askyesno("Delete Confirmation", "Are you sure you want to delete your account?")
        if response:
            try:
                database = mysql.connect(
                    host='127.0.0.1',
                    user='root',
                    passwd='',
                    database='StudentsRegistrationDetails'
                )
                cursorObject = database.cursor()
                cursorObject.execute("START TRANSACTION;")

                sql = "DELETE FROM Students WHERE AadharNumber=%s"
                values = (user_data[3],)
                cursorObject.execute(sql, values)

                database.commit()

                messagebox.showinfo("Success", "Account deleted successfully!")
                delete_details_window.destroy()
            except mysql.Error as err:
                database.rollback()  # Rollback the transaction in case of an error
                messagebox.showerror("Error", f"Error: {err}")
            finally:
                database.close()
        else:
            messagebox.showinfo("Cancelled", "Account deletion cancelled.")

    delete_details_window = tk.Toplevel(root)
    delete_details_window.geometry("400x200")
    delete_details_window.title("Delete Account")
    delete_details_window.configure(bg="#D3D3D3")

    tk.Label(delete_details_window, text="Do you really want to delete your account?", font=("Arial", 10, "bold"), bg="#D3D3D3").pack(pady=20)
    tk.Button(delete_details_window, text="Yes", font=("Arial", 10, "bold"), command=confirm_delete_action, bg="red", border=10, borderwidth=10).pack(side=tk.LEFT, padx=40, pady=20)
    tk.Button(delete_details_window, text="No", font=("Arial", 10, "bold"), command=delete_details_window.destroy, bg="gray", border=10, borderwidth=10).pack(side=tk.RIGHT, padx=40, pady=20)

def login_form():
    def validate_login():
        email_value = email_entry.get()
        password_value = password_entry.get()

        if email_value and password_value:
            try:
                database = mysql.connect(
                    host='127.0.0.1',
                    user='root',
                    passwd='',
                    database='StudentsRegistrationDetails'
                )
                cursorObject = database.cursor()
                sql = "SELECT * FROM Students WHERE EmailId=%s AND Password=%s"
                values = (email_value, password_value)
                cursorObject.execute(sql, values)
                result = cursorObject.fetchone()
                database.close()

                if result:
                    messagebox.showinfo("Success", f"Welcome, {result[1]} !")
                    login_window.destroy()
                    open_csv_visualization()
                else:
                    messagebox.showwarning("Warning", "Invalid email or password")
            except mysql.Error as err:
                messagebox.showerror("Error", f"Error: {err}")
        else:
            messagebox.showwarning("Warning", "Please fill all the fields")

    login_window = tk.Toplevel(root)
    login_window.geometry("400x300")
    login_window.title("User Login")
    login_window.configure(bg="Coral")

    tk.Label(login_window, text="Email ID:", font=("Arial", 10), bg="Coral").pack(pady=10)
    email_entry = tk.Entry(login_window, width=30, font=("Arial", 10))
    email_entry.pack(pady=5)

    tk.Label(login_window, text="Password:", font=("Arial", 10), bg="Coral").pack(pady=10)
    password_entry = tk.Entry(login_window, width=30, show="*", font=("Arial", 10))
    password_entry.pack(pady=5)

    tk.Button(login_window, text="Submit", font=("Arial", 10, "bold"), command=validate_login, bg="Lime green", border=10, borderwidth=10).pack(pady=20)

def open_csv_visualization():
    try:
        data = pd.read_csv("C:/Users/katiy/Downloads/My_Screen_Time_Dataset2.csv")
        messagebox.showinfo("Success", "File read successfully!")
        print(data)

        csv_window = tk.Toplevel()
        csv_window.geometry("400x300")
        csv_window.title("Visualization of our data")
        csv_window.configure(bg="Coral")

        def figure1():
            data['Date'] = pd.to_datetime(data['Date'], format='%d-%m-%Y')
            plt.figure(figsize=(12, 6))
            plt.plot(data['Date'], data['Total_Screen_Time (hours)'], marker='o', color='green')
            plt.title('Total Screen Time Over Dates')
            plt.xlabel('Date')
            plt.ylabel('Total Screen Time (hours)')
            plt.xticks(rotation=45)
            plt.grid()
            plt.show()

        data.rename(columns={
            'Using_Whatsapp (hours)': 'Using_Whatsapp',
            'Using_Instagram (hours)': 'Using_Instagram',
            'Using_Facebook (hours)': 'Using_Facebook',
            'Using_X (hours)': 'Using_X',
            'Using_Youtube (hours)': 'Using_Youtube'
        }, inplace=True)
        data['Date'] = data['Date'].astype(str)
        data = data.dropna(subset=['Date'])

        csv_button1 = tk.Button(csv_window, text="Total Screen Time Over Dates", font=("Arial", 10, "bold"), command=figure1, bg="Gold", border=10, borderwidth=10)
        csv_button1.grid(row=2, columnspan=5, pady=10)

        def figure2():
            plt.figure(figsize=(15, 8))
            plt.bar(data['Date'], data['Using_Whatsapp'], label='WhatsApp', color='lightcoral')
            plt.bar(data['Date'], data['Using_Instagram'], bottom=data['Using_Whatsapp'], label='Instagram', color='gold')
            plt.bar(data['Date'], data['Using_Facebook'], bottom=data['Using_Whatsapp'] + data['Using_Instagram'], label='Facebook', color='lightskyblue')
            plt.bar(data['Date'], data['Using_X'], bottom=data['Using_Whatsapp'] + data['Using_Instagram'] + data['Using_Facebook'], label='X', color='lightgreen')
            plt.bar(data['Date'], data['Using_Youtube'], bottom=data['Using_Whatsapp'] + data['Using_Instagram'] + data['Using_Facebook'] + data['Using_X'], label='YouTube', color='orchid')
            plt.title('Social Media Usage Over Time')
            plt.xlabel('Date')
            plt.ylabel('Usage Time (hours)')
            plt.legend(loc='upper left')
            plt.xticks(rotation=90)
            plt.show()

        csv_button2 = tk.Button(csv_window, text="Social Media Usage Over Time", font=("Arial", 10, "bold"), command=figure2, bg="Lime green", border=10, borderwidth=10)
        csv_button2.grid(row=3, columnspan=5, pady=10)

        back_button = tk.Button(csv_window, text="Back", font=("Arial", 10, "bold"), command=login_form, bg="yellow", border=10, borderwidth=10)
        back_button.grid(row=4, columnspan=5, pady=10)

    except Exception as e:
        messagebox.showerror("Error", f"Could not load file: {e}")

def search_details():
    def search_db():
        email_value = email_entry.get()
        aadhar_value = aadhar_entry.get()

        if not email_value or not aadhar_value:
            messagebox.showwarning("Warning", "Please enter both Email ID and Aadhaar Number.")
            return

        try:
            database = mysql.connect(
                host='127.0.0.1',
                user='root',
                passwd='',
                database='StudentsRegistrationDetails'
            )
            cursorObject = database.cursor()
            cursorObject.execute("SELECT * FROM Students WHERE EmailId = %s AND AadharNumber = %s", (email_value, aadhar_value))
            user_details = cursorObject.fetchone()
            database.close()

            if user_details:
                details = f"UserName: {user_details[1]}\nDateOfBirth: {user_details[2]}\nAadharNumber: {user_details[3]}\nEmailId: {user_details[4]}\nMobileNumber: {user_details[5]}\nBranch: {user_details[7]}"
                messagebox.showinfo("User Details", details)
            else:
                messagebox.showinfo("No Record", "No matching record found.")
        except mysql.Error as e:
            messagebox.showerror("Error", f"Database Error: {e}")

    search_window = tk.Toplevel()
    search_window.title("Search Your Details")
    search_window.geometry("400x300")
    search_window.configure(bg="Fuchsia")

    email_label = tk.Label(search_window, text="Email ID:", font=("Arial", 10), bg="Fuchsia")
    email_label.grid(row=0, column=0, padx=10, pady=10)
    email_entry = tk.Entry(search_window, font=("Arial", 10))
    email_entry.grid(row=0, column=1, padx=10, pady=10)

    aadhar_label = tk.Label(search_window, text="Aadhaar Number:", font=("Arial", 10), bg="Fuchsia")
    aadhar_label.grid(row=1, column=0, padx=10, pady=10)
    aadhar_entry = tk.Entry(search_window, font=("Arial", 10))
    aadhar_entry.grid(row=1, column=1, padx=10, pady=10)

    submit_button = tk.Button(search_window, text="Submit", font=("Arial", 10, "bold"), command=search_db, bg="Lime green", border=10, borderwidth=10)
    submit_button.grid(row=2, columnspan=2, pady=10)

name_label = tk.Label(root, text="Name:", font=("Arial", 10), bg="aqua")
name_label.pack(padx=100, pady=5, anchor=tk.W)
name = tk.Entry(root, font=("Arial", 10))
name.pack(padx=100, pady=5, anchor=tk.W)

dob_label = tk.Label(root, text="Date of Birth (DD/MM/YYYY):", font=("Arial", 10), bg="aqua")
dob_label.pack(padx=100, pady=5, anchor=tk.W)
dob = tk.Entry(root, font=("Arial", 10))
dob.pack(padx=100, pady=5, anchor=tk.W)

aadhar_label = tk.Label(root, text="Aadhar Number:", font=("Arial", 10), bg="aqua")
aadhar_label.pack(padx=100, pady=5, anchor=tk.W)
aadhar = tk.Entry(root, font=("Arial", 10))
aadhar.pack(padx=100, pady=5, anchor=tk.W)

email_label = tk.Label(root, text="Email:", font=("Arial", 10), bg="aqua")
email_label.pack(padx=100, pady=5, anchor=tk.W)
email = tk.Entry(root, font=("Arial", 10))
email.pack(padx=100, pady=5, anchor=tk.W)

phone_label = tk.Label(root, text="Mobile Number:", font=("Arial", 10), bg="aqua")
phone_label.pack(padx=100, pady=5, anchor=tk.W)
phone = tk.Entry(root, font=("Arial", 10))
phone.pack(padx=100, pady=5, anchor=tk.W)

branch_label = tk.Label(root, text="Select Your Branch", font=("Arial", 10), bg="aqua")
branch_label.pack(padx=100, pady=5, anchor=tk.W)
choices = ["----Select----", "Computer Science", "Mechanical", "Electrical", "Civil", "Chemical", "Agriculture"]
branch = ttk.Combobox(root, font=("Arial", 10), values=choices)
branch.pack(padx=100, pady=5, anchor=tk.W)

password_label = tk.Label(root, text="Password:", font=("Arial", 10), bg="aqua")
password_label.pack(padx=100, pady=5, anchor=tk.W)
password = tk.Entry(root, font=("Arial", 10), show='*')
password.pack(padx=100, pady=5, anchor=tk.W)

agree_or_disagree = tk.IntVar()
agree_label = tk.Checkbutton(root, text="Do you agree with Terms and Conditions", font=("Arial", 10), variable=agree_or_disagree)
agree_label.pack(padx=100, pady=5, anchor=tk.W)

submit_button = tk.Button(root, text="Submit", font=("Arial", 10, "bold"), command=submit_form, bg="Lime green", border=10, borderwidth=10)
submit_button.place(x=100, y=680, anchor=tk.W)

login_button = tk.Button(navbar, text="Login", font=("Arial", 10, "bold"), width=10, command=login_form, bg="Coral", border=5, borderwidth=2)
login_button.place(x=100, y=25, anchor=tk.W)

update_button = tk.Button(navbar, text="Update", font=("Arial", 10, "bold"), width=10, command=update_form, bg="orange", border=5, borderwidth=2)
update_button.place(x=270, y=25, anchor=tk.W)

delete_button = tk.Button(navbar, text="Delete", font=("Arial", 10, "bold"), width=10, command=delete_form, bg="red", border=5, borderwidth=2)
delete_button.place(x=440, y=25, anchor=tk.W)

search_button = tk.Button(navbar, text="Search", font=("Arial", 10, "bold"), width=10, command=search_details, bg="Light green", border=5, borderwidth=2)
search_button.place(x=610, y=25, anchor=tk.W)

root.mainloop()
