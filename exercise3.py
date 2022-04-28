"""Write a program to prompt the user for hours and rate per
hour to compute gross pay.
Enter Hours: 35
Enter Rate: 2.75
Pay: 96.25
We won't worry about making sure our pay has exactly two digits after the decimal
place for now. If you want, you can play with the built-in Python round function
to properly round the resulting pay to two decimal places."""

"""As we are compiling the program not interpreting it, 'Hours' and 'Rate' values are taken as string. So I have typecasted them by using int and float"""
print("Enter Hours:")
Hours=int(input())
#print(type(Hours))
print("Enter Rate:")
Rate=float(input())
#print(type(Rate))
Pay=Rate*Hours
#Pay=round(Rate*Hours,1)
print("Pay:",Pay)