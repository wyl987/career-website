from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db

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

@flask_app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not Found", 404
  return render_template('jobpage.html',
                         job = job)
  
@flask_app.route("/job/<id>/apply", methods=['post'])
def apply_job(id):
  data = request.form
  add_application_to_db(id, data)
  return render_template('acknowledge.html')
  

if __name__ == "__main__":
  flask_app.run(host='0.0.0.0', debug=True)
