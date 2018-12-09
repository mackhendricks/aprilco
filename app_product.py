from flask import Flask
import MySQLdb
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Welcome to AprilCo v2!'

@app.route('/backend-service')
def backend_service():
    return 'AprilCo Backend Services'

@app.route('/product')
def product():
    #MySQL varables
    hostname = "127.0.0.1"
    port = "3306"
    username = "root"
    database = "aprilco"

    try:

        db=MySQLdb.connect(host=hostname, user=username, passwd='', db=database)
        c=db.cursor()
        c.execute("""select * from products""")
        row_headers=[x[0] for x in c.description]
        results =c.fetchall()
        json_data=[]
        for row in results:
           json_data.append(dict(zip(row_headers,row)))
        return json.dumps(json_data)
        db.close()
    except Exception as e:
        #print(e)
        return "***Can't connect to database***"


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port='5001')
