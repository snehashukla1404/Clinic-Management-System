# Clinic Management System

A simple desktop-based Clinic Management System developed in **Python** using **Tkinter** for GUI and **MySQL** for database management.  
This project helps manage patients, doctors, and appointments efficiently in a clinical setup.

## ✨ Features
- Add, view, update, and delete patient records
- Add, view, update, and delete doctor records
- Book, view, and manage appointments
- User-friendly GUI built with Tkinter
- Secure database integration with MySQL
- Basic validation and error handling

## 🛠️ Tech Stack
- **Frontend:** Tkinter (Python GUI Library)
- **Backend:** Python 3.x
- **Database:** MySQL

## 📂 Project Structure
 Clinic-Management-System/
      ├── clinic.py            # Main GUI application
      ├── db_config.py         # Database connection settings
      ├── requirements.txt     # Required Python packages
      └── README.md            # Project documentation (this file)


## 🚀 Getting Started

### Prerequisites
- Python 3.x installed
- MySQL server installed and running
- Required Python libraries:
  - `tkinter`
  - `mysql-connector-python`

Install dependencies using:
```bash
`pip install -r requirements.txt`
```
## 📦 Database Setup
- Open **MySQL Workbench** (or any MySQL client).
- Create a new database:
```sql
CREATE DATABASE clinic_db;
```
- Create the required tables (patients, doctors, appointments) as per your application needs.
- Update db_config.py with your MySQL username, password, and database name.











