import random
print("Beat the Number 21")
print("You know the rules")
print("The first to reach 21 is the winner")
print("Use your best strategy to reach the number 21")
print("And also you can only move ahead upto 3 numbers forward")

start = str(input("Do you want to start the game(Y/N): "))
if start == "Y" or "y": #error here fix this make only available for any y or y
	print("Here you go")
	def game(a):
		
		cpu = int(a) + 3
		cpu_sys = random.randint(int(a)+1,cpu)

		if cpu_sys <=21:
			print(" ")	
		if cpu_sys == 21:
			print("CPU: 21")
			print("Oops you lost the game!! ")
			exit()
		elif int(a) == 21:
			print("YAAAYYYY!! Congratulation! You won the game!! ")
			exit()
		elif int(a) >= 22:
			print("You enterred out of boundary!")
			return
		if int(a) == 20:
			print(" \n CPU: 21 \n You lost the game!!")
			exit()
		if int(a) == 18:
			print(" \n CPU: 21 \n You lost the game!!")
			exit()
		if int(a) == 19:
			print(" \n CPU: 21 \n You lost the game!!")
			exit()
		print("\nCPU: ", cpu_sys)

	while True:
		b = input("\nYour play: ")
		if b == 21:
			print("YAAAYYYY!! Congratulation! You won the game!! ") 
			break
		game(b)


else:
	print("So you don't wanna play! ")