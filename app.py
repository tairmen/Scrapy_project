from flask import Flask, render_template
from data import Articles
from pymongo import MongoClient
import pprint
import operator
client = MongoClient()

app = Flask(__name__)

db = client.mydb
dtc = db.HabrSpider

Themes=[]

topic='3D-моделирование'
Themes.append(topic)

print(Themes)

@app.route('/')
def themes():
	return render_template('home.html',Themes= Themes)

@app.route('/<path:id>')
def article(id):
	id_col=dtc

	d = {}
	for elem in id_col.find():
		author_name=str(elem['author'])
		if (author_name == "['{username}']" or author_name == "[]"): continue 
		d.update({author_name[2:-2]:id_col.find({"author":elem['author']}).count()})

	d1 = sorted(d.items(), key=operator.itemgetter(1), reverse=True)

	return render_template('btc_info.html',id=id,dictt=d1)


@app.route('/<path:tid>/user/<path:id>')
def userInfo(tid,id):
	id_col=dtc

	return render_template('user_info.html',id=id,author_mess=id_col.find({'author':id}),user_m_count=id_col.find({'author':id}).count(),all_m_count=id_col.find().count())

if __name__ == '__main__':
	app.run(debug=True)