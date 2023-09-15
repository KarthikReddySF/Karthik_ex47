from flask import Flask,session,redirect,url_for
from flask import render_template,request
import map
app=Flask(__name__,template_folder="templates")

@app.route('/')
def index():
    session['room_name']=map.START
    return redirect(url_for("game"))

@app.route('/game', methods=['GET','POST'])
def game():
    room_name=session.get('room_name')

    if request.method=='GET':
        if room_name:
            room=map.load_room(room_name)
            return render_template("show_room.html",room=room)
        else:
            return render_template("you_died.html")
    else:
        action=request.form.get('action')

        if room_name and action:
            room=map.load_room(room_name)
            next_room=room.go(action)

            if not next_room:
                session['room_name']=map.name_room(room_name)
            else:
                session['room_name']=map.name_room(next_room)
        return redirect(url_for("game"))
    
app.secret_key='A0Zr98j/3yX R`XHH!jmNJLWX/,?RT'
if __name__=="__main__":
    app.run(debug=True)