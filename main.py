# -*- coding:utf-8 -*-
from tkinter.messagebox import * 
from tkinter import *
from LoginPage import * #菜单栏对应的各个子页面

root = Tk() #建立一个根窗口，所有窗口的基础
root.title('学生管理系统')
LoginPage(root)#进入调用登录
root.mainloop()