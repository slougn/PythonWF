name = ''
while name != '退出':
    name = input('请输入您的姓名：')
    print('欢迎' + name)
    with open('guest_book.txt','a') as file_object:
        file_object.write(name+'\n')
    print('写"退出"后退出')
