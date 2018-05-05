magicians = ['大卫','王飞','大鹏','大绿','小乖乖']

def show_magicians(magicians):
    """传递列表"""
    print(magicians)

def make_great(magicians):
    temp = []
    for magician in magicians:
        magician = 'The Great' + magician
        temp.append(magician)
    return temp

show_magicians(make_great(magicians))
show_magicians(magicians)