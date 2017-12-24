from flask import Flask, abort, request, make_response, jsonify, send_file
import time
import os
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


@app.route('/rooms', methods=['GET'])
def get_rooms():
    if request.method == 'GET':
        #TODO:部屋の名前が欲しい.そのあとindex.htmlにその情報をリストで表示
        cur = con.cursor()
        sql = "select name from room;"
        cur.execute(sql)
        rows = cur.fetchall()
        return make_response(jsonify(rows), 200)

##ボタン的なの押したら部屋作れるようにしたい
@app.route("/room_name", methods=["POST"])
def create_room():

    if request.method == 'POST':
        if not request.headers.get("Content-Type") == 'application/json':
            error_message = {
                'error':'not supported Content-Type'
            }
            return make_response(jsonify(error_message), 200)

        cur = con.cursor()
        sql = "insert into ********"
        cur.execute(sql)
        return make_response(jsonify({'result': True}))


@app.route("/")
def main():
    index_path = os.path.join(app.static_folder, 'index.html')
    return send_file(index_path)


# Everything not declared before (not a Flask route / API endpoint)...
@app.route('/<path:path>')
def route_frontend(path):
    # ...could be a static file needed by the front end that
    # doesn't use the `static` path (like in `<script src="bundle.js">`)
    file_path = os.path.join(app.static_folder, path)
    if os.path.isfile(file_path):
        return send_file(file_path)
    # ...or should be handled by the SPA's "router" in front end
    else:
        index_path = os.path.join(app.static_folder, 'index.html')
        return send_file(index_path)


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
