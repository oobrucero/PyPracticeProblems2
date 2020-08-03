operator = input("Enter the operation you would like to perform(+, -, /, *, **, %): ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if operator == "+":
  print(str(num1) + " + " + str(num2) + " is " + str(num1 + num2))
if operator == "-":
  print(str(num1) + " - " + str(num2) + " is " + str(num1 - num2))
if operator == "/":
  print(str(num1) + " / " + str(num2) + " is " + str(num1 / num2))
if operator == "*":
  print(str(num1) + " * " + str(num2) + " is " + str(num1 * num2))
if operator == "**":
  print(str(num1) + " ** " + str(num2) + " is " + str(num1 ** num2))
if operator == "%":
  print(str(num1) + " % " + str(num2) + " is " + str(num1 % num2))
else:
  print("invalid sign")