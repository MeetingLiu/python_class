# 先印出遊戲的格式
# 把game存成list之後比較好編輯
a="+---"*7+"+"
n="|   "*7+"|"
game=[a,n]*6+[a]+["  0   1   2   3   4   5   6"]

k=0
while k<=13:
	print(game[k])
	k+=1

while True:
	while True:
		# 問Player X要選的格子
		X=input("Player X >> ")
		while True:
			if X.isdigit():
				if 0<=int(X)<=6:
					break
				else: # 當輸入的數字超出範圍要再輸入一次
					print("Out of range, try again [0-6].")
					X=input("Player X >> ")
			else: # 當輸入的不是數字要再輸入一次
				print("Invalid input, try again [0-6].")
				X=input("Player X >> ")
		X=int(X) # X為Player X 所選的格子	

		p=2 # p為那一列的第幾個位子
		p=p+X*4
		r=11 # i是第幾列
		if game[1][p]!=" ": # 如果所選的行數已經滿了，就要再選一次
			print("This column is full. Try another column.")
			continue
		# 判斷要放在第幾列	
		while 0<=r<=11:
			if game[r][p]!=" ":
				r=r-2
			else:
				break
		# 更新game的樣子
		game[r]=game[r][0:p]+"X"+game[r][p+1:]
		# 再print出來
		k=0
		while k<=13:
			print(game[k])
			k+=1
		break


	### 判斷當"X"成列時
	### 並把成列的"X"變小
	p=2
	while 2<=p<=26:
		r=11
		s=0
		while 1<=r<=11:
			while game[r][p]=="X":
				s=s+1
				r=r-2
			if s>=4:
				i=1
				while i<=s:
					game[r+2*i]=game[r+2*i][0:p]+"x"+game[r+2*i][p+1:]
					i=i+1
			if game[r][p]!="X":
				r=r-2
				s=0
		p=p+4
	
	### 判斷當"X"成行時
	### 並把成行的"X"變小
	r=11
	while 1<=r<=11:
		p=2
		s=0
		while 2<=p<=26:
			while game[r][p]=="X":
				s=s+1
				p=p+4
				if p>26:
					break
			if s>=4:
				i=1
				while i<=s:
					game[r]=game[r][0:p-4*i]+"x"+game[r][p-4*i+1:]
					i=i+1

			if p>26:
				break
			if game[r][p]!="X":
				p=p+4
				s=0

		r=r-2	
	
	### 判斷"X"由左下到右上連線
	### 並把連線的"X"變小
	p=2	
	r=11
	while 2<=p<=26 and 1<=r<=11:
		s=0
		while game[r][p]=="X":
			s=s+1
			r=r-2
			p=p+4
			if p>26:
				break
		if s>=4:
			i=1
			while i<=s:
				game[r+2*i]=game[r+2*i][0:p-4*i]+"x"+game[r+2*i][p-4*i+1:]
				i=i+1
		if p>26:
			break
		if game[r][p]!="X":
			r=r-2
			p=p+4
			s=0

	### 判斷當"X"由右下到左上連線
	### 並將連線的"X"變小
	p=26	
	r=11
	while 2<=p<=26 and 1<=r<=11:
		s=0
		while game[r][p]=="X":
			s=s+1
			r=r-2
			p=p-4
			if p<2:
				break
		if s>=4:
			i=1
			while i<=s:
				game[r+2*i]=game[r+2*i][0:p+4*i]+"x"+game[r+2*i][p+4*i+1:]
				i=i+1
		if p<2:
			break
		if game[r][p]!="X":
			r=r-2
			p=p-4
			s=0
##### 如果有連線並且"X"已經變小了，Player "X"贏，遊戲結束
	r=11
	while "x" in game[r]:
		k=0
		while k<=13:
			print(game[k])
			k+=1
			while k==13:
				print("Winner: X")
				exit(0)
		r=r-2
##### 如果都沒有連線，格子也都填滿了，平手，遊戲結束


	p=2
	s=0
	while 2<=p<=26:
		if game[1][p]!=" ":
			s=s+1
		p=p+4
	if s==7:
		print("Draw")
		exit(0)





	# 問Player Y要選的格子
	while True:	
		Y=input("Player O >> ")
		while True:
			if Y.isdigit():
				if 0<=int(Y)<=6:
					break
				else: # 當輸入的數字超出範圍要再輸入一次
					print("Out of range, try again [0-6].")
					Y=input("Player O >> ")
			else: # 當輸入的不是數字要再輸入一次
				print("Invalid input, try again [0-6].")
				Y=input("Player O >> ")
		Y=int(Y) # Y為Player O 所選的格子		

		p=2 
		p=p+Y*4 # p為那一列的第幾個位子
		r=11 # i是第幾列
		if game[1][p]!=" ": # 如果所選的行數已經滿了，就要再選一次
			print("This column is full. Try another column.")
			continue
		# 判斷要放第幾行
		while 0<=r<=11:
			if game[r][p]!=" ":
				r=r-2
			else:
				break
		# 更新game的樣子
		game[r]=game[r][0:p]+"O"+game[r][p+1:]
		# 再print出來
		k=0
		while k<=13:
			print(game[k])
			k+=1
		break

		
	
	### 判斷當"O"成列時
	### 並把成列的"O"變小
	p=2
	while 2<=p<=26:
		r=11
		s=0
		while 1<=r<=11:
			while game[r][p]=="O":
				s=s+1
				r=r-2
			if s>=4:
				i=1
				while i<=s:
					game[r+2*i]=game[r+2*i][0:p]+"o"+game[r+2*i][p+1:]
					i=i+1
			if game[r][p]!="O":
				r=r-2
				s=0

		p=p+4
	
	### 判斷當"O"成行時
	### 並把成行的"O"變小
	r=11
	while 1<=r<=11:
		p=2
		s=0
		while 2<=p<=26:
			while game[r][p]=="O":
				s=s+1
				p=p+4
				if p>26:
					break
			if s>=4:
				i=1
				while i<=s:
					game[r]=game[r][0:p-4*i]+"o"+game[r][p-4*i+1:]
					i=i+1
			if p>26:
				break
			if game[r][p]!="O":
				p=p+4
				s=0

		r=r-2	

	### 判斷"O"由左下到右上連線
	### 並把連線的"O"變小
	p=2	
	r=11
	while 2<=p<=26 and 1<=r<=11:
		s=0
		while game[r][p]=="O":
			s=s+1
			r=r-2
			p=p+4
			if p>26:
				break
		if s>=4:
			i=1
			while i<=s:
				game[r+2*i]=game[r+2*i][0:p-4*i]+"o"+game[r+2][p-4*i+1:]
				i=i+1
		if p>26:
			break
		if game[r][p]!="O":
			r=r-2
			p=p+4
			s=0

	### 判斷當"O"由右下到左上連線
	### 並將連線的"O"變小
	p=26	
	r=11
	while 2<=p<=26 and 1<=r<=11:
		s=0
		while game[r][p]=="O":
			s=s+1
			r=r-2
			p=p-4
			if p<2:
				break
		if s>=4:
			i=1
			while i<=s:
				game[r+2*i]=game[r+2*i][0:p+4*i]+"o"+game[r+2*i][p+4*i+1:]
				i=i+1
		if p<2:
			break
		if game[r][p]!="O":
			r=r-2
			p=p-4
			s=0
##### 如果有連線並且"X"已經變小了，Player "X"贏，遊戲結束
	r=11
	while "o" in game[r]:
		k=0
		while k<=13:
			print(game[k])
			k+=1
			while k==13:
				print("Winner: O")
				exit(0)
		r=r-2
	
	### 判斷當平手時
	p=2
	s=0
	while 2<=p<=26:
		if game[1][p]!=" ":
			s=s+1
		p=p+4
	##### 如果都沒有連線，格子也都填滿了，平手，遊戲結束
	if s==7:
		print("Draw")
		exit(0)
		


