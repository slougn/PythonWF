class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('这家店的名字为'+self.restaurant_name+',类型为' + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name+'开门了，大家都来吃呀！')

restaurant_0 = Restaurant('小黑酒家','农家菜馆')
restaurant_0.describe_restaurant()
restaurant_0.open_restaurant()

restaurant_1 = Restaurant('幺妹儿菜馆','川菜')
restaurant_2 = Restaurant('那嘎达菜馆','东北菜')
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()


class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['榴莲口味','土豆口味','屁口味']
    def show_icecream(self):
        print('我们店有这些口味的冰激凌：')
        for f in self.flavors:
            print(f)

icecreamstand_0 = IceCreamStand('二丫冷站','冷饮站')
icecreamstand_0.describe_restaurant()
icecreamstand_0.open_restaurant()
icecreamstand_0.show_icecream()