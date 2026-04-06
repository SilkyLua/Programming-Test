print("This is a public repository!")
name = input("What is your name? ")
print(f'Hello {name}, welcome to the matrix.')
age = input("What is your age? ")
while True:
  if age.isnumeric():
    age = int(age)
    break
  else:
    age = input("What is your age? ")
print(f"Your age is, {age}")

  
