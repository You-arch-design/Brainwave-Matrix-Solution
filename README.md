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

