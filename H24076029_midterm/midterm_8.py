j=9 # j為後面的數
while j>=1:
	i=9 # i為前面的數
	while i>=1: # print出每一列的樣子
		print(i,"x",j,"=",i*(j),end="\t")
		print(i,"x",j-1,"=",i*(j-1),end="\t")
		print(i,"x",j-2,"=",i*(j-2),end="\n")
		i=i-1
	print() # 空白列
	j=j-3 # i為9個一循環，每一個循環結束使j-3