from flask import *
from database import *

teacher=Blueprint('teacher',__name__)

@teacher.route('/teacherhome')
def teacherhome():
	return render_template('teacherhome.html')

@teacher.route('/teacherviewperiods')
def teacherviewperiods():
	data={}
	q="select * from periods"
	r=select(q)
	data['periodss']=r
	return render_template('teacherviewperiods.html',data=data)

@teacher.route('/teacherviewattendance',methods=['get','post'])
def teacherviewattendance():
	data={}
	if "submit" in request.form:
		subject=request.form['subject']
		q="SELECT *,attendance.`date` AS adate FROM attendance INNER JOIN `periods` USING(`period_id`)INNER JOIN `student`USING(`student_id`) where period_id='%s'"%(subject)
		r=select(q)
		data['search']=r
		q="SELECT count(attendance_id) as aid FROM attendance INNER JOIN `periods` USING(`period_id`)INNER JOIN `student`USING(`student_id`) where period_id='%s'"%(subject)

		res=select(q)
		data['cou']=res[0]['aid']
	q="SELECT * from `periods` "
	r=select(q)
	data['view']=r
	
	return render_template('teacherviewattendance.html',data=data)

@teacher.route('/teachermanagestudents',methods=['get','post'])
def teachermanagestudents():
	data={}
	if "register" in request.form:
		fna=request.form['f']
		lna=request.form['l']
		pla=request.form['pl']
		a=request.form['ag']
		em=request.form['e']
		uname=request.form['u']
		pwd=request.form['p']
		ql="insert into login values(null,'%s','%s','student')"%(uname,pwd)
		rl=insert(ql)
		qs="insert into student values(null,'%s','%s','%s','%s','%s','%s')"%(rl,fna,lna,pla,a,em)
		idd=insert(qs)
		
		return redirect(url_for('teacher.teachermanagestudents'))
	if "action" in request.args:
		action=request.args['action']
		sid=request.args['sid']
	else:
		action=None
	if "update" in request.form:
		fna=request.form['f']
		lna=request.form['l']
		pla=request.form['pl']
		a=request.form['ag']
		em=request.form['e']

		q="update student set firstname='%s',lastname='%s',place='%s',age='%s',email='%s' where student_id='%s'"%(fna,lna,pla,a,em,sid)
		r=update(q)
		return redirect(url_for('teacher.teachermanagestudents'))
	if action=="update":
		q="select * from  student where student_id='%s'"%(sid)
		r=select(q)
		data['updatestudent']=r
	if action=="delete":
		q="delete from student where student_id='%s'"%(sid)
		delete(q)
		return redirect(url_for('teacher.teachermanagestudents'))
	q="select * from student"
	r=select(q)
	data['students']=r
	
	return render_template('teachermanagestudents.html',data=data)
