# adding more sandwiches    
sandwich_orders = [
    'egg', 'ham', 'grilled cheese', 'chicken',
    'seefood', 'rosted beef', 'grilled beef','pastrami','pastrami']
finished_sandwiches = []

# display the out of stock 
print("\nHello, I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# display the sandwishes 
print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"Hi, here's your {sandwich} sandwich.")
    