from flask import Flask, jsonify, render_template

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'frontend Developer',
    'location': 'Chennai',
    'salary': '10000'
}, {
    'id': 2,
    'title': 'Backend Developer',
    'location': 'Chennai'
}, {
    'id': 3,
    'title': 'Android Developer',
    'location': 'Chennai',
    'salary': '20000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Jovian company')


@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)