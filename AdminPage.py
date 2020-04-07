# -*- coding:utf-8 -*-
from tkinter.messagebox import * 
from tkinter import *
from student_info_sql import * 
from teacher_info_sql import *
from student_achievement_sql import * 
from tkinter import ttk
import xlwt

class AdminPage(object): 
 def __init__(self, master=None): 
  self.root = master #定义内部变量root 
  self.root.geometry('%dx%d' % (650, 400)) #设置窗口大小 
  self.root.resizable(0,0) #防止用户调整尺寸
  self.createPage() 
    
 def createPage(self): 
  self.admin_menuPage = admin_MenuFrame(self.root) # 创建不同Frame 
#   self.menuPage.pack() #默认显示界面 
    
        
class admin_MenuFrame(Frame): # 继承Frame类 
 def __init__(self, master=None):
  Frame.__init__(self, master) 
  self.root = master #定义内部变量root
  self.createPage()
  
 
 def createPage(self):
        strs="欢迎您！系统最高权限的管理者！"
        Label(self.root, text=strs).place(x=210, y=0)
        Button(self.root, text='查看学生成绩单', command=self.print_student_ach,width=15,height=5).place(x=200, y=95)
        Button(self.root, text='修改学生成绩',command=self.change_ach,width=15,height=5).place(x=350, y=95)
        Button(self.root, text='添加教师账号',command=self.teacher_sign_up,width=15,height=5).place(x=200, y=195)
        Button(self.root, text='删除教师账号',command=self.dele_teacher_number,width=15,height=5).place(x=350, y=195)
        Button(self.root, text='导出学生成绩单为Excel表格',command=self.dao_xls,width=35,height=3).place(x=205, y=300)
        
 def dao_xls(self):
    a=user_slectTable()
    b=user_lie_name()
    a.insert(0,tuple(b))
    def w_excel(res):
        book = xlwt.Workbook(encoding='utf-8') #新建一个excel
        sheet = book.add_sheet('sheet1') #新建一个sheet页
        for row in range(0,len(res)):
            for col in range(0,len(res[row])):
                sheet.write(row,col,res[row][col])
            row+=1
            col+=1
        book.save('student_info.xls')
        print("导出成功！")
    w_excel(a)
    showinfo(title='确认', message='导出成功！')
    
 def dele_teacher_number(self):
        def sure_dele():
            try:
                Teacher_number=self.teacher_number.get()
                teacher_deldb(Teacher_number)
                showinfo(title='确认', message='删除成功！')
                self.dele_menu.destroy()
            except:
                showinfo(title='错误', message='未知错误，请重新删除！')
                self.dele_menu.destroy()
        
        self.dele_menu = Toplevel(self.root)
        self.dele_menu.title('删除教师账号')
        winWidth = 200
        winHeight = 200

        screenWidth = self.dele_menu.winfo_screenwidth()
        screenHeight = self.dele_menu.winfo_screenheight()
        x = int((screenWidth - winWidth) / 2)
        y = int((screenHeight - winHeight) / 2)
        # 设置窗口初始位置在屏幕居中
        self.dele_menu.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
        # 设置窗口图标
        # root.iconbitmap("./image/icon.ico")
        # 设置窗口宽高固定
        self.dele_menu.resizable(0, 0)
            
        self.teacher_number=StringVar()
        Label(self.dele_menu, text='教师号: ').place(x=10, y=30)
        Entry(self.dele_menu, textvariable=self.teacher_number).place(x=50, y=30)
        Button(self.dele_menu, text='确认删除',command=sure_dele).place(x=80, y=80)
        
 def change_ach(self):
        def add_new_subject():
            def sure_add():
                try:
                    Subject_name=self.subject_name.get()
                    achievement_insertData(Subject_name)
                    showinfo(title='确认', message='添加成功！')
                    self.dele_menu.destroy()
                except:
                    showinfo(title='错误', message='未知错误，请重新修改！')
                    self.dele_menu.destroy()
                
            self.change_menu.destroy()
            self.dele_menu = Toplevel(self.root)
            self.dele_menu.title('修改学生成绩')
            winWidth = 200
            winHeight = 200

            screenWidth = self.dele_menu.winfo_screenwidth()
            screenHeight = self.dele_menu.winfo_screenheight()
            x = int((screenWidth - winWidth) / 2)
            y = int((screenHeight - winHeight) / 2)
            # 设置窗口初始位置在屏幕居中
            self.dele_menu.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
            # 设置窗口图标
            # root.iconbitmap("./image/icon.ico")
            # 设置窗口宽高固定
            self.dele_menu.resizable(0, 0)
            
            self.subject_name=StringVar()
            Label(self.dele_menu, text='科目名: ').place(x=10, y=30)
            Entry(self.dele_menu, textvariable=self.subject_name).place(x=50, y=30)
            Button(self.dele_menu, text='确认添加',command=sure_add).place(x=80, y=80)
        
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
        
 def teacher_sign_up(self):
        def insert_sql():
            try:
                age = self.new_age.get()
                number = self.new_number.get()
                name = self.new_name.get()
                pw = self.new_pw.get()
                XWC=user_showdb(number)
                SHB=teacher_showdb(number)
                if XWC == None and SHB == None:
                    teacher_insertData(number,name,pw,age)
                    showinfo(title='提示', message='注册成功')
                    self.window_sign_up.destroy()
                else:
                    showinfo(title='提示',message='教师号重复，注册失败，请修改教师号！')  
            except:
                showinfo(title='错误',message='输入错误，请重新输入！')
                

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
        Label(self.window_sign_up, text='教师号: ').place(x=10, y=90)
        entry_student_number = Entry(self.window_sign_up, textvariable=self.new_number)
        entry_student_number.place(x=130, y=90)
        
        self.new_pw = StringVar()
        Label(self.window_sign_up, text='密码: ').place(x=10, y=130)
        entry_usr_pw = Entry(self.window_sign_up, textvariable=self.new_pw, show='*')
        entry_usr_pw.place(x=130, y=130)

        sign_up = Button(self.window_sign_up, text='注册', command=insert_sql)
        sign_up.place(x=237, y=160)
        
 def print_student_ach(self):
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
            all_str=achievement_slectTable()
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