from pymysql import *


class Register(object):
    def __init__(self):
        self.conn = connect(host='localhost', port=3306, user='xiaoming', password='123456', database='students_data', charset='utf8')
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    @staticmethod
    def show_menu():
        print("---------学生管理系统-----------")
        print("1:登录")
        print("2:注册")
        print("3:修改信息")
        print("4:查询学员信息")
        print("5:显示所有信息")
        print("6:注销账号")
        print("7:退出")
        return input("请输入功能序号：")

    def add_student(self):
        name = input("请输入姓名：")
        gender = input("请输入性别：")
        password = int(input("请输入密码："))
        sql = f"insert into students values (0, '{name}', '{gender}', {password})"
        self.cursor.execute(sql)
        self.conn.commit()

    def stu_register(self):
        name = input("请输入姓名：")
        password = int(input("请输入密码："))
        self.cursor.execute("select name,password from students")
        for temp in self.cursor.fetchall():
            if name == temp[0] and password == temp[1]:
                print("登录成功")
                break
        else:
            print("账号或密码输入错误")

    def del_student(self):
        name = input("请输入要删除账号的姓名：")
        self.cursor.execute("select name,password from students")
        for temp in self.cursor.fetchall():
            if name == temp[0]:
                sql = "delete from students where name=%s"
                self.cursor.execute(sql, [name])
                self.conn.commit()
                break
        else:
            print("姓名输入错误")

    def stu_modify(self):
        name = input("请输入要修改学生的姓名：")
        gender = input("请输入修改后的性别：")
        password = int(input("请输入修改后的密码："))
        self.cursor.execute("select name,password from students")
        for temp in self.cursor.fetchall():
            if name == temp[0]:
                sql = "update students set name=%s,gender=%s,password=%s where name=%s;"
                self.cursor.execute(sql, [name, gender, password, name])
                self.conn.commit()
                break
        else:
            print("姓名输入错误")

    def stu_display(self):
        self.cursor.execute("select * from students")
        print("序号，名字，性别，密码")
        for temp in self.cursor.fetchall():
            print(temp)

    def stu_search(self):
        name = input("请输入要查询学生的姓名：")
        sql = "select * from students where name=%s"
        self.cursor.execute(sql, [name])
        print(self.cursor.fetchall())

    def run(self):
        while True:
            num = self.show_menu()
            if num == '1':
                # 登录
                self.stu_register()
            elif num == '2':
                # 注册
                self.add_student()
            elif num == '3':
                # 修改学生信息
                self.stu_modify()
            elif num == '4':
                # 修改学生信息
                self.stu_search()
            elif num == '5':
                # 显示所有学员信息
                self.stu_display()
            elif num == '6':
                # 删除账号
                self.del_student()
            elif num == '7':
                # 退出
                break
            else:
                pass

