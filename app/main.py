from flask import Flask, abort, request, make_response, jsonify, send_file, request
from flask_socketio import SocketIO, emit
import time
import os
import MySQLdb as mysql
app = Flask(__name__)
socketio = SocketIO(app)

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
        sql = "select room.name, user.name from room, drawn_info, user where drawn_info.room_id == room.id and drawn_info.user_id == user.id;"
        cur.execute(sql)
        rows = cur.fetchall()

    return make_response(jsonify(rows), 200)

@app.route("/mk_room_name", methods=["POST"])
def create_room():
    if request.method == 'POST':
        if not request.headers.get("Content-Type") == 'application/json':
            error_message = {
                'error':'not supported Content-Type'
            }
            return make_response(jsonify(error_message), 200)

        data = request.data
        cur = con.cursor()
        sql = "insert into room(name) values ({})".format(data.name)
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

##
@socketio.on('event', namespace='/test')
def test_message(message):
    #message　point room_info
    # TODO: drawn_info にデータ挿入
    emit('response', {'data': message['data']})

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

if __name__ == "__main__":
    # Only for debugging while developing
    socketio.run(app)
