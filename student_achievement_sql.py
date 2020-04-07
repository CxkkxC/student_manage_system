# -*- coding:utf-8 -*-
import sqlite3
from student_info_sql import *
# 打开成绩数据库
def achievement_opendb():
        conn = sqlite3.connect("student.db")
        cur = conn.execute("""create table if not exists student_achievement(
        student_number varchar(12),
        student_name varchar(10))""")
        return cur, conn
    
#查询所有列名
def achievement_lie_name():
    hel = achievement_opendb()
    cur = hel[1].cursor()
    cur.execute("select * from student_achievement")
    col_name_list = [tuple[0] for tuple in cur.description]  
    return col_name_list
    cur.close()
    
#查询学生成绩全部信息
def achievement_slectTable():
        hel = achievement_opendb()
        cur = hel[1].cursor()
        cur.execute("select * from student_achievement")
        res = cur.fetchall()
        #for line in res:
                #for h in line:
                        #print(h),
                #print(line)
        return res
        cur.close()
        
#  往成绩数据库中添加新的一列科目成绩
def achievement_insertData(subject_name):
        hel = achievement_opendb()
        hel[1].execute("alter table student_achievement add column "+subject_name+" int")
        hel[1].commit()
        hel[1].close()
        
#  往成绩数据库中添加学生跟学生信息表同步更新
def achievement_infoData(number,name):
        hel = achievement_opendb()
        hel[1].execute("insert into student_achievement(student_number,student_name)values (?,?)",(number,name))
        hel[1].commit()
        hel[1].close()
        
#  按某科排序输出 默认升序  添加desc为降序
def achievement_paixu(subject_name,desc):
        if desc==None:
            desc=""
        else:
            desc=desc
        hel = achievement_opendb()
        cur = hel[1].cursor()
        cur.execute("select * from student_achievement order by "+subject_name+" "+desc)
        res = cur.fetchall()
        cur.close()
        return res
        
#查询个人成绩信息
def achievement_showdb(number):
        hel = achievement_opendb()
        cur = hel[1].cursor()
        cur.execute("select * from student_achievement where student_number="+number)
        res = cur.fetchone()
        cur.close()
        return res
    
#   删除成绩数据库中的全部内容
def achievement_delalldb():
        hel = achievement_opendb()              # 返回游标conn
        hel[1].execute("delete from student_achievement")
        print("删库跑路XWC我最帅")
        hel[1].commit()
        hel[1].close()
        
#   删除成绩数据库中的指定学生内容跟学生信息表同步更新
def achievement_deldb(number):
        hel = achievement_opendb()              # 返回游标conn
        hel[1].execute("delete from student_achievement where student_number="+number)
        print("已删除学号为%s 学生的成绩单" %number)
        hel[1].commit()
        hel[1].close()
        
#  修改成绩数据库的个人某科成绩
def achievement_alter(number,subject_name,ach):
        hel = achievement_opendb()
        hel[1].execute("update student_achievement set %s = %s where student_number=%s"%(subject_name,ach,number))
        hel[1].commit()
        hel[1].close()