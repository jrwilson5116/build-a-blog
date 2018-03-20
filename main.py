from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:bab@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    body = db.Column(db.String(2000))

    def __init__(self, name,body):
        self.title = name
        self.body =body


@app.route('/', methods=['POST', 'GET'])
def index():
    tasks = Blog.query.all()
    return render_template('blog.html',title="Blog", tasks=tasks)


@app.route('/newpost',methods=['POST','GET'])
def add_post():
    if request.method == 'POST':
        blog_name = request.form['title']
        blog_body = request.form['body']
        new_blog = Blog(blog_name,blog_body)
        db.session.add(new_blog)
        db.session.commit()
    return render_template('newpost.html')


if __name__=='__main__':
    app.run()