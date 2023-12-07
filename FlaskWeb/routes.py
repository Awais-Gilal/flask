from FlaskWeb import app

@app.route("/")
def home_page():
  return "<h1>Hello! world</h1>"