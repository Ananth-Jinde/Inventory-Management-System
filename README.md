# Inventory Management System

## Overview
This project is an Inventory Management System built using Tkinter for the GUI, integrated with an SQLite database located at `IMS/ims.db`. The main entry point of the application is `IMS/login.py`.

## Features
- **Admin Dashboard Modules**: 
  - Employee Management
  - Supplier Management
  - Category Management
  - Product Management
  - Sales Management
- **Billing Point of Sale (POS)**

## Running the Application
To run the application, navigate to the `IMS` folder and execute the following command:
```bash
python login.py
```

## Bill Storage
Bills are stored in the following location: `IMS/bill`.

## Dependencies
- **Pillow**: Required for handling image files.

## Building the Application
To create a Windows executable, use `cx_Freeze` with the setup script located at `IMS/setup.py`.

## Security Warning
**Important**: Do not commit your credentials located in `IMS/email_pass.py`. It is recommended to use environment variables for sensitive information.