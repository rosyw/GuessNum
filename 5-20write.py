import random

name = input('请输入你的姓名：')
min_round = 0  # 记录最少猜的轮数
total = 0  # 记录总游戏轮数
times = 0  # 记录游戏次数

while True:
    times += 1
    num = random.randint(1, 100)
    count = 0 #记录单次游戏猜的轮数
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
            if min_round == 0 or min_round > count:
                min_round = count
            total += count
            avg = '%0.2f'% (total/times)
            print(f'猜对了！你一共猜了{count}轮')
            print(f'{name}，你已经玩了{times}次，最少{min_round}轮猜出答案，平均{avg}轮猜出答案。')
            break #猜对跳出循环
    goon = input('是否继续游戏？（输入y继续，其他退出）')
    if goon == 'y' or goon == 'Y':
        True
    else:
        print('退出游戏，欢迎下次再来挑战！')
        break

# 把需写入文本的信息放入列表
record = [f'玩家姓名：{name}',f'总游戏次数：{times}',f'最快猜出的轮数：{min_round}',f'总游戏轮数：{count}']
# 写入文本，每个元素后换行
with open('game_one_user.txt', 'w') as f:
    f.writelines([i +'\n' for i in record])