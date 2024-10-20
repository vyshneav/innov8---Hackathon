from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
class Todo(db.Model):                                                                                                                                                                                                                                       
  sno = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(200), nullable=False)
  password = db.Column(db.String(500), nullable=False)
  date_created = db.Column(db.DateTime, default=datetime.utcnow)
  def __repr__(self) -> str:
    return f"{self.sno} - {self.title}"



@app.route('/login', methods=['GET','POST'])
def index():
    if request.method== 'POST':
     User_id= request.form["username"]
     Password= request.form["password"]  
     credentials = Todo(username=User_id, password= Password)
     db.session.add(credentials)
     db.session.commit()
     return redirect("/mainpage")

    allcred = Todo.query.all()
    return render_template('index.html', ALLCRED= allcred)
@app.route('/mainpage',methods=['GET','POST'])
def main():
    
    
    return ('mainpage.html')
@app.route('/search', methods=['GET','POST'])
def search():
    
   
    

if __name__ == '__main__':
 app.run(debug=True)