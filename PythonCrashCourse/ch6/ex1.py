friend ={'firstname':'run',
         'lastname':'yu',
         'age':29,
        'city':'handan'}

print(friend)

favorite_number = {'yurun':3,
                   'wangfei':4,
                   'xiaohong':7,
                   'hanmeimei':2,
                   'Jim Green':8}
print(favorite_number['Jim Green'])

dictionary={'what':'什么',
            'why':'为什么',
            'when':'什么时候',
            'fuck':'呵呵',
            'diss':'鄙视',
            'food':'食物',
            'T-shirt':'T恤衫',
            'book':'书',
            'pen':'笔',
            'ballpen':'圆珠笔'}
#print(''''what'的意思是 ''' +
#      dictionary['what']+'.')
for key,value in dictionary.items():
    print(key+'的意思是'+value+'.')