guest_list = []
guest_list.append('xiaoming')
guest_list.append('xiaohong')
guest_list.append('dawei')
guest_list.append('dongmingzhu')

print(guest_list)

guest_removed = 'dawei'
guest_list.remove('dawei')
print('Today '+guest_removed.title()+' can not comming!')

guest_list.append('laowang')
print(guest_list)

guest_list.insert(0,'laozhang')
guest_list.insert(2,'laosun')
guest_list.append('laoniu')
print(guest_list)
