operator = input("Enter the operation you would like to perform(+, -, /, *, **, %): ")
int1 = int(input("Enter the first number: "))
int2 = int(input("Enter the second number: "))
if operator == "+":
  print(str(int1) + " + " + str(int2) + " is " + str(int1 + int2))
elif operator == "-":
  print(str(int1) + " - " + str(int2) + " is " + str(int1 - int2))
elif operator == "/":
  print(str(int1) + "/" + str(int2) + " is " + str(int1 / int2))
elif operator == "*":
  print(str(int1) + " * " + str(int2) + " is " + str(int1 * int2))
elif operator == "%":
  print(str(int1) + " % " + str(int2) + " is " + str(int1 % int2))
elif operator == "**":
  print(str(int1) + "^" + str(int2) + " is " + str(int1 ** int2))
else:
  print("The operator you entered is not valid")