from flask import *
from database import *
import demjson

api=Blueprint('api',__name__)

@api.route('/studenthome')
def studenthome():
	return demjsom.encode(data)

@api.route('/login')
def login():
	data={}
	username=request.args['username']
	password=request.args['password']
	q="select login.login_id,student_id as sid,login.usertype from login inner join student using(login_id) where username='%s' and password='%s' union select login.login_id,teacher_id as sid,login.usertype from login inner join teacher using(login_id) where username='%s' and password='%s'"%(username,password,username,password)
	r=select(q)
	if r:
		data['status']="success"
		data['data']=r
	else:
		data['status']="failed"
	return demjson.encode(data)


@api.route('/studentviewperiods')
def studentviewperiods():
	data={}
	q="select * from periods"
	r=select(q)
	if r:
		data['status']="success"
		data['data']=r
	else:
		data['status']="failed"
	return demjson.encode(data)

@api.route('/studentviewattendance')
def studentviewattendance():
	data={}
	period_id=request.args['period_id']
	login_id=request.args['login_id']
	q="SELECT *,attendance.`date` AS adate FROM attendance INNER JOIN `periods` USING(`period_id`)INNER JOIN `student`USING(`student_id`) where period_id='%s' and login_id='%s'"%(period_id,login_id)
	r=select(q)
	if r:
		data['status']="success"
		data['data']=r
	else:
		data['status']="failed"
	data['method']="studentviewattendance"
	return demjson.encode(data)

@api.route('/teacherviewattendance')
def teacherviewattendance():
	data={}
	period_id=request.args['period_id']
	q="SELECT *,attendance.`date` AS adate FROM attendance INNER JOIN `periods` USING(`period_id`)INNER JOIN `student`USING(`student_id`) where period_id='%s' "%(period_id)
	r=select(q)
	if r:
		data['status']="success"
		data['data']=r
	else:
		data['status']="failed"
	data['method']="teacherviewattendance"
	return demjson.encode(data)


@api.route('/studentperiods')
def studentperiods():
	data={}
	q="select * from periods"
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="success"
	data['method']="studentperiods"
	return demjson.encode(data)


@api.route('/studentviewperiodss')
def studentviewperiodss():
	data={}
	q="select * from periods"
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="success"
	data['method']="studentviewperiodss"
	return demjson.encode(data)


@api.route('/markattendnace')
def markattendnace():
	data={}
	pid=request.args['pid']
	id=request.args['id']
	q="insert into attendance values(null,(select student_id from student where login_id='%s'),'%s',curdate())" %(id,pid)
	insert(q)
	data['status']="success"
	data['method']="markattendnace"
	return demjson.encode(data)
	