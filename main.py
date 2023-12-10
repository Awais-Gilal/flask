from FlaskWeb import app, db
import os

if __name__ == "__main__":
  if not os.path.exists("instance/database.db"):
    with app.app_context():
      db.create_all()
  
  #app.run(host="0.0.0.0", port=21)
  app.run(debug=True)