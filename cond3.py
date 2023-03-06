#task8
deposit=1  
withdraw=2000
check_balance=3
current_balance=5000
if(withdraw<=current_balance):
    print('cash out withdraw amount')
else:
    print('you do not have enouhh balance')   
#task9 position in GameXone
a=int(input('enter your experience years:'))
if(a>=4):
    print('you will be hired as a developer')
else:
    print('you will be hired as a manager')    
#task10   Career counseling
a=input('enter your interest:')
ar='arts'
ma='management'
dr='drawing'
lo='logics'
pr='programming'
bio='biology'
if(a==ar) or (a==ma) or(a==dr) :
    print('Arts Department will suit you')
elif(a==lo) or (a==pr):
     print('You should choose engineering domain') 
elif(a==bio) :
    print('you sholud choose Biology')       
