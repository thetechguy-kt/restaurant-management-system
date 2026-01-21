# <b>Restaurant Table and Order Management System</b>
[![Documentation](https://img.shields.io/badge/Documentation-available-brightgreen)](./README.md)
[![License: GNU](https://img.shields.io/badge/License-GNU%20v3.0-yellow.svg)](./LICENSE)
![Platforms](https://img.shields.io/badge/Platform-Windows%20|%20Linux-blue)
[![Python](https://img.shields.io/badge/Python-3.11-orange?logo=python)](https://www.python.org/)

<i>A simple, offline restaurant management system with table tracking, order taking, kitchen workflow, and billing — built using Python and Streamlit.</i>

### <i>This project is licensed under the GNU General Public License v3.0 — see the LICENSE file for details.</i>

This multi-part web application is designed to streamline restaurant operations by managing table availability, taking orders linked to tables, displaying kitchen order statuses, and generating bills. The menu is loaded dynamically from an Excel file, and all data is stored locally using JSON files to enable offline use.

### One-Time ChangeLog ###
4th January 2026:
  - The Release 1 is uploaded in GitHub.
  - Some bugs have been fixed.
  - Any Queries can be sent to my E-Mail ID: [karthikeyanvijayabaskar@gmail.com](mailto:karthikeyanvijayabaskar@gmail.com)

For the full ChangeLog: [Click Here](https://github.com/thetechguy-kt/restaurant-management-system/blob/main/Changelog.md)

## Core Modules

1. **Table Management**  
   Manage table statuses: Available or Occupied.  
   Occupying a table when an order is started; releasing when billing is complete.

2. **Order Taking**  
   Select occupied tables, browse the menu (loaded from Excel), add items with quantities, and save orders.

3. **Kitchen View**  
   Displays active orders and their statuses. Kitchen staff can update order status from Pending to Ready.

4. **Billing System**  
   Generate bills for ready orders, and upon payment, reset table status to Available.

5. **Admin Panel**  
   Configure number of tables dynamically.  
   Edit the menu by updating the Excel file (`data/menu.xlsx`).

## Usage
1. Navigate modules from the sidebar: Tables, Order, Kitchen, Billing, Admin.
2. Toggle Touch Mode for tablet-friendly UI.
3. Update tables count dynamically in Admin panel.
4. Edit menu anytime by updating `data/menu.xlsx`.

## Installation of Dependancies
Use the command: `pip install -r requirements.txt`

## Editing of the menu
Create and populate data/menu.xlsx with columns: id, name, price.

**Example:**
| id  | name        | price  |
|-----|-------------|--------|
| 1   | Burger      | 50     |
| 2   | Pizza       | 120    |
| 3   | Sandwich    | 40     |
| 3   | Cold Drink  | 30     |

## Run the app
Run the app using the command: `streamlit run app.py`

# 📁 File Overview

| File/Folder         | Description                                        |
|---------------------|--------------------------------------------------|
| `app.py`            | Main Streamlit app entry point                    |
| `modules/tables.py` | Table management module                           |
| `modules/orders.py` | Order taking module                              |
| `modules/kitchen.py`| Kitchen order status module                      |
| `modules/billing.py`| Billing and checkout module                       |
| `modules/admin.py`  | Admin settings module                             |
| `utils/storage.py`  | JSON read/write utility functions                 |
| `utils/styles.py`   | Touch mode CSS injection                          |
| `utils/menu_loader.py` | Excel menu loader utility                       |
| `data/menu.xlsx`    | Editable menu in Excel format                      |
| `data/tables.json`  | Stores table statuses                              |
| `data/orders.json`  | Stores current orders                              |

<b> Note: 
  - Place all files in a single folder, to make the application work properly. You can also chnage the file's location for your convenience, but don't forget to change in the code also.
</b>

