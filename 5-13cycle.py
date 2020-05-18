import random
num = random.randint(1,100)
count = 0
try:
    while True:
        guess = int(input('猜猜我想的是哪个数（1-100的整数）：'))
        # 每次猜数前计一次
        count += 1
        # 通过条件判断是否才对
        if guess < num:
            print('猜小了，再试试')
        elif guess > num:
            print('猜大了，再试试')
        else:
            print('猜对了！你一共猜了%d次' % count)
            break #猜对跳出循环
#如果输入小数，报错（但是超过1-100范围的整数不会报错，这种异常需要自己定义？）
except ValueError:
    print('你猜的不是整数哦')