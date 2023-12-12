from FlaskWeb import app, db
from flask import render_template
from FlaskWeb.modules import Posts, Messages
from FlaskWeb.forms import PostForm, MessageForm


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


@app.route("/postform" , methods=["GET", "POST"])
def post_form_page():
  form = PostForm
  return render_template("postForm.html", form=form)