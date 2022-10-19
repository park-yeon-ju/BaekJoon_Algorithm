curNum = 0
firstNum = 0
cnt = 0

curNum = int(input())
firstNum = curNum

while True :
    newNum = 0
    left = 0
    right = 0
    cnt = cnt + 1
    
    if curNum < 10 :
        newNum = curNum*10 + curNum

    else :
        left = curNum//10
        right = curNum %10
        newNum = (right)*10 + (left+right)%10

    curNum = newNum

    if curNum == firstNum :
        break

print(cnt)
