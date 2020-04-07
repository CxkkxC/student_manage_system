# -*- coding:utf-8 -*-
from tkinter.messagebox import * 
from tkinter import *
from tkinter import ttk
from student_info_sql import * 
from teacher_info_sql import *
from student_achievement_sql import * 
from AdminPage import * 
import xlwt

global numbers,i
i=0
class LoginPage(object):
    def __init__(self, master=None):
        self.root = master
        winWidth = 650
        winHeight = 400
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()

        x = int((screenWidth - winWidth) / 2)
        y = int((screenHeight - winHeight) / 2)
        # 设置窗口初始位置在屏幕居中
        self.root.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
        # 设置窗口图标
        # root.iconbitmap("./image/icon.ico")
        # 设置窗口宽高固定
        self.root.resizable(0, 0)
        self.student_number = StringVar()
        self.student_pw = StringVar() 
        self.createPage()
    
    def createPage(self):
        '''
        登录页面
        1:创建图片组件
        2:根目录基础上添加Frame容器
        3:Frame容器上添加注册控件
        '''
        bm=PhotoImage(file=r'cxk.gif')
        self.lab3=Label(self.root,image=bm)
        self.lab3.bm=bm
        self.lab3.pack()
        
        self.page = Frame(self.root) 
        self.page.pack()
        Label(self.page).grid(row=0, stick=W) 
        Label(self.page, text = '学号: ').grid(row=1, stick=W, pady=10) 
        Entry(self.page, textvariable=self.student_number).grid(row=1, column=1, stick=E) 
        Label(self.page, text = '密码: ').grid(row=2, stick=W, pady=10) 
        Entry(self.page, textvariable=self.student_pw, show='*').grid(row=2, column=1, stick=E) 
        Button(self.page, text='管理员登录', command=self.admin_loginCheck).grid(row=3, column=0)
        #self.root.bind('<KeyPress-Return>',self.admin_loginCheck1)#绑定键盘上的回车登录
        Button(self.page, text='学生注册',command=self.signup).grid(row=3, column=3) 
        Button(self.page, text='学生/教师登录', command=self.student_loginCheck).grid(row=3,column=1) 
        #self.root.bind('<KeyPress-Return>',self.user_loginCheck1)#绑定键盘上的回车登录
        
    def admin_loginCheck(self):
        global numbers
        '''
        管理员登录
        1:获取管理员账号与密码
        2:将获取到的账号与密码与数据库文件配对，配对成功返回值为正确，否则为错误
        3:将返回值判断，正确则登录界面清除，登录界面图片清除，进入管理员界面
        异常捕获：未填写账号或者密码
        '''
        try:
            Admin_number=self.student_number.get()
            #print(User_id)
            Admin_pw=self.student_pw.get()
            #print(User_pw)
#             pd=admin_Select_id_pw(Admin_id,Admin_pw)
#             if pd:
            if Admin_number=="1" and Admin_pw=="1":
                self.page.destroy()
                self.lab3.pack_forget()
                AdminPage(self.root)
            else:
                showinfo(title='错误', message='账号或密码错误！')
        except:
                showinfo(title='错误',message='输入错误，请重新输入！')

    def student_loginCheck(self):
        global numbers,i
        '''
        学生登录
        1:获取学生学号与密码
        2:将获取到的学号与密码与数据库文件配对，配对成功返回值为正确，否则为错误
        3:将返回值判断，正确则登录界面清除，登录界面图片清除，进入用户界面，异常捕获：未填写账号或者密码
        '''
        try:
            Student_number=self.student_number.get()
            #print(User_id)
            Student_pw=self.student_pw.get()
            #print(User_pw)
            pd_student=user_slect_number_pw(Student_number,Student_pw)
            pd_teacher=teacher_slect_number_pw(Student_number,Student_pw)
            if pd_student:
                numbers=Student_number
                self.page.destroy()
                self.lab3.pack_forget()
                StudentPage(self.root)
            elif pd_teacher:
                numbers=Student_number
                self.page.destroy()
                self.lab3.pack_forget()
                TeacherPage(self.root)
            elif i>2:
                showinfo(title='错误', message='密码三次输入错误，此次登录被终止！')
                self.root.destroy()
            else:
                i+=1
                showinfo(title='错误', message='账号或密码错误！')
        except:
            showinfo(title='错误',message='输入错误，请重新输入！')
                
    
    def signup(self):
        '''
        学生注册页面
        1:新建一个置于顶层的窗口
        2:将布局控件放入
        3:每个窗口的控件布局必须是一致的，place(),grid(),pack()中的一种
        '''
        def insert_sql():
            '''
            添加学生
            1:获取学生姓名，年龄，学号，密码
            2:将获取到的账号与数据库文件配对，查看是否存在相同学号，如不存在，将学生插入数据库文件，存在则提示修改账户名
            异常捕获：信息未填写
            '''
            try:
                age = self.new_age.get()
                number = self.new_number.get()
                name = self.new_name.get()
                pw = self.new_pw.get()
                if len(number) < 12:
                    showinfo(title='提示', message='学号为12位的数字，请重新输入！')
                else:
                    XWC=user_showdb(number)#先判断账号是否存在于学生或者教师数据库
                    SHB=teacher_showdb(number)
                    if XWC == None and SHB == None:
                        user_insertData(number,name,pw,age)
                        showinfo(title='提示', message='注册成功')
                        self.window_sign_up.destroy()
                    else:
                        self.window_sign_up.destroy()
                        showinfo(title='提示',message='学号重复，注册失败，请修改学号！')  
            except:
                self.window_sign_up.destroy()
                showinfo(title='错误',message='未知错误，请重新输入！')
                

        self.window_sign_up = Toplevel(self.root)
        winWidth = 300
        winHeight = 200
        self.window_sign_up.title('注册窗口')
        screenWidth = self.window_sign_up.winfo_screenwidth()
        screenHeight = self.window_sign_up.winfo_screenheight()
        x = int((screenWidth - winWidth) / 2)
        y = int((screenHeight - winHeight) / 2)
        # 设置窗口初始位置在屏幕居中
        self.window_sign_up.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x-50, y-50))
        # 设置窗口图标
        # root.iconbitmap("./image/icon.ico")
        # 设置窗口宽高固定
        self.window_sign_up.resizable(0, 0)
        

        self.new_name = StringVar()
        Label(self.window_sign_up, text='姓名: ').place(x=10, y=10) 
        entry_new_name = Entry(self.window_sign_up, textvariable=self.new_name) 
        entry_new_name.place(x=130, y=10)

        self.new_age= StringVar()
        Label(self.window_sign_up, text='年龄: ').place(x=10, y=50)
        entry_usr_age = Entry(self.window_sign_up, textvariable=self.new_age)
        entry_usr_age.place(x=130, y=50)

        self.new_number = StringVar()
        Label(self.window_sign_up, text='学号: ').place(x=10, y=90)
        entry_student_number = Entry(self.window_sign_up, textvariable=self.new_number)
        entry_student_number.place(x=130, y=90)
        
        self.new_pw = StringVar()
        Label(self.window_sign_up, text='密码: ').place(x=10, y=130)
        entry_usr_pw = Entry(self.window_sign_up, textvariable=self.new_pw, show='*')
        entry_usr_pw.place(x=130, y=130)

        sign_up = Button(self.window_sign_up, text='注册', command=insert_sql)
        sign_up.place(x=237, y=160)
        
class StudentPage(object): 
 def __init__(self, master=None): 
  self.root = master #定义内部变量root 
  self.root.geometry('%dx%d' % (650, 400)) #设置窗口大小 
  self.root.resizable(0,0) #防止用户调整尺寸
  self.createPage() 
    
 def createPage(self): 
  self.menuPage = MenuFrame(self.root) # 创建不同Frame 
#   self.menuPage.pack() #默认显示界面 
    
        
class MenuFrame(Frame): # 继承Frame类 
 def __init__(self, master=None):
  Frame.__init__(self, master) 
  self.root = master #定义内部变量root
  self.createPage()
  
 
 def createPage(self):
        global numbers
        strs="欢迎您！学号为：%s 的同学！"%numbers
        Label(self.root, text=strs).place(x=210, y=0)
        Button(self.root, text='查看个人成绩单', command=self.print_ach,width=20,height=10).place(x=150, y=95)
        Button(self.root, text='修改个人密码',command=self.change_pw,width=20,height=10).place(x=350, y=95)
        Button(self.root, text='导出个人成绩单为Excel表格',command=self.ach_dao_xls,width=25).place(x=230, y=295)
        
 def ach_dao_xls(self):
    try:
        global numbers
        a=achievement_showdb(numbers)
        a=tuple(a)
        b=achievement_lie_name()
        c=[]
        c.append(tuple(b))
        c.append(a)
        def w_excel(res):
            book = xlwt.Workbook(encoding='utf-8') #新建一个excel
            sheet = book.add_sheet('sheet1') #新建一个sheet页
            for row in range(0,len(res)):
                for col in range(0,len(res[row])):
                    sheet.write(row,col,res[row][col])
                row+=1
                col+=1
            book.save('%s_student_achievement.xls'%numbers)
            print("导出成功！")
        w_excel(c)
        showinfo(title='确认', message='导出成功！')
    except:
        showinfo(title='错误', message='未知错误，请重新导出！')
 
 def print_ach(self):
        global numbers
        self.ach = Toplevel(self.root)
        self.ach.title('个人成绩单')
        winWidth = 300
        winHeight = 200
        screenWidth = self.ach.winfo_screenwidth()
        screenHeight = self.ach.winfo_screenheight()
        x = int((screenWidth - winWidth) / 2)
        y = int((screenHeight - winHeight) / 2)
        # 设置窗口初始位置在屏幕居中
        self.ach.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
        # 设置窗口图标
        # root.iconbitmap("./image/icon.ico")
        # 设置窗口宽高固定
        self.ach.resizable(0, 0)
        b=achievement_lie_name()
        a=achievement_showdb(numbers)
        a=list(a)
        if len(a)==2:
            strs="暂无科目成绩,请等待教师添加"
            Label(self.ach, text=strs).pack()
        else:
            for i,j in enumerate(a): 
                if i>=2:
                    strs=b[i]+":"+str(j)
                    Label(self.ach, text=strs).pack()
 def change_pw(self):
        def sure_change():
                global numbers
                try:
                    New_pw=self.new_pw.get()
                        #print(User_id)
                    New_pws=self.new_pws.get()
                        #print(User_pw)
                    if New_pw==New_pws:
                        user_alter_pw(numbers,New_pw)
                        print("学号为%s的学生已修改密码，新密码为：%s"%(numbers,New_pw))
                        showinfo(title='提示',message='密码已修改，请重启软件重新登录！')
                        self.root.destroy()
                    else:
                        showinfo(title='错误',message='两次密码不一致，请重新输入！')
                except:
                    showinfo(title='错误',message='未知错误，请重新输入！')
        global numbers
        self.change_pw = Toplevel(self.root)
        self.change_pw.title('修改密码')
        winWidth = 230
        winHeight = 210
        screenWidth = self.change_pw.winfo_screenwidth()
        screenHeight = self.change_pw.winfo_screenheight()
        x = int((screenWidth - winWidth) / 2)
        y = int((screenHeight - winHeight) / 2)
        # 设置窗口初始位置在屏幕居中
        self.change_pw.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
        # 设置窗口图标
        # root.iconbitmap("./image/icon.ico")
        # 设置窗口宽高固定
        self.change_pw.resizable(0, 0)
        self.new_pw = StringVar()
        self.new_pws = StringVar() 
        Label(self.change_pw, text='请输入新密码').place(x=110, y=0)
        Label(self.change_pw, text='新密码: ').place(x=25, y=20)
        Entry(self.change_pw, textvariable=self.new_pw, show='*').place(x=70, y=20)
        Label(self.change_pw, text='重复新密码: ').place(x=0, y=50)
        Entry(self.change_pw, textvariable=self.new_pws, show='*').place(x=70, y=50)
        Button(self.change_pw, text='确认修改',command=sure_change).place(x=90, y=90)
        
                    
class TeacherPage(object): 
 def __init__(self, master=None): 
  self.root = master #定义内部变量root 
  self.root.geometry('%dx%d' % (650, 400)) #设置窗口大小 
  self.root.resizable(0,0) #防止用户调整尺寸
  self.createPage() 
    
 def createPage(self): 
  self.teacher_menuPage = teacher_MenuFrame(self.root) # 创建不同Frame 
#   self.menuPage.pack() #默认显示界面 
    
        
class teacher_MenuFrame(Frame): # 继承Frame类 
 def __init__(self, master=None):
  Frame.__init__(self, master) 
  self.root = master #定义内部变量root
  self.createPage()
  
 
 def createPage(self):
        global numbers
        strs="欢迎您！教师号为：%s 的老师！"%numbers
        Label(self.root, text=strs).place(x=210, y=0)
        Button(self.root, text='查看学生成绩单', command=self.print_student_ach,width=20,height=10).place(x=150, y=95)
        Button(self.root, text='修改学生成绩',command=self.change_ach,width=20,height=10).place(x=350, y=95)
        
 def change_ach(self):
        def add_new_subject():
            def sure_add():
                try:
                    Subject_name=self.subject_name.get()
                    achievement_insertData(Subject_name)
                    showinfo(title='确认', message='添加成功！')
                    self.add_menu.destroy()
                except:
                    showinfo(title='错误', message='未知错误，请重新修改！')
                    self.add_menu.destroy()
                
            self.change_menu.destroy()
            self.add_menu = Toplevel(self.root)
            self.add_menu.title('修改学生成绩')
            winWidth = 200
            winHeight = 200

            screenWidth = self.add_menu.winfo_screenwidth()
            screenHeight = self.add_menu.winfo_screenheight()
            x = int((screenWidth - winWidth) / 2)
            y = int((screenHeight - winHeight) / 2)
            # 设置窗口初始位置在屏幕居中
            self.add_menu.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
            # 设置窗口图标
            # root.iconbitmap("./image/icon.ico")
            # 设置窗口宽高固定
            self.add_menu.resizable(0, 0)
            
            self.subject_name=StringVar()
            Label(self.add_menu, text='科目名: ').place(x=10, y=30)
            Entry(self.add_menu, textvariable=self.subject_name).place(x=50, y=30)
            Button(self.add_menu, text='确认添加',command=sure_add).place(x=80, y=80)
        
        def sure_change():
            try:
                Student_number=self.student_number.get()
                Student_ach=self.student_ach.get()
                Subject_name=self.comvalue.get()
                if Student_ach >100 or Student_ach < 0:
                    showinfo(title='错误', message='成绩数值错误，请重新修改！')
                else:
                    achievement_alter(Student_number,Subject_name,Student_ach)
                    showinfo(title='确认', message='修改成功！')
                    self.change_menu.destroy()
            except:
                showinfo(title='错误', message='未知错误，请重新修改！')
                self.change_menu.destroy()
                
        self.change_menu = Toplevel(self.root)
        self.change_menu.title('修改学生成绩')
        winWidth = 550
        winHeight = 300
        
        screenWidth = self.change_menu.winfo_screenwidth()
        screenHeight = self.change_menu.winfo_screenheight()
        x = int((screenWidth - winWidth) / 2)
        y = int((screenHeight - winHeight) / 2)
        # 设置窗口初始位置在屏幕居中
        self.change_menu.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
        # 设置窗口图标
        # root.iconbitmap("./image/icon.ico")
        # 设置窗口宽高固定
        self.change_menu.resizable(0, 0)
        def go(*args):
            #处理事件，*args表示可变参数 
            print(comboxlist.get())
            return comboxlist.get()#打印选中的值  
        self.comvalue=StringVar()#窗体自带的文本，新建一个值  
        comboxlist=ttk.Combobox(self.change_menu,textvariable=self.comvalue) #初始化  
        achievement_lie_name()#获取科目列表
        b=achievement_lie_name()
        # print(b)
        a=["无"]
        j=0
        for i in b:
            if j>=2:
                a.append(i)
            j+=1
        a=tuple(a)
#         print(a)
        comboxlist["values"]=a
        comboxlist.current(0)  #选择第一个  
        comboxlist.bind("<<ComboboxSelected>>",go)  #绑定事件,(下拉列表框被选中时，绑定go()函数) 
        Label(self.change_menu, text="请选择科目").place(x=140, y=50)
        comboxlist.place(x=230, y=50)
        Label(self.change_menu, text="如果没有科目").place(x=140, y=98)
        Button(self.change_menu, text='请添加科目',command=add_new_subject,width=22).place(x=230, y=95)
        
        self.student_number = StringVar()
        self.student_ach = IntVar()
        Label(self.change_menu, text='学号: ').place(x=180, y=150)
        Entry(self.change_menu, textvariable=self.student_number).place(x=220, y=150)
        Label(self.change_menu,  text='成绩(0~100): ').place(x=135, y=200)
        Entry(self.change_menu,  textvariable=self.student_ach).place(x=220, y=200)
        Button(self.change_menu, text='确认修改',command=sure_change).place(x=250, y=250)
        
 def print_student_ach(self):
        def dao_subject_ach():
            try:
                b=achievement_lie_name()
                chiose=""
                Subject_name=self.comvalue.get()
                V=self.v.get()
                if V==0:
                    chiose=None
                if V==1:
                    chiose="desc"
                all_str=achievement_paixu(Subject_name,chiose)
                all_str.insert(0,b)
                def w_excel(res):
                    book = xlwt.Workbook(encoding='utf-8') #新建一个excel
                    sheet = book.add_sheet('sheet1') #新建一个sheet页
                    for row in range(0,len(res)):
                        for col in range(0,len(res[row])):
                            sheet.write(row,col,res[row][col])
                        row+=1
                        col+=1
                    book.save('%s排序成绩.xls'%Subject_name)
                    print("导出成功！")
                w_excel(all_str)
                showinfo(title='确认', message='导出成功！')
            except:
                showinfo(title='错误', message='未知错误，请重新导出！')
        def paixu():
            chiose=""
            Subject_name=self.comvalue.get()
            V=self.v.get()
            if V==0:
                chiose=None
            if V==1:
                chiose="desc"
            self.teacher_menu = Toplevel(self.root)
            self.teacher_menu.title('学生成绩单')
            winWidth = 650
            winHeight = 400
            screenWidth = self.teacher_menu.winfo_screenwidth()
            screenHeight = self.teacher_menu.winfo_screenheight()
            x = int((screenWidth - winWidth) / 2)
            y = int((screenHeight - winHeight) / 2)
            # 设置窗口初始位置在屏幕居中
            self.teacher_menu.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x-50, y-50))
            # 设置窗口图标
            # root.iconbitmap("./image/icon.ico")
            # 设置窗口宽高固定
            self.teacher_menu.resizable(0, 0)
            S=Scrollbar(self.teacher_menu)
            T=Text(self.teacher_menu,width=400)
            S.pack(side=RIGHT,fill=Y)
            T.pack(side=LEFT,fill=Y)
            S.config(command=T.yview)
            T.config(yscrollcommand=S.set)
            # insert的第一个参数为索引;第二个为添加的内容
            try:
                all_str=achievement_paixu(Subject_name,chiose)
                b=achievement_lie_name()
                strss="         学号"+"       |"+"    姓名"+"    |"
                for i,j in enumerate(b):
                    if i>=2:
                        strss+="   "+str(j)+"   |"
                strss+='\n\n'
                T.insert(END,strss)
                for i in all_str:
                    strs=""
                    for j in i:
                        strs=strs+"    "+str(j)+"    |"
                    strs+="\n\n"
                    T.insert(END,strs)
                T.pack()
            except:
                self.teacher_menu.destroy()
                showinfo(title='错误', message='无学生成绩，请确认数据库是否有学生信息！')
            
        self.student_ach_menu = Toplevel(self.root)
        self.student_ach_menu.title('按科目升/降序查看成绩')
        winWidth = 300
        winHeight = 300
        screenWidth = self.student_ach_menu.winfo_screenwidth()
        screenHeight = self.student_ach_menu.winfo_screenheight()

        x = int((screenWidth - winWidth) / 2)
        y = int((screenHeight - winHeight) / 2)
        # 设置窗口初始位置在屏幕居中
        self.student_ach_menu.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
        # 设置窗口图标
        # root.iconbitmap("./image/icon.ico")
        # 设置窗口宽高固定
        self.student_ach_menu.resizable(0, 0)

        def go(*args):
            #处理事件，*args表示可变参数 
            print(comboxlist.get())
            return comboxlist.get()#打印选中的值  

        self.comvalue=StringVar()#窗体自带的文本，新建一个值  
        comboxlist=ttk.Combobox(self.student_ach_menu,textvariable=self.comvalue) #初始化
        achievement_lie_name()#获取科目列表
        b=achievement_lie_name()
        # print(b)
        a=["无"]
        j=0
        for i in b:
            if j>=2:
                a.append(i)
            j+=1
        a=tuple(a)
        comboxlist["values"]=a
        comboxlist.current(0)  #选择第一个  
        comboxlist.bind("<<ComboboxSelected>>",go)  #绑定事件,(下拉列表框被选中时，绑定go()函数) 
        Label(self.student_ach_menu, text="请选择科目:").place(x=10, y=35)
        comboxlist.place(x=80, y=35)

        self.v= IntVar()
        r1 = Radiobutton(self.student_ach_menu, variable=self.v, value=0, text="升序")
        r2 = Radiobutton(self.student_ach_menu, variable=self.v, value=1, text="降序")
        self.v.set(0)
        
        r1.place(x=244, y=25)
        r2.place(x=244, y=45)
        Button(self.student_ach_menu, text='查看学生成绩单', command=paixu,width=20,height=3).place(x=80, y=105)
        Button(self.student_ach_menu, text='导出某科升序/降序学生成绩单', command=dao_subject_ach,width=30,height=3).place(x=44, y=175)