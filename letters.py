ustring = input("Enter the string you would like to search through: ")
char = input("Enter the character you would like to know the count of: ")
if len(char) != 1:
  print("That character is invalid")
else:
  upchar = char.upper()
  lowchar = char.lower()
  ustring = ustring.lower()
  print("The letter " + "\"" + upchar + "\"" + " is in your string " + str(ustring.count(lowchar))+ " times.")