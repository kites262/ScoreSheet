import xlsxwriter
from time import time
from datetime import datetime

now = (str(datetime.fromtimestamp(time()))
       .replace(':', '-')
       .replace(' ', '_'))

fileName = f"SCORE_{now[2:19]}.XLSX"

scoreList = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1566, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 3553, 2136, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 4670, 3399, 1345, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 6951, 5478, 3400, 0, 2581, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 7087, 5910, 3860, 0, 2524, 0, 2369, 0, 0, 0, 0, 0, 0, 0],
    [0, 7456, 6295, 4250, 0, 2912, 0, 2600, 0, 391, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 7586, 6718, 4951, 0, 3668, 0, 4258, 0, 1893, 1746, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 7945, 7455, 6113, 0, 5036, 0, 6216, 0, 3900, 3803, 0, 2067, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 7290, 7203, 6410, 0, 5663, 0, 7461, 0, 5358, 5374, 0, 3790, 0, 2013],
]


workbook = xlsxwriter.Workbook(fileName)
worksheet = workbook.add_worksheet()

column = 1
cache = 0
total_score = 0
history = []

isContinue = True

print("输入以空格分隔的两个数字, A表示结束本轮.")

while isContinue:

    # user input
    user_input = input("\033[94mEnter>>> \033[92m")
    numbers = user_input.split()
    inputs = numbers
    numbers = [int(num) for num in numbers if num.isdigit()]

    # terminate
    if 'A' in inputs:
        isContinue = False
        break

    # del
    if 'del' in inputs:
        if len(history) != 0:
            history.pop()
            print("\033[91m已清除上一次输入, 目前列表:\033[0m", end='')
            if len(history) != 0:
                cache = history[-1]
            else:
                cache = 0
        print(history)
        continue

    # 2 numbers
    if len(numbers) != 2:
        print("\033[91m格式错误！请输入两个数字.\033[0m")
        continue

    # out of index Test
    if numbers[0] > 13 or numbers[1] > 16:
        print("\033[91m输入错误！数字超出范围，请重新核对并输入.\033[0m")
        continue

    # set score
    score = scoreList[numbers[1]][numbers[0]]

    # cache Test
    if cache == score:
        print("\033[91m重复输入！上一次已经输入了该组数据..\033[0m")
        continue

    # null Test
    if score == 0:
        print("\033[91m输入错误！数字对应分数不存在，请重新核对并输入.\033[0m")
        continue

    total_score += score
    cache = score

    # write score
    history.append(score)
    worksheet.write(2, column, score)
    column += 1
    print(history)

# END & SAVE
worksheet.write(0, 0, "START")
worksheet.write(0, 1, now)

worksheet.write(1, 0, "END")
worksheet.write(1, 1, str(datetime.fromtimestamp(time())).replace(':', '-').replace(' ', '_'))

worksheet.write(2, 0, "SCORES")
worksheet.write(3, 0, "TOTAL")

worksheet.write(3, 1, total_score)

print(f"\033[0m本回合计分结束, 总分数为 \033[91m{total_score}\033[0m")
print(f"结果已保存到 {fileName} 文件中")

workbook.close()
