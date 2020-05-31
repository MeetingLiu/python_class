n=int(input("Input the total number of students (n>0) : "))
# 從1到n存成一個list
i=0
circle=[]
while i<n:
	i=i+1
	circle += [i]
# 第一個被取出的是第2個，所以a=2
a=2
while len(circle)>1:
	while a<len(circle):
		circle.remove(circle[a])
		a=a+2 # 取出一個後，下一個被取出的會是第a+2個，因為list會少一項
	a=a-len(circle) # 當a超出範圍時，要再回到list的最前面取
print("The last ID is :", circle[0])
