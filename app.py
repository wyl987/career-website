from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

flask_app = Flask(__name__)

@flask_app.route("/")
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('home.html', 
                         jobs=jobs)

@flask_app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

if __name__ == "__main__":
  flask_app.run(host='0.0.0.0', debug=True)
