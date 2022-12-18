from flask import Flask, render_template, request
import mysql.connector

conn=mysql.connector.connect(host="localhost",user="newuser",password="a234567Z?",database ="Periodic_Table")
cursor = conn.cursor()

app = Flask(__name__)

@app.route("/")
def index():
	return "Welcome to the Periodic table Database"

@app.route("/Elements")
def Elements():
	cursor.execute("SELECT * FROM Elements")
	value = cursor.fetchall()
	return render_template("Main.html", data = value, name = 'Elements')

@app.route("/Alkali_Metals")
def Alkali():
        cursor.execute("SELECT ElemName, AtomNum, AtomMass, Discovery FROM Elements WHERE Class = 'Alkali Metal'")
        value = cursor.fetchall()
        return render_template("Elements.html", data = value, name = 'Elements')
@app.route("/Metalloids")
def Metalloids():
        cursor.execute("SELECT ElemName, AtomNum, AtomMass, Discovery FROM Elements WHERE Class = 'Metalloid'")
        value = cursor.fetchall()
        return render_template("Elements.html", data = value, name = 'Elements')
@app.route("/Actinides")
def Actinides():
        cursor.execute("SELECT ElemName, AtomNum, AtomMass, Discovery FROM Elements WHERE Class = 'Actinides'")
        value = cursor.fetchall()
        return render_template("Elements.html", data = value, name = 'Elements')
@app.route("/Alkaline_earth_metals")
def Alkaline():
        cursor.execute("SELECT ElemName, AtomNum, AtomMass, Discovery FROM Elements WHERE Class = 'Alkaline Earth Metal'")
        value = cursor.fetchall()
        return render_template("Elements.html", data = value, name = 'Elements')
@app.route("/Reactive_nonmetals")
def ReactiveNon():
        cursor.execute("SELECT ElemName, AtomNum, AtomMass, Discovery FROM Elements WHERE Class = 'Reactive nonmetal'")
        value = cursor.fetchall()
        return render_template("Elements.html", data = value, name = 'Elements')
@app.route("/Unknown_Properties")
def Unknown():
	cursor.execute("SELECT ElemName, AtomNum, AtomMass, Discovery FROM Elements WHERE Class = 'Unknown'")
	value = cursor.fetchall()
	return render_template("Elements.html", data = value, name = 'Elements')
@app.route("/Transition_metals")
def Transition():
        cursor.execute("SELECT ElemName, AtomNum, AtomMass, Discovery FROM Elements WHERE Class = 'Transition Material'")
        value = cursor.fetchall()
        return render_template("Elements.html", data = value, name = 'Elements')
@app.route("/Noble_gases")
def Noble():
        cursor.execute("SELECT ElemName, AtomNum, AtomMass, Discovery FROM Elements WHERE Class = 'Noble Gas'")
        value = cursor.fetchall()
        return render_template("Elements.html", data = value, name = 'Elements')
@app.route("/Post-transition_metals")
def PostTransition():
	cursor.execute("SELECT ElemName, AtomNum, AtomMass, Discovery FROM Elements WHERE Class = 'Post-transition metals'")
	value = cursor.fetchall()
	return render_template("Elements.html", data = value, name = 'Elements')
@app.route("/Lanthanides")
def Lanthanides():
        cursor.execute("SELECT ElemName, AtomNum, AtomMass, Discovery FROM Elements WHERE Class = 'Lanthanide'")
        value = cursor.fetchall()
        return render_template("Elements.html", data = value, name = 'Elements')

if __name__ == "__main__":
	app.run(debug = True)
