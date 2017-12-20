from flask import Flask, abort, request, make_response, jsonify
import time
import MySQLdb as mysql
app = Flask(__name__)

config = {
    "user": "root",
    "password": "honya_morake",
    "host": "db",
    "db": "whiteboard"
}

con = None

while(con is None):
    try:
        con = mysql.connect(
                user = config["user"],
                passwd = config["password"],
                host = config["host"],
                db = config["db"]
        )
    except Exception as e:
        print(e)
        print("Could not establish connection to db, retrying..")
    time.sleep(1)

@app.route("/")
def hello():
    #TODO:部屋の名前が欲しい.そのあとindex.htmlにその情報をリストで表示
    cur = con.cursor()
    sql = "select name from room;"
    cur.execute(sql)
    rows = cur.fetchall()

    with open('./static/index.html', 'r') as file:
        return file.read()

##ボタン的なの押したら部屋作れるようにしたい
@app.route("/room_name", methods=["POST"])
def create_room():
    if not request.headers.get("Content-Type") == 'application/json':
        error_message = {
            'error':'not supported Content-Type'
        }
        return make_response(jsonify(error_message), 400)

    cur = con.cursor()
    sql = "insert into ********"
    cur.execute(sql)
    return make_response(jsonify({'result': True}))

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
