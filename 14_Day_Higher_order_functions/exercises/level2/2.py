#Use map to create a new list by changing each number to its square in the numbers list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def square(number):
  return number**2

numbers_square = map(square, numbers)
print(list(numbers_square))
