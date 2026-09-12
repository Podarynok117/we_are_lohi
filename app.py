from flask import *
from flask_socketio import * 
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
@socketio.on("message")
def handle_message(message):
    print("Нам повідомили отаке:",message )
    emit("message", message)
socketio.run(app, debug=True)