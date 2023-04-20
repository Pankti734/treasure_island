print("Welcome to Treasure Island.\nYour misiion is to find the treasure.")
direction=input("Enter where do you want to go?")
if direction=="Left":
 choice=input("Do you want to wait or swim?")
 if(choice=="wait"):
   door=input("Enter the door number 1 , 2 or 3")
   if(door=="Red"):
     print("Game over")
   elif(door=="Yellow")
     print("You win")
   elif(door=="Blue")
     print("Game over")
 else:
   print("Game over")
else:
 print("Game over")
