def factiorial(num):
  answer = 1
  for x in range(1, num + 1):
    answer *= x
  return answer

int1 = int(input("Enter the number you want to find the factorial of: "))
print(factiorial(int1))