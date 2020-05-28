import requests

# 读取玩家数据
try:
    with open('game_many_user.txt') as f:
        all_record = {}
        data = f.readlines()
        #以字典形式提取每个玩家的游戏记录，所有玩家的字典放在一个列表中
        for i in data:
            i = i.strip('\n')
            i = i.split()
            # print(i)
            # 把字符串转换成整型
            data_key = [int(j) for j in i[1:]]
            # 新建字典管理玩家数据
            all_record[i[0]] = data_key
            # print(all_record)
# 如果文本不存在，新建一个
except FileNotFoundError:
    f = open('game_many_user.txt','w')
    f.close()

# 查看输入的名字是否存在
name = input('请输入你的姓名：')
if name in all_record.keys():
    former_avg = '%0.2f'% (all_record[name][2]/all_record[name][0])
    times = all_record[name][0]  # 记录游戏次数
    min_round = all_record[name][1] # 记录最少猜的轮数
    total = all_record[name][2]  # 记录总游戏轮数
    print(f'{name}，你已经玩了{times}次，最少{min_round}轮猜出答案，平均{former_avg}轮猜出答案。开始游戏！')
else:
    print(f'欢迎{name}加入GuessNum游戏，开始你的第一次游戏吧！')
    times = 0
    min_round = 0
    total = 0

while True:
    times += 1
    req = requests.get('https://python666.cn/cls/number/guess/')
    num = int(req.text)
    count = 0 #记录单次游戏猜的轮数
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
                if min_round == 0 or min_round > count:
                    min_round = count
                total += count
                avg = '%0.2f'% (total/times) # format( total/times , '.2f')
                print(f'猜对了！你一共猜了{count}轮')
                print(f'{name}，你已经玩了{times}次，最少{min_round}轮猜出答案，平均{avg}轮猜出答案。')
                break #猜对跳出循环
    except ValueError:
        print('你猜的不是整数哦')

    goon = input('是否继续游戏？（输入y继续，其他退出）')
    if goon == 'y' or goon == 'Y':
        True
    else:
        print('退出游戏，欢迎下次再来挑战！')
        break

#更新记录玩家数据的字典
all_record[name]=[times, min_round,total]
# 写入文本，每个元素后换行
with open('game_many_user.txt', 'w') as f:
    # 遍历字典的键和值，替换值列表中的中括号和逗号
    for k,v in all_record.items():
        s = k +' '+ str(v)
        s= s.replace('[','').replace(']','').replace(',','')
        f.write(s+'\n')

