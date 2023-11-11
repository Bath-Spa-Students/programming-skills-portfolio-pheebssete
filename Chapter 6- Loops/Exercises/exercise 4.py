# making sandwich list 
sandwich_orders = ['egg', 'ham', 'grilled cheese', 'chicken']
finished_sandwiches = []

# display sandwich orders
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"\nI'm working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"\nI made a {sandwich} sandwich.")
    