from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title': 'Data Analyst',
    'location': 'Melbourne, Australia',
    'salary': '$80,000'
  },
  {
    'id':2,
    'title': 'Software Developer',
    'location': 'Melbourne, Australia',
    'salary': '$90,000'
  },
  {
    'id':3,
    'title': 'Python Developer',
    'location': 'Melbourne, Australia',
    'salary': '$100,000'
  },
  {
    'id':4,
    'title': 'Full Stack Developer',
    'location': 'Melbourne, Australia',
    'salary': '$100,000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', 
                         jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
