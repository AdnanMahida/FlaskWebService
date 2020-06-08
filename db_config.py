#created by AdnanMahida
from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
 
# MySQL configurations 
app.config['MYSQL_DATABASE_USER'] = 'root' #db user name
app.config['MYSQL_DATABASE_PASSWORD'] = '' # db password 
app.config['MYSQL_DATABASE_DB'] = 'mydb' #db name
app.config['MYSQL_DATABASE_HOST'] = 'localhost' # host name
mysql.init_app(app)