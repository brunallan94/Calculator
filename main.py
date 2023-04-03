# Creating a calculator

import logging

# configuring logging module
logging.basicConfig(level = logging.DEBUG,
                    format = "%(asctime)s - %(levelname)s - %(message)s")

def add(x, y):
    logging.info(f"{x} + {y} = {int(x)+int(y)}")

def subtract(x, y):
    logging.info(f"{x} - {y} = {int(x)-int(y)}")
    
def multiply(x, y):
    logging.info(f"{x} x {y} = {int(x)*int(y)}")

def divide(x = int, y = int):
    logging.info(f"{x} / {y} = {int(x)/int(y)}")

logging.info('WELCOME TO CALCULATOR \n')
logging.info("""         A. addition
         B. subtraction
         C. multiplication
         D. division""")

while True:
    answer = input('Select the choices from above or q to quit:')
    
    if answer.lower() == "a":
        x = input('write your first number here: ')
        y = input('write your second number here: ')
        if x.isdigit() and y.isdigit():
            x = int(x)
            y = int(y)
        else:
            logging.warning("Please type in a number!!! \n")
            continue
            
        add(x, y)
        
    elif answer.lower() == "b":
        x = input('write your first number here: ')
        y = input('write your second number here: ')
        if x.isdigit() and y.isdigit():
            x = int(x)
            y = int(y)
        else:
            logging.warning("Please type in a number!!! \n")
            continue
            
        x = input('write your first number here: ')
        y = input('write your second number here: ')
        subtract(x, y)
        
    elif answer.lower() == "c":
        x = input('write your first number here: ')
        y = input('write your second number here: ')
        if x.isdigit() and y.isdigit():
            x = int(x)
            y = int(y)
        else:
            logging.warning("Please type in a number!!! \n")
            continue
            
        x = input('write your first number here: ')
        y = input('write your second number here: ')
        multiply(x, y)
        
    elif answer.lower() == "d":
        x = input('write your first number here: ')
        y = input('write your second number here: ')
        if x.isdigit() and y.isdigit():
            x = int(x)
            y = int(y)
        else:
            logging.warning("Please type in a number!!! \n")
            continue
            
        x = input('write your first number here: ')
        y = input('write your second number here: ')
        divide(x, y)
        
    elif answer.lower() == "q":
        logging.info("GOODBYE!")
        break
    
    else:
        logging.error("Put in the correct keyword!!!")
        continue
    
    
    
    
