# guess list 
friends = ["Leona", "Aliyah", "Gwen", "Jayde", "Daniella", "Francis"]
print ("Official Guest List: ")
print (friends)
print ()

# Problem 
friends_1 = ["Leona", "Aliyah", "Gwen", "Jayde", "Daniella", "Francis"]
print(f"Sorry {friends_1.pop(3)} , I can't invite you to the late night dinner.")
print(f"Sorry {friends_1.pop(4)} , I can't invite you to the late night dinner.")
print(f"Sorry {friends_1.pop(2)} , I can't invite you to the late night dinner.")
print ()

# Guess who have been removed 
removed = ["Jayde" , "Francis" , "Gwen"]
msg = """ Due to some problem with table plan, 
I can't invite you now to my late night dinner."""
print (f'Sorry, {removed [0] + msg}')
print (f'Sorry, {removed [1] + msg}')
print (f'Soryy, {removed [2] + msg}')
print () 

# Guess who is still invited 
inv = ["Leona" , "Aliyah"]  
msg = " You are still invited to my late night dinner"
print (f'Hello!, {inv [0] + msg}')
print (f'Hello!, {inv [1] + msg}')

# Empty the guess list 
inv = ["Leona" , "Aliyah"]  
del(inv[0])
del(inv[1])

