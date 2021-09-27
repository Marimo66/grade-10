print("Welcome to Camel!")
print("This is a classic text-based game but with a simple story change!")
print()

print("So now that I've said that, welcome to Science Lab! You have been taken hostage and placed into a research labratory where a mad scientist plans on using you for their evil experiments! Due to a poisonous gas leak, you were given a chance in the chaos and managed to break out of your original confined space. Now while the gas is floating closer and closer, you must run for your life and reach the exit before the gas envelops you!")
print()
print("You start off with the 3 sandwiches they gave you for a previous lunch.")
print("At 6 hunger and tiredness, you will lose. Be sure to keep an eye on your status.")
print()
print("So now that you know the goal, what action will you take?")

#variables
import random

done = False
metres_traveled = 0
hunger = 0
tiredness = 0
#If hunger reaches 6, the user dies. 3 is when you get hungry. If tiredness reaches 6, the user cannot travel any further, 3 as well for tired. 
#If the gas is less than 50 metres behind, it is getting really close.
#If the user travels 500 metres, they win. 

gas_distance = -50
sandwich_storage = 3
	

while not done:
	
	if metres_traveled >= 500 and done != True:
		print("You see the exit ahead! Pushing yourself to run the last few metres, you leap out of the door and take a deep breath at the fresh air. You made it out alive!")
		print("Game complete!")
		print(f"Completed with {hunger} hunger, {tiredness} tiredness!")
		done = True
		exit()
	
	print()
	
	print("A. Stop and take a short breath.")
	print("B. Walk forward.")
	print("C. Run faster ahead.")
	print("D. Eat a sandwich")
	print("E. Status check.")
	print("Q. Quit.")
	
	userchoice = input()
	
	if userchoice.upper() == "Q":
		print()
		print("Quitting...")
		done = True
		exit()
		
	elif userchoice.upper() == "A":
		print()
		if tiredness > 0:
			tiredness -= 1
			print("You rest for a few seconds. -1 tiredness.")
		else:
			print("You were not tired and didn't need to rest!")
			
		gas_distance += random.randrange(20, 51)
		print("The gas moves up and is now", metres_traveled - gas_distance, "m away.")
		
	elif userchoice.upper() == "B":
		print()
		metres_walked = random.randrange(40, 81)
		metres_traveled += metres_walked
		if metres_traveled < 500:
			print(f"You walked {metres_walked}m and are now", 500 - metres_traveled, "m away from the exit.")
			hunger += 1
			tiredness += 1
			gas_distance += random.randrange(20, 51)
			print("The gas moves up and is now", metres_traveled - gas_distance, "m away.")
	
	elif userchoice.upper() == "C":
		print()
		metres_ran = random.randrange(60, 101)
		metres_traveled += metres_ran
		if metres_traveled < 500:
			print(f"You ran {metres_ran}m and are now", 500 - metres_traveled, "m away from the exit.")
			hunger += random.randrange(1, 4)
			tiredness += random.randrange(1, 4)
			gas_distance += random.randrange(20, 51)
			print("The gas moves up and is now", metres_traveled - gas_distance, "m away.")
		
	elif userchoice.upper() == "D":
		print()
		if sandwich_storage > 0:
			hunger -= random.randrange(1, 3)
			tiredness -= random.randrange(1, 3)
			print("You took one sandwich and ate while you ran. -1 hunger and tiredness.")
		elif sandwich_storage <= 0: 
			print("No sandwichs in storage!")
		gas_distance += random.randrange(20, 51)
		print("The gas moves up and is now", metres_traveled - gas_distance, "m away.")
		
	elif userchoice.upper() == "E":
		print()
		print(f"Hunger level: {hunger}\nTiredness: {tiredness}\nSandwich storage amount: {sandwich_storage}\nMetres traveled: {metres_traveled}m\nThe poisonous gas is", metres_traveled - gas_distance, "m away from you.")
		
	if hunger == 3:
		print("You are hungry!")
	elif hunger == 4 or hunger == 5:
		print("You are very hungry!")
	elif hunger >= 6:
		print("You die of hunger!")
		done = True
		exit()

	if tiredness == 3:
		print("You are getting tired.")
	if tiredness == 4 or tiredness == 5:
		print("You are tired.")
	if tiredness >= 6:
		print("You start to feel your legs go out under you. You become too tired to move further. The gas catches up and the world goes dark.")
		done = True
		exit()
	
	if gas_distance >= metres_traveled:
		print("The gas has caught up to you! You suffocate and the world goes dark.")
		done = True
		quit()
	elif metres_traveled - gas_distance <= 50:
		print("The gas is getting close!")

	allychance = random.randrange(1,21)
	if allychance == 1 and done == False:
		distancehelped = random.randrange(20, 101)
		metres_traveled += distancehelped
		print()
		print(f"Someone working in the lab feels bad about what they are doing and decides to assist you. They transport you {distancehelped}m and you get time to fully rest up and eat.")
		tiredness = 0
		hunger = 0
		gas_distance += random.randrange(20, 51)
		print("The gas moves up and is now", metres_traveled - gas_distance, "m away.")
