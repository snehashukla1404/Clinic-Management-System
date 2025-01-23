import tkinter as tk
from tkinter import messagebox
import mysql.connector

def insert_data():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Citibank@123",
        database="pbl"
    )
    selected_table = table_var.get()

    try:
        cursor = connection.cursor()

        if selected_table == "employee":
            print("Inserting data into employee table...")
            sql = "INSERT INTO employee (emp_id, f_name, l_name, DOB, address, salary) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (
                entry_fields["emp_id"]["entry"].get(),
                entry_fields["f_name"]["entry"].get(),
                entry_fields["l_name"]["entry"].get(),
                entry_fields["DOB"]["entry"].get(),
                entry_fields["address"]["entry"].get(),
                entry_fields["salary"]["entry"].get()
            )
            print("Values:", values)

        elif selected_table == "patient":
            print("Inserting data into patient table...")
            sql = "INSERT INTO patient (p_id, f_name, l_name, DOB, address, emp_id) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (
                entry_fields["p_id"]["entry"].get(),
                entry_fields["f_name"]["entry"].get(),
                entry_fields["l_name"]["entry"].get(),
                entry_fields["DOB"]["entry"].get(),
                entry_fields["address"]["entry"].get(),
                entry_fields["emp_id"]["entry"].get()
            )
            print("Values:", values)

        elif selected_table == "patient_mail_details":
            print("Inserting data into patient_mail_details table...")
            sql = "INSERT INTO patient_mail_details (p_id, , email_id) VALUES (%s, %s)"
            values = (
                entry_fields["p_id"]["entry"].get(),
                entry_fields["email_id"]["entry"].get()
            )
            print("Values:", values)

        elif selected_table == "patient_phone_number":
            print("Inserting data into patient_phone_number table...")
            sql = "INSERT INTO patient_phone_number (p_id, phone_number) VALUES (%s, %f)"
            values = (
                entry_fields["p_id"]["entry"].get(),
                entry_fields["phone_number"]["entry"].get()
            )
            print("Values:", values)

        elif selected_table == "employee_mail_details":
            print("Inserting data into employee_mail_details table...")
            sql = "INSERT INTO employee_mail_details (emp_id, email_id) VALUES (%s, %s)"
            values = (
                entry_fields["emp_id"]["entry"].get(),
                entry_fields["email_Id"]["entry"].get()
            )
            print("Values:", values)

        elif selected_table == "employee_phone_number":
            print("Inserting data into employee_phone_number table...")
            sql = "INSERT INTO employee_phone_number (emp_id, phone_number) VALUES (%s, %f)"
            values = (
                entry_fields["emp_id"]["entry"].get(),
                entry_fields["phone_number"]["entry"].get()
            )
            print("Values:", values)

        elif selected_table == "permanent employee":
            print("Inserting data into permanent table...")
            sql = "INSERT INTO permanent (emp_id, working_hours_weekly, experience, Specialization) VALUES (%s, %d, %d, %s)"
            values = (
                entry_fields["emp_id"]["entry"].get(),
                entry_fields["working_hours_weekly"]["entry"].get(),
                entry_fields["experience"]["entry"].get(),
                entry_fields["specialization"]["entry"].get()
            )
            print("Values:", values)

        elif selected_table == "trainee":
            print("Inserting data into trainee table...")
            sql = "INSERT INTO trainee (emp_id, working_hours_weekly, experience, Specialization) VALUES (%s, %d, %d, %s)"
            values = (
                entry_fields["emp_id"]["entry"].get(),
                entry_fields["working_hours_weekly"]["entry"].get(),
                entry_fields["experience"]["entry"].get(),
                entry_fields["specialization"]["entry"].get()
            )
            print("Values:", values)

        elif selected_table == "visiting employee":
            print("Inserting data into visiting table...")
            sql = "INSERT INTO visiting (emp_id, working_hours_weekly, experience, Specialization) VALUES (%s, %d, %d, %s)"
            values = (
                entry_fields["emp_id"]["entry"].get(),
                entry_fields["working_hours_weekly"]["entry"].get(),
                entry_fields["experience"]["entry"].get(),
                entry_fields["specialization"]["entry"].get()
            )
            print("Values:", values)

        elif selected_table == "nurse":
            print("Inserting data into nurse table...")
            sql = "INSERT INTO nurse (emp_id, working_hours_weekly) VALUES (%s, %d)"
            values = (
                entry_fields["emp_id"]["entry"].get(),
                entry_fields["working_hours_weekly"]["entry"].get()
            )
            print("Values:", values)

        elif selected_table == "medical_history":
            print("Inserting data into medical_history table...")
            sql = "INSERT INTO medical_history (mh_id, blood_pressure, weight, sugar_level, height, blood_group, current_disease, chronic_disease, genetic_disease, p_id) VALUES (%s, %s, %d, %s, %s, %s, %s, %s, %s, %s)"
            values = (
                entry_fields["mh_id"]["entry"].get(),
                entry_fields["blood_pressure"]["entry"].get(),
                entry_fields["weight"]["entry"].get(),
                entry_fields["sugar_level"]["entry"].get(),
                entry_fields["height"]["entry"].get(),
                entry_fields["blood_group"]["entry"].get(),
                entry_fields["current_disease"]["entry"].get(),
                entry_fields["chronic_disease"]["entry"].get(),
                entry_fields["genetic_disease"]["entry"].get(),
                entry_fields["p_id"]["entry"].get()
            )
            print("Values:", values)

        elif selected_table == "tests":
            print("Inserting data into tests table...")
            sql = "INSERT INTO tests (t_id, p_id, emp_id, test_name, test_result) VALUES (%s, %s, %s, %s, %s)"
            values = (
                entry_fields["t_id"]["entry"].get(),
                entry_fields["p_id"]["entry"].get(),
                entry_fields["emp_id"]["entry"].get(),
                entry_fields["test_name"]["entry"].get(),
                entry_fields["test_result"]["entry"].get()
            )
            print("Values:", values)
            
            messagebox.showinfo("data insertion successful")
            

    except mysql.connector.Error as error:
        print("Error:", error)
        messagebox.showerror("Error", f"Error inserting data: {error}")
    finally:
        if connection.is_connected():
            cursor.execute(sql, values)
            connection.commit()
            cursor.close()
            connection.close()


def on_table_select():
    selected_table = table_var.get()
    if selected_table == "employee":
        hide_attributes(
            ["email_id", "phone_number", "mh_id", "blood_pressure", "weight", "sugar_level", "height", "blood_group",
             "current_disease", "chronic_disease", "genetic_disease", "p_id", "working_hours_weekly", "experience",
             "specialization", "t_id", "test_name", "test_result"], entry_fields)

    elif selected_table == "employee_mail_details":
        hide_attributes(
            ["f_name", "l_name", "DOB", "address", "salary", "phone_number", "mh_id", "blood_pressure", "weight",
             "sugar_level", "height", "blood_group", "current_disease", "chronic_disease", "genetic_disease", "p_id",
             "working_hours_weekly", "experience", "specialization", "t_id", "test_name", "test_result"], entry_fields)

    elif selected_table == "employee_phone_number":
        hide_attributes(
            ["f_name", "l_name", "DOB", "address", "salary", "email_id", "mh_id", "blood_pressure", "weight",
             "sugar_level", "height", "blood_group", "current_disease", "chronic_disease", "genetic_disease", "p_id",
             "working_hours_weekly", "experience", "specialization", "t_id", "test_name", "test_result"], entry_fields)

    elif selected_table == "medical_history":
        hide_attributes(["emp_id", "f_name", "l_name", "DOB", "address", "salary", "email_id", "phone_number",
                         "working_hours_weekly", "experience", "specialization", "t_id", "test_name", "test_result"],
                        entry_fields)

    elif selected_table == "nurse":
        hide_attributes(
            ["f_name", "l_name", "DOB", "address", "salary", "email_id", "phone_number", "mh_id", "blood_pressure",
             "weight", "sugar_level", "height", "blood_group", "current_disease", "chronic_disease", "genetic_disease",
             "p_id", "experience", "specialization", "t_id", "test_name", "test_result"], entry_fields)

    elif selected_table == "patient":
        hide_attributes(
            ["salary", "email_id", "phone_number", "mh_id", "blood_pressure", "weight", "sugar_level", "height",
             "blood_group", "current_disease", "chronic_disease", "genetic_disease", "working_hours_weekly",
             "experience", "specialization", "t_id", "test_name", "test_result"], entry_fields)

    elif selected_table == "permanent":
        hide_attributes(
            ["f_name", "l_name", "DOB", "address", "salary", "email_id", "phone_number", "mh_id", "blood_pressure",
             "weight", "sugar_level", "height", "blood_group", "current_disease", "chronic_disease", "genetic_disease",
             "p_id", "t_id", "test_name", "test_result"], entry_fields)

    elif selected_table == "trainee":
        hide_attributes(
            ["f_name", "l_name", "DOB", "address", "salary", "email_id", "phone_number", "mh_id", "blood_pressure",
             "weight", "sugar_level", "height", "blood_group", "current_disease", "chronic_disease", "genetic_disease",
             "p_id", "t_id", "test_name", "test_result"], entry_fields)

    elif selected_table == "visiting":
        hide_attributes(
            ["f_name", "l_name", "DOB", "address", "salary", "email_id", "phone_number", "mh_id", "blood_pressure",
             "weight", "sugar_level", "height", "blood_group", "current_disease", "chronic_disease", "genetic_disease",
             "p_id", "t_id", "test_name", "test_result"], entry_fields)

    elif selected_table == "tests":
        hide_attributes(
            ["f_name", "l_name", "DOB", "address", "salary", "email_id", "phone_number", "mh_id", "blood_pressure",
             "weight", "sugar_level", "height", "blood_group", "current_disease", "chronic_disease", "genetic_disease",
             "working_hours_weekly", "experience", "specialization"], entry_fields)

    elif selected_table == "receptionist":
        hide_attributes(
            ["f_name", "l_name", "DOB", "address", "salary", "email_id", "phone_number", "mh_id", "blood_pressure",
             "weight", "sugar_level", "height", "blood_group", "current_disease", "chronic_disease", "genetic_disease",
             "p_id", "experience", "specialization", "t_id", "test_name", "test_result"], entry_fields)

    elif selected_table == "patient_phone_number":
        hide_attributes(
            ["emp_id", "f_name", "l_name", "DOB", "address", "salary", "email_id", "mh_id", "blood_pressure", "weight",
             "sugar_level", "height", "blood_group", "current_disease", "chronic_disease", "genetic_disease",
             "working_hours_weekly", "experience", "specialization", "t_id", "test_name", "test_result"], entry_fields)

    elif selected_table == "patient_mail_details":
        hide_attributes(
            ["emp_id", "f_name", "l_name", "DOB", "address", "salary", "phone_number", "mh_id", "blood_pressure",
             "weight", "sugar_level", "height", "blood_group", "current_disease", "chronic_disease", "genetic_disease",
             "working_hours_weekly", "experience", "specialization", "t_id", "test_name", "test_result"], entry_fields)

    else:
        # If the selected table doesn't match any condition,
        # then show all attributes back
        hide_attributes([], entry_fields)


def hide_attributes(attributes_to_hide, all_attributes):
    for attribute, widget in all_attributes.items():
        if attribute in attributes_to_hide:
            widget["label"].grid_remove()
            widget["entry"].grid_remove()
        else:
            widget["label"].grid()
            widget["entry"].grid()


def find_data(table_name, conditions=None):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Citibank@123",
            database="pbl"
        )
        if connection:
            cursor = connection.cursor()
            query = f"SELECT * FROM {table_name}"
            if conditions:
                condition_str = " AND ".join(conditions)
                query += f" WHERE {condition_str}"
            cursor.execute(query)
            results = cursor.fetchall()
            if results:
                messagebox.showinfo("Result", f"Data found in {table_name}: {results}")
            else:
                messagebox.showinfo("Result", f"No data found in {table_name}.")
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to find data: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def on_find():
    table_name = table_var.get()
    conditions = []
    for attribute, entry in entry_fields.items():
        if entry["entry"].get():
            conditions.append(f"{attribute}='{entry['entry'].get()}'")
    find_data(table_name, conditions)

def delete_data(table_name, conditions=None):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Citibank@123",
            database="pbl"
        )
        if connection:
            cursor = connection.cursor()
            query = f"DELETE FROM {table_name}"
            if conditions:
                condition_str = " AND ".join(conditions)
                query += f" WHERE {condition_str}"
            cursor.execute(query)
            connection.commit()  # Commit the changes after DELETE operation
            affected_rows = cursor.rowcount  # Get the number of affected rows
            if affected_rows > 0:
                messagebox.showinfo("Result", f"{affected_rows} row(s) deleted from {table_name}.")
            else:
                messagebox.showinfo("Result", f"No data deleted from {table_name}.")
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to delete data: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def on_find_del():
    table_name = table_var.get()
    conditions = []
    for attribute, entry in entry_fields.items():
        if entry["entry"].get():
            conditions.append(f"{attribute}='{entry['entry'].get()}'")
    delete_data(table_name, conditions)

def create_gui():
    global connection
    global table_var
    global entry_fields

    root = tk.Tk()
    root.title("CLINIC DATABASE")
    root.geometry("700x600")
    
    root.config(bg='cyan')

    tk.Label(root, text="SELECT A TABLE:",bg="cyan").grid(row=0, column=0)
    table_var = tk.StringVar()
    table_var.set("select table")  
    table_dropdown = tk.OptionMenu(root, table_var, "employee", "employee_mail_details", "employee_phone_number",
                                   "medical_history", "nurse", "patient", "patient_mail_details",
                                   "patient_phone_number", "permanent employee", "receptionist", "tests", "trainee", "visiting employee")
    table_dropdown.grid(row=0, column=1)

    table_var.trace("w", lambda *args: on_table_select())
    

    entry_fields = {
        "emp_id": {"label": tk.Label(root, text="employee Id:", padx = 40,bg="cyan"), "entry": tk.Entry(root)},
        "f_name": {"label": tk.Label(root, text="first name:",padx=45, bg="cyan"), "entry": tk.Entry(root)},
        "l_name": {"label": tk.Label(root, text="last name:",padx=44,bg="cyan"), "entry": tk.Entry(root)},
        "DOB": {"label": tk.Label(root, text="DOB:",padx=58,bg="cyan"), "entry": tk.Entry(root)},
        "address": {"label": tk.Label(root, text="address:",padx=50,bg="cyan"), "entry": tk.Entry(root)},
        "salary": {"label": tk.Label(root, text="salary:",padx=55,bg="cyan"), "entry": tk.Entry(root)},
        "email_id": {"label": tk.Label(root, text="email id:",padx=48,bg="cyan"), "entry": tk.Entry(root)},
        "phone_number": {"label": tk.Label(root, text="phone number:",padx=30,bg="cyan"), "entry": tk.Entry(root)},
        "mh_id": {"label": tk.Label(root, text="mh id:",padx=54,bg="cyan"), "entry": tk.Entry(root)},
        "blood_pressure": {"label": tk.Label(root, text="blood pressure:",bg="cyan",padx=30), "entry": tk.Entry(root)},
        "weight": {"label": tk.Label(root, text="weight:",padx=52,bg="cyan"), "entry": tk.Entry(root)},
        "sugar_level": {"label": tk.Label(root, text="sugar level:",padx=41,bg="cyan"), "entry": tk.Entry(root)},
        "height": {"label": tk.Label(root, text="height:",padx=53,bg="cyan"), "entry": tk.Entry(root)},
        "blood_group": {"label": tk.Label(root, text="blood group:",padx=36,bg="cyan"), "entry": tk.Entry(root)},
        "current_disease": {"label": tk.Label(root, text="current disease:",padx=29,bg="cyan"), "entry": tk.Entry(root)},
        "chronic_disease": {"label": tk.Label(root, text="chronic disease:",padx=28,bg="cyan"), "entry": tk.Entry(root)},
        "genetic_disease": {"label": tk.Label(root, text="genetic disease:",padx=28,bg="cyan"), "entry": tk.Entry(root)},
        "p_id": {"label": tk.Label(root, text="patient id:",padx=58,bg="cyan"), "entry": tk.Entry(root)},
        "working_hours_weekly": {"label": tk.Label(root, text="working hours weekly:",padx=10,bg="cyan"), "entry": tk.Entry(root)},
        "experience": {"label": tk.Label(root, text="experience:",padx=42,bg="cyan"), "entry": tk.Entry(root)},
        "specialization": {"label": tk.Label(root, text="specialization:",padx=34,bg="cyan"), "entry": tk.Entry(root)},
        "t_id": {"label": tk.Label(root, text="test id:",padx=60,bg="cyan"), "entry": tk.Entry(root)},
        "test_name": {"label": tk.Label(root, text="test name:",padx=42,bg="cyan"), "entry": tk.Entry(root)},
        "test_result": {"label": tk.Label(root, text="test result:",padx=44,bg="cyan"), "entry": tk.Entry(root)}
    }

    for i, (attribute, entry) in enumerate(entry_fields.items(), start=1):
        entry["label"].grid(row=i, column=1)
        entry["entry"].grid(row=i, column=3)

    insert_button = tk.Button(root, text="Insert Into Database",bg="pink", command=insert_data)
    insert_button.grid(row=26,column=0, columnspan=2, pady=10)

    find_button = tk.Button(root, text="Find from database", bg="pink",command=on_find)
    find_button.grid(row=26, column=4,columnspan=2, pady=10)
    
    delete_button = tk.Button(root, text="delete from database", bg="pink",command=on_find_del)
    delete_button.grid(row=26, column=6, columnspan=2, pady=10)

    root.mainloop()


if __name__ == "__main__":
    create_gui()
