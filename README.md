# Inventory Management System

## Overview
The Inventory Management System (IMS) is a Python application that serves as a comprehensive solution for managing inventory with a user-friendly Tkinter GUI interface.

## Tkinter GUI Entry Point
The main entry point for the application is located at `IMS/login.py`. This script initializes the GUI and handles user authentication.

## Modules
The project is structured in a modular way to enhance maintainability and scalability. Key modules include:
- `IMS/database.py`: Manages SQLite database connections and queries.
- `IMS/billing.py`: Handles billing calculations and receipts generation.
- Additional utility modules to support various functionalities.

## Setup
To set up the project, ensure you have the necessary Python environment. Use `requirements.txt` to install dependencies:
```bash
pip install -r requirements.txt
```

## Dependencies
The following dependencies are required to run the project:
- `tkinter`: For the GUI interface.
- `sqlite3`: For database management.
- `cx_Freeze`: For packaging the application.

## SQLite Database
The application utilizes an SQLite database to store inventory data securely. Database schema and configuration can be found in `IMS/database.py`.

## Billing
The billing module includes functionalities to calculate and manage transactions, providing users with receipts and inventory updates.

## cx_Freeze Setup
For packaging the application, `cx_Freeze` is utilized. The setup script for building the executable is included in the project root. Run the following command to build:
```bash
python setup.py build
```

## Project Structure
```
Inventory-Management-System/
│
├── IMS/
│   ├── login.py
│   ├── database.py
│   ├── billing.py
│   └── ...
│
├── requirements.txt
├── setup.py
└── README.md
```

## Conclusion
This README provides essential information for users and developers to navigate and utilize the Inventory Management System. For any issues or contributions, please refer to the project's GitHub repository.