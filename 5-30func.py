import requests

#定义猜一次数字的函数，返回该次游戏所猜轮数count
def oneRound(num):
    count = 0  # 记录单次游戏猜的轮数
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
            print(f'猜对了！你一共猜了{count}轮')
            return count
            break  # 猜对跳出循环

#定义一个函数表示游戏的外部循环，可以猜多次
def guessNum(times = 0,min_round = 0,total = 0):
    while True:
        times += 1
        req = requests.get('https://python666.cn/cls/number/guess/')
        num = int(req.text)
        count2 = oneRound(num)
        total += count2
        avg = '%0.2f' % (total / times)  # format( total/times , '.2f')
        if min_round == 0 or min_round > count2:
            min_round = count2
        print(f'{name},你已经玩了{times}次，最少{min_round}轮猜出答案，平均{avg}轮猜出答案。')
        goon = input('是否继续游戏？（输入y继续，其他退出）')
        if goon not in 'Yy':
            print('退出游戏，欢迎下次再来挑战！')
            # 把总次数，最快轮数，总轮数返回成一个列表
            return [times,min_round,total]
            break

# 定义一个main()函数，读取、匹配和写入数据
def main():
    # 读取文本内容转换成字典
    with open('game_many_user.txt') as f:
        all_record = {}
        data = f.readlines()
        # 以字典形式提取每个玩家的游戏记录，所有玩家的字典放在一个列表中
        for i in data:
            i = i.strip('\n')
            i = i.split()
            # print(i)
            # 把字符串转换成整型
            data_key = [int(j) for j in i[1:]]
            # # 新建字典管理玩家数据
            all_record[i[0]] = data_key
        # print(all_record)

    # 把name设置为全局变量，可在guessNum()函数中调用
    global name
    name = input('请输入你的姓名：')
    # 如果name可匹配字典的键，则还原之前的数据
    if name in all_record.keys():
        former_avg = '%0.2f' % (all_record[name][2] / all_record[name][0])
        times = all_record[name][0]  # 记录游戏次数
        min_round = all_record[name][1]  # 记录最少猜的轮数
        total = all_record[name][2]  # 记录总游戏轮数
        print(f'{name}，你已经玩了{times}次，最少{min_round}轮猜出答案，平均{former_avg}轮猜出答案。开始游戏！')
        # 把guessNumber()的返回值作为name的值，下同理
        all_record[name] = guessNum(times,min_round,total)
    # 如不可匹配，新建一个玩家数据
    else:
        print(f'欢迎{name}加入GuessNum游戏，开始你的第一次游戏吧！')
        all_record[name] = guessNum()

    with open('game_many_user.txt', 'w') as f:
        # 遍历字典的键和值，替换值列表中的中括号和逗号
        for k, v in all_record.items():
            s = k + ' ' + str(v)
            s = s.replace('[', '').replace(']', '').replace(',', '')
            f.write(s + '\n')

main()