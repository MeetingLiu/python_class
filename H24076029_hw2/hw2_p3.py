year=int(input("Please input Year: "))
month=int(input("Please input Month: "))

# 依照高斯公式設定條件
if (month==1 or month==2):
	y1=year-1
	m=month+10
else:
	m=month-2
	y1=year
y=y1%100 # 年的最後兩位
d=1
c=y1//100 #世紀-1
w=(d+int(2.6*m-0.2)+5*(y%4)+3*y+5*(c%4))%7

# 設定每月第一週1號分別為星期幾時的格式
print("Sun","Mon","Tue","Wed","Thu","Fri","sat")
format1=("%02d  %02d  %02d  %02d  %02d  %02d  %02d")
format2=("    %02d  %02d  %02d  %02d  %02d  %02d")
format3=("        %02d  %02d  %02d  %02d  %02d")
format4=("            %02d  %02d  %02d  %02d")
format5=("                %02d  %02d  %02d")
format6=("                    %02d  %02d")
format7=("                        %02d")
# 設定每月最後一週最後一天分別為星期幾時的格式
format6_1=("%02d  %02d  %02d  %02d  %02d  %02d     ")
format5_1=("%02d  %02d  %02d  %02d  %02d          ")
format4_1=("%02d  %02d  %02d  %02d               ")
format3_1=("%02d  %02d  %02d                    ")
format2_1=("%02d  %02d                         ")
format1_1=("%02d                              ")

# 設定每月第一週1號分別為星期幾的狀況
if w==7:
	w0,w1,w2,w3,w4,w5,w6=1,2,3,4,5,6,7
if w==1:
	w0,w1,w2,w3,w4,w5,w6=0,1,2,3,4,5,6
if w==2:
	w0,w1,w2,w3,w4,w5,w6=-1,0,1,2,3,4,5
if w==3:
	w0,w1,w2,w3,w4,w5,w6=-2,-1,0,1,2,3,4
if w==4:
	w0,w1,w2,w3,w4,w5,w6=-3,-2,-1,0,1,2,3
if w==5:
	w0,w1,w2,w3,w4,w5,w6=-4,-3,-2,-1,0,1,2
if w==6:
	w0,w1,w2,w3,w4,w5,w6=-5,-4,-3,-2,-1,0,1
# 只印出每月第一週會大於1的數字
i=0
a1=format1 % (w0+i,w1+i,w2+i,w3+i,w4+i,w5+i,w6+i)
if w5+i<1:
	a1=format7 % (w6+i)
elif w4+i<1:
	a1=format6 % (w5+i,w6+i)
elif w3+i<1:
	a1=format5 % (w4+i,w5+i,w6+i)
elif w2+i<1:
	a1=format4 % (w3+i,w4+i,w5+i,w6+i)
elif w1+i<1:
	a1=format3 % (w2+i,w3+i,w4+i,w5+i,w6+i)
elif w0+i<1:
	a1=format2 % (w1+i,w2+i,w3+i,w4+i,w5+i,w6+i)
# 印出每月第二、三、四週
i=7
a2=format1 % (w0+i,w1+i,w2+i,w3+i,w4+i,w5+i,w6+i)
i+=7
a3=format1 % (w0+i,w1+i,w2+i,w3+i,w4+i,w5+i,w6+i)
i+=7
a4=format1 % (w0+i,w1+i,w2+i,w3+i,w4+i,w5+i,w6+i)
i+=7		
a5=format1 % (w0+i,w1+i,w2+i,w3+i,w4+i,w5+i,w6+i)

# 判斷哪一年哪一個月有幾天
if (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
	n=31
elif (month==4 or month==6 or month==9 or month==11):
	n=30
elif (month==2 and year%4==0):
	n=29
elif (month==2 and year%4!=0):
	n=28
# 如果當月只有4週，就print出來
if w0+i>n:
	print(a1+"\n"+a2+"\n"+a3+"\n"+a4)
else: # 只印出屬於當月的日期
	if w6+i>n:
		a5=format6_1 % (w0+i,w1+i,w2+i,w3+i,w4+i,w5+i)
	if w5+i>n:
		a5=format5_1 % (w0+i,w1+i,w2+i,w3+i,w4+i)
	if w4+i>n:
		a5=format4_1 % (w0+i,w1+i,w2+i,w3+i)
	if w3+i>n:
		a5=format3_1 % (w0+i,w1+i,w2+i)
	if w2+i>n:
		a5=format2_1 % (w0+i,w1+i)
	if w1+i>n:
		a5=format1_1 % (w0+i)
i+=7
a6=format1 % (w0+i,w1+i,w2+i,w3+i,w4+i,w5+i,w6+i)

# 如果當月有5週，只印出屬於當月的日期
if w0+i>n:
	print(a1+"\n"+a2+"\n"+a3+"\n"+a4+"\n"+a5)
else :
	if w6+i>n:
		a6=format6_1 % (w0+i,w1+i,w2+i,w3+i,w4+i,w5+i)
	if w5+i>n:
		a6=format5_1 % (w0+i,w1+i,w2+i,w3+i,w4+i)
	if w4+i>n:
		a6=format4_1 % (w0+i,w1+i,w2+i,w3+i)
	if w3+i>n:
		a6=format3_1 % (w0+i,w1+i,w2+i)
	if w2+i>n:
		a6=format2_1 % (w0+i,w1+i)
	if w1+i>n:
		a6=format1_1 % (w0+i)
	print(a1+"\n"+a2+"\n"+a3+"\n"+a4+"\n"+a5+"\n"+a6)









# 好方法！！！
a=int(input("Please input Year: "))
b=int(input("Please input Month: "))
print("Sun Mon Tue Wed Thu Fri Sat")
if a%4!=0:
	y=365
if a%4==0 and a%100!=0:
	y=366
if a%100==0 and a%400!=0:
	y=365
if a%400==0:
	y=366
if y==365 and b==2:
	d=28
if y==366 and b==2:
	d=29
if b==1 or b==3 or b==5 or b==7 or b==8 or b==10 or b==12:
	d=31
if b==4 or b==6 or b==9 or b==11:
	d=30
c=a//100
y=a%100
if b!=1 and b!=2:
	m=b-2
if b==1:
	m=11
if b==2:
	m=12
w=(1+int(2.6*m-0.2)+y+int(y/4)+int(c/4)-2*c)%7
s=1
if w!=0 or w!=1 or w!=2:
	x=7-w+1
if w==0:
	x=1
if w==1:
	x=0
if b==2:
	w=w-2
	x=7-w+1
myformat = "%02d"
print(" "*(w*4),end="")
while s<=d : 
	if s<=10:	
		print(myformat%(s),end="  ")
		s+=1
	else:
		print(s,end="  ")
		s+=1
	if s%7==x:
		print("")

		