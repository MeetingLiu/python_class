p=str(input(str("Input the polynomials: ")))

# 將每個括弧分成大的list裡的小list
p=p.split(")(")
k=0
li=[]
while k<len(p):
	adj=p[k]
	adj=adj.strip("(")
	adj=[adj.strip(")")]
	li.append(adj)
	k=k+1

# 把每個括弧裡的不同項分成不同字串
# "+" "-"都要保留
lis=[]
j=0
while j<len(li):
	li1=li[j][0].replace("-","+"+"-") # 先換成前面都有"+"
	li1=li1.split("+") # 再一起從"+"做分割
	if "" in li1:
		li1.remove("")
	j=j+1
	lis.append(li1)

# 將每一項係數都乘起來
mul=1
while len(lis)>1:
	m=0
	n=0
	s=[]
	while n<len(lis[1]) and m<len(lis[0]):
		# 先看一個括弧
		if "*" in lis[0][m]: # 如果有"*"，代表係數不為1
			mi1=lis[0][m].index("*")
			mul=mul*(int(lis[0][m][0:mi1]))
		elif "-" in lis[0][m]: # 如果沒有"*"，但有"-"，代表係數為-1
			mi1=0
			mul==mul*(-1)
		else : # 如果沒有"*"，也沒有"-"，代表係數為1
			mi1=-1
			mul==mul*1

		# 再看第二個括弧
		if "*" in lis[1][n]:
			mi2=lis[1][n].index("*")
			mul=mul*(int(lis[1][n][0:mi2]))
		elif "-" in lis[1][n] :
			mi2=0
			mul=mul*(-1)
		else :
			mi2=-1
			mul=mul*1
		# 將乘好的整理在一起
		# 如果有3個一上的括弧，要繼續乘
		s1=[str(mul)+"*"+str(lis[0][m][mi1+1:])+str(lis[1][n][mi2+1:])]
		if s1[0][0]!="-":
			s1[0]="+"+s1[0]
			s.extend(s1)
		else:
			s.extend(s1)
		n=n+1
		if n>=len(lis[1]):
			m=m+1
			n=0
		mul=1

	lis[0]=s
	del lis[1]
lis=s

# 將每一項分成係數與變數
i=0
j=0
while i<len(lis) :
	while j<len(lis[i]):
		if lis[i][j].isalpha():
			lis[i]=[lis[i][:j],lis[i][j:]]
		j=j+1
	i=i+1
	j=0

# 同未知數處理
# 先把同一個變數有幾個就寫出幾個
# 例如: XX^3Y^2 變成XXXXYY
p=0
while p<len(lis):
	while "^" in lis[p][1]:
		a=lis[p][1].find("^")
		b=a+1
		while a<b<len(lis[p][1]):
			if b==len(lis[p][1])-1:
				t=lis[p][1][a+1]
			if lis[p][1][b].isalpha():
				t=lis[p][1][a+1:b]
				break
			else:
				b=b+1
		lis[p][1]=lis[p][1].replace(lis[p][1][a-1:b], lis[p][1][a-1]*int(t))
# 再將同一個變數的整理，次方為該係數的總和
# 例如: XXXYY 變成X^3Y^2
	lis[p][1]=list(lis[p][1])
	lis[p][1].sort()
	i=0
	pp=""
	while i<len(lis[p][1]):
		pp=pp+lis[p][1][i]
		i=i+1
	lis[p][1]=pp
	i=0
	while i+1< len(lis[p][1]):
		c=0
		if lis[p][1][i]==lis[p][1][i+1]:
			c=lis[p][1].count(lis[p][1][i])
		if c>1:
			if i+c==len(lis[p][1])-2:
				a=lis[p][1][i:]
			else:
				a=lis[p][1][i:i+c]
			b=lis[p][1][i]+"^"+str(c)
			lis[p][1]=lis[p][1].replace(a, b)
		i=i+1
	p=p+1


# 同類項合併
# 當後面的變數一樣時，將前面的係數相加
d=0
while d<len(lis):
	e=d+1
	while e<len(lis):
		if lis[d][1]==lis[e][1]:
			a=int(lis[d][0][: lis[d][0].find("*")])
			b=int(lis[e][0][: lis[e][0].find("*")])
			if a+b>0:
				lis[d][0]=lis[d][0].replace(lis[d][0][:], "+"+str(a+b)+"*")				
			elif a+b==0:
				del lis[d]
				del lis[e]
			elif a+b<0:
				lis[d][0]=lis[d][0].replace(lis[d][0][:], str(a+b)+"*")					
			del lis[e]
		e=e+1
	d=d+1


# 算出來的結果若細數為1則不用寫
v=0
lis_end=""
while v<len(lis):
	a=lis[v][0].find("*")
	if lis[v][0][a-1]=="1":
		lis[v][0]=lis[v][0].replace(lis[v][0][a-1:a+1],"")
	lis_end += lis[v][0]+lis[v][1]
	v=v+1

# 算出來的結果若開頭有"+"，則不用寫
if lis_end[0]=="+":
	lis_end=lis_end.replace(lis_end[:],lis_end[1:])
# 印出結果
print("Output Result:", lis_end)
