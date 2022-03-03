from flask import *
from database import *
import qrcode
import uuid

admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhome():
	return render_template('adminhome.html')


@admin.route('/adminmanageteacher',methods=['get','post'])
def adminmanageteacher():
	data={}
	if "register" in request.form:
		fna=request.form['f']
		lna=request.form['l']
		pla=request.form['pl']
		pho=request.form['ph']
		em=request.form['e']
		de=request.form['desg']
		uname=request.form['u']
		pwd=request.form['p']
		ql="insert into login values(null,'%s','%s','teacher')"%(uname,pwd)
		rl=insert(ql)
		qs="insert into teacher values(null,'%s','%s','%s','%s','%s','%s','%s')"%(rl,fna,lna,pla,pho,em,de)
		insert(qs)
		return redirect(url_for('admin.adminmanageteacher'))
	if "action" in request.args:
		action=request.args['action']
		mid=request.args['mid']
	else:
		action=None
	if "update" in request.form:
		fna=request.form['f']
		lna=request.form['l']
		pla=request.form['pl']
		pho=request.form['ph']
		em=request.form['e']
		de=request.form['desg']

		q="update teacher set firstname='%s',lastname='%s',place='%s',phone='%s',email='%s',desgination='%s' where teacher_id='%s'"%(fna,lna,pla,pho,em,de,mid)
		r=update(q)
		return redirect(url_for('admin.adminmanageteacher'))
	if action=="update":
		q="select * from  teacher where teacher_id='%s'"%(mid)
		r=select(q)
		data['updateteacher']=r
	if action=="delete":
		q="delete from teacher where teacher_id='%s'"%(mid)
		delete(q)
		return redirect(url_for('admin.adminmanageteacher'))
	q="select * from teacher"
	r=select(q)
	data['teachers']=r
	return render_template('adminmanageteacher.html',data=data)


@admin.route('/adminmanageperiods',methods=['get','post'])
def adminmanageperiods():
	data={}
	if "register" in request.form:
		s=request.form['s']
		d=request.form['d']
		ft=request.form['ft']
		tt=request.form['tt']
		qs="insert into periods values(null,'%s','%s','%s','%s','')"%(s,d,ft,tt)
		idd=insert(qs)
		path = "static/qrcode/" + str(uuid.uuid4()) + ".png"
		img = qrcode.make(str(idd))
		img.save(path)
		q="update periods set qrcode='%s' where period_id='%s'" %(path,idd)
		update(q)
		return redirect(url_for('admin.adminmanageperiods'))
	if "action" in request.args:
		action=request.args['action']
		mid=request.args['mid']
	else:
		action=None
	if "update" in request.form:
		s=request.form['s']
		d=request.form['d']
		ft=request.form['ft']
		tt=request.form['tt']
		
		q="update periods set subject='%s',date='%s',fromtime='%s',totime='%s' where period_id='%s'"%(s,d,ft,tt,mid)
		idd=update(q)
		path = "static/qrcode/" + str(uuid.uuid4()) + ".png"
		img = qrcode.make(str(idd))
		img.save(path)
		return redirect(url_for('admin.adminmanageperiods'))
	if action=="update":
		q="select * from  periods where period_id='%s'"%(mid)
		r=select(q)
		data['updateperiod']=r
	if action=="delete":
		q="delete from periods where period_id='%s'"%(mid)
		delete(q)
		return redirect(url_for('admin.adminmanageperiods'))
	q="select * from periods"
	r=select(q)
	data['periodss']=r
	return render_template('adminmanageperiods.html',data=data)

@admin.route('/adminviewstudent',methods=['get','post'])
def adminviewstudent():
	data={}
	q="select * from student"
	r=select(q)
	data['students']=r
	return render_template('adminviewstudent.html',data=data)


@admin.route('/adminviewattendance')
def adminviewattendance():
	data={}
	sid=request.args['sid']
	q="SELECT *,attendance.`date` AS adate FROM attendance INNER JOIN `periods` USING(`period_id`)WHERE `student_id`='%s'"%(sid)	
	r=select(q)
	data['attend']=r

	return render_template('adminviewattendance.html',data=data)

@admin.route('/adminviewfullattendance',methods=['get','post'])
def adminviewfullattendance():
	data={}
	if "submit" in request.form:
		subject=request.form['subject']
		q="SELECT *,attendance.`date` AS adate FROM attendance INNER JOIN `periods` USING(`period_id`)INNER JOIN `student`USING(`student_id`) where period_id='%s'"%(subject)
		r=select(q)
		data['search']=r
	q="SELECT * from `periods` "
	r=select(q)
	data['view']=r
	q="SELECT *,attendance.`date` AS adate FROM attendance INNER JOIN `periods` USING(`period_id`)INNER JOIN `student`USING(`student_id`)"	
	r=select(q)
	data['attend']=r

	if "search" in request.form:
	 	sn="%"+request.form['sname']
	 	print(sn)
	 	q="select *,attendance.`date` AS adate FROM attendance INNER JOIN `periods` USING(`period_id`)INNER JOIN `student`USING(`student_id`) where  firstname like '%s' or attendance.date like '%s'"%(sn,sn)
	 	print(q)
	 	r=select(q)
	 	print(r)
	 	data['search']=r



	return render_template('adminviewfullattendance.html',data=data)