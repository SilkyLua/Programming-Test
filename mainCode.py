print("This is a public repository!")
name = input("What is your name? ")
print(f'Hello {name}, welcome to the matrix.')

"Elmedin Behluli added this line to the code"
color = input("Favorite color? ")
print(f"{color} is a nice choice!")

#Zabi added this beautiful code
age = input("What is your age? ")
while True:
  if age.isnumeric():
    age = int(age)
    break
  else:
    age = input("What is your age? ")
print(f"Your age is, {age}")
