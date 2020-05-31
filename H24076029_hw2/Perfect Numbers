n=int(input("Input the range number: "))
print("Perfect numbers: ")

i=2 # i 為可能的perfect number
while i<=n: 
	j=1 # j為i的因數
	s=0 # s為i的因數和
	while i>=j: # 判斷i的因數為哪些
		if (i%j==0) :
			s=s+j # 加總i的所有因數
		j=j+1
	if s==i*2: # 當i的所有因數和為i的兩倍，i就是perfect number
		print(i)

	i=i+1 # 尋找其他可能的perfect number
