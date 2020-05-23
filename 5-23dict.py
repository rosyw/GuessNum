import random

# 读取玩家数据
with open('game_one_user.txt') as f:
    data = f.read()
    data = data.split()
    # 把字符串转换成整型
    data_key = [int(i) for i in data[1:]]
    # 新建字典管理玩家数据
    rank = {}
    rank[data[0]] = data_key
    print(rank)

name = input('请输入你的姓名：')
if name in rank:
    former_avg = '%0.2f'% (rank[name][2]/rank[name][0])
    print(f'{name}，你已经玩了{rank[name][0]}次，最少{rank[name][1]}轮猜出答案，平均{former_avg}轮猜出答案。开始游戏！')
    min_round = rank[name][1]  # 记录最少猜的轮数
    times = rank[name][0]  # 记录游戏次数
    total = rank[name][2]  # 记录总游戏轮数
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
            avg = '%0.2f'% (total/times) # format( total/times , '.2f')
            print(f'猜对了！你一共猜了{count}轮')
            print(f'{name}，你已经玩了{times}次，最少{min_round}轮猜出答案，平均{avg}轮猜出答案。')
            break #猜对跳出循环
    goon = input('是否继续游戏？（输入y继续，其他退出）')
    if goon == 'y' or goon == 'Y':
        True
    else:
        print('退出游戏，欢迎下次再来挑战！')
        break


record = f'{name} {times} {min_round} {total}'
# 写入文本，每个元素后换行
with open('game_one_user.txt', 'w') as f:
    f.write(record)