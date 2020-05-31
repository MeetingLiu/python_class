n=int(input("Input the range number: "))
# num為範圍內可能的Perfect number
num=2
# lis內放Perfect number
lis=[]
# 找num是否為perfect number
while num<=n:
	i=1 # i為num可能的因數
	s=0
	while i<num: # 找num的因數
		if num % i==0: 
			s += i
		i=i+1
	if s==num: # 判斷num除自己外的因數和是否為自己
		lis=lis+[num]
	num=num+1
print("Perfect number:", lis)