#程序作者：梁润泽
#程序时间：12/5/

import random
x = random.randint(0,2)

user = int(input('请输入：剪刀（0）、石头（1）、布（2）：'))

if x == 0:
    x = '剪刀（0）'
elif x == 1:
    x = '石头（1）'
else :
    x = '布（2）'

if user == 0:
    user = '剪刀（0）'
elif user == 1:
    user = '石头（1）'
elif user ==2:
    user = '布（2）'
else:  print('Error:No Correct Name')                                                  
print('你的输入为：%s\n随机生成数字为：%s'%(x,user))

if((user == 0 and x ==2)
    or(user == 1 and x == 0)
    or(user == 2 and x == 1)):
    print('用户赢了！！！')
elif user == x :
    print('平局')
else :
    print('哈哈哈，你输了！！！')
