from FlaskWeb import app
from flask import render_template


@app.route("/")
@app.route("/home")
def home_page():
  return render_template("index.html")

@app.route("/about")
def about_page():
  return render_template("about.html")

@app.route("/contact")
def contact_page():
  return render_template("contact.html")

@app.route("/post")
def post_page():
  return render_template("post.html")
