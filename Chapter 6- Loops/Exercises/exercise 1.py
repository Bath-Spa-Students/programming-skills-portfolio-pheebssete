pizza = ("""\nHello! Welcome to the pizzapie! Put what toppings you want in your pizza:"
type 'quit' in the next enter if your done: """)

#print display
while True:
  add_on = input(pizza)
  if  add_on != "quit":
      print(f"\n Alright! I'll add a " + (add_on) + " to your pizza.")
  else: 
      print("\n Okay, your pizza now making. Thank you!")
      break
  