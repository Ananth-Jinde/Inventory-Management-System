# Inventory Management System

## Overview
This project is an inventory management system built using Tkinter for the graphical user interface and SQLite as the database. It is designed to help users manage their inventory effectively and efficiently.

## Modules
- **Tkinter:** Provides the GUI elements for user interaction.
- **SQLite:** Handles data storage without requiring a separate database server.
- **Pandas (optional):** For data analysis and reporting features.

## Setup
To set up the inventory management system on your local machine, follow these steps:
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Ananth-Jinde/Inventory-Management-System.git
   cd Inventory-Management-System
   ```
2. **Install dependencies:**
   Ensure you have Python installed. Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application
To run the inventory management system, execute:
```bash
python main.py
```
This command will launch the GUI where users can interact with the system.

## Project Structure
- **main.py:** The entry point to the application.
- **gui.py:** Contains all Tkinter GUI components.
- **database.py:** Manages SQLite database connections and queries.
- **utils.py:** Contains helper functions for various tasks.

## Database Schema Summary
The SQLite database consists of the following tables:
- **items:** Stores item details such as name, quantity, and price.
- **categories:** Defines categories to organize items.
- **transactions:** Records all inventory transactions, such as sales and restocking.

## Usage Flow
1. User starts the application.
2. User can add, update, or remove items.
3. The inventory can be viewed in real-time.
4. Users can generate reports based on transactions or item status.

## Troubleshooting
- **Common issues:** If the application fails to start, ensure all dependencies are installed. Review error messages for guidance on missing modules.

## Security Notes
- Ensure that sensitive data is not hardcoded in the application. Use environment variables for sensitive configuration.
- Perform regular updates to dependencies to mitigate security vulnerabilities.