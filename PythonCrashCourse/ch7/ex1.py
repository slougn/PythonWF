# car = input('你想租赁什么样的汽车？')
# print('让我看看有没有你要租赁的'+car+'。')

# number_person = input('请问你们有几个人订餐？')
# number_person = int(number_person)
# if number_person <= 8:
#     print('还有空位。')
# else:
#     print('对不起，没有那么多空位。')

number = input('请输入一个数字：')
number = int(number)
if (number % 10) == 0:
    print(str(number)+'是10的倍数。')
else:
    print(str(number)+'不是10的倍数。')