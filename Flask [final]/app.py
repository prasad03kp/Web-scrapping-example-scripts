import webbrowser

from flask import Flask, render_template, request
app = Flask(__name__)
from tabulate import tabulate
import mysql.connector
import re
import os
head=list()
link=list()
class Database:
   def index(self):
      k = mysql.connector.connect(
         host='localhost',
         user='root',
         passwd='xxxxxxxx',
         database='DBname',
         auth_plugin='mysql_native_password'
      )
      cur=k.cursor()
      cur.execute("""SELECT * FROM TBname""")
      result=cur.fetchall()

      return result
def match(a,fstring):
   if re.search(a, fstring,re.IGNORECASE):
      return True
   else:
      return  False
@app.route('/')
def links():
   def db_query():
      db = Database()
      emps = db.index()

      return emps

   res = db_query()
   for row in res:
      head.append(row[1])
      link.append(row[2])
   print(head[:])
   print(link[:])
   #return render_template('links.html', result=res, content_type='application/json')
   #print(tabulate(res, headers=['Title','Sub title','link'], tablefmt='psql'))
   return render_template('main.html')


@app.route('/', methods=['POST'])
def my_form_post():
    a = request.form['text']
    for i in range(0, len(head)):
       if (match(a, head[i])):
          url = link[i]
          webbrowser.open(url)
          return render_template('main.html')
    for i in range(0, len(head)):
       if (match(a, link[i])):
          url = link[i]
          webbrowser.open(url)
          return render_template('main.html')
    return render_template('main1.html')


if __name__ == '__main__':
   app.run(debug = True)