
from datetime import datetime

#While loop statements
  
#print(datetime.now().second)

#wait_until = datetime.now().second + 2

'''
while datetime.now().second != wait_until:
    pass

'''
#print(f'we are at {wait_until} seconds!')


#Break
#wait_until = datetime.now().second + 2

'''
while True:
    if datetime.now().second == wait_until:
       print(f'we are at {wait_until} seconds!')
       break

'''

#Continue
wait_until = datetime.now().second + 2
'''
while datetime.now().second != wait_until:
        continue
        print('still waiting')
       
print(f'we are at {wait_until} seconds!')
'''

while True:
    if datetime.now().second < wait_until:
        continue
    break
print(f'we are at {wait_until} seconds!')
