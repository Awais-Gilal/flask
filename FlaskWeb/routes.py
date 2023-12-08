from FlaskWeb import app

@app.route("/")
def home_page():
  return "<h1>Hello! world</h1>"

@app.route("/about")
def about_page()