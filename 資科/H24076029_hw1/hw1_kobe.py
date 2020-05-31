
# coding: utf-8

# In[43]:


# open the file
filename='C:\kobe.csv'
linelist=[]
myfile=open(filename,'r')
for line in myfile:
    line=line.strip()
    linelist.append(line.split(','))
myfile.close()


# In[44]:


# define data to set dic including each row data
def data(i):    
    dic={}
    for item in linelist[0]:
        dic[item]=linelist[i][linelist[0].index(item)]
    return dic


# * (1)

# In[45]:


_2pt=0 # how many 2pt field balls
_2pt_flag=0 # get scores from 2pt field
_3pt=0 # how many 3pt field balls
_3pt_flag=0 # get scores from 3pt field
for i in range(len(linelist)):
    dic=data(i)
    if dic['opponent']=='HOU':
        if dic['shot_type']=='2PT Field Goal':
#             print(dic['shot_made_flag'])
            _2pt+=1
            _2pt_flag+=int(dic['shot_made_flag'])
        elif dic['shot_type']=='3PT Field Goal':
            _3pt+=1
            _3pt_flag+=int(dic['shot_made_flag'])
# calcualte the hit rate
_2pt_result=_2pt_flag/_2pt
_3pt_result=_3pt_flag/_2pt

print('(1) ANS:')
print('2PT Field Goal: %5.3f' % (_2pt_result))
print('3PT Field Goal: %5.3f' % (_3pt_result))


# * (2)

# In[46]:


dic_score={} # the score of each team
for i in range(1,len(linelist)):
    dic=data(i)
    dic_score[dic['opponent']]=[0,0] # [得分，場數]
for i in range(1,len(linelist)):
    dic=data(i)
    if dic['shot_type']=='2PT Field Goal':
        dic_score[dic['opponent']][0]+=(2*int(dic['shot_made_flag']))
    elif dic['shot_type']=='3PT Field Goal':
        dic_score[dic['opponent']][0]+=(3*int(dic['shot_made_flag']))
    if dic['game_id']!=data(i-1)['game_id']:
        dic_score[dic['opponent']][1]+=1
# calcualte the average score      
for key in dic_score:
        dic_score[key]=dic_score[key][0]/dic_score[key][1]
# print(dic_score)
score=list(dic_score.values())
score.sort()
# the list of ascending average score
print('\n(2) ANS:')
for i in range(1,6):
    for key in dic_score:
        if dic_score[key]==score[i]:
            print('%d %s %5.2f' % (i,key, score[i]))
        


# * (3)

# In[47]:


dic_score={}        
for i in range(1,len(linelist)):
    dic=data(i)
    if dic['playoffs']=='1':
        dic_score[dic['game_id']]=[0,dic['opponent']] # {game_id: [得分，對手]}
    
for i in range(1,len(linelist)):
    dic=data(i)
    if dic['playoffs']=='1':
        if int(dic['minutes_remaining'])<3: # 最後3分鐘
            if int(dic['period'])<=4: # 不包含延長賽
                if dic['shot_type']=='2PT Field Goal':
                    dic_score[dic['game_id']][0]+=(2*int(dic['shot_made_flag']))
                elif dic['shot_type']=='3PT Field Goal':
                    dic_score[dic['game_id']][0]+=(3*int(dic['shot_made_flag']))
# the list id descending score
score=list(dic_score.values())
score.sort(reverse=True)

print('\n(3) ANS:')
for i in range(5):
    for key in list(dic_score.keys()):
        if dic_score[key]==score[i]:
            print('id = %s , vs. %s : %d' % (key, dic_score[key][1], score[i][0]))
            del dic_score[key]


# * (4)

# In[48]:


dic_score={}        
for i in range(1,len(linelist)):
    dic=data(i)
    if dic['playoffs']=='1': # 季後賽
        dic_score[dic['season']]=[0,0] # [得分次數，出手次數]

for i in range(1,len(linelist)):
    dic=data(i)  
    if dic['playoffs']=='1': # 季後賽
        if int(dic['minutes_remaining'])<1: # 最後1分鐘內
            if dic['action_type']=='Jump Shot': # 使用jump shot
                dic_score[dic['season']][1]+=1
                if dic['shot_made_flag']=='1':
                    dic_score[dic['season']][0]+=1
# the list of hit rate
# delete the data which doesn't hit
for t in list(dic_score.keys()):
    if dic_score[t][1]==0:
        del dic_score[t]
    else:
        dic_score[t]=dic_score[t][0]/dic_score[t][1]
date=list(dic_score.keys())
date.sort()
print('\n(4) ANS:')
for time in date:
    print('%s : %5.3f' % (time, dic_score[time]))
          


# * (5)

# In[49]:


date=[] # 先排序日期
all=[] # [[日期，命中球數]]
for i in range(1,len(linelist)):
    dic=data(i)
    # 將日期從1999/1/3 --> 19990103
    dic['game_date']=dic['game_date'].split('/')
    if len(dic['game_date'][1])==1:
        dic['game_date'][1]='0'+dic['game_date'][1]
    if len(dic['game_date'][2])==1:
        dic['game_date'][2]='0'+dic['game_date'][2]    
    dic['game_date']=dic['game_date'][0]+dic['game_date'][1]+dic['game_date'][2]
    all.append([dic['game_date'], dic['shot_made_flag']])

result={} # [得分次數，出手次數]
for i in range(len(all)):
    # 在result與上一場一樣，代表同一場，加上得分次數及出手次數
    if all[i][0]==all[i-1][0]:
        result[all[i][0]][0]+=int(all[i][1])
        result[all[i][0]][1]+=1
    # 如果日期與上一個資料不一樣，建立新的資料在result
    else:
        result[all[i][0]]=[int(all[i][1]),1]
# calculate the hit rate of each date
# if the hit rate>=0.33, add 'y' to the result[data]
for date in result:
    if result[date][0]/result[date][1]>=0.33:
        result[date]=[result[date][0]/result[date][1]]
        result[date].append('y')
    
a=[] # 連續日期
for i in list(result.keys()):
    a.append(i)
a.sort()

time=0 # 連續命中率達0.33以上的次數
cont=[] # 連續命中率達0.33以上的日期
judge=[] # [[time,judge]]
for i in range(len(a)):       
    if result[a[i]][-1]=='y':
        # 如果這場跟上一場命中率都達0.33以上，次數+1，append日期到cont裡面
        if result[a[i-1]][-1]=='y':
            time+=1
            cont.append(a[i])
        # 如果這場命中率達0.33，但上一場沒有，就重新累積
        else:
            time=1
            cont=[a[i]]
    # 如果這場命中率沒有達0.33，但上一場有，將上一場的資料append到judge裡面，再重新累積
    else:
        if result[a[i-1]][-1]=='y':
            judge.append([cont, time])
        time=0
        cont=[]
# the list of the descending hit rate
time=[]
for i in range(len(judge)):
    time.append(judge[i][1])

time=list(set(time))
time.sort(reverse=True)

print('\n(5) ANS')
for j in range(0,3):
    for i in range(len(judge)):
        if judge[i][1]==time[j]:
            a=judge[i][0][0][0:4]+'/'+judge[i][0][0][4:6]+'/'+judge[i][0][0][6:]
            b=judge[i][0][-1][0:4]+'/'+judge[i][0][-1][4:6]+'/'+judge[i][0][-1][6:]
            print(time[j], a, '~', b)


# * (6)

# In[50]:


dic_score={}        
for i in range(1,len(linelist)):
    dic=data(i)
    dic_score[dic['game_date']]=[0,0,0,dic['opponent']]
    # {日期:[上半場得分，下半場得分，出手次數，對手]}

for i in range(1,len(linelist)):
    dic=data(i)
    if int(dic['period'])<=2: # 上半場
        if dic['shot_type']=='2PT Field Goal':
            dic_score[dic['game_date']][0]+=(2*int(dic['shot_made_flag']))
            dic_score[dic['game_date']][2]+=1
        elif dic['shot_type']=='3PT Field Goal':
            dic_score[dic['game_date']][0]+=(3*int(dic['shot_made_flag']))
            dic_score[dic['game_date']][2]+=1
    if 5>int(dic['period'])>2: # 下半場不包含延長賽
        if dic['shot_type']=='2PT Field Goal':
            dic_score[dic['game_date']][1]+=(2*int(dic['shot_made_flag']))
            dic_score[dic['game_date']][2]+=1
        elif dic['shot_type']=='3PT Field Goal':
            dic_score[dic['game_date']][1]+=(3*int(dic['shot_made_flag']))
            dic_score[dic['game_date']][2]+=1
#  留下上半場得分多於下半場的資料，並計算命中率，append在dic_score的最後一項          
for key in list(dic_score.keys()):
    if dic_score[key][0]<=dic_score[key][1]:
        del dic_score[key]
    else:
        dic_score[key].append((dic_score[key][0]+dic_score[key][1])/dic_score[key][2])
# the list of descending hit rate
rate=[]
for key in list(dic_score.keys()):
    rate.append(dic_score[key][-1])
rate.sort(reverse=True)

print('\n(6) ANS:')
for i in range(-3,0):
    for key in list(dic_score.keys()):   
        if dic_score[key][-1]==rate[i]:
            print(key, ',', dic_score[key][3], ',', dic_score[key][0]-dic_score[key][1], ',', dic_score[key][0]+dic_score[key][1])
            # print(日期，對手，上下半場得分差，該場得分)
            del dic_score[key]


# * (7)

# In[51]:


dic_score={}        
for i in range(1,len(linelist)):
    dic=data(i)
    dic_score[dic['game_date']]=['',0,dic['opponent']]
    # {日期:[是否失手(1為得分，0為失手)，得分，對手]}
for i in range(1,len(linelist)):
    dic=data(i)
    k=dic['game_date']
    if dic['shot_type']=='2PT Field Goal':
        dic_score[k][1]+=(2*int(dic['shot_made_flag']))
    elif dic['shot_type']=='3PT Field Goal':
        dic_score[k][1]+=(3*int(dic['shot_made_flag']))
    if int(dic['shot_made_flag'])==0:
        dic_score[k][0]+='0'
    else:
        dic_score[k][0]+='1'
        
for key in list(dic_score.keys()):
    dic_score[key][0]=dic_score[key][0].split('1') # 從1分開，代表中斷連續
    for k in range(len(dic_score[key][0])):
        dic_score[key][0][k]=dic_score[key][0][k].count('0') # 算有幾個0 --> 連續失手幾次
    dic_score[key][0]=max(dic_score[key][0]) # 連續失手最多的次數
# 從小到大連續失手次數
time=[]
for key in list(dic_score.keys()):
    time.append(dic_score[key][0])
time.sort(reverse=True)

print('\n(7) ANS:')
for i in range(3):
    for key in list(dic_score.keys()):   
        if dic_score[key][0]==time[i]:
            print(key, ',', dic_score[key][2], ',', dic_score[key][0], ',', dic_score[key][1])
            # print(日期，對手，連續失手次數，該場得分)
            del dic_score[key]

