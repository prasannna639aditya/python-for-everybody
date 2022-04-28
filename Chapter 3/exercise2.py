"""Rewrite your pay program using try and except so that your
program handles non-numeric input gracefully by printing a message
and exiting the program. The following shows two executions of the
program:
Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input
Enter Hours: forty
Error, please enter numeric input"""
#print("Enter Hours:")
try:
    Hours=int(input("Enter Hours:"))
    Rate=float(input("Enter Rate:"))
    Pay=Hours*Rate
    print("Pay:",Pay)
except:
    print("Error,please enter numeric input")