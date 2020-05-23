from flask import Flask,render_template,url_for,request,redirect
import pymysql

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('./sql/form.html')



"""@app.route('/<string:page_name>')
def html_pages(page_name):
    return render_template(page_name)


@app.route('/<string:sub_pagename>')
def html_pages1(subpage_name):
	return render_template('./sql/form.html')



def write_to_file(data):
 	with open ('database.txt',mode='a') as database:
 		email=data['email']
 		subject=data['subject']
 		message=data['message']
 		file=database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
 	with open ('database.csv',newline='',mode='a') as database2:
 		email=data['email']
 		subject=data['subject']
 		message=data['message']
 		csv_writer=csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
 		csv_writer.writerow([email,subject,message])
"""
"""@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
	if request.method =='POST':
		try:
			data=request.form.to_dict()
			write_to_file(data)
			return redirect('/thankyou.html')
		except :
			return 'did not save to database'
	else:
		return'Something went wrong'"""

db=pymysql.connect('localhost','root','2331998ayo', 'futa')


@app.route('/submit',methods=['POST','GET'])
def submit_form():
	if request.method =='POST':
		try:
			email=request.form['firstname']   
			subject=request.form['subject']
			message=request.form['message']
			cur=db.cursor()
			cur.execute('INSERT INTO student(email,subject,message) VALUES(%s,%s,%s.format(email,subject,message)))')
			mysql.connection.commit()
			cur.close()
			return 'success'
		except :
			return 'did not save to database'
	else:
		return'Something went wrong'


if __name__=='__main__':

	app.run()
