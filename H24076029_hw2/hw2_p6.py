string=str(input("Enter a string: "))

i=1
j=len(string)

while True:
	while 0<j: # 當字串的第一個字屬於迴文的情況
		if(string[0:j:1]==string[j-1::-1] and len(string[0:j:1])>=2): # 迴文的字串必須兩個字以上才算
			print("Longest palindrome substring is:", string[0:j:1])
			print("Length is:", len(string[0:j:1])) # 判斷迴文的字串有幾個字
			exit(0) # 當找到迴文的字串便結束程式
		j=j-1
	while True: # 當字串的第一個字以後才屬於迴文的情況
		j=len(string)
		while i<j: # 從字串的第一個字開始找迴文
			if (string[i:j:1]==string[j-1:i-1:-1] and len(string[i:j:1])>=2): # 迴文的字串必須兩個字以上才算
				print("Longest palindrome substring is:", string[i:j:1])
				print("Length is:", len(string[i:j:1])) # 判斷迴文的字串有幾個字
				exit(0) # 當找到迴文的字串便結束程式
			j=j-1
		i=i+1



####好寫法
# s=input("Enter a string: ")
# l=len(s)
# i=0
# lmax=""
# while i<=l:		  
# 	j=l			
# 	while i<=j:
# 		w=s[i:j]
# 		if w==w[::-1]:
# 			if len(w)>len(lmax):
# 				lmax=w
# 		j=j-1
# 	i=i+1
# print("Longest palindrome substring is: %s"%(lmax))
# print("Length is: %d"%(len(lmax)))