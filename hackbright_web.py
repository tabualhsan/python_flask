"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    grades = hackbright.get_grades_by_github(github)
    html = render_template("students_info.html",
                           first=first,
                           last=last,
                           github=github)

    return html

    # return f"{github} is the GitHub account for {first} {last}"
@app.route("/student-search")
def get_student_form():

    return render_template("student_search.html")
@app.route("/new_student" methods= ['POST'])
def student_add():
    
    github = request.form.get('github')
    first = request.form.get('first')
    last = request.form.get('last')

    hackbright.make_new_student(first, last, github)

    return render_template("new_student.html",
                           github=github)


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")
