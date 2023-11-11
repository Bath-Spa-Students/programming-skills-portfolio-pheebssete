# Guess list  
friends = ["Leona", "Aliyah", "Gwen", "Jayde"]
msg = "Hello!, you are invited to my late night dinner at my house, "

print (msg + friends [0])
print (msg + friends [1])
print (msg + friends [2])
print (msg + friends [3])
print ()

# Jayde Can't Make It  
print (friends [3] + " can't come to the late night dinner ")
print()

# I'll Invite Ken Instead 
friends = ["Leona", "Aliyah", "Gwen", "Jayde"]
friends[3]= "Ken" 

print ("But, " + friends [3] + " can come to the late night dinner!")
print ()

# Problem 
print (f"\n Sorry {friends.pop(2)} , I can't accomodate you for the late night dinner.")
print (f"\n Sorry {friends.pop(1)} I can't accomodate you for the late night dinner.")
print ()

# Guess who have been removed 
msg = """Due to some problem with table plan, 
 I can't invite you now to my late night dinner. """
print (msg + friends[0])
print (msg + friends[1])
print ()

# Guess who is still invited 
msg = " You are still invited to my late night dinner"
print (f'Hello!, {friends [0] + msg}')
print (f'Hello!, {friends [1] + msg}')
print ()

# Empty the guess list
del(friends [0])
del(friends [0])
print ("Guess List" , friends)
