# Inventory Management System (IMS)

## 📋 Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Technology Stack](#technology-stack)
4. [System Requirements](#system-requirements)
5. [Installation Guide](#installation-guide)
6. [Configuration](#configuration)
7. [Running the Application](#running-the-application)
8. [Project Structure](#project-structure)
9. [Module Documentation](#module-documentation)
10. [Database Schema](#database-schema)
11. [Usage Guide](#usage-guide)
12. [Building Executable](#building-executable)
13. [Security Features](#security-features)
14. [Troubleshooting](#troubleshooting)
15. [Development](#development)
16. [License](#license)

---

## Overview

The **Inventory Management System (IMS)** is a comprehensive desktop application designed to streamline inventory operations, employee management, supplier coordination, and point-of-sale (POS) billing. Built with Python, Tkinter, and SQLite, it provides a user-friendly GUI for managing inventory efficiently without requiring a dedicated database server.

This system is ideal for small to medium-sized retail businesses, warehouses, and organizations that need centralized inventory and billing management.

### Key Objectives
- **Centralized Inventory Control:** Track product stock levels, categories, and suppliers in real-time.
- **Employee Management:** Manage employee profiles, roles, and credentials with secure authentication.
- **Supplier Coordination:** Maintain supplier contact information and invoice tracking.
- **Digital Billing:** Generate and track sales transactions with automatic bill generation.
- **User Authentication:** Secure login system with password reset via OTP email.

---

## Features

### 🔐 Authentication & Security
- **Secure Login System:** Employee credentials stored in SQLite with role-based access.
- **Password Reset:** OTP-based password recovery via email (Gmail SMTP).
- **Input Validation:** Numeric OTP validation, SQL injection prevention via parameterized queries.

### 📊 Inventory Management
- **Product CRUD:** Add, edit, delete, and search products with category and supplier associations.
- **Category Management:** Create and organize product categories.
- **Stock Tracking:** Real-time product quantity updates after each sale.
- **Supplier Management:** Maintain supplier invoices and contact information.

### 👥 Employee Management
- **Employee Records:** Store employee details including name, email, gender, DOB, contact, address, and salary.
- **User Types:** Different user roles (e.g., Admin, Staff) with role-based permissions.
- **Search & Filter:** Advanced search by employee name, ID, or email.

### 💳 Point-of-Sale (POS) Billing
- **Product Search:** Quick product lookup during billing.
- **Shopping Cart:** Add multiple products with quantity validation before checkout.
- **Automatic Bill Generation:** Generate and save bill receipts as text files.
- **Bill History:** View and track previously generated bills.
- **Inventory Update:** Automatic stock deduction after sale completion.

### 📈 Dashboard
- **Real-time Counts:** View total products, suppliers, categories, employees, and sales at a glance.
- **Navigation Hub:** Central hub for accessing all system modules.
- **Sales Tracking:** Total number of sales transactions.

---

## Technology Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| **GUI Framework** | Tkinter | 8.6 (with Tcl/Tk) |
| **Database** | SQLite | 3.x (file-based) |
| **Image Processing** | Pillow | 12.1.1 |
| **Build Tool** | cx-Freeze | 8.6.3 (optional) |
| **Language** | Python | 3.14+ |
| **OS Platform** | Windows | 10/11 |

---

## System Requirements

### Minimum Requirements
- **OS:** Windows 10 or later (64-bit)
- **Python:** 3.8 or higher
- **RAM:** 512 MB minimum
- **Disk Space:** 100 MB (including dependencies)
- **Display:** 1024x768 minimum resolution

### Recommended Requirements
- **OS:** Windows 11
- **Python:** 3.12 or higher
- **RAM:** 2 GB or more
- **Disk Space:** 500 MB
- **Display:** 1366x768 or higher

### Internet (Optional)
- Email SMTP access (Gmail) for password reset OTP functionality. Requires internet connection only when using "Forgot Password" feature.

---

## Installation Guide

### Prerequisites
Ensure you have Python 3.8+ installed. Verify installation:
```bash
python --version
```

### Step 1: Clone or Download the Repository
```bash
git clone https://github.com/Ananth-Jinde/Inventory-Management-System.git
cd "Inventory Management System"
cd "Project Files"
```

Or download and extract the ZIP file to your desired location.

### Step 2: Create a Virtual Environment (Recommended)
```bash
python -m venv venv
venv\Scripts\activate
```

On Mac/Linux:
```bash
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

**Dependencies include:**
- Pillow==12.1.1 (image rendering)
- cx-Freeze==8.6.3 (optional, for building executables)

### Step 4: Initialize the Database
On first run, the application will automatically create and initialize the SQLite database:
```bash
python create_db.py
```

This creates the database file at `data/ims.db` with all required tables (employee, supplier, category, product).

### Step 5: Verify Installation
Check that all files are in place:
```bash
dir
```

Expected structure:
```
Project Files/
├── assets/
│   ├── images/
│   └── icons/
├── data/
│   ├── ims.db
│   └── bills/
├── tools/
│   ├── build/
│   └── external/
├── *.py (all modules)
└── requirements.txt
```

---

## Configuration

### Environment Variables Setup

For the password reset (OTP email) feature to work, configure email credentials:

#### Windows PowerShell:
```powershell
$env:IMS_EMAIL="your-email@gmail.com"
$env:IMS_EMAIL_PASS="your-app-password"
```

Or set permanently in System Properties > Environment Variables.

#### Windows Command Prompt:
```cmd
set IMS_EMAIL=your-email@gmail.com
set IMS_EMAIL_PASS=your-app-password
```

#### Linux/Mac:
```bash
export IMS_EMAIL="your-email@gmail.com"
export IMS_EMAIL_PASS="your-app-password"
```

### Gmail Configuration
To use Gmail for OTP emails:
1. Enable 2-Factor Authentication on your Google Account.
2. Generate an **App Password** at https://myaccount.google.com/apppasswords
3. Use the 16-character app password as `IMS_EMAIL_PASS` (not your regular Gmail password).

### Alternative Email Providers
The system uses SMTP. To use a different provider (Outlook, Yahoo, etc.), modify the SMTP server details in `login.py`:
```python
server.connect('smtp.gmail.com', 587)  # Change host and port as needed
```

---

## Running the Application

### Method 1: Direct Python Execution
```bash
cd "Project Files"
python login.py
```

### Method 2: Using Command Line (Windows)
```cmd
cd "Project Files"
python login.py
```

### Method 3: Double-clicking (After setup.py build)
If you've built an executable, double-click the `.exe` file generated in the `build/` directory.

### First Login
**Default Admin Credentials:**
- **Employee ID:** 1
- **Password:** 123

⚠️ **IMPORTANT:** Change this password immediately after first login.

---

## Project Structure

```
Inventory Management System/
├── README.md                          # This file
├── Project Files/
│   ├── assets/
│   │   ├── images/                   # UI images (logo, icons, menu graphics)
│   │   │   ├── logo1.png
│   │   │   ├── menu_im.png
│   │   │   ├── phone.png
│   │   │   ├── cat.jpg
│   │   │   └── ...
│   │   └── icons/
│   │       └── IMS_ICON.ico          # Application icon
│   ├── data/
│   │   ├── ims.db                    # SQLite database file
│   │   └── bills/                    # Generated bill text files
│   │       ├── 12302327.txt
│   │       ├── 2253030.txt
│   │       └── ...
│   ├── tools/
│   │   ├── build/                    # Build support files
│   │   │   ├── tcl86t.dll
│   │   │   └── tk86t.dll
│   │   └── external/                 # Optional external tools
│   │       ├── SQLiteBrowserPortable.msi
│   │       └── DB_Browser.lnk
│   ├── login.py                      # Authentication entry point
│   ├── Dashboard.py                  # Admin dashboard & navigation
│   ├── employee.py                   # Employee CRUD module
│   ├── supplier.py                   # Supplier management module
│   ├── category.py                   # Product category module
│   ├── product.py                    # Product inventory module
│   ├── billing.py                    # POS billing system
│   ├── sales.py                      # Bill history viewer
│   ├── create_db.py                  # Database schema initialization
│   ├── email_pass.py                 # Email configuration helper
│   ├── setup.py                      # cx-Freeze build configuration
│   └── requirements.txt              # Python dependencies
└── .gitignore                         # Git ignore rules
```

---

## Module Documentation

### 1. **login.py** (275 lines)
**Purpose:** Authentication gateway and password recovery.

**Key Features:**
- Employee login with credential validation
- "Forgot Password" OTP email reset functionality
- Input validation (numeric OTP validation)
- Environment-based email configuration (no hardcoded credentials)

**Entry Point:**
```bash
python login.py
```

**Main Classes:**
- `Login`: Tkinter window for login interface
- Email SMTP handler for OTP delivery

---

### 2. **Dashboard.py** (180 lines)
**Purpose:** Admin hub with real-time statistics and navigation.

**Displays:**
- Total Products count
- Total Suppliers count
- Total Categories count
- Total Employees count
- Total Sales count

**Navigation Buttons:** Quick-launch buttons for all modules (Employee, Supplier, Category, Product, Billing, Sales History)

**Main Classes:**
- `Dashboard`: Tkinter window with stats and navigation

---

### 3. **employee.py** (300+ lines)
**Purpose:** Employee master data CRUD operations.

**Operations:**
- **Create:** Add new employee with full profile (name, email, gender, DOB, contact, salary, etc.)
- **Read:** Search employees by ID, name, or email
- **Update:** Edit existing employee records
- **Delete:** Remove employee records with confirmation

**Features:**
- Parameterized SQL queries (SQL injection prevention)
- Advanced search with column-wise filtering
- Scrollable table view

**Main Classes:**
- `Employee`: Tkinter Toplevel window for employee management

---

### 4. **supplier.py** (260+ lines)
**Purpose:** Supplier contact and invoice management.

**Operations:**
- Add supplier with invoice number, name, contact, and description
- Search suppliers by invoice number or name
- Update supplier information
- Delete supplier records

**Features:**
- Bill history viewing per supplier
- Parameterized SQL search
- Scrollable table interface

**Main Classes:**
- `Supplier`: Tkinter Toplevel window for supplier operations

---

### 5. **category.py** (200+ lines)
**Purpose:** Product category management.

**Operations:**
- Create new product categories
- View categories as a list
- Edit category names
- Delete categories (with confirmation)

**Features:**
- Category icon/image display
- Simple CRUD interface
- Category search functionality

**Main Classes:**
- `Category`: Tkinter Toplevel window for categories

---

### 6. **product.py** (340+ lines)
**Purpose:** Product inventory and master data management.

**Operations:**
- Add products with category, supplier, price, and quantity
- Search products by name, category, or supplier
- Update product details (price, quantity, status)
- Delete products
- Mark products as active/inactive

**Features:**
- Dropdown selectors for Category and Supplier
- Parameterized search queries
- Stock quantity tracking
- Advanced filtering

**Main Classes:**
- `Product`: Tkinter Toplevel window for product management

---

### 7. **billing.py** (500+ lines)
**Purpose:** Point-of-Sale (POS) billing system.

**Operations:**
- Search products dynamically during billing
- Add products to shopping cart with quantity
- Remove or modify cart items
- Generate bills with automatic invoice numbering
- Print/Save bills as text files
- Automatic inventory deduction after sale

**Features:**
- Real-time product search
- Shopping cart with line-item totals
- Customer information entry
- Automatic bill generation with timestamp
- Quantity validation
- Cart item guards (prevent crashes on empty cart)

**Main Classes:**
- `Billing`: Tkinter Toplevel window for billing interface

**Bill Format:**
Generated bills include:
- Invoice Number
- Date and Time
- Customer Information
- Itemized product list (Name, Quantity, Price, Total)
- Grand Total
- Footer with company/shop details

---

### 8. **sales.py** (180+ lines)
**Purpose:** Historical bill lookup and viewing.

**Operations:**
- View list of all generated bills
- Search bills by invoice number
- Display bill content in text format
- Track sales transactions

**Features:**
- Scrollable bill list
- Bill preview window
- File reading with context managers

**Main Classes:**
- `Sales`: Tkinter Toplevel window for sales history

---

### 9. **create_db.py**
**Purpose:** Database schema initialization and table creation.

**Tables Created:**
1. **employee** - Employee master data
2. **supplier** - Supplier information
3. **category** - Product categories
4. **product** - Product inventory

**Run once to initialize database:**
```bash
python create_db.py
```

---

### 10. **email_pass.py** (6 lines)
**Purpose:** Email configuration helper.

**Functionality:**
- Reads email credentials from environment variables
- Provides fallback empty strings if not set
- Used by `login.py` for OTP email delivery

---

## Database Schema

### Table: employee
| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| eid | INTEGER | PRIMARY KEY AUTO | Employee ID |
| name | TEXT | NOT NULL | Employee full name |
| email | TEXT | NOT NULL UNIQUE | Email address |
| gender | TEXT | - | Male/Female/Other |
| contact | TEXT | NOT NULL | Phone number |
| dob | TEXT | - | Date of Birth (YYYY-MM-DD) |
| doj | TEXT | NOT NULL | Date of Joining |
| pass | TEXT | NOT NULL | Password (plaintext) |
| utype | TEXT | - | User Type (Admin/Staff) |
| address | TEXT | - | Residential address |
| salary | REAL | - | Monthly salary |

### Table: supplier
| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| invoice | INTEGER | PRIMARY KEY | Invoice number |
| name | TEXT | NOT NULL | Supplier name |
| contact | TEXT | NOT NULL | Contact number |
| desc | TEXT | - | Description/notes |

### Table: category
| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| CId | INTEGER | PRIMARY KEY AUTO | Category ID |
| name | TEXT | NOT NULL UNIQUE | Category name |

### Table: product
| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| pid | INTEGER | PRIMARY KEY AUTO | Product ID |
| Category | INTEGER | FOREIGN KEY | Reference to category.CId |
| Supplier | INTEGER | FOREIGN KEY | Reference to supplier.invoice |
| name | TEXT | NOT NULL | Product name |
| price | REAL | NOT NULL | Selling price |
| qty | INTEGER | NOT NULL | Current quantity in stock |
| status | TEXT | - | Active/Inactive status |

### ER Diagram
```
employee (1) -------- (Many) product
supplier (1) -------- (Many) product
category (1) -------- (Many) product
```

---

## Usage Guide

### Starting Fresh

1. **Launch Application:**
   ```bash
   python login.py
   ```

2. **Login with Default Admin:**
   - ID: `1`
   - Password: `123`

3. **Change Default Password:**
   - Go to Dashboard → Employee Management
   - Find Employee ID 1
   - Edit and update password

4. **Setup Initial Data:**
   - Dashboard → Supplier Management: Add suppliers
   - Dashboard → Category Management: Add product categories
   - Dashboard → Product Management: Add products

### Daily Operations

#### Billing (POS)
1. Click **Billing** on Dashboard
2. Use search to find products
3. Enter quantity and add to cart
4. Verify cart total
5. Click **Generate Bill**
6. Bill auto-saves to `data/bills/`

#### Inventory Check
1. Click **Product Management** on Dashboard
2. View all products with current quantities
3. Use search/filter to find specific products

#### Employee Management
1. Click **Employee Management** on Dashboard
2. Add new staff, update profiles, or deactivate employees

#### Supplier & Category Management
Similar workflows for managing suppliers and categories.

---

## Building Executable

### Prerequisites
- cx-Freeze 8.6.3 (automatically installed via `requirements.txt`)
- Windows 10/11

### Build Process
```bash
cd "Project Files"
python setup.py build
```

This generates:
- Standalone executable in `build/exe.win-amd64-3.xx/`
- All dependencies bundled (Tkinter, PIL, etc.)
- No Python installation required for end users

### Running the Built Executable
Navigate to `build/exe.win-amd64-3.xx/` and run `login.exe`.

---

## Security Features

### 🔒 Implemented Security Measures

1. **Input Validation:**
   - OTP validation ensures numeric-only input
   - Product quantity must be numeric
   - Email format validation

2. **SQL Injection Prevention:**
   - All database queries use parameterized statements
   - Column whitelisting via `col_map` dictionaries
   - No string concatenation in SQL queries

3. **File I/O Safety:**
   - Context managers (`with` statements) for all file operations
   - Resource cleanup guaranteed even on exceptions

4. **Environment-Based Secrets:**
   - Email credentials read from env vars, not hardcoded
   - No secrets in version control

5. **Error Handling:**
   - Try-catch blocks on critical operations
   - Graceful error messages for users
   - No stack traces exposed to end users

### ⚠️ Known Limitations

1. **Plaintext Passwords:** Employee passwords currently stored as plaintext. For production, implement password hashing (bcrypt, argon2).
2. **No Role-Based Access Control:** All logged-in users have admin access.
3. **No Audit Logging:** Changes not tracked for compliance.
4. **No Data Encryption:** Database file not encrypted.

### Recommended Improvements
- Migrate to hashed passwords (bcrypt/Argon2)
- Implement role-based permissions
- Add audit logging for compliance
- Encrypt sensitive database columns
- Use OAuth/SSO for authentication

---

## Troubleshooting

### Issue 1: Application Won't Start

**Problem:** Double-clicking `login.py` does nothing or shows an error.

**Solutions:**
1. Check Python is installed:
   ```bash
   python --version
   ```
2. Install dependencies:
   ```bash
   cd "Project Files"
   pip install -r requirements.txt
   ```
3. Try running from command line to see error:
   ```bash
   python login.py
   ```

---

### Issue 2: "ModuleNotFoundError: No module named 'PIL'"

**Problem:** Pillow not installed.

**Solution:**
```bash
pip install Pillow==12.1.1
```

---

### Issue 3: Database File Not Found

**Problem:** `ims.db` missing or `data/` folder not present.

**Solution:**
```bash
cd "Project Files"
python create_db.py
```

This creates the database with all necessary tables.

---

### Issue 4: "Cannot Connect to Database"

**Problem:** Database locked or corrupted.

**Solutions:**
1. Close all instances of the application
2. Check file permissions on `data/ims.db`
3. Delete `data/ims.db` and rebuild: `python create_db.py`

---

### Issue 5: OTP Email Not Sending

**Problem:** "Forgot Password" feature doesn't send emails.

**Solutions:**
1. Check environment variables are set:
   ```powershell
   $env:IMS_EMAIL
   $env:IMS_EMAIL_PASS
   ```
   Both should return values (not blank).

2. If using Gmail, ensure:
   - 2-Factor Authentication is enabled on Google Account
   - You're using an **App Password** (not regular Gmail password)
   - The 16-character app password is set correctly

3. Check internet connectivity (required for SMTP)

4. Review error message in console for specific SMTP error codes

---

### Issue 6: Slow Startup or Lag

**Problem:** Application takes time to start or feels sluggish.

**Solutions:**
1. Ensure adequate system RAM (2GB+ recommended)
2. Close other applications
3. Check disk space (at least 500MB free)
4. If database is very large (1000+ products), consider optimizing queries

---

### Issue 7: Bill Not Generating

**Problem:** Clicking "Generate Bill" shows error.

**Solutions:**
1. Verify cart is not empty
2. Check customer info is filled
3. Ensure `data/bills/` folder exists (if not, create it manually)
4. Check write permissions on `data/bills/`

---

## Development

### Project Architecture

The application follows an **Object-Oriented Design** with a **Tkinter-based MVC pattern:**
- **Model:** SQLite database (`ims.db`)
- **View:** Tkinter GUI windows
- **Controller:** Python modules (employee.py, product.py, etc.)

### Code Standards

- **Naming:** Snake_case for functions/variables, CamelCase for classes
- **Documentation:** Docstrings on all major functions
- **Error Handling:** Try-catch blocks on I/O and database operations
- **SQL:** Parameterized queries only, no string concatenation

### Adding a New Module

To add a new feature (e.g., Customer Manager):

1. Create `customer.py` in `Project Files/`
2. Define a class inheriting from Tkinter `Toplevel`
3. Implement CRUD operations with parameterized SQL
4. Import and add button in `Dashboard.py`
5. Add database table in `create_db.py`

### Database Query Examples

**Safe (Parameterized):**
```python
cursor.execute("SELECT * FROM product WHERE name LIKE ?", (f"%{search_term}%",))
```

**Unsafe (DO NOT USE):**
```python
cursor.execute(f"SELECT * FROM product WHERE name LIKE '%{search_term}%'")  # SQL injection risk
```

### File Structure Best Practices
- Keep related modules in same folder
- Use `assets/` for images, icons
- Use `data/` for database and generated files
- Use `tools/` for build and external dependencies

---

## License

This project is open-source and distributed under the **MIT License**.

For more details, see LICENSE file (if present) or contact the project maintainer.

---

## Support & Contact

For issues, feature requests, or contributions:
- **GitHub:** https://github.com/Ananth-Jinde/Inventory-Management-System
- **Email:** jinde.ananth@example.com
- **Issues Page:** Create a GitHub issue with detailed description and steps to reproduce

---

## Changelog

### Version 1.0.0 (Current)
- ✅ Core CRUD modules (Employee, Supplier, Category, Product)
- ✅ POS Billing system
- ✅ User authentication with password reset
- ✅ Dashboard with real-time stats
- ✅ Bill history tracking
- ✅ SQLite database integration
- ✅ Tkinter GUI interface
- ✅ Security hardening (parameterized SQL, input validation)
- ✅ Environment-based configuration
- ✅ Windows executable build support (cx-Freeze)

### Future Enhancements (Roadmap)
- 🔜 Password hashing (bcrypt)
- 🔜 Role-based access control (RBAC)
- 🔜 Audit logging
- 🔜 Customer master data table
- 🔜 Advanced reporting (PDF export, charts)
- 🔜 Multi-user concurrent access
- 🔜 Mobile app companion
- 🔜 Cloud database integration
- 🔜 Barcode/QR code scanning
- 🔜 Email receipt delivery

---

**Last Updated:** March 30, 2026  
**Version:** 1.0.0  
**Status:** Stable
