from flask import *
from database import *

public=Blueprint('public',__name__)


@public.route('/')
def home():
	return render_template('home.html')


@public.route('/login',methods=['get','post'])
def login():
	if "login" in request.form:
		uname=request.form['un']
		pwd=request.form['pa']
		q="select * from login where username='%s' and password='%s'"%(uname,pwd)
		res=select(q)
		if res:
			if res[0]['usertype']=="admin":
				return redirect(url_for('admin.adminhome'))
			elif res[0]['usertype']=="teacher":
				q="select * from teacher where login_id='%s'"%(res[0]['login_id'])
				r=select(q)
				session['teacherid']=r[0]['teacher_id']
				return redirect(url_for('teacher.teacherhome'))

	return render_template('login.html')