# Fully Functional ATM in Python  

This is a simple  fully functional ATM program written in Python. It allows users to authenticate using a PIN, check their balance, deposit money, and withdraw funds.  

## Features  

- User authentication with a PIN (3 attempts allowed)  
- Check account balance  
- Deposit money  
- Withdraw money (with validation for sufficient balance)  
- User-friendly menu-driven interface  

## Prerequisites  

- Python 3.x installed  

## How to Run  

1. Clone this repository or download the ATM.py file.  
2. Open a terminal and navigate to the project directory.  
3. Run the script using:  

   bash
   python ATM.py
     

4. Enter your PIN (default: 1234).  
5. Choose an option from the menu to perform transactions.  

## Example Usage  


Enter your PIN: ****  
Authentication successful!  

1. Check Balance  
2. Deposit  
3. Withdraw  
4. Exit  
Choose an option: 1  
Your balance: $1000  


## Customization  

- You can change the default balance and PIN by modifying the __init__ method in the ATM class.  
- The number of authentication attempts can also be adjusted in the authenticate() method.  

## License  

This project is open-source and available for educational purposes.  




### Task 2
# Inventory Management System

## Overview
The **Inventory Management System** is a simple desktop application built using Python and Tkinter. It provides an easy-to-use graphical user interface (GUI) for managing inventory items, including adding, updating, removing, and displaying inventory records.

## Features
- **Add Items**: Enter item name and quantity to add an item to the inventory.
- **Mark Essential Items**: Checkbox option to mark an item as essential.
- **Update Items**: Modify the quantity of an existing item.
- **Remove Items**: Delete an item from the inventory.
- **Reset Inventory**: Clear all inventory records.
- **Show Inventory**: Display all stored inventory records in a pop-up.
- **Treeview Table**: Visual representation of inventory with sortable columns.

## Technologies Used
- **Python**: Core programming language.
- **Tkinter**: GUI framework for creating the user interface.
- **ttk (Themed Tkinter Widgets)**: Used for enhanced UI components.
- **messagebox**: Provides alerts and notifications.

## Installation & Setup
### Prerequisites
Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Steps to Run
1. Clone or download the project repository.
2. Navigate to the project directory.
3. Run the following command in the terminal or command prompt:
   ```bash
   python you.py
   ```

## How to Use
1. **Add an Item**:
   - Enter the item name in the "Item Name" field.
   - Enter the quantity in the "Quantity" field.
   - (Optional) Check the "Mark as Essential" box.
   - Click the "Add Item" button.

2. **Update an Item**:
   - Select an item from the list.
   - Modify the quantity in the input field.
   - Click "Update Item."

3. **Remove an Item**:
   - Select an item from the list.
   - Click "Remove Item."

4. **View Inventory**:
   - Click "Show Inventory" to display all items in a pop-up message.

5. **Reset Inventory**:
   - Click "Reset Inventory" to clear all stored items.

## File Structure
```
Inventory Management System
│── you.py  # Main application script
│── README.md  # Documentation file
```

## Future Enhancements
- Add database support (SQLite) for persistent data storage.
- Implement search functionality.
- Include filtering and sorting features for inventory items.
- Export inventory data to CSV format.

## License
This project is open-source and free to use for educational purposes.


