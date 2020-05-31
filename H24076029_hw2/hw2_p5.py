# 設置猜拳表格的格式
format="%-15s %-15s %-15s"
print(format%("Player A","Player B","Result"))
print(format%("Rock","Rock","Tie"))
print(format%("Rock","Paper","Player B"))
print(format%("Rock","Scissors","Player A"))
print(format%("Paper","Rock","Player A"))
print(format%("Paper","Paper","Tie"))
print(format%("Paper","Scissors","Player B"))
print(format%("Scissors","Rock","Player B"))
print(format%("Scissors","Paper","Player A"))
print(format%("Scissors","Scissors","Tie"))
print("-"*45)

# 設置Player A、Player B輸入字串時的情況
while True:
	while True:
		A=str(input("Player A? "))
		if A==("bye"):
			exit(0) # 當Player A輸入"bye"就結束整個程式
		elif (A=="rock" or A=="paper" or A=="scissors"):
			break # 當Player A輸入"rock" or "paper" or "scissors"，結束這個迴圈
		else:
			print("Invalid input. Please enter again.")
	while True:
		B=str(input("Player B? "))
		if B==("bye"):
			exit(0) # 當Player B輸入"bye"就結束整個程式
		elif B=="rock" or B=="paper" or B=="scissors":
			break # 當Player B輸入"rock" or "paper" or "scissors"，結束這個迴圈
		else:
			print("Invalid input. Please enter again.")
	print(A,B)
	
	# 判斷Player A，Player B誰贏
	if (A=="rock" and B=="rock"):
		print("Outcome: Tie"+'\n')
	elif (A=="rock" and B=="paper"):
		print("Outcome: Player B wins!"+"\n")
	elif (A=="rock" and B=="scissors"):
		print("Outcome: Player A wins!"+"\n")
	elif (A=="paper" and B=="rock"):
		print("Outcome: Player A wins!"+"\n")
	elif (A=="paper" and B=="paper"):
		print("Outcome: Tie"+"\n")
	elif (A=="paper" and B=="scissors"):
		print("Outcome: Player B wins!"+"\n")
	elif (A=="scissors" and B=="rock"):
		print("Outcome: Player B wins!"+"\n")
	elif (A=="scissors" and B=="paper"):
		print("Outcome: Player A wins!"+"\n")
	elif (A=="scissors" and B=="scissors"):
		print("Outcome: Tie"+"\n")