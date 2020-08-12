list1 = [6, 1, 3, 0, 2]
num = int(input("Enter the number you want to search for: "))
for x in range(0, len(list1)):
  if list1[x] == num:
    print("The number " + str(num) + " is in index position " + str(x) + " in the list.")
    break
  if x == len(list1) - 1:
    print("The number is not in the list.")