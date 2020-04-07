# -*- coding:utf-8 -*-
import sqlite3
# 打开教师数据库
def teacher_opendb():
        conn = sqlite3.connect("student.db")
        cur = conn.execute("""create table if not exists teacher_info(
        id integer PRIMARY KEY autoincrement,
        teacher_number varchar(12),
        teacher_name varchar(10),
        teacher_passworld varchar(128),
        age varchar(2))""")
        return cur, conn
    
#查询所有列名
def teacher_lie_name():
    hel = teacher_opendb()
    cur = hel[1].cursor()
    cur.execute("select * from teacher_info")
    col_name_list = [tuple[0] for tuple in cur.description]  
    return col_name_list
    cur.close()

#查询教师全部信息
def teacher_slectTable():
        hel = teacher_opendb()
        cur = hel[1].cursor()
        cur.execute("select * from teacher_info")
        res = cur.fetchall()
        #for line in res:
                #for h in line:
                        #print(h),
                #print(line)
        return res
        cur.close()
        
#  往教师数据库中添加内容
def teacher_insertData(number,name,pw,age):
        hel = teacher_opendb()
        hel[1].execute("insert into teacher_info(teacher_number,teacher_name, teacher_passworld,age)values (?,?,?,?)",(number,name,pw,age))
        hel[1].commit()
        hel[1].close()
        
#查询教师个人信息
def teacher_showdb(number):
        hel = teacher_opendb()
        cur = hel[1].cursor()
        cur.execute("select * from teacher_info where teacher_number="+number)
        res = cur.fetchone()
        cur.close()
        return res
    
#   删除教师数据库中的全部内容
def teacher_delalldb():
        hel = teacher_opendb()              # 返回游标conn
        hel[1].execute("delete from teacher_info")
        print("删库跑路XWC我最帅")
        hel[1].commit()
        hel[1].close()
        
#   删除教师数据库中的指定内容
def teacher_deldb(number):
        hel = teacher_opendb()              # 返回游标conn
        hel[1].execute("delete from teacher_info where teacher_number="+number)
        print("已删除教师号为 %s 教师" %number)
        hel[1].commit()
        hel[1].close()
        
#  修改教师数据库的内容
def teacher_alter(number,name,pw,age):
        hel = teacher_opendb()
        hel[1].execute("update teacher_info set teacher_name=?, teacher_passworld= ?,age=? where teacher_number="+number,(name,pw,age))
        hel[1].commit()
        hel[1].close()
        
#  修改教师数据库密码的内容
def teacher_alter_pw(number,pw):
    hel = teacher_opendb()
    hel[1].execute("update teacher_info set teacher_passworld= %s where teacher_number=%s"%(pw,number))
    hel[1].commit()
    hel[1].close()
        
# 登录查询教师数据
def teacher_slect_number_pw(number,pw):
        hel = teacher_opendb()
        cur = hel[1].cursor()
        cur.execute("select * from teacher_info where teacher_number="+number+" and teacher_passworld= "+pw)
        hel[1].commit()
        for row in cur:
            if row:
                return True
            else:
                return False
        cur.close()
        hel[1].close()