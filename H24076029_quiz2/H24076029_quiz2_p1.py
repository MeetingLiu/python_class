### (a)+(b)


t=1
while True:
	sn=str(input("(a)+(b): Enter a positive integer with square-number length: "))
	while t**2<len(sn):
		if len(sn)==t**2:
			break
		t=t+1
	if len(sn)==t**2: # 若確定字數為平方數就繼續
		break
	else:
		print("Not square-number length. Try again!") # 若字數不為平方數就重來一次

### (c) 把數字變成list
print("(c) Put numbers into a 1-dim list, and print out.")
dim1=[]
i=0
while i<len(sn):
	dim1 += [int(sn[i])] # 一個一個取出來
	i=i+1
print(dim1)
print()



### (d)
print("(d) Compute the neighbor product in 1-dim list, and print out.")
ndim1=[]

i=0
while i<len(dim1):
	s=1
	if i==0: # 判斷的為第一個字，只要乘自己跟後面一個
		s=dim1[i]*dim1[i+1]
	elif i==len(dim1)-1:# 判斷的為最後一個字，只要乘自己跟前面一個
		s=dim1[len(dim1)-1]*dim1[len(dim1)-2]
	else:# 判斷的不為第一個字也不為第一個字，要乘自己跟前面一個跟後面一個
		s=dim1[i-1]*dim1[i]*dim1[i+1]
	ndim1.extend([s])
	i=i+1
print(ndim1)
print()


### (e)
print("(e) Put numbers into a 2-dim list, and print out.")
i=0 # 因為為3 的平方數，所以分成三列
dim2=[]
while i+t<=len(dim1):
	if i+t==len(dim1):
		dim1_=dim1[i:]
	else:
		dim1_=dim1[i:i+t]
	dim2.append(dim1_)
	i=i+3

j=0 # 再把List的每一項print出來
while j<len(dim2):
	print(dim2[j])
	j=j+1
print()


### (f)
print("(f) Zero padding to the 2-dim list, and print out.")
u=[0]*(t+2) #最前面跟最後面個補一列全為0
dim2.insert(0,u)
dim2.append(u)
i=1 
while i<len(dim2)-1: # 中間每列的前後都要補0
	dim2[i]=[0]+dim2[i]+[0]
	i=i+1
j=0 
while j<len(dim2):
	print(dim2[j])
	j=j+1
print()


### (g)
print("(g) Compute the neighbor summation in 2-dim list, and print out.")

r=1
ndim2=[]

while r<len(dim2)-1:
	c=1
	s=[]
	while c<len(dim2[r])-1: # 判斷的數跟自己跟上下左右相加
		s=s+[dim2[r][c]+dim2[r-1][c]+dim2[r+1][c]+dim2[r][c-1]+dim2[r][c+1]]
		c=c+1
	ndim2.append(s)
	r=r+1

j=0
while j<len(ndim2):
	print(ndim2[j])
	j=j+1
print()