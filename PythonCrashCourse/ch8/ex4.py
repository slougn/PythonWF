def make_bread(*filling):
    print(filling)

make_bread('土豆')
make_bread('土豆','茄子','苦瓜')

def user_profile(first_name,last_name,**Info):
    profile = {}
    profile['first_name'] = first_name
    profile['last_name'] = last_name
    for key,value in Info.items():
        profile[key] = value
    return profile

print(user_profile('飞','王',地址 = '珠海',公司 = 'Gree'))