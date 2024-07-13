# Making a High Tech calculator
a = input("What state do you you want the calculator to be in")#on or off
if a == "on" or a == "ON" or a == "On":
 a2 = int(input("Enter your first number"))
 a3 = (input("Enter the operator")) # +, -, *, /
 a4 = int(input("Enter the second number"))
 if a3 == "+":
   print(f"The addition of {a2} and {a4} is {a2+a4}")
 elif a3 == "-":
   print(f"The suntraction of {a2} and {a4} is {a2-a4}")
 elif a3 == "*":
   print("The Multiplacation of",a2,"and",a4,"is", a2*a4)
 elif a3 == "/":
   print("The division of",a2,"and",a4,"is",a2/a4)
 else:
   print("invalid operator")
elif a == "off" or a == "OFF" or a == "off":
  print("The calculator is powering off")
else:
  print("invalid state")
  