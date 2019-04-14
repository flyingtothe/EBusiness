import MySQLdb as mdb
import time
#将con设定为全局连接
conn = mdb.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='EBusiness', charset='utf8');
cur = conn.cursor()
i = 0
while i<=100:
	print(i)
	t = time.time()
	name = "张三" + str(i)
	type = ""
	introduce =""
	shelf_life = format("yyyy-mm-dd",str(t))
	warranty = format("yyyy-mm-dd",str(t))
	product_param = ""
	price = ""
	inventory = ""
	sql = "insert into ebapp_goods(name,type,introduce,shelf_life,warranty,product_param,price,inventory) values (%s,%s,%s,%s,%s,%s,%s,%s)"
	params = (name,type,introduce,shelf_life,warranty,product_param,price,inventory)
	#sql = "insert into table(key1,key2,key3) values (%s,%s,%s)"%(value1,value2,value3)
	temp=cur.execute(sql,params)
	i +=1

print(2)
conn.commit()
recount = cur.execute('select *from Goods')
rows = cur.fetchall()


cur.close()
conn.close()
for time in rows:
	# print temp #查看影响条目
	# print rows #查看数据库表内容
	print(time)