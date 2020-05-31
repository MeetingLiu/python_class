# open the file
filename='C:\Python 3.7\workspace\kobe.csv'
linelist=[]
myfile=open(filename,'r')
for line in myfile:
	line=line.strip()
	linelist.append(line.split(","))
myfile.close()
# def set():
# 	a=linelist[0].index('action_type')
# 	b=linelist[0].index('combined_shot_type')
# 	c=linelist[0].index('shot_distance')
# 	d=linelist[0].index('shot_distance')
# 	e=linelist[0].index('shot_distance')
# 	f=linelist[0].index('shot_distance')

# (1)
def one():
	# find the place of shot_distance
	a=linelist[0].index('shot_distance')
	shot_distance=[]
	i=1
	while i<len(linelist):
		shot_distance+=[linelist[i][a]]
		i=i+1
	shot_distance.sort()
	# find the most frequent digit
	countmax=shot_distance[0]
	for n in range(0,int(max(shot_distance))):
		if shot_distance.count(n)<shot_distance.count(n+1):
			countmax=n+1
	return(countmax)

# (2)
def two():
	# find the place of shot_zone_area and shot_made_flag
	a=linelist[0].index('shot_zone_area')
	b=linelist[0].index('shot_made_flag')
	i=1
	# area list includes every kind of shot_zone_area
	area=[]
	while i<len(linelist):
		area+=[linelist[i][a]]
		i=i+1
	area1=list(set(area))
	area1.sort()
	n=1
	dic={"c":0}
	bc,c,lc,l,rc,r=0,0,0,0,0,0

	# def shot_made_flag():
	# calaulate the times of shot_made_flag in each shot_zone_area
	while n<len(linelist):
		if linelist[n][a]==area1[0]:
			bc=bc+int(linelist[n][b])
		if linelist[n][a]==area1[1]:
			c=c+int(linelist[n][b])
		if linelist[n][a]==area1[2]:
			lc=lc+int(linelist[n][b])
		if linelist[n][a]==area1[3]:
			l=l+int(linelist[n][b])
		if linelist[n][a]==area1[4]:
			rc=rc+int(linelist[n][b])
		if linelist[n][a]==area1[5]:
			r=r+int(linelist[n][b])
		n=n+1
	# calculate the hit rate
	result=[bc/area.count(area1[0]),c/area.count(area1[1]),lc/area.count(area1[2]),l/area.count(area1[3]),rc/area.count(area1[4]),r/area.count(area1[5])]
	return (area1[result.index(max(result))])
# (3)
def three():
	# find the place of each variable
	o=linelist[0].index('opponent')
	b=linelist[0].index('shot_type')
	c=linelist[0].index('shot_made_flag')

	pt2=0 # 2PT Field Goal
	c2=0 # the times of 2PT Field Goal
	pt3=0 # 3PT Field Goal
	c3=0 # the times of 3PT Field Goal
	for n in range(1,len(linelist)):
		if linelist[n][o]=="SAS":
			if linelist[n][b]=="2PT Field Goal":
				pt2+=int(linelist[n][c])
				c2+=1
			elif linelist[n][b]=="3PT Field Goal":
				pt3+=int(linelist[n][c])
				c3+=1
	# calculate the rate
	rate2=pt2/c2
	rate3=pt3/c3
	return("2PT Field Goal: %5.3f \n3Pt Field Goal: %5.3f" % (rate2,rate3))



# (4)
def opp():
	o=linelist[0].index('opponent')
	date=linelist[0].index('game_date')
	n=1
	oppo=[linelist[1][o]]
	while n+1<len(linelist):
		if linelist[n+1][date]!=linelist[n][date]:
			oppo.append(linelist[n+1][o])
		n=n+1
	# opponent is different kind of the opponent
	opponent=list(set(oppo))
	# count how many times against the each opponent
	opponent_count=[]
	for i in range(0,len(opponent)):
		opponent_count.append(oppo.count(opponent[i]))
	return (opponent,opponent_count)

def four(opponent,opponent_count):
	# arrange the count of playing times with each team
	result_opponent=[]
	result_count=[]
	for i in range(0,len(opponent)):
		max_place=opponent_count.index(max(opponent_count))
		result_opponent.append(opponent[max_place])
		result_count.append(max(opponent_count))
		del opponent[max_place]
		del opponent_count[max_place]

	for i in range(0,5):
		print("%s : %d" % (result_opponent[i],result_count[i]))
	return "\t"
# def format_four():
# 	for i in range(0,5):
# 		print("%s : %d" % (result_oppoent[i],result_count[i]))
# 	return "\t"

# (5)
def five(opponent,opponent_count):
	o=linelist[0].index('opponent')
	b=linelist[0].index('shot_made_flag')
	c=linelist[0].index('shot_type')
	# calculate the gotten score with each team
	result=[]
	for i in range(0,len(opponent)):
		score=0
		for n in range(0,len(linelist)):
			if linelist[n][o]==opponent[i]:

				if linelist[n][c]=="2PT Field Goal":
					
					score+=2*int(linelist[n][b])
				elif linelist[n][c]=="3PT Field Goal":

					score+=3*int(linelist[n][b])
		# calculate the average score
		average=score/opponent_count[i]
		result.append(average)
	# arrange the average score with each team
	result_opponent=[]
	result_average=[]
	for i in range(0,len(opponent)):
		max_place=result.index(max(result))
		result_opponent.append(opponent[max_place])
		result_average.append(max(result))
		del opponent[max_place]
		del result[max_place]
	# find the top5 average scores
	for i in range(0,5):
		print((i+1),end="\t")
		print("%s %5.2f" % (result_opponent[i],result_average[i]))
	return "\t"

# (6)
o=linelist[0].index('opponent')
id_place=linelist[0].index('game_id')
flag=linelist[0].index('shot_made_flag')
_type=linelist[0].index('shot_type')
mins=linelist[0].index('minutes_remaining')

# o=linelist[0].index('opponent')
# date=linelist[0].index('game_date')
n=1
_id=[linelist[1][id_place]]
while n+1<len(linelist):
	if linelist[n+1][id_place]!=linelist[n][id_place]:
		_id.append(linelist[n+1][id_place])
	n=n+1
# _id_each is different kind of the _id_each
_id_each=list(set(_id))
print(_id_each)

# # count how many times against the each _id_each
# _id_count=[]
# for i in range(0,len(_id_each)):
# 	_id_count.append(_id.count(_id_each[i]))
result=[]
_opponent=[linelist[1][o]]
for i in range(0,len(_id_each)):
	score=0
	for n in range(1,len(linelist)):		
		if linelist[n][id_place]==_id_each[i]:
			if int(linelist[n][mins])<3:
				if linelist[n][_type]=="2PT Field Goal":						
					score+=2*int(linelist[n][flag])
				elif linelist[n][_type]=="3PT Field Goal":
					score+=3*int(linelist[n][flag])
	_opponent.append(linelist[n][o])

	result.append(score)

print(max(result))

result_id=[]
result_opponent=[]
result_score=[]
for i in range(0,len(_id_each)):
	max_place=result.index(max(result))
	result_id.append(_id_each[max_place])
	result_opponent.append()
	result_score.append(max(result))












print("\n(1) ANS: "+one())
print("\n(2) Ans: "+two())
print("\n(3) Ans: \n"+three())
opponent,opponent_count=opp()
print("\n(4) Ans:")
print(four(opponent,opponent_count))
opponent,opponent_count=opp()
print("\n(5) Ans:")
print(five(opponent,opponent_count))