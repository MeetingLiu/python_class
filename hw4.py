import random
import time

column = ["a","b","c","d","e","f","g","h","i"]
rule = "Enter the column followed by the row (ex: a5). To add or remove a flag, add \'f\' to the cell (ex: a5f)." 
player_list=[]

mines=10
correct_mines=0

def plot_table(player_list):
	'''
	給定玩家遊戲格後，列印出table
	'''
	print(" ",end="")
	# 印出行的編號
	for i in range(len(column)):
		print("   "+column[i],end="")
	print()
	i=1
	# 印出每一列
	while i<len(player_list)-1:
		for n in range(1,10):
			print("  "+"+---"*9+"+")
			print(n,end="")
			j=1
			while j<len(player_list[i])-1:
				print(" | "+str(player_list[i][j]),end="")
				j=j+1
			print(" |")
			i=i+1
	print("  "+"+---"*9+"+")
	return "\t"
	 

def new_game():
	'''
	開始一個新的遊戲，創造一個玩家遊戲格，並列印出空白遊戲格，且說明規則。
	返回空白遊戲格，地雷數以及命中地雷數。
	'''
	# 列11個list， 每個list有11個字串，方便計算
	player_list=[]
	for i in range(1,12):
		a=[]
		for j in range(1,12):
			a.append(" ")
		# print(a)
		player_list.append(a)
	print(plot_table(player_list))
	# 印出規則
	print(rule+"Type \'help\' to show this message again\n")
	mines=10
	correct_mines=0
	for i in range(len(player_list)):
		mines -= player_list[i].count("F")
	return (player_list, mines, correct_mines)

def check_valid():
	'''
	讓玩家輸入位置，檢查是否符合格式。
	返回位置(字串)以及其位置(幾行幾列)
	'''
	while True:
		cell=input("Enter the cell (%d mines left): " % (10-(time.time()-tStart)//60))
		# print(cell[0],cell[1])
		if cell=="help":
			print(plot_table(player_list))
			print(rule+"\n")
			continue
		# 先檢查行在不再範圍裡
		if cell[0] not in "abcdefghi":
			print(plot_table(player_list))
			print("Invalid cell. "+rule+"\n")
			continue
		# 再檢查列在不在範圍裡
		if int(cell[1]) not in range(1,10):
			print(plot_table(player_list))
			print("Invalid cell. "+rule+"\n")
			continue
		elif int(cell[1]) in range(1,10):
			break
	#將行換成數字
	data={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9} 
	#位置字串
	input_s=str(cell) 
	#幾行幾列
	input_no=str(data[cell[0]])+str(cell[1]) 

	return (input_s, input_no)

def creat_ans(input_no):
	'''
	剩餘80位置隨機抽取10個放入地雷
	並計算個位置的數值
	返回答案list
	'''
	# 第一個選的位置必為0
	player_list[int(input_no[1])][int(input_no[0])]="0"	
	# 將每個位置都編號，在player_table中隨機取10個位子
	_r=[]
	for i in range(1,10):
		_r += list(range(2+11*i,10+1+11*i))
	a=int(input_no[1])*11+int(input_no[0])+1
	r=[]
	# 考慮如果是在第一列，最後一列，第一行，最後一行
	if int(input_no[0])==1:
		if int(input_no[1])==1:
			r=_r[_r.index(a+2):_r.index(a+11-3)+1]+_r[_r.index(a+11+2):]
		elif int(input_no[1])==9:
			r=_r[:_r.index(a-11-3)+1]+_r[_r.index(a-11+2):_r.index(a-3)+1]+_r[_r.index(a+2):]
		else:
			r=_r[:_r.index(a-11-3)+1]+_r[_r.index(a-11+2):_r.index(a-3)+1]+_r[_r.index(a+2):_r.index(a+11-3)+1]+_r[_r.index(a+11+2):]
	elif int(input_no[0])==9:
		if int(input_no[1])==1:
			r=_r[:_r.index(a-1)]+_r[_r.index(a+3):_r.index(a+11-1)]+_r[_r.index(a+11+3):]
		elif int(input_no[1])==9:
			r=_r[:_r.index(a-11-1)]+_r[_r.index(a-11+3):_r.index(a-1)]
		else:
			r=_r[:_r.index(a-11-1)]+_r[_r.index(a-11+3):_r.index(a-1)]+_r[_r.index(a+3):_r.index(a+11-1)]+_r[_r.index(a+11+3):]
	else:
		r=_r[:_r.index(a-11-1)]+_r[_r.index(a-11+2):_r.index(a-1)]+_r[_r.index(a+2):_r.index(a+11-1)]+_r[_r.index(a+11+2):]
	# sample不會重複取樣
	lis=random.sample(r, k=10)
	ans_list=[]
	for i in range(1,12):
		ans_list.append([0]*11)
	for i in lis:
		ans_list[i//11][(i%11)-1]="X"
	# 判斷每個位置的數字
	i=1
	while 1<=i<=len(ans_list)-2:
		j=1
		while 1<=j<=len(ans_list[i])-2:
			if ans_list[i][j]=="X":
				if ans_list[i-1][j]!="X":
					ans_list[i-1][j]=int(ans_list[i-1][j])+1
				if ans_list[i+1][j]!="X":
					ans_list[i+1][j]=int(ans_list[i+1][j])+1
				if ans_list[i][j-1]!="X":
					ans_list[i][j-1]=int(ans_list[i][j-1])+1
				if ans_list[i][j+1]!="X":
					ans_list[i][j+1]=int(ans_list[i][j+1])+1
				if ans_list[i-1][j-1]!="X":
					ans_list[i-1][j-1]=int(ans_list[i-1][j-1])+1
				if ans_list[i-1][j+1]!="X":
					ans_list[i-1][j+1]=int(ans_list[i-1][j+1])+1
				if ans_list[i+1][j-1]!="X":
					ans_list[i+1][j-1]=int(ans_list[i+1][j-1])+1
				if ans_list[i+1][j+1]!="X":
					ans_list[i+1][j+1]=int(ans_list[i+1][j+1])+1
			j=j+1
		i=i+1
	return ans_list

def check_0_list(input_no,player_list,ans_list):
	'''
	輸入位置，玩家遊戲格，答案list
	判斷位置是否為0，且是否九宮格內有0，只要有0的地方周圍都要print出來
	並print出遊戲格
	最後返回玩家遊戲格
	'''
	# 如果判斷的格子為0，要去找他周圍的0
	if ans_list[int(input_no[1])][int(input_no[0])]==0:
		_0_list=[input_no]
		# 把是0的位置放到_0_list裡面，再一一去比對
		i=0
		while i<len(_0_list):
			r=int(_0_list[i][1])
			c=int(_0_list[i][0])
			# 把0周圍邊界的格子都印出來
			if ans_list[r][c]==0:
				player_list[r][c]==ans_list[r][c]
				if r-1>=1:
					if player_list[r-1][c]==" ":
						if ans_list[r-1][c]!="X":
							if ans_list[r-1][c]==0:
								_0_list.append(str(c)+str(r-1))	 
							player_list[r-1][c]=ans_list[r-1][c]
				if r+1<=9:
					if player_list[r+1][c]==" ":
						if ans_list[r+1][c]!="X":
							if ans_list[r+1][c]==0:
								_0_list.append(str(c)+str(r+1))	 
							player_list[r+1][c]=ans_list[r+1][c]
				if c-1>=1:
					if player_list[r][c-1]==" ":
						if ans_list[r][c-1]!="X":
							if ans_list[r][c-1]==0:
								_0_list.append(str(c-1)+str(r))	 
							player_list[r][c-1]=ans_list[r][c-1]
				if c+1<=9:
					if player_list[r][c+1]==" ":
						if ans_list[r][c+1]!="X":
							if ans_list[r][c+1]==0:
								_0_list.append(str(c+1)+str(r))	 
							player_list[r][c+1]=ans_list[r][c+1]
				if r-1>= 1:
					if c-1>=1:
						if player_list[r-1][c-1]==" ":
							if ans_list[r-1][c-1]!="X":
								if ans_list[r-1][c-1]==0:
									_0_list.append(str(c-1)+str(r-1))	 
								player_list[r-1][c-1]=ans_list[r-1][c-1]
				if r-1>=1 :
					if c+1<=9 :
						if player_list[r-1][c+1]==" ":
							if ans_list[r-1][c+1]!="X":
								if ans_list[r-1][c+1]==0:
									_0_list.append(str(c+1)+str(r-1))	 
								player_list[r-1][c+1]=ans_list[r-1][c+1]
				if r+1<=9 :
					if c-1>=1:
						if player_list[r+1][c-1]==" ":
							if ans_list[r+1][c-1]!="X":
								if ans_list[r+1][c-1]==0:
									_0_list.append(str(c-1)+str(r+1))	 
								player_list[r+1][c-1]=ans_list[r+1][c-1]
				if r+1<=9:
					if c+1<=9:
						if player_list[r+1][c+1]==" ":
							if ans_list[r+1][c+1]!="X":
								if ans_list[r+1][c+1]==0:
									_0_list.append(str(c+1)+str(r+1))	 
								player_list[r+1][c+1]=ans_list[r+1][c+1]
			i=i+1
	# 如果判斷的格子不為0，就直接印出來
	else:
		player_list[int(input_no[1])][int(input_no[0])]=ans_list[int(input_no[1])][int(input_no[0])]
	print(plot_table(player_list))
	return(player_list)

def put_flag(input_s,input_no,mines,correct_mines):
	'''
	輸入字串，位置，地雷剩餘數，命中地雷數
	如果玩家輸入為長度3的字串，進行插旗子，拿旗子，或是判斷不能放旗子
	返回玩家遊戲格，剩餘地雷數，命中地雷數
	'''
	if len(input_s)==3:
		if input_s[2]=="f":
			# 原格子為空白的才能插旗子
			if player_list[int(input_no[1])][int(input_no[0])]==" ":
				player_list[int(input_no[1])][int(input_no[0])]="F"
				mines-=1
				if ans_list[int(input_no[1])][int(input_no[0])]=="X":
					correct_mines+=1
				print(plot_table(player_list))
			# 原格子已經有旗子，可以把旗子拿掉
			elif player_list[int(input_no[1])][int(input_no[0])]=="F":
				player_list[int(input_no[1])][int(input_no[0])]=" "		
				mines+=1
				if ans_list[int(input_no[1])][int(input_no[0])]=="X":
					correct_mines-=1
				print(plot_table(player_list))			
			else:
				print(plot_table(player_list))
				print("Cannot put a flag there\n")			
	return (player_list,mines,correct_mines)


def win_or_not(correct_mines):
	'''
	輸入命中地雷數
	如果命中地雷數到達10，則print出玩家花費時間
	返回是否贏得遊戲
	'''
	spent=time.time()-tStart
	if correct_mines==10:
		print("You win. It took you %d minutes and %d seconds." % (spent//60, spent%60))
		print()
		return True
	else:
		False
def play_again(ans_list):
	'''
	輸入答案list
	列印出答案，詢問玩家是否重新一局
	返回是否開新局
	'''
	print(plot_table(ans_list))
	again=input("Play again? (y/n):")
	if again=="y":
		return new_game()
	else:
		exit(0)
def flag_there(input_no):
	'''
	輸入位置，
	判斷是否已擺放旗子，回傳是否
	'''
	if player_list[int(input_no[1])][int(input_no[0])]=="F":
		print(plot_table(player_list))
		print("There is a flag there\n")
		return True
	else:
		return False

def already_shown(input_no):
	'''
	輸入位置
	回傳是否已出現
	'''
	if player_list[int(input_no[1])][int(input_no[0])]!=" ":
		print(plot_table(player_list))
		print("That cell is already shown\n")
		return True
	else:
		return False

# the following is the main program of minesweeper
game = True
while game:
	tStart = time.time() #開始計時
	player_list,mines,correct_mines = new_game() 
	input_s,input_no = check_valid() 
	ans_list = creat_ans(input_no)
	player_list = check_0_list(input_no,player_list,ans_list)
	while True: 
		input_s,input_no = check_valid()
		player_list,mines,correct_mines = put_flag(input_s,input_no,mines,correct_mines)
		if win_or_not(correct_mines):
			game = play_again(ans_list)
			break
		if len(input_s) == 2:
			if flag_there(input_no) or already_shown(input_no):
				continue
			elif ans_list[int(input_no[1])][int(input_no[0])] == "X":
				print("\n \nGame Over\n")
				game = play_again(ans_list)
				break
			else:
				player_list = check_0_list(input_no,player_list,ans_list)

