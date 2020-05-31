
# coding: utf-8

# In[17]:


import random
ranks=['ACE','2','3','4','5','6','7','8','9','10','JACK','QUEEN','KING']
suits=['SPADE','HEART','CLUB','DIAMOND']


# In[18]:


def deal(k):
    player=[] # 玩家
    dealer=[] # 電腦
    deck=[] # 各種花色數字組合 # (花色，數字)
    for i in range(k): # 設定想要幾副牌
        for s in suits:
            for r in ranks:
                deck.append((s,r)) 
    random.shuffle(deck)
    player.append(deck[0])
    del deck[0] # 不會重複拿到一樣的牌
    player.append(deck[0])
    del deck[0]
    dealer.append(deck[0])
    del deck[0]
    dealer.append(deck[0])
    del deck[0]
    return (player,dealer,deck)


# In[19]:


def print_value(who):
    pvalue=0 # 玩家的總點數
    ace_count=0 # 有幾張ACE
    for p in who:
        if p[1] in "JACK,QUEEN,KING":
            pvalue+=10
        elif p[1] in '2,3,4,5,6,7,8,9,10':
            pvalue+=int(p[1])
        elif p[1]=='ACE':
            pvalue+=11 # ACE先代表11點
            ace_count+=1
    
    # 如果玩家點數超過21，如果有ACE，就把ACE的點數當成1；否則輸了
    if pvalue<21:
        print('\n'+"Your current value is %d" % (pvalue))
    elif pvalue==21:
        print('\n'+"Your current value is Blackjack! (21)")
    else:
        if ace_count>0:
            for i in range(ace_count): # 將ACE換成1點
                pvalue-=10
                if pvalue==21: # 如果剛好是21就不換了
                    print('\n'+"Your current value is Blackjack! (21)")
                    break
            if pvalue<21:
                print('\n'+"Your current value is %d" % (pvalue))
            elif pvalue>21:
                print('\n'+'Your current value is Bust! (>21)')
            
        else:
            print('\n'+'Your current value is Bust! (>21)')
    print("with the hand: ",end="")
    # 依照格式print出
    for p in who:
        if who.index(p)!=len(who)-1:
            print(str(p[1])+'-'+str(p[0]),end=", ")
        else:
            print(str(p[1])+'-'+str(p[0]))
    
    return pvalue


# In[20]:


def hit_or_stay(value,who): # 問玩家要不要繼續給牌
    while True:
        chose=str(input('\nHit or stay? (Hit = 1, Stay = 0): '))
        if chose=='1':
            who.append(deck[0])
            del deck[0]
            print("You draw %s " % (str(who[-1][1])+'-'+str(who[-1][0])))
            value=print_value(who)
        elif chose=='0': # 如國不要繼續給牌，則換電腦
            break
        if value>21:
            print('\n*** Dealer wins! ***') # 如果玩家點數超過21，直接判電腦獲勝，結束遊戲
            break
    
    return value


# In[21]:


def play_again(): # 遊戲結束後，要不要重新開始一局
    again=input('\nWant to play again? (y/n): ')
    if again=='y':
        return deal(k)
    elif again=='n':
        game=False


# In[22]:


def print_dealervalue(who): 
    dvalue=0 # 電腦的總點數
    ace_count=0 # 有幾張ACE
    for p in who:
        if p[1] in "JACK,QUEEN,KING":
            dvalue+=10
        elif p[1] in '2,3,4,5,6,7,8,9,10':
            dvalue+=int(p[1])
        elif p[1]=='ACE':
            dvalue+=11
            ace_count+=1
    # 電腦原先拿到的兩張的點數
    if len(dealer)==2:
        if dvalue==21:
            print('\nDealer\'s current value is Blackjack! (21)')
        elif dvalue<21:
            print('\n'+"Dealer\'s current value is %d" % (dvalue))
        elif dvalue>21:
            if ace_count>0:
                for i in range(ace_count): # 將ACE換成1點
                    dvalue-=10
                    if dvalue==21: # 如果剛好是21就不換了
                        print('\n'+'Dealer\'s current value is Blackjack! (21)')
                        break
                if dvalue<21:
                    print('\n'+"Dealer\'s current value is %d" % (dvalue))
                elif pvalue>21:
                    print('\n'+'Dealer\'s current value is Bust! (>21)')
            else:
                print('\n'+'Dealer\'s current value is Bust! (>21)')
        print("with the hand: ",end="")
        for p in who:
            if who.index(p)!=len(who)-1:
                print(str(p[1])+'-'+str(p[0]),end=", ")
            else:
                print(str(p[1])+'-'+str(p[0]))
        print()
        
    return dvalue,ace_count


# In[23]:


def dealer_hit(value,who,ppvalue,ace_count):
    hit=True
    while hit:
        # 如果電腦的點數<=17，會自動給牌；當電腦點數超過17時，就不會再給牌了
        if value<=17:
            who.append(deck[0])
            del deck[0]
            print("Dealer draws %s " % (str(who[-1][1])+'-'+str(who[-1][0])))  

            if who[-1][1] in "JACK,QUEEN,KING":
                value+=10
            elif who[-1][1] in '2,3,4,5,6,7,8,9,10':
                value+=int(who[-1][1])
            elif who[-1][1]=='ACE':
                value+=11
                ace_count+=1
            
        elif value>17:
            if len(who)>2:
                if 21>value>17:
                    print("\nDealer\'s current value is %d" % (value))
                    hit=False
                elif value==21:
                    print('\nDealer\'s current value is Blackjack! (21)')
                    hit=False
                elif value>21:
                    if ace_count>0:
                        for i in range(ace_count): # 將ACE變成1點
                            dvalue-=10
                            if dvalue==21: # 如果剛好21就不繼續換了
                                print('\n'+'Dealer\'s current value is Blackjack! (21)')
                                break
                            if dvalue<21:
                                print('\n'+"Dealer\'s current value is %d" % (dvalue))
                            elif pvalue>21:
                                print('\n'+'Dealer\'s current value is Bust! (>21)')
                    else:
                        print('\nDealer\'s current value is Bust! (>21)') 
                        hit=False
      
            else:
                hit=False
    # 如果自動給牌，要print出被給了哪張牌
    if len(who)>2:
        print("with the hand: ",end="")
        for p in who:
            if who.index(p)!=len(who)-1:
                print(str(p[1])+'-'+str(p[0]),end=", ")
            else:
                print(str(p[1])+'-'+str(p[0]))
    # 判斷玩家跟電腦誰贏            
    if 21>=value>17:
        if value>ppvalue:
            print("\n*** Dealer wins! ***")
        elif value<ppvalue:
            print('\n*** You beat the dealer! ***')
        elif value==ppvalue:
            print('\n*** You tied the dealer, nobody wins. ***')
    elif value>21:
        print('\n*** You beat the dealer! ***')   
    


# In[24]:


k=1
game=True
while game:
    player,dealer,deck=deal(k) # 先給玩家跟電腦各兩張牌
    pvalue=print_value(player) # 玩家一剛開始兩張牌的總點數
    ppvalue=hit_or_stay(pvalue,player) # 玩家被給玩牌後的總點數
    if ppvalue<=21: # 若玩家總點數<=21，則換電腦
        dvalue,ace_count=print_dealervalue(dealer)
        dealer_hit(dvalue,dealer,ppvalue,ace_count) 

    game=play_again() # 遊戲結束後詢問要不要繼續

