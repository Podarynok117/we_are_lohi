from flask import *
from flask_socketio import *
import sqlite3

con=sqlite3.connect("chat.db")
cursor=con.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT,
hesh_password TEXT
)
""")
cursor.close()
con.commit()
con.close()



app = Flask(__name__)
socketio=SocketIO(app)
messages=[]
"""@app.route("/", methods=["GET","POST"])
def index():
    if request.method=="POST":
        message=request.form["eman"]
        messages.append(message)
        print(message)
    return render_template("index.html", mg=messages)"""
#fdfdfdfdfdfdfdfdfdfdfdfdfdfdfd
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/registration", methods=["POST", "GET"])
def registration():
    if request.method=='POST':
        username=request.form["username"]
        password=request.form["password"]
        con=sqlite3.connect("chat.db")
        cursor=con.cursor()
        cursor.execute("INSERT INTO users (username, hesh_password) VALUES (?,?)", (username, password))
        cursor.close()
        con.commit()
        con.close()
        return "І нашо ти це зробили?"
    return render_template("registration.html")

@socketio.on("message")
def handle_message(message):
    print("Нам повідомили отаке:",message )
    socketio.emit("message", message)
socketio.run(app, debug=True, host="0.0.0.0", port=5000)