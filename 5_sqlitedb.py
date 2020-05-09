import sqlite3
conn = sqlite3.connect('tasbih.db')
c = conn.cursor()

# insert 1 data
c.execute('insert into tasbihcount (tasbih) values (1)')
conn.commit()

# select all data
c.execute('select * from tasbihcount order by tanggal desc')
data = c.fetchall()
print(data)

# select blank data
c.execute('select * from tasbihcount where id=222')
data = c.fetchone()
print(data)

# select data group by
c.execute('select tanggal, sum(tasbih) from tasbihcount group by tanggal order by tanggal desc')
data = c.fetchone()
print(data)
print(type(data))
print(data[1])
