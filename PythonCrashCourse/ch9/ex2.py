class User():
    def __init__(self,first_name,last_name,gender,profession,company):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.profession = profession
        self.company = company
        self.login_attempts = 0
    def describe_user(self):
        print(self.last_name+self.first_name+',他的职业是'+self.profession+', 公司是'+self.company+'。')
    def greet_user(self):
        if self.gender == '男':
            print('Hello '+self.last_name+'先生，欢迎您！您的登录次数为'+str(self.login_attempts))
        else:
            print('Hello ' + self.last_name + '小姐，欢迎您！您的登录次数为'+str(self.login_attempts))
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self,first_name,last_name,gender,profession,company):
        super().__init__(first_name,last_name,gender,profession,company)
        self.privileges = Privileges()
        # self.privileges = ['can add post','can delete post','can ban user']
    # def show_privileges(self):
    #     print('权限包括：')
    #     for p in self.privileges:
    #         print(p)
class Privileges():
    def __init__(self):
        self.privileges = ['can add post','can delete post','can ban user']
    def show_privileges(self):
        print('权限包括：')
        for p in self.privileges:
            print(p)


user_0 = User('飞','王','男','工人','格力电器')
user_1 = User('润','于','男','矿工','冀中能源')
user_2 = User('杨','白','女','营业员','招商银行')
user_0.describe_user()
user_0.greet_user()
user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()
user_2.increment_login_attempts()
user_2.increment_login_attempts()
user_2.increment_login_attempts()
user_2.greet_user()
user_2.reset_login_attempts()
user_2.greet_user()
admin_0 = Admin('boss','big','男','社会哥','黑涩会')
admin_0.describe_user()
admin_0.greet_user()
admin_0.privileges.show_privileges()