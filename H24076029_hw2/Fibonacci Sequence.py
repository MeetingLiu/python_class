n=int(input("Input an integar number: "))
# set n0,n1
n0=0
n1=1
count=0
while n>count+1: # 設要做計算的次數
	nth=n0+n1
	n0=n1
	n1=nth
	count+=1

print("The %d-th Fibonacci sequence number is:" % (n), n1)

