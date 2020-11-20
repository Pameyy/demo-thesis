from flask import Flask, render_template, request, session, redirect, url_for, flash, send_from_directory
import pymysql,re,os
import glob
from pymysql import cursors
from datetime import date
import datetime
from werkzeug import secure_filename
import cv2

import re
import easyocr

reader = easyocr.Reader(['en'],True)


app = Flask(__name__, template_folder='template')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

db = pymysql.connect(host="localhost",
                     user='root',
                     password = '1234',
                     db = 'test',
                     charset='utf8',
                     use_unicode=True)

cursor1 = db.cursor(cursors.DictCursor)
cursor = db.cursor()

#query date of show bill

dateN = date.today()

strD = str(dateN)

splitDate = strD.split("-")

year = int(splitDate[0])
month = int(splitDate[1])

if month == 1 :
    
    month_pre = month + 11
    year_pre = year - 1

    strF = date(year_pre,month_pre,25)
    strL = date(year,month,25)
    
else:

    month_pre = month -1 
    strF = date(year,month_pre,25)
    strL = date(year,month,25)



app.config['UPLOAD_FOLDER'] = 'upload/'
app.config["UPLOAD_METER"] = 'static/upload/meter/'
app.config["UPLOAD_WATER"] = 'static/upload/water/'

@app.route('/start')
def start():
    return redirect(url_for('login'))

@app.route('/')
def welcome():
    return render_template("welcome.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
# Output message if something goes wrong...
    msg = ''
    name_user = ''
    bill = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
        # Fetch one record and return result
        account = cursor.fetchone()

                # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account[0]
            session['username'] = account[1]

            status = account[6]
            name_user = account[3]

            if status == "staff":
                return render_template('index.html')
                # return redirect(url_for('start_index'))
            
            elif status == "resident":

                cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
                user = cursor.fetchone()
                user_id = user[0]
                name_user = user[3]
                # print(user)

                cursor.execute('SELECT id,room_name FROM room WHERE user_id = %s', user_id)
                room = cursor.fetchone()
                room_id = room[0]
                name_room = room[1]
                # print(room_id)

                Qdate = ''
                history =''

                

                cursor.execute('SELECT * FROM history WHERE date between %s and %s and room_id =%s',
                               (strF, strL, room_id))
                Qdate = cursor.fetchone()
                print(Qdate)
                print(strF)
                print(strL)

                year = int(Qdate[2])
                
                cursor.execute('SELECT month.month, bill.water, bill.electric, bill.cost_total FROM bill INNER JOIN month ON bill.month = month.id_month WHERE room_id = %s AND year = %s ORDER BY bill.month;', (room_id,year))
                history = cursor.fetchall()
                # print(history)

                return render_template('home_resident.html', Qdate = Qdate, name_user = name_user, history=history,name_room=name_room )
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    return render_template('login.html' , msg=msg)


@app.route('/register', methods=['GET', 'POST'])
def register():

    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        fullname = request.form['fullname']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        tel = request.form['tel']
        status = request.form['status']

        # Check if account exists using MySQL
        cursor.execute('SELECT * FROM users WHERE username = %s', username)
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            # register_get_data = """INSERT INTO users(fullname, username, password, email) VALUES(%s, %s, %s, %s) """
            # cursor.execute(register_get_data,(fullname,username, password, email))
            # db.commit()

            register_get_data = """INSERT INTO users(fullname, username, password, email, tel , status) VALUES(%s, %s, %s, %s, %s, %s) """
            cursor.execute(register_get_data, (fullname, username, password, email, tel, status))
            db.commit()
            msg = 'You have successfully registered!'

    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)



@app.route('/start')
def start_index():
    return render_template('index.html')

@app.route('/modals')
def table():
    return render_template('modals.html')

@app.route('/testform')
def testform():
    return render_template('testForm.html')    

@app.route('/upload_for_ocr')
def upload_for_ocr():
    return render_template('upload.html')


@app.route('/upload', methods=['GET','POST'])
def ocr():
    image_path = ''
    text = ''

    cursor.execute("SELECT id,room_name FROM room")
    data = [item for item in cursor.fetchall()]
    

    if request.method =='POST':
        f_meter = request.files['file_meter']
        water = request.files['file_water']

        filenameM = secure_filename(f_meter.filename)
        filenameM = str(len(os.listdir(app.config['UPLOAD_METER'])) + 1) + '.jpg'
        filenameM_path = os.path.join(app.config["UPLOAD_METER"], filenameM)
        f_meter.save(filenameM_path)


        filenameW = secure_filename(water.filename)
        filenameW = str(len(os.listdir(app.config['UPLOAD_WATER'])) + 1) + '.jpg'
        filenameW_path = os.path.join(app.config["UPLOAD_WATER"], filenameW)
        water.save(filenameW_path)

#detecd meter electric
        image_meter = max(glob.glob(r'static/upload/meter\*.jpg'), key=os.path.getctime)
        resMT = cv2.imread(image_meter)
        scale_percent = 20  # percent of original size
        width = int(resMT.shape[1] * scale_percent / 100)
        height = int(resMT.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized_meter = cv2.resize(resMT, dim, interpolation = cv2.INTER_AREA)
        parsed = reader.readtext(resized_meter)
        print(parsed)
        textMt = '\n'.join(map(lambda x: x[1], parsed))
        res_mt = re.findall(r"\d", textMt)
        
        if len(res_mt) == 0:
            ocrMT = 'ไม่สามารถตรวจจับเลขได้ กรุณากรอกเลขมิเตอร์'
        else:
            ocrMT = int("".join(map(str, res_mt)))
        

# detech meter water
        image_water = max(glob.glob(r'static/upload/water\*.jpg'), key=os.path.getctime)
        resWT = cv2.imread(image_water)
        scale_percent = 20  # percent of original size
        width = int(resWT.shape[1] * scale_percent / 100)
        height = int(resWT.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized_water= cv2.resize(resWT, dim, interpolation = cv2.INTER_AREA)
        parsed = reader.readtext(resized_water)
        print(parsed)
        textWt = '\n'.join(map(lambda x: x[1], parsed))
        res_wt = re.findall(r"\d", textWt)
        if len(res_wt) == 0:
            ocrWT = 'ไม่สามารถตรวจจับเลขได้ กรุณากรอกเลขมิเตอร์'
        else:
            ocrWT = int("".join(map(str, res_wt)))

        

        print(image_meter)
        print(image_water)

        print("meter : ",ocrMT)
        print("Water : ",ocrWT)

       
        return render_template('forms.html',data=data,ocrMT=ocrMT,ocrWT=ocrWT,filenameMT =image_meter, filenameWT = image_water,path_meter = filenameM_path,path_water=filenameW_path )
        # return render_template('forms.html',data=data,ocrMT=ocrMT,ocrWT=ocrWT,filenameMT =image_meter, filenameWT = image_water )
    return redirect(url_for('upload_for_ocr'))


@app.route('/upload/meter/<filename>')
def send_imageMT(image_meter):
    return send_from_directory('static/upload/meter/', image_meter)

@app.route('/upload/water/<filename>')
def send_imageWT(image_water):
    return send_from_directory('static/upload/water/', image_water)



@app.route('/savedata', methods = ['GET','POST'])
def savedata():
    # msg = ''
    if request.method == 'POST':
        month = int(request.form['month'])
        year = int(request.form['year'])
        number_electric = request.form['electric']
        number_water = request.form['water']
        room_id = int(request.form['room'])
        path_meter = request.form['path_meter']
        path_water = request.form['path_water']

        sql_get_data = "INSERT INTO meter(month, year, number_electric , number_water , room_id) VALUE ( %s, %s, %s,%s,%s)"

        cursor.execute(sql_get_data, (month, year, number_electric , number_water , room_id))
        db.commit()

        save_path = "INSERT INTO image_path(month, year, path_meter , path_water , room_id) VALUE ( %s, %s, %s,%s,%s)"

        cursor.execute(save_path, (month, year, path_meter , path_water , room_id))
        db.commit()


        msg = 'ทำการบันทึกข้อมูลสำเร็จ'
    return redirect(url_for('upload_for_ocr', msg = msg ))



@app.route('/queryforcalculate', methods=['GET','POST'])
def queryforcalculate():
    cursor.execute("SELECT id,room_name FROM room")
    data = [item for item in cursor.fetchall()]
    # cursor.close()
    # print(data)
    return render_template("calculate.html",data=data)

@app.route('/comfirm_data', methods=['GET','POST'])
def comfirm_data():
    if request.method == 'POST':
        room = request.form['room']
        month = request.form['month']
        year = request.form['year']

        
        #query name room
        cursor.execute("SELECT * FROM room WHERE id=%s",(room))
        name_room = cursor.fetchone()
        # print(name_room)
        room_id = int(name_room[0])
        name_room = name_room[1]
        
        cursor.execute("SELECT t1.number_electric,t1.number_water, t3.month, t2.room_name FROM meter AS t1 INNER JOIN room AS t2 ON t1.room_id = t2.id INNER JOIN month AS t3 ON t1.month = t3.id_month WHERE t1.room_id=%s && t1.month=%s && t1.year=%s ",(room, month, year))
        res_now = cursor.fetchone()
        print(res_now)

        return render_template('confirm_data.html',
            roomd_id = room,
            name_month = res_now[2],
            name_room = res_now[3],
            year = year,
            number_electric = res_now[0],
            number_water = res_now[1],
            month = month)


        # return redirect(url_for('queryforcalculate'))
    return redirect(url_for('queryforcalculate'))




@app.route('/calculate', methods=['GET','POST'])
def calculate():
    water = ''
    electric = ''
    bf_mt = ''
    bf_wt = ''
    this_mt = ''
    this_wt = ''
    dateN = date.today()
    room = ''
    month = ''
    year = ''
    prev_month = ''
    room_id = ''
    rent_room = ''
    total = int



    if request.method == 'POST':
        room = request.form['room']
        month = request.form['month']
        year = request.form['year']

        #query name room
        cursor.execute("SELECT * FROM room WHERE id=%s",(room))
        name_room = cursor.fetchone()
        # print(name_room)
        room_id = int(name_room[0])
        name_room = name_room[1]

        # query unit
        cursor.execute("SELECT * FROM units")
        units = cursor.fetchone()

        if month == "1":
           
            cursor.execute("SELECT number_electric,number_water,month,year FROM meter WHERE room_id=%s && month=%s && year=%s ",(room, month, year))
            res_now = cursor.fetchone()
            print(res_now)

            # query data present
            cursor.execute("SELECT number_electric,number_water,month,year FROM meter WHERE room_id=%s && month=%s+11 && year=%s-1 ", (room,month,year))
            res_pass = cursor.fetchone()
            print(res_pass)

        
            mt_now = res_now[0]
            wt_pass = res_pass[1]

            mt_pass = res_pass[0]
            wt_now = res_now[1]
            

            ## calculate for electric
            electric_unit = units[1]
            if mt_now >= mt_pass:
                cal_unit = mt_now - mt_pass
                cost_mt = cal_unit * electric_unit
                print(cost_mt)
            else:
                cal_unit = ((10000 - mt_pass)+mt_now)
                cost_mt = cal_unit * electric_unit
                print(cost_mt)

            water_unit = units[2]
            if wt_now >= wt_pass:
                cal_unit = wt_now - wt_pass
                cost_water = cal_unit * water_unit
                print(cost_water)
            else:
                cal_unit = ((1000 - wt_pass )+ wt_now)
                cost_water = cal_unit * water_unit
                print(cost_water)

            rent_room = units[3]
            total = int(rent_room + cost_mt + cost_water)

            print(total)
            print(month, year, dateN, cost_water, cost_mt, room_id)

            sql_save_bill = "INSERT INTO bill(month, year, date, water, electric,cost_total, room_id) VALUE (%s, %s, %s, %s, %s, %s,%s)"
            cursor.execute(sql_save_bill, (int(month), int(year), dateN, int(cost_water), int(cost_mt),int(total) ,int(room_id)))
            db.commit()

            save_history = "INSERT INTO history(month, year, date, water, electric, cost_total, before_meter, before_water, after_meter, after_water, room_id) VALUE (%s, %s, %s, %s, %s, %s,%s,%s, %s, %s,%s)"
            cursor.execute(save_history,
                           (int(month), int(year), dateN, int(cost_water), int(cost_mt), int(total), int(mt_pass), int(wt_pass), int(mt_now)
                           , int(wt_now), int(room_id)))
            db.commit()

            return render_template('bills.html', water= cost_water
                                   ,electric = cost_mt
                                   ,bf_mt = mt_pass
                                   ,bf_wt = wt_pass
                                   ,this_mt = mt_now
                                   ,this_wt = wt_now
                                   ,dateN = dateN
                                   ,room = name_room
                                   ,year = year
                                   ,room_id = room_id,
                                   total=total,
                                   rent_room = rent_room)


        else:
            
            cursor.execute("SELECT number_electric,number_water,month,year FROM meter WHERE room_id=%s && month=%s && year=%s ",
                (room, month, year))
            res_now = cursor.fetchone()
            print(res_now)

            # query data present
            cursor.execute("SELECT number_electric,number_water,month,year FROM meter WHERE room_id=%s && month=%s-1 && year=%s ",
                (room, month, year))
            res_pass = cursor.fetchone()
            print(res_pass)

            mt_now = res_now[0]
            wt_pass = res_pass[1]

            wt_now = res_now[1]
            mt_pass = res_pass[0]

            ## calculate for electric
            electric_unit = units[1]
            if mt_now >= mt_pass:
                cal_unit = mt_now - mt_pass
                cost_mt = cal_unit * electric_unit
                print(cost_mt)
            else:
                cal_unit = ((10000 - mt_pass) + mt_now)
                cost_mt = cal_unit * electric_unit
                print(cost_mt)

            water_unit = units[2]
            if wt_now >= wt_pass:
                cal_unit = wt_now - wt_pass
                cost_water = cal_unit * water_unit
                print(cost_water)
            else:
                cal_unit = ((1000 - wt_pass) + wt_now)
                cost_water = cal_unit * water_unit
                print(cost_water)

            rent_room = units[3]
            total = int(rent_room + cost_mt + cost_water)

            print(total)
            print(month, year, dateN, cost_water, cost_mt, room_id)

            sql_save_bill = "INSERT INTO bill(month, year, date, water, electric,cost_total, room_id) VALUE (%s, %s, %s, %s, %s, %s,%s)"
            cursor.execute(sql_save_bill,
                           (int(month), int(year), dateN, int(cost_water), int(cost_mt), int(total), int(room_id)))
            db.commit()

            save_history = "INSERT INTO history(month, year, date, water, electric, cost_total, before_meter, before_water, after_meter, after_water, room_id) VALUE (%s, %s, %s, %s, %s, %s,%s,%s, %s, %s,%s)"
            cursor.execute(save_history,
                           (int(month), int(year), dateN, int(cost_water), int(cost_mt), int(total), int(mt_pass), int(wt_pass), int(mt_now)
                           , int(wt_now), int(room_id)))
            db.commit()

            return render_template('bills.html', water=cost_water
                                   , electric=cost_mt
                                   , bf_mt=mt_pass
                                   , bf_wt=wt_pass
                                   , this_mt=mt_now
                                   , this_wt=wt_now
                                   , dateN=dateN
                                   , room=name_room
                                   , year=year
                                   , room_id=room_id,
                                   total=total,
                                   rent_room=rent_room)

    return redirect(url_for('queryforcalculate'))


@app.route('/queryforshow', methods=['GET','POST'])
def qeuryforshow():
    data =''
    cursor.execute("SELECT id,room_name FROM room")
    data1 = [item for item in cursor.fetchall()]

    # cursor.close()
    # print(data1)
    return render_template('report.html', data=data1)


@app.route('/report_room',methods=['GET','POST'])
def report_room():
    query=''
    data = ''
    cursor.execute("SELECT id,room_name FROM room")
    data1 = [item for item in cursor.fetchall()]


    if request.method == 'POST':
        room = request.form['room']
        # month = request.form['month']
        year = request.form['year']

        cursor.execute('SELECT month.month, bill.year, bill.water, bill.electric, bill.cost_total FROM bill INNER JOIN month ON bill.month = month.id_month WHERE room_id=%s and year=%s  ORDER BY bill.month ;', (room,year))
        query = cursor.fetchall()
        

        return render_template('report.html',query=query
                               ,data=data1)

@app.route('/report_month', methods = ['GET','POST'])
def report_month():

    query=''
    data = ''
    cursor.execute("SELECT id,room_name FROM room")
    data1 = [item for item in cursor.fetchall()]

    if request.method == 'POST':

        month_re = request.form['month']
        year = request.form['year']

        cursor.execute('SELECT n2.room_name,n3.month, n1.water, n1.electric, n1.cost_total FROM bill AS n1 INNER JOIN room AS n2 ON n1.room_id = n2.id INNER JOIN month AS n3 ON n1.month = n3.id_month WHERE n1.month=%s and n1.year=%s ORDER BY month;', (month_re,year))
        quert_month = cursor.fetchall()
        
    
    return render_template('report.html',quert_month=quert_month ,data = data1)

@app.route('/users')
def users():

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    cursor.execute("SELECT * FROM room")
    room = cursor.fetchall()

    

    return render_template('users.html', users =users, room= room )

@app.route('/update_users',methods = ['GET','POST'])
def update_users():

    if request.method == 'POST':
        id_user = request.form['id_user']
        fullname = request.form['fullname']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        tel = request.form['tel']
        status = request.form['status']
        
        print(id_user,fullname,username,password,email,tel,status)

        cursor.execute(""" UPDATE users SET fullname=%s, username=%s, password=%s ,email=%s ,tel=%s, status=%s  WHERE id=%s """
        ,(fullname,username,password,email,tel,status,id_user))
        db.commit()

        # print(id,fullname,username,password,email,tel,status)
    
        return redirect(url_for('users'))
    else:
        return redirect(url_for('start_index'))


@app.route('/insert_room', methods=['GET','POST'])
def insert_room():
    if request.method == 'POST':
        room_name = request.form['room_name']
        user_id = request.form['users_id']

        sql_insert_room = """INSERT INTO room(room_name,user_id ) VALUE(%s,%s) """
        cursor.execute(sql_insert_room,(room_name,user_id))
        db.commit()
        print('input room seccess')
    return redirect(url_for('units_setting'))


@app.route('/insert_user', methods=['GET','POST'])
def insert_user():
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        fullname = request.form['fullname']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        tel = request.form['tel']
        status = request.form['status']

        # Check if account exists using MySQL
        cursor.execute('SELECT * FROM users WHERE username = %s', username)
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            
            add_user = """INSERT INTO users(fullname, username, password, email, tel , status) VALUES(%s, %s, %s, %s, %s, %s) """
            cursor.execute(add_user, (fullname, username, password, email, tel, status))
            db.commit()
            msg = 'You have successfully add users!'

    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return redirect(url_for('users'))


@app.route('/units_setting' , methods = ['GET','POST'])
def units_setting():
    units=''
    room =''
    
    cursor.execute("SELECT * FROM units")
    units = cursor.fetchone()
    print(units)

    cursor.execute('SELECT room.id, room.room_name ,room.user_id, users.fullname  FROM room INNER JOIN users ON room.user_id = users.id')
    room = cursor.fetchall()
    print(room)

    cursor.execute('SELECT id,fullname FROM users')
    user = cursor.fetchall()


    return render_template('unit_setting.html', units=units,room=room,user = user)


@app.route('/update_unit', methods=['GET','POST'])
def update_unit():

    if request.method == 'POST':
        id_unit = request.form['id_unit']
        meter = request.form['meter']
        water = request.form['water']
        rent_room = request.form['rent_room']
        
        cursor.execute(""" UPDATE units SET unit_meter=%s, unit_water=%s, rent_room=%s WHERE id=%s """
        ,(meter, water, rent_room , id_unit))
        db.commit()


        return redirect(url_for('units_setting'))
    else:
        return redirect(url_for('users'))


@app.route('/data_room' , methods= ['GET','POST'])
def data_room():
    name_room =''

    if request.method == 'POST':
        room_id = request.form['room_id']
        year = request.form['year']

        

        cursor.execute("SELECT month.month, bill.water, bill.electric, bill.cost_total FROM bill INNER JOIN month ON bill.month = month.id_month WHERE room_id=%s AND year=%s ORDER BY bill.month;",(room_id,year))
        history = cursor.fetchall()
        

        cursor.execute('SELECT * FROM history WHERE date between %s and %s and room_id =%s',
                               (strF, strL, room_id))
        Qdate = cursor.fetchone()

        cursor.execute('SELECT room_name FROM room WHERE id = %s', room_id)
        room = cursor.fetchone()
        name_room = room[0]
        
        

        return render_template('home_resident.html',history = history, Qdate = Qdate, name_room = name_room)


@app.route('/update_room', methods = ['GET','POST'])
def update_room():
    if request.method == 'POST':
        id_room = request.form['id']
        room_name = request.form['room_name']
        users_id = request.form['user_id']

        upRoom = cursor.execute(""" UPDATE room SET name_room=%s, user_id=%s, WHERE id=%s """
        ,(room_name, users_id, id_room))
        db.commit()

        return redirect(url_for('units_setting'))
    else:
        return redirect(url_for('users'))


######## test


@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    
    cursor.execute("DELETE FROM users WHERE id=%s", (id_data))
    db.commit()
    return redirect(url_for('users'))

@app.route('/delete_room/<string:id_data>', methods = ['GET'])
def delete_room(id_data):
    flash("Record Has Been Deleted Successfully")
    
    cursor.execute("DELETE FROM room WHERE id=%s", (id_data))
    db.commit()
    return redirect(url_for('units_setting'))



if __name__ =="__main__" :
    # app.run(host = "localhost", port = 10200, debug=True)
    app.run(host="0.0.0.0", port=10200, debug=True)
