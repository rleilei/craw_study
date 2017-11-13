import codecs
import sqlite3
import


class DataOutput():
    def __init__(self):
        self.datas=[]
    def store_data(self,data):
        if data is None:
            return
        self.datas.append(data)
    def output_html(self):
       return





#创建sqlite3数据连接
        # conn = sqlite3.connect('baike.db')#建立连接对象
        # cur = conn.cursor()#建立游标对象
        # create_table="create table if not exists baike(url text,title text,content text)"#创建表格
        # cur.execute(create_table)#执行SQL语句，创建表格
        # for data in self.datas:
        #     inser_data="insert into baike values('%s','%s','%s')"%(data['url'],data['title'],data['content'])
        #     #print(inser_data)
        #     cur.execute(inser_data)#插入数据，多个数据可用executemany
        #     conn.commit()
        # cur.close()
        # conn.close()

#查询sqlite3数据
# conn = sqlite3.connect('baike.db')  # 建立连接对象
# cur = conn.cursor()  # 建立游标对象
# cur.execute('select * from baike')
# for row in cur.fetchall():
#     print(row)

        # #将数据保存在网页文件中
        # font =codecs.open(r'D:\桌面\baike.html','w','utf-8')
        # font.write("<html>")
        # font.write("<head><title>百度百科</title><br><meta charset='utf-8'></head>")
        # font.write("<body>")
        # font.write("<table width='100%' align='center' border='1' rules='all'>")
        # font.write("<tr align='center'>")
        # #font.write("<th>URL</th>")
        # font.write("<th width ='100'>TITLE</th>")
        # font.write("<th>CONTENT</th>")
        # font.write("</tr>")
        # font.write("<h1>%s</h1>"%len(self.datas))
        # for data1 in self.datas:
        #     font.write("<tr align='left'>")
        #     #font.write("<td><i><font size='1px'><a href=%s target=_blank>%s</a></font></i></td>"%(data1['url'],data1['url']))
        #     font.write("<td width ='100'><font size='3px'><a href=%s target=_blank>%s</a></font></td>"%(data1['url'],data1['title']))
        #     font.write("<td><font size='2px'>%s</font></td>"%(data1['content']))
        #     font.write("</tr>")
        #     #self.datas.remove(data1)
        # #font.write("</table>")
        # font.write("</table>")
        # font.write("</body>")
        # font.write("</html>")
        # font.close()
