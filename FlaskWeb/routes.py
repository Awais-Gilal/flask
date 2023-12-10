from FlaskWeb import app, db
from flask import render_template
from FlaskWeb.modules import Posts, Messages


@app.route("/")
@app.route("/home")
def home_page():
  with app.app_context():
    posts = Posts.query.all()
  return render_template("index.html", posts=posts)






















@app.route("/about")
def about_page():
  return render_template("about.html")

@app.route("/contact")
def contact_page():
  return render_template("contact.html")

@app.route("/post")
def post_page():
  return render_template("postPage.html")
