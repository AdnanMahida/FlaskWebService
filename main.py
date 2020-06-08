#created by AdnanMahida
import pymysql #for mysql client
from app import app #init 
from db_config import mysql #config details
from flask import jsonify #restful module
from flask import flash, request #resquest module
from flask_restful import reqparse

@app.route('/')
def index():
    return jsonify( {'isworking':'true'})

@app.route('/insert-user',methods=['GET', 'POST'])
def insert_user():
    try:
        parser = reqparse.RequestParser() #object of request parser
        #args
        parser.add_argument('username', type=str)
        parser.add_argument('contect', type=str)
        
        args = parser.parse_args()
        # storing in variable
        _username = args['username']
        _contect =args['contect']
        # query
        sql = "INSERT INTO users(user_name, user_contect) VALUES(%s, %s)"
        param_data = (_username, _contect)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, param_data)
        conn.commit()
        if cursor.rowcount >0:
            return {'result':'true'}
        else:
            return {'result':'false'}
    except Exception as e:
        return {'error': str(e)}


@app.route('/is-existing-user',methods=['GET', 'POST'])
def is_existing_user():
    try:
        parser = reqparse.RequestParser() #object of request parser
        #args
        parser.add_argument('user_id', type=str)
        args = parser.parse_args()
        _user_id =args['user_id']
        sql = """SELECT * FROM users WHERE user_id =%s """
        conn = mysql.connect()
        cursor = conn.cursor()
        rows_count=cursor.execute(sql, _user_id)
        if rows_count > 0:
            return {'result':'true'}
        else:
            return {'result':'false'}
    except Exception as e:
        return {'error': str(e)}


@app.route('/get-users',methods=['GET', 'POST'])
def get_category_items():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM users """)
        rows =  cursor.fetchall()
        payload = []
        content = {}
        for result in rows:
            content = {'user_id': result[0], 'user_name': result[1], 'user_contect': result[2]
                       ,'user_email':result[3]}
            payload.append(content)
            content = {}
        return jsonify(payload)
    
    except Exception as e:
        return {'error': str(e)}

   
if __name__ == "__main__":
    app.debug = True #for debug server  
    app.run(host = '0.0.0.0', port=5000)#change port and id address with local address
    
    