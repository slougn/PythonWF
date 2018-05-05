bread_order = ['白面馒头','麦馒头','南瓜馒头','叉烧包','蛋黄包']
finished_bread = []
while bread_order:
    bread = bread_order.pop()
    print(bread+'已经做好了！')
    finished_bread.append(bread)

print('做好的订单有：')
for bread in finished_bread:
    print(bread)


bread_order = ['白面馒头','五香牛肉包子','麦馒头','五香牛肉包子','南瓜馒头','叉烧包','五香牛肉包子','蛋黄包']
print(bread_order)
print('五香牛肉包子已经售罄！！')
while '五香牛肉包子' in bread_order:
    bread_order.remove('五香牛肉包子')
print('确认订单：')
for bread in bread_order:
    print(bread)