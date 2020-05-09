from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def rekapharian():
   conn = sqlite3.connect('tasbih.db')
   c = conn.cursor()
   c.execute('select tanggal, sum(tasbih) from tasbihcount group by tanggal order by tanggal desc')
   data = c.fetchall()
   return render_template('app.html', data=data)

if __name__ == '__main__':
   app.run(
      debug = True,
      host = '192.168.43.10'
   )
