from flask import Flask, render_template, jsonify
import courses as cs
import projects as ps
import skills
app=Flask(__name__)
@app.route("/")
def hello_world():
  return render_template("home.html",courses=cs.courses,projects=ps.projects,skills=skills.Skills)
@app.route("/About_Sahib") 
def open_About_page():
  return render_template("About_page.html")
@app.route("/Courses") 
def open_Courses_page():
  return render_template("Courses_page.html",courses=cs.courses)
@app.route("/Featured_Projects") 
def open_Vision_page():
  return render_template("Vision_page.html")
@app.route("/Contact_Page") 
def open_Contact_Page():
  return render_template("Contact_Page.html")

if __name__=='__main__':
   app.run(host='0.0.0.0',debug=True)  