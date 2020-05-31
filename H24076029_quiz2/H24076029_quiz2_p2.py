
line=[input("Enter the matrix by multiple lines: "+"\n")]

while line!="q":
	a=[input("")]
	line=line+a

	if a==["q"]:
		break
line.pop()
i=0
while i+1<len(line):
	if len(line)!=len(line[i]):
		exit(0)
	if len(line[i])!=len(line[i+1]):
		break
	i=i+1
print(line)
p=0
line2=[]
while p<len(line):

	line1=list(line[p])
	line2.append(line1)	
	p=p+1
print(line2)

a=0
while a<len(line2):
	if "0" in line2[a]:
		b=0
		while b<len(line2[a]):
			if line2[a][b]==0:
				line2[a]=["0"]*int(len(line2[a]))
				i=1
				while a-i>=0:
					line2[a-i][b]="0"
					i=i+1
				j=1
				while a+j<len(line2):
					line2[a+j][b]="0"
				break
			b=b+1

	a=a+1
print(line2)
t=0
while t<len(line2):
	s=0
	while s<len(line2[t]):
		print(line2[t][s])
		s=s+1
	t=t+1