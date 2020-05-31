seat=str(input("Input sequence of seats: "))
# 將seat轉換成list
seat=seat.split(" ")
n=0
s=[]
while n<len(seat):
	l=int(max(seat[:n+1])) # 取n以左的最大值
	r=int(max(seat[n:])) # 取n以右的最大值
	judge=min([l,r]) # 找兩邊最大值的最小值
	s=s+[judge-int(seat[n])] # 在減掉n就是積水的量
	n=n+1
print("Water:", sum(s))