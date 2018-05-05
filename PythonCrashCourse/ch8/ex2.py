def make_shirt(size=99,type='I love Python'):
    print('做了一件大小为'+str(size)+"字样为'"+type+"'的T-恤衫")

make_shirt(24,'中兴要牛掰')
make_shirt()
make_shirt(76)

def city_country(city,country):
    return (city+','+country)

print(city_country('handan','China'))
print(city_country(country='China',city='zhuhai'))

def make_album(singer,album,num = 0):
    Info_album = {}
    Info_album['singer'] = singer
    Info_album['album'] = album
    if num != 0:
        Info_album['num'] = num
    return Info_album
print(make_album('周杰伦','依然范特西'))