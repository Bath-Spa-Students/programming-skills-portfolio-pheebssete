# variables
age_required = ("\nHi! Welcome to the theater, as the theater has rules, may I know your age? ")
b = ("Type quit if you are finish: ")

# display
while True:
  age = input(age_required)
  age = int(age)
  exit = input(b)
  if b == "quit":
      break
  if age < 3:
      print(" The ticket is free in this level of age. ")
  elif age < 13: 
      print(" The ticket costs $10 in this level of age. ") 
  else:
      print(" The ticket costs $15 in this level of age. ")
      break

      