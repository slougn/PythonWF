users = ['admin','a','b','c','d']
if users == []:
    print('We need to find some users!')
else:
    for user in users:
        if user == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Hello '+ user +', thank you for logging in again!')

current_users = ['What','whEre','when','why','wether']
items_c_u = []
for item in current_users:
    items_c_u.append(item.lower())
print(items_c_u)

new_users = ['WHat','wHeRe','some','any','go']
for user in new_users:
    if user.lower() in items_c_u:
        print('用户名被占用')
    else:
        print('用户名可以利用')